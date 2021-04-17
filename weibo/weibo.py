# -*- coding: utf-8 -*-
import json
import os
from urllib import parse

import requests
import urllib3

urllib3.disable_warnings()


class WeiBoCheckIn:
    def __init__(self, check_item):
        self.check_item = check_item

    @staticmethod
    def sign(token):
        headers = {"User-Agent": "Weibo/52588 (iPhone; iOS 14.5; Scale/3.00)"}
        response = requests.get(
            url=f"https://api.weibo.cn/2/checkin/add?c=iphone&{token}", headers=headers, verify=False
        )
        result = response.json()
        if result.get("status") == 10000:
            msg = f'连续签到: {result.get("data").get("continuous")}天\n本次收益: {result.get("data").get("desc")}'
        elif result.get("errno") == 30000:
            msg = f"每日签到: 已签到"
        elif result.get("status") == 90005:
            msg = f'每日签到: {result.get("msg")}'
        else:
            msg = f"每日签到: 签到失败"
        return msg

    @staticmethod
    def card(token):
        headers = {"User-Agent": "Weibo/52588 (iPhone; iOS 14.5; Scale/3.00)"}
        response = requests.get(
            url=f"https://api.weibo.cn/2/!/ug/king_act_home?c=iphone&{token}", headers=headers, verify=False
        )
        result = response.json()
        if result.get("status") == 10000:
            nickname = result.get("data").get("user").get("nickname")
            msg = (
                f'用户昵称: {nickname}\n每日打卡: {result.get("data").get("signin").get("title").split("<")[0]}天\n'
                f'积分总计: {result.get("data").get("user").get("energy")}'
            )
        else:
            msg = f"每日打卡: 活动过期或失效"
        return msg

    @staticmethod
    def pay(token):
        headers = {
            "Accept-Encoding": "gzip, deflate",
            "Connection": "keep-alive",
            "Content-Type": "application/x-www-form-urlencoded",
            "Host": "pay.sc.weibo.com",
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Weibo (iPhone10,1__weibo__11.2.1__iphone__os14.5)",
        }
        data = token + "&lang=zh_CN&wm=3333_2001"
        response = requests.post(
            url=f"https://pay.sc.weibo.com/aj/mobile/home/welfare/signin/do", headers=headers, data=data, verify=False
        )
        try:
            result = response.json()
            if result.get("status") == 1:
                msg = f'微博钱包: {result.get("score")} 积分'
            elif result.get("status") == 2:
                msg = f"微博钱包: 已签到"
                info_response = requests.post(
                    url="https://pay.sc.weibo.com/api/client/sdk/app/balance", headers=headers, data=data
                )
                info_result = info_response.json()
                msg += f"\n当前现金: {info_result.get('data').get('balance')} 元"
            else:
                msg = f"微博钱包: Cookie失效"
            return msg
        except Exception as e:
            msg = f"微博钱包: Cookie失效"
            return msg

    def main(self):
        weibo_show_url = self.check_item.get("weibo_show_url")
        query_dict = dict(parse.parse_qsl(parse.urlsplit(weibo_show_url).query))
        token = "&".join([f"{key}={value}" for key, value in query_dict.items() if key in ["from", "uid", "s", "gsid"]])
        sign_msg = self.sign(token=token)
        card_msg = self.card(token=token)
        pay_msg = self.pay(token=token)
        msg = f"{sign_msg}\n{card_msg}\n{pay_msg}"
        return msg


if __name__ == "__main__":
    with open(
        os.path.join(os.path.dirname(os.path.dirname(__file__)), "config/config.json"), "r", encoding="utf-8"
    ) as f:
        datas = json.loads(f.read())
    _check_item = datas.get("WEIBO_COOKIE_LIST", [])[0]
    print(WeiBoCheckIn(check_item=_check_item).main())
