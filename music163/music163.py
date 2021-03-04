# -*- coding: utf-8 -*-
import base64
import hashlib
import json
import os

import requests
import urllib3
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from requests import utils

urllib3.disable_warnings()


class Music163CheckIn:
    def __init__(self, check_item):
        self.check_item = check_item

    @staticmethod
    def md5(text):
        hl = hashlib.md5()
        hl.update(text.encode(encoding="utf-8"))
        return hl.hexdigest()

    @staticmethod
    def encrypt(key, text):
        backend = default_backend()
        cipher = Cipher(algorithms.AES(key.encode("utf8")), modes.CBC(b"0102030405060708"), backend=backend)
        encryptor = cipher.encryptor()
        length = 16
        count = len(text.encode("utf-8"))
        if count % length != 0:
            add = length - (count % length)
        else:
            add = 16
        pad = chr(add)
        text1 = text + (pad * add)
        ciphertext = encryptor.update(text1.encode("utf-8")) + encryptor.finalize()
        crypted_str = str(base64.b64encode(ciphertext), encoding="utf-8")
        return crypted_str

    def protect(self, text):
        return {
            "params": self.encrypt("TA3YiYCfY2dDJQgg", self.encrypt("0CoJUm6Qyw8W8jud", text)),
            "encSecKey": "84ca47bca10bad09a6b04c5c927ef077d9b9f1e37098aa3eac6ea70eb59df0aa28b691b7e75e4f1f9831754919ea784c8f74fbfadf2898b0be17849fd656060162857830e241aba44991601f137624094c114ea8d17bce815b0cd4e5b8e2fbaba978c6d1d14dc3d1faf852bdd28818031ccdaaa13a6018e1024e2aae98844210",
        }

    def sign(self, session, phone, password):
        sign_msg, music_count_msg = None, None
        url = "https://music.163.com/weapi/login/cellphone"
        daily_task_url = "https://music.163.com/weapi/point/dailyTask"
        resource_url = "https://music.163.com/weapi/v1/discovery/recommend/resource"
        logindata = {
            "phone": phone,
            "countrycode": "86",
            "password": self.md5(password),
            "rememberLogin": "true",
        }
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36",
            "Referer": "http://music.163.com/",
            "Accept-Encoding": "gzip, deflate",
        }
        headers2 = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36",
            "Referer": "http://music.163.com/",
            "Accept-Encoding": "gzip, deflate",
            "Cookie": "os=pc; osver=Microsoft-Windows-10-Professional-build-10586-64bit; appver=2.0.3.131777; channel=netease; __remember_me=true;",
        }

        res = session.post(url=url, data=self.protect(json.dumps(logindata)), headers=headers2, verify=False)
        temp_cookie = res.cookies
        res_data = res.json()
        if res_data["code"] != 200:
            sign_msg = "登录失败！请检查密码是否正确！"
            return sign_msg, music_count_msg
        res = session.post(url=daily_task_url, data=self.protect('{"type":0}'), headers=headers, verify=False)
        res_data = json.loads(res.text)
        if res_data["code"] != 200 and res_data["code"] != -2:
            sign_msg = res_data["msg"]
        else:
            if res_data["code"] == 200:
                sign_msg = "签到成功，经验+" + str(res_data["point"])
            else:
                sign_msg = "重复签到"

        res = session.post(
            url=resource_url,
            data=self.protect('{"csrf_token":"' + requests.utils.dict_from_cookiejar(temp_cookie)["__csrf"] + '"}'),
            headers=headers,
            verify=False,
        )
        res_data = json.loads(res.text, strict=False)
        count = 0
        buffer = []
        for x in res_data["recommend"]:
            url = (
                "https://music.163.com/weapi/v3/playlist/detail?csrf_token="
                + requests.utils.dict_from_cookiejar(temp_cookie)["__csrf"]
            )
            protect_data = {
                "id": x["id"],
                "n": 1000,
                "csrf_token": requests.utils.dict_from_cookiejar(temp_cookie)["__csrf"],
            }
            res = session.post(url=url, data=self.protect(json.dumps(protect_data)), headers=headers, verify=False)
            res_data = json.loads(res.text, strict=False)
            buffer = []
            count = 0
            for j in res_data["playlist"]["trackIds"]:
                data2 = {
                    "action": "play",
                    "json": {
                        "download": 0,
                        "end": "playend",
                        "id": j["id"],
                        "sourceId": "",
                        "time": "240",
                        "type": "type",
                        "wifi": 0,
                    },
                }
                buffer.append(data2)
                count += 1
                if count >= 310:
                    break
            if count >= 310:
                break
        postdata = {"logs": json.dumps(buffer)}
        res = session.post(
            url="http://music.163.com/weapi/feedback/weblog", data=self.protect(json.dumps(postdata)), verify=False
        )
        res_data = json.loads(res.text, strict=False)
        if res_data["code"] == 200:
            music_count_msg = f"{count} 首"
        else:
            music_count_msg = res_data["message"]
        return sign_msg, music_count_msg

    def main(self):
        phone = self.check_item.get("music163_phone")
        password = self.check_item.get("music163_password")
        session = requests.session()
        sign_msg, music_count_msg = self.sign(session=session, phone=phone, password=password)
        msg = f"帐号信息: {phone}\n签到状态: {sign_msg}\n刷歌数量: {music_count_msg}"
        return msg


if __name__ == "__main__":
    with open(
        os.path.join(os.path.dirname(os.path.dirname(__file__)), "config/config.json"), "r", encoding="utf-8"
    ) as f:
        datas = json.loads(f.read())
    _check_item = datas.get("MUSIC163_ACCOUNT_LIST", [])[0]
    print(Music163CheckIn(check_item=_check_item).main())
