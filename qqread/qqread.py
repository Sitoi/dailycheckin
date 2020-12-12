# -*- coding: utf8 -*-
import json
import os
import random
import re
import time
from datetime import datetime, timedelta

import requests


class QQReadCheckIn:
    def __init__(self, qqread_account_list):
        self.qqread_account_list = qqread_account_list
        self.delaysec = 1  # 每次任务延迟时间 默认1秒
        self.limit_time = 18  # 每日最大上传阅读时间，默认为18小时
        self.once_time = 5  # 单次上传阅读时间，默认为5分钟
        self.drawamount = 0  # [0, 10, 30, 50, 100] 分别为关闭自动提现、提现10元、30元、50元、100元，默认为关闭

    @staticmethod
    def valid(headers):
        qqnum = "未获取到"
        try:
            response = requests.get(url="https://mqqapi.reader.qq.com/mqq/user/init", headers=headers)
            if not response.json()["data"]["isLogin"]:
                qqnum = re.findall(r"ywguid=(.*?);ywkey", headers["Cookie"])[0]
                return False, f"【HEADERS 过期】: {qqnum}"
            return True, ""
        except Exception as e:
            print(e)
            return False, f"【HEADERS 过期】: {qqnum}"

    @staticmethod
    def gettime():
        """获取北京时间"""
        bj_dt = datetime.utcnow() + timedelta(hours=8)
        return bj_dt

    @staticmethod
    def get_timestamp() -> int:
        """获取当日0点时间戳"""
        bj_dt = (datetime.utcnow() + timedelta(hours=8)).strftime("%Y-%m-%d") + " 00:00:00"
        time_array = time.strptime(bj_dt, "%Y-%m-%d %H:%M:%S")
        time_stamp = int(time.mktime(time_array) * 1000)
        return time_stamp

    def delay(self):
        """延时"""
        time.sleep(self.delaysec)

    def get_template(self, headers, function_id):
        """请求模板"""
        function_url = f"https://mqqapi.reader.qq.com/mqq/{function_id}"
        self.delay()
        data = requests.get(url=function_url, headers=headers).json()
        return data

    def qqreadtask(self, headers):
        """获取任务列表"""
        task_data = self.get_template(headers=headers, function_id="red_packet/user/page?fromGuid=")["data"]
        return task_data

    def qqreadmytask(self, headers):
        """获取“我的”页面任务"""
        mytask_data = self.get_template(headers=headers, function_id="v1/task/list")["data"]["taskList"]
        return mytask_data

    def qqreadinfo(self, headers):
        """获取用户名"""
        info_data = self.get_template(headers=headers, function_id="user/init")["data"]
        return info_data

    def qqreadticket(self, headers):
        """书券签到"""
        qqreadticketurl = "https://mqqapi.reader.qq.com/mqq/sign_in/user"
        self.delay()
        ticket_data = requests.post(url=qqreadticketurl, headers=headers).json()["data"]
        return ticket_data

    def qqreadsign(self, headers):
        """每日打卡"""
        sign_data = self.get_template(headers=headers, function_id="red_packet/user/clock_in/page")["data"]
        return sign_data

    def qqreadsign2(self, headers):
        """每日打卡翻倍"""
        sign2_data = self.get_template(headers=headers, function_id="red_packet/user/clock_in_video")
        return sign2_data

    def qqreadtodayread(self, headers):
        """每日阅读"""
        todayread_data = self.get_template(headers=headers, function_id="red_packet/user/read_book")
        return todayread_data

    def qqreadvideo(self, headers):
        """视频奖励"""
        video_data = self.get_template(headers=headers, function_id="red_packet/user/watch_video")
        return video_data

    def qqreadbox(self, headers):
        """宝箱奖励"""
        box_data = self.get_template(headers=headers, function_id="red_packet/user/treasure_box")
        return box_data

    def qqreadbox2(self, headers):
        """宝箱奖励翻倍"""
        box2_data = self.get_template(headers=headers, function_id="red_packet/user/treasure_box_video")
        return box2_data

    def qqreadwktime(self, headers):
        """获取本周阅读时长"""
        wktime_data = self.get_template(headers=headers, function_id="v1/bookShelfInit")["data"]["readTime"]
        return wktime_data

    def qqreadwkpickinfo(self, headers):
        """周阅读时长奖励查询"""
        wkpickinfo_data = self.get_template(headers=headers, function_id="pickPackageInit")["data"]
        return wkpickinfo_data

    def qqreadwkpick(self, headers, num):
        """周阅读时长奖励领取"""
        wkpick_data = self.get_template(headers=headers, function_id=f"pickPackage?readTime={num}")
        return wkpick_data

    def qqreadtodaytime(self, headers, bidnum):
        """获取本日阅读时长"""
        bid = re.findall(r'bid=(\d+)&', bidnum)[0]
        todaytime_data = self.get_template(
            headers=headers,
            function_id=f"page/config?router=%2Fpages%2Fbook-read%2Findex&options=%7B%22bid%22%3A%22{bid}%22%7D")[
            'data']['pageParams']['todayReadSeconds']
        return todaytime_data // 60

    def qqreadtodaygift(self, headers, sec):
        """本日阅读时长奖励"""
        todaygift_data = self.get_template(headers=headers, function_id=f"red_packet/user/read_time?seconds={sec}")
        return todaygift_data.get("data")

    def qqreadaddtime(self, headers, addtimeurl):
        """上传阅读时长"""
        sectime = random.randint(self.once_time * 60 * 1000, (self.once_time + 1) * 60 * 1000)
        findtime1 = re.compile(r'readTime%22%3A(\d+)%2C')
        url = re.sub(findtime1.findall(addtimeurl)[0], str(sectime), str(addtimeurl))
        self.delay()
        addtime_data = requests.get(url=url, headers=headers).json()
        return addtime_data

    def qqreadssr(self, headers, sec):
        """每日阅读时长奖励"""
        readssr_data = self.get_template(headers=headers, function_id=f"red_packet/user/read_time?seconds={sec}")
        return readssr_data

    def qqreadwithdrawinfo(self, headers):
        """查询提现信息"""
        withdrawinfo_data = self.get_template(headers=headers, function_id=f"red_packet/user/withdraw/list?pn=1")
        return withdrawinfo_data.get("data").get("list")[0]

    def qqreadwithdrawal(self, headers, amount):
        """提现"""
        qqreadwithdrawalurl = f"https://mqqapi.reader.qq.com/mqq/red_packet/user/withdraw?amount={amount}"
        self.delay()
        withdrawal_data = requests.post(qqreadwithdrawalurl, headers=headers).json()
        if withdrawal_data["data"]["code"] == 0:
            msg = withdrawal_data["msg"]
        else:
            msg = withdrawal_data["data"]["msg"]
        return msg

    def qqreadtrack(self, headers, data: dict):
        """Track"""
        qqreadtrackurl = "https://mqqapi.reader.qq.com/log/v4/mqq/track"
        dis = data.get("dataList", [{}])[0].get("dis")
        data = re.sub(str(dis), str(int(time.time() * 1000)), str(data))
        self.delay()
        track_data = requests.post(url=qqreadtrackurl, data=json.dumps(eval(data)), headers=headers).json()
        return track_data

    def totalamount(self, headers) -> str:
        """统计今日获得金币"""
        totalamount = 0
        for pn in range(12):
            url = f"https://mqqapi.reader.qq.com/mqq/red_packet/user/trans/list?pn={pn + 1}"
            amount_data = requests.get(url=url, headers=headers).json()["data"]["list"]
            for i in amount_data:
                if i["createTime"] >= self.get_timestamp():
                    totalamount += i["amount"]
        return str(totalamount)

    def main(self):
        msg_result_list = []
        for index, secrets in enumerate(self.qqread_account_list):
            print(f"============开始运行第 {index + 1} 个账号===========")
            start_time = time.time()
            msg_list = []
            qqread_headers = secrets.get("qqread_headers")
            qqread_bodys = secrets.get("qqread_bodys")
            qqread_timeurl = secrets.get("qqread_timeurl")
            msg_list.append(f"=== {self.gettime().strftime('%Y-%m-%d %H:%M:%S')} ===")
            msg_list.append(f"=== 📣系统通知📣 ===")
            valid_flag, valid_msg = self.valid(headers=qqread_headers)
            if valid_flag:
                info_data = self.qqreadinfo(qqread_headers)
                todaytime_data = self.qqreadtodaytime(qqread_headers, qqread_timeurl)
                wktime_data = self.qqreadwktime(qqread_headers)
                print(f"Track update {self.qqreadtrack(qqread_headers, qqread_bodys)['msg']}")
                task_data = self.qqreadtask(qqread_headers)
                mytask_data = self.qqreadmytask(qqread_headers)
                task_list = task_data["taskList"]

                msg_list.append(f"【用户信息】: {info_data['user']['nickName']}")
                msg_list.append(f"【账户余额】: {task_data['user']['amount']}金币")
                msg_list.append(f"【今日阅读】: {todaytime_data}分钟")
                msg_list.append(f"【本周阅读】: {wktime_data}分钟")
                for one_task in task_list:
                    msg_list.append(f"【{one_task['title']}】: {one_task['amount']}金币,{one_task['actionText']}")
                msg_list.append(
                    f"【第{task_data['invite']['issue']}期|{task_data['invite']['dayRange']}】:"
                    f"已邀请 {task_data['invite']['inviteCount']} 人，"
                    f"再邀请 {task_data['invite']['nextInviteConfig']['count']} 人"
                    f"获得 {task_data['invite']['nextInviteConfig']['amount']} 金币"
                )
                msg_list.append(
                    f"【{task_data['fans']['title']}】: {task_data['fans']['fansCount']}个好友,"
                    f"{task_data['fans']['todayAmount']}金币"
                )
                msg_list.append(f"【宝箱任务{task_data['treasureBox']['count'] + 1}】: {task_data['treasureBox']['tipText']}")

                if task_data["treasureBox"]["doneFlag"] == 0:
                    box_data = self.qqreadbox(qqread_headers)
                    if box_data["code"] == 0:
                        msg_list.append(f"【宝箱奖励{box_data['data']['count']}】: 获得{box_data['data']['amount']}金币")

                for one_task in task_list:
                    if one_task["title"].find("立即阅读") != -1 and one_task["doneFlag"] == 0:
                        todayread_data = self.qqreadtodayread(qqread_headers)
                        if todayread_data["code"] == 0:
                            msg_list.append(f"【每日阅读】: 获得{todayread_data['data']['amount']}金币")

                    if one_task["title"].find("打卡") != -1:
                        sign_data = self.qqreadsign(qqread_headers)
                        if one_task["doneFlag"] == 0:
                            msg_list.append(f"【今日打卡】: 获得{sign_data['todayAmount']}金币，已连续签到{sign_data['clockInDays']}天")
                        if sign_data["videoDoneFlag"] == 0:
                            sign2_data = self.qqreadsign2(qqread_headers)
                            if sign2_data["code"] == 0:
                                msg_list.append(f"【打卡翻倍】: 获得{sign2_data['data']['amount']}金币")

                    if one_task["title"].find("视频") != -1 and one_task["doneFlag"] == 0:
                        video_data = self.qqreadvideo(qqread_headers)
                        if video_data["code"] == 0:
                            msg_list.append(f"【视频奖励】: 获得{video_data['data']['amount']}金币")

                    if one_task["title"].find("阅读任务") != -1 and one_task["doneFlag"] == 0:
                        if 1 <= todaytime_data < 15:
                            todaygift_data = self.qqreadtodaygift(qqread_headers, 30)
                            if todaygift_data["amount"] > 0:
                                msg_list.append(f"【阅读金币1】: 获得{todaygift_data['amount']}金币")
                        if 5 <= todaytime_data < 30:
                            time.sleep(2)
                            todaygift_data = self.qqreadtodaygift(qqread_headers, 300)
                            if todaygift_data["amount"] > 0:
                                msg_list.append(f"【阅读金币2】: 获得{todaygift_data['amount']}金币")
                        if todaytime_data >= 30:
                            time.sleep(2)
                            todaygift_data = self.qqreadtodaygift(qqread_headers, 1800)
                            if todaygift_data["amount"] > 0:
                                msg_list.append(f"【阅读金币3】: 获得{todaygift_data['amount']}金币")

                for my_task in mytask_data:
                    if my_task["title"].find("每日签到") != -1 and my_task["doneFlag"] == 0:
                        ticket_data = self.qqreadticket(qqread_headers)
                        if ticket_data["takeTicket"] > 0:
                            msg_list.append(f"【书券签到】: 获得{ticket_data['takeTicket']}书券")

                if wktime_data >= 1200:
                    wkpickinfo_data = self.qqreadwkpickinfo(qqread_headers)
                    package = ["10", "10", "20", "30", "50", "80", "100", "120"]
                    if not wkpickinfo_data[-1]["isPick"]:
                        for m, i in enumerate(wkpickinfo_data):
                            info = self.get_template(qqread_headers, f"pickPackage?readTime={i['readTime']}")
                            if info["code"] == 0:
                                msg_list.append(f"【周时长奖励{m + 1}】: 领取{package[m]}书券")
                    else:
                        msg_list.append("【周时长奖励】: 已全部领取")

                if task_data["treasureBox"]["videoDoneFlag"] == 0:
                    time.sleep(6)
                    box2_data = self.qqreadbox2(qqread_headers)
                    if box2_data["code"] == 0:
                        msg_list.append(f"【宝箱翻倍】: 获得{box2_data['data']['amount']}金币")

                if todaytime_data // 60 <= self.limit_time:
                    addtime_data = self.qqreadaddtime(qqread_headers, qqread_timeurl)
                    if addtime_data["code"] == 0:
                        msg_list.append(f"【阅读时长】: 成功上传{self.once_time}分钟")

                if (
                        self.drawamount != 0
                        and task_data["user"]["amount"] >= self.drawamount * 10000
                        and self.gettime().hour == 21
                ):
                    withdrawinfo_data = self.qqreadwithdrawinfo(qqread_headers)["createTime"]
                    if withdrawinfo_data < self.get_timestamp():
                        withdrawal_data = self.qqreadwithdrawal(qqread_headers, self.drawamount * 10000)
                        msg_list.append(f"【自动提现】: 提现{self.drawamount}元（{withdrawal_data}）")
                msg_list.append(f"【今日收益】: {self.totalamount(secrets.get('qqread_headers'))}金币")

            else:
                msg_list.append(valid_msg)
            msg_list.append(f"\n🕛耗时：{time.time() - start_time}秒")
            msg = "\n".join(msg_list)
            print(msg)
            msg_result_list.append(msg)
        return msg_result_list


if __name__ == "__main__":
    with open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "config.json"), "r", encoding="utf-8") as f:
        datas = json.loads(f.read())
    _qqread_account_list = datas.get("qqread", [])
    QQReadCheckIn(qqread_account_list=_qqread_account_list).main()
