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


class VQQCheckIn:
    """
    腾讯视频签到
    """

    def __init__(self, dingtalk_secret, dingtalk_access_token, vqq_cookie_list):

        self.dingtalk_secret = dingtalk_secret
        self.dingtalk_access_token = dingtalk_access_token
        self.vqq_cookie_list = vqq_cookie_list

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

    def sign_once(self, session, headers):
        """
        一次签到
        """
        url = "http://v.qq.com/x/bu/mobile_checkin?isDarkMode=0&uiType=REGULAR"
        res = session.get(url=url, headers=headers)
        match = re.search(r'isMultiple" />\s+(.*?)\s+<', res.text)
        if match:
            value = match.group(1)
            msg = f"成长值{value}"
        else:
            msg = "签到失败(可能已签到)"
        return msg

    def sign_twice(self, session, headers):
        """
        二次签到
        """
        this_time = int(round(time.time() * 1000))
        url = "https://vip.video.qq.com/fcgi-bin/comm_cgi?name=hierarchical_task_system&cmd=2&_=" + str(this_time)
        res = session.get(url=url, headers=headers)
        ret = re.search('ret": (.*?),|}', res.text).group(1)
        if ret == "0":
            value = re.search('checkin_score": (.*?),', res.text).group(1)
            msg = f"成长值x{value}"
        else:
            msg = res.text
        return msg

    def main(self):
        for vqq_cookie in self.vqq_cookie_list:
            vqq_cookie = vqq_cookie.get("vqq_cookie")
            session = requests.session()
            headers = {"Cookie": vqq_cookie}
            sign_once_msg = self.sign_once(session=session, headers=headers)
            sign_twice_msg = self.sign_twice(session=session, headers=headers)
            msg = f"【腾讯视频签到】\n签到奖励1: {sign_once_msg}\n签到奖励2: {sign_twice_msg}"
            print(msg)
            if self.dingtalk_secret and self.dingtalk_access_token:
                self.message_to_dingtalk(msg)


if __name__ == '__main__':
    with open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "config.json"), "r", encoding="utf-8") as f:
        data = json.loads(f.read())
    dingtalk_secret = data.get("dingtalk", {}).get("dingtalk_secret")
    dingtalk_access_token = data.get("dingtalk", {}).get("dingtalk_access_token")
    vqq_cookie_list = data.get("vqq", [])
    VQQCheckIn(
        dingtalk_secret=dingtalk_secret,
        dingtalk_access_token=dingtalk_access_token,
        vqq_cookie_list=vqq_cookie_list,
    ).main()
