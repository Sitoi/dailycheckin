# -*- coding: utf-8 -*-
import base64
# import binascii
import hashlib
import json
import os
import random

import requests
import urllib3
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
# from Crypto.Cipher import AES
from requests import utils

urllib3.disable_warnings()


class Music163CheckIn:
    def __init__(self, check_item):
        self.check_item = check_item
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/84.0.4147.89 "
            "Safari/537.36",
            "Referer": "http://music.163.com/",
            "Accept-Encoding": "gzip, deflate",
        }

    # @staticmethod
    # def create_secret_key(size):
    #     return str(binascii.hexlify(os.urandom(size))[:16], encoding="utf-8")
    #
    # @staticmethod
    # def aes_encrypt(text, sec_key):
    #     pad = 16 - len(text) % 16
    #     text = text + pad * chr(pad)
    #     encryptor = AES.new(sec_key.encode("utf8"), 2, b"0102030405060708")
    #     ciphertext = encryptor.encrypt(text.encode("utf8"))
    #     ciphertext = str(base64.b64encode(ciphertext), encoding="utf-8")
    #     return ciphertext
    #
    # @staticmethod
    # def rsa_encrypt(text, pub_key, modulus):
    #     text = text[::-1]
    #     rs = int(text.encode("utf-8").hex(), 16) ** int(pub_key, 16) % int(modulus, 16)
    #     return format(rs, "x").zfill(256)
    #
    # def encrypt(self, text):
    #     sec_key = self.create_secret_key(16)
    #     enc_text = self.aes_encrypt(self.aes_encrypt(text, "0CoJUm6Qyw8W8jud"), sec_key)
    #     enc_sec_key = self.rsa_encrypt(
    #         sec_key,
    #         "010001",
    #         (
    #             "00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629"
    #             "ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d"
    #             "813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7 "
    #         ),
    #     )
    #     return {"params": enc_text, "encSecKey": enc_sec_key}

    @staticmethod
    def _encrypt(key, text):
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

    def encrypt(self, text):
        return {
            "params": self._encrypt("TA3YiYCfY2dDJQgg", self._encrypt("0CoJUm6Qyw8W8jud", text)),
            "encSecKey": "84ca47bca10bad09a6b04c5c927ef077d9b9f1e37098aa3eac6ea70eb59df0aa28b691b7e75e4f1f9831754919ea784c8f74fbfadf2898b0be17849fd656060162857830e241aba44991601f137624094c114ea8d17bce815b0cd4e5b8e2fbaba978c6d1d14dc3d1faf852bdd28818031ccdaaa13a6018e1024e2aae98844210",
        }

    def login(self, session, phone, password):
        login_url = "https://music.163.com/weapi/login/cellphone"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/84.0.4147.89 Safari/537.36",
            "Referer": "http://music.163.com/",
            "Accept-Encoding": "gzip, deflate",
            "Cookie": "os=pc; osver=Microsoft-Windows-10-Professional-build-10586-64bit; appver=2.0.3.131777; "
            "channel=netease; __remember_me=true;",
        }
        hl = hashlib.md5()
        hl.update(password.encode(encoding="utf-8"))
        md5_password = str(hl.hexdigest())
        login_data = self.encrypt(
            json.dumps({"phone": phone, "countrycode": "86", "password": md5_password, "rememberLogin": "true"})
        )
        res = session.post(url=login_url, data=login_data, headers=headers)
        ret = res.json()
        if ret["code"] == 200:
            csrf = requests.utils.dict_from_cookiejar(res.cookies)["__csrf"]
            nickname = ret["profile"]["nickname"]
            level_data = self.get_level(session=session, csrf=csrf, login_data=login_data)
            level = level_data["level"]
            now_play_count = level_data["nowPlayCount"]
            next_play_count = level_data["nextPlayCount"]
            return csrf, nickname, level, now_play_count, next_play_count
        else:
            return False, ret.get("message"), 0, 0, 0

    def sign(self, session):
        sign_url = "https://music.163.com/weapi/point/dailyTask"
        res = session.post(url=sign_url, data=self.encrypt('{"type":0}'), headers=self.headers)
        ret = json.loads(res.text)
        if ret["code"] == 200:
            return "签到成功，经验+ " + str(ret["point"])
        elif ret["code"] == -2:
            return "今天已经签到过了"
        else:
            return "签到失败: " + ret["message"]

    def task(self, session, csrf):
        url = "https://music.163.com/weapi/v6/playlist/detail?csrf_token=" + csrf
        recommend_url = "https://music.163.com/weapi/v1/discovery/recommend/resource"
        music_lists = []
        res = session.post(url=recommend_url, data=self.encrypt('{"csrf_token":"' + csrf + '"}'), headers=self.headers)
        ret = res.json()
        if ret["code"] != 200:
            print("获取推荐歌曲失败: ", str(ret["code"]), ":", ret["message"])
        else:
            lists = ret["recommend"]
            music_lists = [(d["id"]) for d in lists]
        music_id = []
        for m in music_lists:
            res = session.post(
                url=url, data=self.encrypt(json.dumps({"id": m, "n": 1000, "csrf_token": csrf})), headers=self.headers,
            )
            ret = json.loads(res.text)
            for i in ret["playlist"]["trackIds"]:
                music_id.append(i["id"])
        post_data = json.dumps(
            {
                "logs": json.dumps(
                    list(
                        map(
                            lambda x: {
                                "action": "play",
                                "json": {
                                    "download": 0,
                                    "end": "playend",
                                    "id": x,
                                    "sourceId": "",
                                    "time": 240,
                                    "type": "song",
                                    "wifi": 0,
                                },
                            },
                            random.sample(music_id, 420 if len(music_id) > 420 else len(music_id)),
                        )
                    )
                )
            }
        )
        res = session.post(url="http://music.163.com/weapi/feedback/weblog", data=self.encrypt(post_data))
        ret = res.json()
        if ret["code"] == 200:
            return "刷听歌量成功"
        else:
            return "刷听歌量失败: " + ret["message"]

    def get_level(self, session, csrf, login_data):
        url = "https://music.163.com/weapi/user/level?csrf_token=" + csrf
        res = session.post(url=url, data=login_data, headers=self.headers)
        ret = json.loads(res.text)
        return ret["data"]

    def main(self):
        phone = self.check_item.get("music163_phone")
        password = self.check_item.get("music163_password")
        session = requests.session()
        csrf, nickname, level, now_play_count, next_play_count = self.login(
            session=session, phone=phone, password=password
        )
        res_sign = ""
        res_task = ""
        if csrf:
            res_sign = self.sign(session=session)
            res_task = self.task(session=session, csrf=csrf)
        msg = (
            f"帐号信息: {nickname}\n当前等级: {level}\n当前听歌数量: {now_play_count}\n"
            f"升级需听歌数量: {next_play_count - now_play_count}\n签到状态: {res_sign}\n刷歌状态: {res_task}"
        )
        return msg


if __name__ == "__main__":
    with open(
        os.path.join(os.path.dirname(os.path.dirname(__file__)), "config/config.json"), "r", encoding="utf-8"
    ) as f:
        datas = json.loads(f.read())
    _check_item = datas.get("MUSIC163_ACCOUNT_LIST", [])[0]
    print(Music163CheckIn(check_item=_check_item).main())
