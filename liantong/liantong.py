# -*- coding: utf-8 -*-
import json
import os
import random
import re
import time
from datetime import datetime

import requests


class LianTongCheckIn:
    def __init__(self, check_item):
        self.check_item = check_item

    # 每日签到
    @staticmethod
    def daysign(session, liantong_data):
        headers = {
            "Host": "m.client.10010.com",
            "Accept": "*/*",
            "User-Agent": "ChinaUnicom4.x/810 CFNetwork/1209 Darwin/20.2.0",
            "Accept-Language": "zh-cn",
        }
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        data = f"reqtime={timestamp}&{liantong_data}"
        try:
            req1 = session.post(url="http://m.client.10010.com/mobileService/login.htm", headers=headers, data=data)
            a_token = req1.cookies.get("a_token")
            if a_token and req1.status_code == 200:
                phone = req1.json().get("default")
                req2 = session.post(
                    url="https://act.10010.com/SigninApp/signin/querySigninActivity.htm?token=" + a_token
                )
                if req2.status_code == 200:
                    req3 = session.post(
                        url="https://act.10010.com/SigninApp/signin/daySign", data="btnPouplePost".encode("utf-8")
                    )
                    if req3.status_code == 200:
                        session.post(url="https://act.10010.com/SigninApp/signin/getIntegral")
                        return f"帐号信息: {phone}"
            return f"帐号信息: 获取失败\n签到信息: 请检查参数是否过期"
        except Exception as e:
            return f"帐号信息: 获取失败\n签到信息: {e}"

    @staticmethod
    def get_encryptmobile(session):
        page = session.post(url="https://m.client.10010.com/dailylottery/static/textdl/userLogin")
        page.encoding = "utf-8"
        match = re.search(r"encryptmobile=\w+", page.text, flags=0)
        usernumber = match.group(0)[14:]
        return usernumber

    def choujiang(self, session):
        choujiang_msg = []
        try:
            numjsp = self.get_encryptmobile(session=session)
            session.post(url="https://m.client.10010.com/mobileservicequery/customerService/share/defaultShare.htm")
            session.get(
                url="https://m.client.10010.com/dailylottery/static/doubleball/firstpage?encryptmobile=" + numjsp
            )
            session.get(
                url="https://m.client.10010.com/dailylottery/static/outdailylottery/getRandomGoodsAndInfo?areaCode=076"
            )
            session.get(
                url="https://m.client.10010.com/dailylottery/static/active/findActivityInfo?areaCode=076&groupByType=&mobile="
                    + numjsp
            )
            for i in range(3):
                luck = session.post(
                    url="https://m.client.10010.com/dailylottery/static/doubleball/choujiang?usernumberofjsp=" + numjsp
                )
                luck.encoding = "utf-8"
                res = luck.json()
                choujiang_msg.append(res["RspMsg"])
        except Exception as e:
            choujiang_msg.append(str(e))
        return "天天抽奖: " + "；".join(choujiang_msg)

    def pointslottery_task(self, session):
        try:
            numjsp = self.get_encryptmobile(session=session)
            one_free = session.post(
                url="https://m.client.10010.com/dailylottery/static/integral/choujiang?usernumberofjsp=" + numjsp
            )
            one_free.encoding = "utf-8"
            res1 = one_free.json()
            jifeng_msg = res1["RspMsg"]
        except Exception as e:
            jifeng_msg = str(e)
        return "积分抽奖: " + jifeng_msg

    @staticmethod
    def gamecentersign_task(session):
        data1 = {"methodType": "signin", "clientVersion": "8.0100", "deviceType": "Android"}
        data2 = {"methodType": "iOSIntegralGet", "gameLevel": "1", "deviceType": "iOS"}
        try:
            game_center = session.post(url="https://m.client.10010.com/producGame_signin", data=data1)
            game_center.encoding = "utf-8"
            res = game_center.json()
            if res["respCode"] == "0000" and res["respDesc"] == "打卡并奖励成功":
                gamecentersign_msg = "游戏中心签到: 获得 " + str(res["currentIntegral"]) + " 积分"
            elif res["respCode"] == "0000":
                gamecentersign_msg = "游戏中心签到: " + res["respDesc"]
            else:
                print(res)
                gamecentersign_msg = "游戏中心签到: 失败"
            game_center_exp = session.post(url="https://m.client.10010.com/producGameApp", data=data2)
            game_center_exp.encoding = "utf-8"
            res1 = game_center_exp.json()
            if res1["code"] == "0000":
                gamecentersign_msg += "\n游戏频道打卡: 获得" + str(res1["integralNum"]) + "积分"
            else:
                gamecentersign_msg += "\n游戏频道打卡: " + res1["msg"]
        except Exception as e:
            gamecentersign_msg = "游戏中心签到：" + str(e)
        return gamecentersign_msg

    @staticmethod
    def day100integral_task(session):
        data = {"from": random.choice("123456789") + "".join(random.choice("0123456789") for i in range(10))}
        try:
            integral = session.post(
                url="https://m.client.10010.com/welfare-mall-front/mobile/integral/gettheintegral/v1", data=data
            )
            integral.encoding = "utf-8"
            res = integral.json()
            return "100定向积分: " + res["msg"]
        except Exception as e:
            return "100定向积分: " + str(e)

    @staticmethod
    def dongaopoints_task(session):
        data = {"from": random.choice("123456789") + "".join(random.choice("0123456789") for i in range(10))}
        trance = [0, 600, 300, 300, 300, 300, 300, 600]
        try:
            dongao_point = session.post(
                url="https://m.client.10010.com/welfare-mall-front/mobile/winterTwo/getIntegral/v1", data=data
            )
            dongao_point.encoding = "utf-8"
            res1 = dongao_point.json()
            dongao_num = session.post(
                url="https://m.client.10010.com/welfare-mall-front/mobile/winterTwo/winterTwoShop/v1", data=data
            )
            dongao_num.encoding = "utf-8"
            res2 = dongao_num.json()
            if res1["resdata"]["code"] == "0000":
                dongao_msg = (
                    "冬奥积分活动: " + res1["resdata"]["desc"] + "，" + str(trance[int(res2["resdata"]["signDays"])]) + "积分"
                )

            else:
                dongao_msg = "冬奥积分活动: " + res1["resdata"]["desc"] + "，" + res2["resdata"]["desc"]
        except Exception as e:
            dongao_msg = "冬奥积分活动: " + str(e)
        return dongao_msg

    @staticmethod
    def get_wotree_glowlist(session):
        response = session.post(url="https://m.client.10010.com/mactivity/arbordayJson/index.htm")
        res = response.json()
        return res["data"]["flowChangeList"]

    def wotree_task(self, session):
        try:
            flow_list = self.get_wotree_glowlist(session=session)
            for flow in flow_list:
                take_flow = session.get(
                    url="https://m.client.10010.com/mactivity/flowData/takeFlow.htm?flowId=" + flow["id"]
                )
                take_flow.encoding = "utf-8"
                res1 = take_flow.json()
                if res1["code"] == "0000":
                    print("沃之树-领流量: 4M 流量")
                else:
                    print("沃之树-领流量: 已领取过")
                time.sleep(1)
            session.post(url="https://m.client.10010.com/mactivity/arbordayJson/getChanceByIndex.htm?index=0")
            grow = session.post(url="https://m.client.10010.com/mactivity/arbordayJson/arbor/3/0/3/grow.htm")
            grow.encoding = "utf-8"
            res2 = grow.json()
            return "沃之树-浇水: 获得" + str(res2["data"]["addedValue"]) + "培养值" + "\n沃之树-领流量: 获得12M流量"
        except Exception as e:
            return "沃之树: " + str(e)

    @staticmethod
    def openbox_task(session):
        data1 = {"thirdUrl": "https://img.client.10010.com/shouyeyouxi/index.html#/youxibaoxiang"}
        data2 = {"methodType": "reward", "deviceType": "Android", "clientVersion": "8.0100", "isVideo": "Y"}
        data3 = {
            "methodType": "taskGetReward",
            "taskCenterId": "187",
            "clientVersion": "8.0100",
            "deviceType": "Android",
        }
        try:
            box = session.post(
                url="https://m.client.10010.com/mobileService/customer/getShareRedisInfo.htm", data=data1
            )
            box.encoding = "utf-8"
            watch_ad = session.post(url="https://m.client.10010.com/game_box", data=data2)
            watch_ad.encoding = "utf-8"
            draw_reward = session.post(url="https://m.client.10010.com/producGameTaskCenter", params=data3)
            draw_reward.encoding = "utf-8"
            res = draw_reward.json()
            if res["code"] == "0000":
                openbox_msg = "100M寻宝箱: " + "获得100M流量"
            else:
                openbox_msg = "100M寻宝箱: " + "任务失败"
        except Exception as e:
            openbox_msg = "100M寻宝箱:" + str(e)
        return openbox_msg

    @staticmethod
    def collectflow_task(session):
        liuliang = 0
        try:
            for i in range(3):
                watch_video = session.post(
                    url="https://act.10010.com/SigninApp/mySignin/addFlow", data={"stepflag": "22"}
                )
                watch_video.encoding = "utf-8"
                res1 = watch_video.json()
                if res1["reason"] == "00":
                    liuliang += int(res1.get("addNum", 0))
                elif res1["reason"] == "01":
                    print("4G流量包-看视频: 已完成")

            for i in range(3):
                download_prog = session.post(
                    url="https://act.10010.com/SigninApp/mySignin/addFlow", data={"stepflag": "23"}
                )
                download_prog.encoding = "utf-8"
                res2 = download_prog.json()
                if res2["reason"] == "00":
                    liuliang += int(res2.get("addNum", 0))
                elif res2["reason"] == "01":
                    print("4G流量包-下软件: 已完成")
        except Exception as e:
            return "4G流量包: " + str(e)
        return "4G流量包: 获得 " + str(liuliang) + "M"

    @staticmethod
    def dayoneg(session):
        try:
            # 观看视频任务
            session.post(url='https://act.10010.com/SigninApp/doTask/finishVideo')
            # 请求任务列表
            get_task_info = session.post(url='https://act.10010.com/SigninApp/doTask/getTaskInfo')
            get_task_info.encoding = 'utf-8'
            get_prize = session.post(url='https://act.10010.com/SigninApp/doTask/getPrize')
            get_prize.encoding = 'utf-8'
            session.post(url='https://act.10010.com/SigninApp/doTask/getTaskInfo')
            res1 = get_task_info.json()
            res2 = get_prize.json()
            if res1['data']['taskInfo']['status'] == '1':
                msg = '1G流量日包: ' + res2['data']['statusDesc']
            else:
                msg = '1G流量日包: ' + res1['data']['taskInfo']['btn']
            time.sleep(1)
        except Exception as e:
            msg = '1G流量日包: 错误，' + str(e)
        return msg

    @staticmethod
    def user_info(session):
        resp = session.get(url="https://m.client.10010.com/mobileService/home/queryUserInfoSeven.htm?showType=3")
        user_info_msg = []
        for one in resp.json().get("data", {}).get("dataList", []):
            user_info_msg.append(one.get("remainTitle") + ": " + one.get("number") + one.get("unit"))
        return "\n".join(user_info_msg)

    def main(self):
        session = requests.session()
        liantong_data = self.check_item.get("data")
        sign_msg = self.daysign(session=session, liantong_data=liantong_data)
        dayoneg_msg = self.dayoneg(session=session)
        choujiang_msg = self.choujiang(session=session)
        pointslottery_msg = self.pointslottery_task(session=session)
        gamecentersign_msg = self.gamecentersign_task(session=session)
        day100integral_msg = self.day100integral_task(session=session)
        dongaopoints_msg = self.dongaopoints_task(session=session)
        wotree_msg = self.wotree_task(session=session)
        openbox_msg = self.openbox_task(session=session)
        collectflow_msg = self.collectflow_task(session=session)
        user_info_msg = self.user_info(session=session)
        msg = (
            f"{sign_msg}\n{user_info_msg}\n{choujiang_msg}\n{pointslottery_msg}\n"
            f"{gamecentersign_msg}\n{day100integral_msg}\n{dongaopoints_msg}\n{wotree_msg}\n"
            f"{openbox_msg}\n{collectflow_msg}\n{dayoneg_msg}"
        )
        return msg


if __name__ == "__main__":
    with open(
        os.path.join(os.path.dirname(os.path.dirname(__file__)), "config/config.json"), "r", encoding="utf-8"
    ) as f:
        datas = json.loads(f.read())
    _check_item = datas.get("LIANTONG_ACCOUNT_LIST", [])[0]
    print(LianTongCheckIn(check_item=_check_item).main())
