# -*- coding: utf-8 -*-
import base64
import hashlib
import hmac
import json
import os
import time
import urllib.parse

import requests


class YouDaoCheckIn:
    def __init__(self, dingtalk_secret, dingtalk_access_token, youdao_cookie_list):
        self.dingtalk_secret = dingtalk_secret
        self.dingtalk_access_token = dingtalk_access_token
        self.youdao_cookie_list = youdao_cookie_list

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
        ad_space = 0
        url = "https://note.youdao.com/yws/api/daupromotion?method=sync"
        res = requests.post(url=url, headers=headers)
        if "error" not in res.text:
            checkin_response = requests.post(
                url="https://note.youdao.com/yws/mapi/user?method=checkin", headers=headers
            )
            for i in range(3):
                ad_response = requests.post(
                    url="https://note.youdao.com/yws/mapi/user?method=adRandomPrompt", headers=headers
                )
                ad_space += ad_response.json()["space"] // 1048576
            if "reward" in res.text:
                sync_space = res.json()["rewardSpace"] // 1048576
                checkin_space = checkin_response.json()["space"] // 1048576
                space = sync_space + checkin_space + ad_space
                youdao_message = "+{0}M".format(space)
            else:
                youdao_message = "获取失败"
        else:
            youdao_message = "Cookie 可能过期"
        return youdao_message

    def main(self):
        for youdao_cookie in self.youdao_cookie_list:
            youdao_cookie = youdao_cookie.get("youdao_cookie")
            headers = {"Cookie": youdao_cookie}
            msg = self.sign(headers=headers)
            msg = f"【有道云笔记签到】\n获取空间: {msg}"
            print(msg)
            if self.dingtalk_secret and self.dingtalk_access_token:
                self.message_to_dingtalk(msg)


if __name__ == '__main__':
    with open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "config.json"), "r", encoding="utf-8") as f:
        data = json.loads(f.read())
    dingtalk_secret = data.get("dingtalk", {}).get("dingtalk_secret")
    dingtalk_access_token = data.get("dingtalk", {}).get("dingtalk_access_token")
    youdao_cookie_list = data.get("youdao", [])
    YouDaoCheckIn(
        dingtalk_secret=dingtalk_secret,
        dingtalk_access_token=dingtalk_access_token,
        youdao_cookie_list=youdao_cookie_list,
    ).main()
