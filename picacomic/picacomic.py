# -*- coding: utf-8 -*-
import hashlib
import hmac
import json
import os
import random
import string
import time

import requests


class PicacomicCheckIn:
    def __init__(self, check_item):
        self.check_item = check_item

    @staticmethod
    def generate_headers(path: str, data: dict = None, token: str = None):
        api_key = "C69BAF41DA5ABD1FFEDC6D2FEA56B"
        api_secret = "~d}$Q7$eIni=V)9\\RK/P.RM4;9[7|@/CA}b~OW!3?EV`:<>M7pddUBL5n|0/*Cn"
        headers = {
            "api-key": api_key,
            "accept": "application/vnd.picacomic.com.v1+json",
            "app-channel": "2",
            "app-version": "2.2.1.2.3.3",
            "app-uuid": "defaultUuid",
            "app-platform": "android",
            "app-build-version": "44",
            "User-Agent": "okhttp/3.8.1",
            "image-quality": "original",
        }
        current_time = str(int(time.time()))
        nonce = "".join(random.choices(string.ascii_lowercase + string.digits, k=32))
        raw = path + current_time + nonce + "POST" + api_key
        raw = raw.lower()
        h = hmac.new(api_secret.encode(), digestmod=hashlib.sha256)
        h.update(raw.encode())
        signature = h.hexdigest()
        headers["time"] = current_time
        headers["nonce"] = nonce
        headers["signature"] = signature
        if data is not None:
            headers["Content-Type"] = "application/json; charset=UTF-8"
        if token is not None:
            headers["authorization"] = token
        return headers

    def sign(self, email, password):
        try:
            data = {"email": email, "password": password}
            sign_headers = self.generate_headers(path="auth/sign-in", data=data)
            sign_response = requests.post(
                url="https://picaapi.picacomic.com/auth/sign-in",
                data=json.dumps({"email": "sitoi", "password": "123456st"}),
                headers=sign_headers,
                timeout=60,
            ).json()
            token = sign_response.get("data", {}).get("token")
            punch_headers = self.generate_headers(path="users/punch-in", token=token)
            response = requests.post(
                url="https://picaapi.picacomic.com/users/punch-in", headers=punch_headers, timeout=60
            ).json()
            if response.get("data", {}).get("res", {}).get("status", {}) == "ok":
                msg = "打卡成功"
            else:
                msg = "重复签到"
        except Exception as e:
            msg = str(e)
        return msg

    def main(self):
        picacomic_email = self.check_item.get("picacomic_email")
        picacomic_password = self.check_item.get("picacomic_password")
        sign_msg = self.sign(email=picacomic_email, password=picacomic_password)
        msg = f"帐号信息: {picacomic_email}\n签到状态: {sign_msg}"
        return msg


if __name__ == "__main__":
    with open(
        os.path.join(os.path.dirname(os.path.dirname(__file__)), "config/config.json"), "r", encoding="utf-8"
    ) as f:
        datas = json.loads(f.read())
    _check_item = datas.get("PICACOMIC_ACCOUNT_LIST", [])[0]
    print(PicacomicCheckIn(check_item=_check_item).main())
