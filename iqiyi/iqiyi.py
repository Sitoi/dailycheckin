# -*- coding: utf-8 -*-
import base64
import hashlib
import hmac
import json
import os
import re
import time
import urllib.parse

import requests


class IQIYICheckIn:
    def __init__(self, dingtalk_secret, dingtalk_access_token, iqiyi_cookie_list):
        self.dingtalk_secret = dingtalk_secret
        self.dingtalk_access_token = dingtalk_access_token
        self.iqiyi_cookie_list = iqiyi_cookie_list
        self.task_list = []
        self.growth_task = 0

    @staticmethod
    def parse_cookie(cookie):
        p00001 = re.findall(r"P00001=(.*?);", cookie)[0]
        p00003 = re.findall(r"P00003=(.*?);", cookie)[0]
        return p00001, p00003

    def message_to_dingtalk(self, content):
        timestamp = str(round(time.time() * 1000))
        secret_enc = self.dingtalk_secret.encode("utf-8")
        string_to_sign = "{}\n{}".format(timestamp, self.dingtalk_secret)
        string_to_sign_enc = string_to_sign.encode("utf-8")
        hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
        sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
        send_data = {"msgtype": "text", "text": {"content": content}}
        requests.post(
            url="https://oapi.dingtalk.com/robot/send?access_token={0}&timestamp={1}&sign={2}".format(
                self.dingtalk_access_token, timestamp, sign
            ),
            headers={"Content-Type": "application/json", "Charset": "UTF-8"},
            data=json.dumps(send_data),
        )
        return content

    def user_information(self, p00001):
        """
        用户信息查询
        """
        time.sleep(3)
        url = "http://serv.vip.iqiyi.com/vipgrowth/query.action"
        params = {"P00001": p00001}
        res = requests.get(url=url, params=params)
        if res.json()["code"] == "A00000":
            try:
                res_data = res.json()["data"]
                level = res_data["level"]  # VIP 等级
                growthvalue = res_data["growthvalue"]  # 当前 VIP 成长值
                distance = res_data["distance"]  # 升级需要成长值
                deadline = res_data["deadline"]  # VIP 到期时间
                today_growth_value = res_data["todayGrowthValue"]  # 今日成长值
                msg = (
                    f"VIP 等级: {level}\n当前成长值: {growthvalue}\n"
                    f"升级需成长值: {distance}\n今日成长值: +{today_growth_value}\nVIP 到期时间: {deadline}"
                )
            except Exception as e:
                msg = res.json()
        else:
            msg = res.json()
        return msg

    def sign(self, p00001):
        """
        VIP 签到
        """
        url = "https://tc.vip.iqiyi.com/taskCenter/task/queryUserTask"
        params = {"P00001": p00001, "autoSign": "yes"}
        res = requests.get(url=url, params=params)
        if res.json()["code"] == "A00000":
            try:
                growth = res.json()["data"]["signInfo"]["data"]["rewardMap"]["growth"]
                continue_sign_days_sum = res.json()["data"]["signInfo"]["data"]["continueSignDaysSum"]
                reward_day = (
                    7 if continue_sign_days_sum % 28 <= 7 else (14 if continue_sign_days_sum % 28 <= 14 else 28)
                )
                rouund_day = 28 if continue_sign_days_sum % 28 == 0 else continue_sign_days_sum % 28
                msg = f"+{growth}成长值\n连续签到: {continue_sign_days_sum}天\n签到周期: {rouund_day}天/{reward_day}天"
            except Exception as e:
                msg = res.json()["data"]["signInfo"]["msg"]
        else:
            msg = res.json()["msg"]
        return msg

    def query_user_task(self, p00001):
        """
        获取 VIP 日常任务 和 taskCode(任务状态)
        """
        url = "https://tc.vip.iqiyi.com/taskCenter/task/queryUserTask"
        params = {"P00001": p00001}
        res = requests.get(url=url, params=params)
        if res.json()["code"] == "A00000":
            for item in res.json()["data"]["tasks"]["daily"]:
                self.task_list.append(
                    {
                        "name": item["name"],
                        "taskCode": item["taskCode"],
                        "status": item["status"],
                        "taskReward": item["taskReward"]["task_reward_growth"],
                    }
                )
        return self

    def join_task(self, p00001):
        """
        遍历完成任务
        """
        url = "https://tc.vip.iqiyi.com/taskCenter/task/joinTask"
        params = {"P00001": p00001, "taskCode": "", "platform": "bb136ff4276771f3", "lang": "zh_CN"}
        for item in self.task_list:
            if item["status"] == 2:
                params["taskCode"] = item["taskCode"]
                requests.get(url=url, params=params)

    def get_task_rewards(self, p00001):
        """
        获取任务奖励
        :return: 返回信息
        """
        url = "https://tc.vip.iqiyi.com/taskCenter/task/getTaskRewards"
        params = {"P00001": p00001, "taskCode": "", "platform": "bb136ff4276771f3", "lang": "zh_CN"}
        for item in self.task_list:
            if item["status"] == 0:
                params["taskCode"] = item["taskCode"]
                res = requests.get(url=url, params=params)
                if res.json()["code"] == "A00000":
                    self.growth_task += item["taskReward"]
        msg = f"+{self.growth_task}成长值"
        return msg

    def draw(self, draw_type, p00001, p00003):
        """
        查询抽奖次数(必),抽奖
        :param draw_type: 类型。0 查询次数；1 抽奖
        :param p00001: 关键参数
        :param p00003: 关键参数
        :return: {status, msg, chance}
        """
        url = "https://iface2.iqiyi.com/aggregate/3.0/lottery_activity"
        params = {
            "lottery_chance": 1,
            "app_k": "b398b8ccbaeacca840073a7ee9b7e7e6",
            "app_v": "11.6.5",
            "platform_id": 10,
            "dev_os": "8.0.0",
            "dev_ua": "FRD-AL10",
            "net_sts": 1,
            "qyid": "2655b332a116d2247fac3dd66a5285011102",
            "psp_uid": p00003,
            "psp_cki": p00001,
            "psp_status": 3,
            "secure_v": 1,
            "secure_p": "GPhone",
            "req_sn": round(time.time() * 1000),
        }
        if draw_type == 1:
            del params["lottery_chance"]
        res = requests.get(url=url, params=params)
        if not res.json().get("code"):
            chance = int(res.json().get("daysurpluschance"))
            msg = res.json().get("awardName")
            return {"status": True, "msg": msg, "chance": chance}
        else:
            try:
                msg = res.json().get("kv", {}).get("msg")
            except Exception as e:
                msg = res.json()["errorReason"]
        return {"status": False, "msg": msg, "chance": 0}

    def main(self):
        for iqiyi_cookie in self.iqiyi_cookie_list:
            p00001, p00003 = self.parse_cookie(iqiyi_cookie.get("iqiyi_cookie"))
            sign_msg = self.sign(p00001=p00001)
            chance = self.draw(0, p00001=p00001, p00003=p00003)["chance"]
            if chance:
                draw_msg = ""
                for i in range(chance):
                    ret = self.draw(1, p00001=p00001, p00003=p00003)
                    draw_msg += ret["msg"] + ";" if ret["status"] else ""
            else:
                draw_msg = "抽奖机会不足"
            self.query_user_task(p00001=p00001).join_task(p00001=p00001)
            task_msg = self.query_user_task(p00001=p00001).get_task_rewards(p00001=p00001)
            user_msg = self.user_information(p00001=p00001)
            msg = (
                f"【爱奇艺等级】\n{user_msg}\n-----------------------------\n"
                f"【爱奇艺签到】\n签到奖励: {sign_msg}\n任务奖励: {task_msg}\n抽奖奖励: {draw_msg}"
            )
            print(msg)
            if self.dingtalk_secret and self.dingtalk_access_token:
                self.message_to_dingtalk(msg)


if __name__ == "__main__":
    with open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "config.json"), "r", encoding="utf-8") as f:
        data = json.loads(f.read())
    dingtalk_secret = data.get("dingtalk", {}).get("dingtalk_secret")
    dingtalk_access_token = data.get("dingtalk", {}).get("dingtalk_access_token")
    iqiyi_cookie_list = data.get("iqiyi", [])
    IQIYICheckIn(
        dingtalk_secret=dingtalk_secret,
        dingtalk_access_token=dingtalk_access_token,
        iqiyi_cookie_list=iqiyi_cookie_list,
    ).main()
