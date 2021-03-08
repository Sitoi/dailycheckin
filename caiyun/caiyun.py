# -*- coding: utf-8 -*-
import json
import os
import re
from urllib import parse

import requests
from requests import utils


class CaiYunCheckIn:
    def __init__(self, check_item):
        self.check_item = check_item
        self.user_agent = "Mozilla/5.0 (Linux; Android 10; M2007J3SC Build/QKQ1.191222.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36 MCloudApp/7.6.0"

    @staticmethod
    def get_encrypt_time(session):
        payload = parse.urlencode({"op": "currentTimeMillis"})
        resp = session.post(
            url="http://caiyun.feixin.10086.cn:7070/portal/ajax/tools/opRequest.action", data=payload
        ).json()
        if resp.get("code") != 10000:
            print("获取时间戳失败: ", resp["msg"])
            return 0
        return resp.get("result", 0)

    def get_ticket(self, session):
        payload = {"sourceId": 1003, "type": 1, "encryptTime": self.get_encrypt_time(session=session)}
        resp = requests.post(url="https://proxy.xuthus.cc/api/10086_calc_sign", data=payload)
        resp = resp.json()
        if resp.get("code") != 200:
            ticket = False, "加密失败: ", resp.get("msg")
        else:
            ticket = True, resp.get("data")
        return ticket

    @staticmethod
    def user_info(session):
        resp = session.get(url="https://caiyun.feixin.10086.cn:7071/portal/newsignin/index.jsp").text
        account = re.findall(r'var loginAccount = \"(.*?)\";', resp)
        if account:
            account = account[0]
        else:
            account = "未获取到用户信息"
        return account

    def sign(self, session):
        flag, ticket = self.get_ticket(session=session)
        if flag:
            payload = parse.urlencode({"op": "receive", "data": ticket, })
            resp = session.post(
                url="http://caiyun.feixin.10086.cn:7070/portal/ajax/common/caiYunSignIn.action",
                data=payload,
            ).json()
            if resp["code"] != 10000:
                msg = "签到失败:" + resp["msg"]
            else:
                msg = f'月签到天数: {resp["result"]["monthDays"]}\n当前总积分:{resp["result"]["totalPoints"]}'
            return msg
        else:
            return ticket

    def draw(self, session):
        payload = parse.urlencode({"op": "luckDraw", "data": self.get_ticket(session=session)})
        resp = session.post(
            url="http://caiyun.feixin.10086.cn:7070/portal/ajax/common/caiYunSignIn.action",
            data=payload,
        ).json()
        if resp["code"] != 10000:
            return f"抽奖失败: {resp['msg']}"
        else:
            if resp["result"]["type"] == "40160":
                return "抽奖成功: 小狗电器小型手持床铺除螨仪"
            elif resp["result"]["type"] == "40175":
                return "抽奖成功: 飞科男士剃须刀"
            elif resp["result"]["type"] == "40120":
                return "抽奖成功: 京东京造电动牙刷"
            elif resp["result"]["type"] == "40140":
                return "抽奖成功: 10-100M随机长期存储空间"
            elif resp["result"]["type"] == "40165":
                return "抽奖成功: 夏新蓝牙耳机"
            elif resp["result"]["type"] == "40170":
                return "抽奖成功: 欧莱雅葡萄籽护肤套餐"
            else:
                return "抽奖成功: 谢谢参与"

    def main(self):
        caiyun_referer = self.check_item.get("caiyun_referer")
        caiyun_draw = int(self.check_item.get("caiyun_draw", False))
        caiyun_cookie = {
            item.split("=")[0]: item.split("=")[1] for item in self.check_item.get("caiyun_cookie").split("; ")
        }

        session = requests.session()
        requests.utils.add_dict_to_cookiejar(session.cookies, caiyun_cookie)
        session.headers.update({
            "Host": "caiyun.feixin.10086.cn:7070",
            "Accept": "*/*",
            "X-Requested-With": "XMLHttpRequest",
            "User-Agent": self.user_agent,
            "Content-Type": "application/x-www-form-urlencoded",
            "Origin": "http://caiyun.feixin.10086.cn:7070",
            "Referer": caiyun_referer,
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        })
        username = self.user_info(session=session)
        sign_msg = self.sign(session=session)
        if caiyun_draw:
            draw_msg = self.draw(session=session)
        else:
            draw_msg = ""
        msg = f"用户信息: {username}\n{sign_msg}\n{draw_msg}".strip()
        return msg


if __name__ == "__main__":
    with open(
        os.path.join(os.path.dirname(os.path.dirname(__file__)), "config/config.json"), "r", encoding="utf-8"
    ) as f:
        datas = json.loads(f.read())
    _check_item = datas.get("CAIYUN_COOKIE_LIST", [])[0]
    print(CaiYunCheckIn(check_item=_check_item).main())
