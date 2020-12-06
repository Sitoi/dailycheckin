# -*- coding: utf-8 -*-
import base64
import hashlib
import hmac
import json
import os
import time
import urllib.parse

import requests


class PojieCheckIn:
    """
    吾爱破解论坛签到
    *签到得2个爱币
    """

    def __init__(self, dingtalk_secret, dingtalk_access_token, pojie_cookie_list):
        self.dingtalk_secret = dingtalk_secret
        self.dingtalk_access_token = dingtalk_access_token
        self.pojie_cookie_list = pojie_cookie_list

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

    def sign(self, headers):
        """
        签到
        """
        url = "https://www.52pojie.cn/home.php?mod=task&do=apply&id=2"
        res = requests.get(url=url, headers=headers)
        if "任务已完成" in res.content.decode("gbk"):
            msg = '任务已完成'
        elif "本期您已申请过此任务" in res.content.decode("gbk"):
            msg = '签到过了'
        elif "需要先登录" in res.content.decode("gbk"):
            msg = '未登录，请检查 Cookies'
        else:
            print("（52）签到错误信息", res.content.decode("gbk"))
            msg = "未知错误，检查日志"
        return msg

    def main(self):
        for pojie_cookie in self.pojie_cookie_list:
            pojie_cookie = pojie_cookie.get("pojie_cookie")
            headers = {"Cookie": pojie_cookie}
            msg = self.sign(headers=headers)
            msg = f"【吾爱破解签到】\n签到状态: {msg}"
            print(msg)
            if self.dingtalk_secret and self.dingtalk_access_token:
                self.message_to_dingtalk(msg)


if __name__ == '__main__':
    with open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "config.json"), "r", encoding="utf-8") as f:
        data = json.loads(f.read())
    dingtalk_secret = data.get("dingtalk", {}).get("dingtalk_secret")
    dingtalk_access_token = data.get("dingtalk", {}).get("dingtalk_access_token")
    pojie_cookie_list = data.get("52pojie", [])
    PojieCheckIn(
        dingtalk_secret=dingtalk_secret,
        dingtalk_access_token=dingtalk_access_token,
        pojie_cookie_list=pojie_cookie_list,
    ).main()
