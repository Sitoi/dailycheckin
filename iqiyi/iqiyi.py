# -*- coding: utf-8 -*-
import json
import os
import re
import time

import requests


class IQIYICheckIn:
    def __init__(self, check_item):
        self.check_item = check_item

    @staticmethod
    def parse_cookie(cookie):
        p00001 = re.findall(r"P00001=(.*?);", cookie)[0]
        p00003 = re.findall(r"P00003=(.*?);", cookie)[0]
        return p00001, p00003

    @staticmethod
    def user_information(p00001):
        """
        用户信息查询
        """
        time.sleep(3)
        url = "http://serv.vip.iqiyi.com/vipgrowth/query.action"
        params = {"P00001": p00001}
        res = requests.get(url=url, params=params).json()
        if res["code"] == "A00000":
            try:
                res_data = res.get("data", {})
                level = res_data.get("level", 0)  # VIP 等级
                growthvalue = res_data.get("growthvalue", 0)  # 当前 VIP 成长值
                distance = res_data.get("distance", 0)  # 升级需要成长值
                deadline = res_data.get("deadline", "非 VIP 用户")  # VIP 到期时间
                today_growth_value = res_data.get("todayGrowthValue", 0)  # 今日成长值
                msg = (
                    f"VIP 等级: {level}\n当前成长值: {growthvalue}\n"
                    f"升级需成长值: {distance}\n今日成长值: +{today_growth_value}\nVIP 到期时间: {deadline}"
                )
            except Exception as e:
                msg = str(e)
                print(msg)
        else:
            msg = res.get("msg")
        return msg

    @staticmethod
    def sign(p00001):
        """
        VIP 签到
        """
        url = "https://tc.vip.iqiyi.com/taskCenter/task/queryUserTask"
        params = {"P00001": p00001, "autoSign": "yes"}
        res = requests.get(url=url, params=params).json()
        if res["code"] == "A00000":
            try:
                growth = res["data"]["signInfo"]["data"]["rewardMap"]["growth"]
                continue_sign_days_sum = res["data"]["signInfo"]["data"]["continueSignDaysSum"]
                reward_day = (
                    7 if continue_sign_days_sum % 28 <= 7 else (14 if continue_sign_days_sum % 28 <= 14 else 28)
                )
                rouund_day = 28 if continue_sign_days_sum % 28 == 0 else continue_sign_days_sum % 28
                msg = f"+{growth}成长值\n连续签到: {continue_sign_days_sum}天\n签到周期: {rouund_day}天/{reward_day}天"
            except Exception as e:
                print(e)
                msg = res["data"]["signInfo"].get("msg")
        else:
            msg = res.get("msg")
        return msg

    @staticmethod
    def query_user_task(p00001):
        """
        获取 VIP 日常任务 和 taskCode(任务状态)
        """
        url = "https://tc.vip.iqiyi.com/taskCenter/task/queryUserTask"
        params = {"P00001": p00001}
        task_list = []
        res = requests.get(url=url, params=params).json()
        if res["code"] == "A00000":
            for item in res["data"]["tasks"]["daily"]:
                task_list.append(
                    {
                        "name": item["name"],
                        "taskCode": item["taskCode"],
                        "status": item["status"],
                        "taskReward": item["taskReward"]["task_reward_growth"],
                    }
                )
        return task_list

    @staticmethod
    def join_task(p00001, task_list):
        """
        遍历完成任务
        """
        url = "https://tc.vip.iqiyi.com/taskCenter/task/joinTask"
        params = {"P00001": p00001, "taskCode": "", "platform": "bb136ff4276771f3", "lang": "zh_CN"}
        for item in task_list:
            if item["status"] == 2:
                params["taskCode"] = item["taskCode"]
                requests.get(url=url, params=params)

    @staticmethod
    def get_task_rewards(p00001, task_list):
        """
        获取任务奖励
        :return: 返回信息
        """
        url = "https://tc.vip.iqiyi.com/taskCenter/task/getTaskRewards"
        params = {"P00001": p00001, "taskCode": "", "platform": "bb136ff4276771f3", "lang": "zh_CN"}
        growth_task = 0
        for item in task_list:
            if item["status"] == 0:
                params["taskCode"] = item.get("taskCode")
                requests.get(url=url, params=params)
            elif item["status"] == 4:
                requests.get(
                    url='https://tc.vip.iqiyi.com/taskCenter/task/notify',
                    params=params
                )
                params["taskCode"] = item.get("taskCode")
                requests.get(url=url, params=params)
            elif item["status"] == 1:
                growth_task += item["taskReward"]
        msg = f"+{growth_task}成长值"
        return msg

    @staticmethod
    def draw(draw_type, p00001, p00003):
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
        res = requests.get(url=url, params=params).json()
        if not res.get("code"):
            chance = int(res.get("daysurpluschance"))
            msg = res.get("awardName")
            return {"status": True, "msg": msg, "chance": chance}
        else:
            try:
                msg = res.get("kv", {}).get("msg")
            except Exception as e:
                print(e)
                msg = res["errorReason"]
        return {"status": False, "msg": msg, "chance": 0}

    def main(self):
        p00001, p00003 = self.parse_cookie(self.check_item.get("iqiyi_cookie"))
        sign_msg = self.sign(p00001=p00001)
        chance = self.draw(0, p00001=p00001, p00003=p00003)["chance"]
        if chance:
            draw_msg = ""
            for i in range(chance):
                ret = self.draw(1, p00001=p00001, p00003=p00003)
                draw_msg += ret["msg"] + ";" if ret["status"] else ""
        else:
            draw_msg = "抽奖机会不足"
        task_msg = ""
        for one in range(6):
            task_list = self.query_user_task(p00001=p00001)
            self.join_task(p00001=p00001, task_list=task_list)
            time.sleep(10)
            task_msg = self.get_task_rewards(p00001=p00001, task_list=task_list)
        user_msg = self.user_information(p00001=p00001)
        msg = f"{user_msg}\n" f"签到奖励: {sign_msg}\n任务奖励: {task_msg}\n抽奖奖励: {draw_msg}"
        return msg


if __name__ == "__main__":
    with open(
        os.path.join(os.path.dirname(os.path.dirname(__file__)), "config/config.json"), "r", encoding="utf-8"
    ) as f:
        datas = json.loads(f.read())
    _check_item = datas.get("IQIYI_COOKIE_LIST", [])[0]
    print(IQIYICheckIn(check_item=_check_item).main())
