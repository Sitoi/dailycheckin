# -*- coding: utf-8 -*-
import json
import os
import time

import requests
from requests import utils


class SamsungCheckIn:
    def __init__(self, samsung_cookie_list):
        self.samsung_cookie_list = samsung_cookie_list

    @staticmethod
    def sign(session):
        try:
            params = {"ramdon": str(int(round(time.time() * 1000)))}
            user_info = session.get(
                url=f"http://www.samsungmembers.cn/Shared/CheckUserLogin?ramdon=1613969035891", params=params
            ).json()
            username = user_info.get("Data", {}).get("UserName")
        except Exception as e:
            print(e)
            username = "获取用户名失败"
        try:
            current = session.post(url="http://www.samsungmembers.cn/Shared/Sign").json()
            if current.get("State"):
                data = current.get("Data")
                msg = f'获得经验 {data.get("EmpricCount")}, 获得星钻 {data.get("CreditCount")}'
            else:
                msg = current.get("Error")
        except Exception as e:
            msg = f"签到失败\n错误信息: {e}"
        sign_msg = f"用户昵称: {username}\n签到状态: {msg}"
        return sign_msg

    def main(self):
        msg_list = []
        for samsung_cookie in self.samsung_cookie_list:
            samsung_cookie = {
                item.split("=")[0]: item.split("=")[1] for item in samsung_cookie.get("samsung_cookie").split("; ")
            }
            session = requests.session()
            requests.utils.add_dict_to_cookiejar(session.cookies, samsung_cookie)
            session.headers.update(
                {
                    "Accept": "*/*",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36 Edg/88.0.705.74",
                    "X-Requested-With": "XMLHttpRequest",
                    "Origin": "http://www.samsungmembers.cn",
                    "Referer": "http://www.samsungmembers.cn/",
                    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
                }
            )
            sign_msg = self.sign(session=session)
            msg = f"【盖乐世社区】\n{sign_msg}"
            msg_list.append(msg)
        return msg_list


if __name__ == "__main__":
    with open(
        os.path.join(os.path.dirname(os.path.dirname(__file__)), "config/config.json"), "r", encoding="utf-8"
    ) as f:
        datas = json.loads(f.read())
    _samsung_cookie_list = datas.get("SAMSUNG_COOKIE_LIST", [])
    SamsungCheckIn(samsung_cookie_list=_samsung_cookie_list).main()
