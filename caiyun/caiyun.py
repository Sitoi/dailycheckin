# -*- coding: utf-8 -*-
import base64
import json
import os
import re
from urllib import parse

import requests
from requests import utils

import rsa


class CaiYunCheckIn:
    def __init__(self, check_item):
        self.check_item = check_item
        self.public_key = """-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCJ6kiv4v8ZcbDiMmyTKvGzxoPR3fTLj/uRuu6dUypy6zDW+EerThAYON172YigluzKslU1PD9+PzPPHLU/cv81q6KYdT+B5w29hlKkk5tNR0PcCAM/aRUQZu9abnl2aAFQow576BRvIS460urnju+Bu1ZtV+oFM+yQu04OSnmOpwIDAQAB
-----END PUBLIC KEY-----"""

    @staticmethod
    def get_encrypt_time(session):
        payload = parse.urlencode({"op": "currentTimeMillis"})
        resp = session.post(
            url="https://caiyun.feixin.10086.cn:7071/portal/ajax/tools/opRequest.action", data=payload
        ).json()
        if resp.get("code") != 10000:
            print("获取时间戳失败: ", resp["msg"])
            return 0
        return resp.get("result", 0)

    def get_ticket(self, session):
        payload = json.dumps({"sourceId": 1003, "type": 1, "encryptTime": self.get_encrypt_time(session=session)})
        pubkey = rsa.PublicKey.load_pkcs1_openssl_pem(self.public_key)
        crypto = b""
        divide = int(len(payload) / 117)
        divide = divide if (divide > 0) else divide + 1
        line = divide if (len(payload) % 117 == 0) else divide + 1
        for i in range(line):
            crypto += rsa.encrypt(payload[i * 117: (i + 1) * 117].encode(), pubkey)
        crypto1 = base64.b64encode(crypto)
        return crypto1.decode()

    @staticmethod
    def user_info(session):
        resp = session.get(url="https://caiyun.feixin.10086.cn:7071/portal/newsignin/index.jsp").text
        account = re.findall(r"var loginAccount = \"(.*?)\";", resp)
        if account:
            account = account[0]
        else:
            account = "未获取到用户信息"
        return account

    def sign(self, session):
        ticket = self.get_ticket(session=session)
        payload = parse.urlencode({"op": "receive", "data": ticket})
        resp = session.post(
            url="https://caiyun.feixin.10086.cn:7071/portal/ajax/common/caiYunSignIn.action", data=payload,
        ).json()
        if resp["code"] != 10000:
            msg = "签到失败:" + resp["msg"]
        else:
            msg = f'月签到天数: {resp["result"]["monthDays"]}\n当前总积分:{resp["result"]["totalPoints"]}'
        return msg

    def main(self):
        caiyun_cookie = {
            item.split("=")[0]: item.split("=")[1] for item in self.check_item.get("caiyun_cookie").split("; ")
        }
        session = requests.session()
        requests.utils.add_dict_to_cookiejar(session.cookies, caiyun_cookie)
        session.headers.update(
            {
                "User-Agent": "Mozilla/5.0 (Linux; Android 10; M2007J3SC Build/QKQ1.191222.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36 MCloudApp/7.6.0",
                "Content-Type": "application/x-www-form-urlencoded",
                "Origin": "https://caiyun.feixin.10086.cn:7071",
                "Referer": "https://caiyun.feixin.10086.cn:7071/portal/newsignin/index.jsp",
            }
        )
        username = self.user_info(session=session)
        sign_msg = self.sign(session=session)
        msg = f"用户信息: {username}\n{sign_msg}".strip()
        return msg


if __name__ == "__main__":
    with open(
        os.path.join(os.path.dirname(os.path.dirname(__file__)), "config/config.json"), "r", encoding="utf-8"
    ) as f:
        datas = json.loads(f.read())
    _check_item = datas.get("CAIYUN_COOKIE_LIST", [])[0]
    print(CaiYunCheckIn(check_item=_check_item).main())
