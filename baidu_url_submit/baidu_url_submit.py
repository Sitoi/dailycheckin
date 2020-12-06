# -*- coding: utf-8 -*-
import base64
import hashlib
import hmac
import json
import os
import time
import urllib.parse
from urllib import parse

import requests


class BaiduUrlSubmit:
    def __init__(self, dingtalk_secret, dingtalk_access_token, baidu_url_submit_list):
        self.dingtalk_secret = dingtalk_secret
        self.dingtalk_access_token = dingtalk_access_token
        self.baidu_url_submit_list = baidu_url_submit_list

    def message_to_dingtalk(self, content: str):
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

    def url_submit(self, data_url: str, submit_url: str, times: int = 100) -> str:
        site = parse.parse_qs(parse.urlsplit(submit_url).query).get("site")[0]
        urls_data = requests.get(url=data_url)
        remian = 100000
        success_count = 0
        error_count = 0
        for one in range(times):
            response = requests.post(url=submit_url, data=urls_data)
            if response.json().get("success"):
                remian = response.json().get("remain")
                success_count += response.json().get("success")
            else:
                error_count += 1
        msg = (
            f"【百度站点提交】\n站点地址: {site}\n当天剩余的可推送 url 条数: {remian}\n成功推送的 url 条数: {success_count}\n"
            f"成功推送的 url 次数: {times - error_count}\n失败推送的 url 次数: {error_count}"
        )
        return msg

    def main(self):
        for baidu_url_submit in self.baidu_url_submit_list:
            data_url = baidu_url_submit.get("data_url")
            submit_url = baidu_url_submit.get("submit_url")
            times = int(baidu_url_submit.get("times", 100))
            if data_url and submit_url:
                msg = self.url_submit(data_url=data_url, submit_url=submit_url, times=times)
                print(msg)
                if self.dingtalk_secret and self.dingtalk_access_token:
                    self.message_to_dingtalk(msg)


if __name__ == "__main__":
    with open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "config.json"), "r", encoding="utf-8") as f:
        data = json.loads(f.read())
    dingtalk_secret = data.get("dingtalk", {}).get("dingtalk_secret")
    dingtalk_access_token = data.get("dingtalk", {}).get("dingtalk_access_token")
    baidu_url_submit_list = data.get("BaiduUrlSubmit", [])
    BaiduUrlSubmit(
        dingtalk_secret=dingtalk_secret,
        dingtalk_access_token=dingtalk_access_token,
        baidu_url_submit_list=baidu_url_submit_list,
    ).main()
