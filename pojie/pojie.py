# -*- coding: utf-8 -*-
import json
import os
import re

import requests


class PojieCheckIn:
    def __init__(self, pojie_cookie_list):
        self.pojie_cookie_list = pojie_cookie_list

    @staticmethod
    def sign(headers):
        try:
            url = "https://www.52pojie.cn/home.php?mod=task&do=apply&id=2"
            res = requests.get(url=url, headers=headers)
            if "任务已完成" in res.content.decode("gbk"):
                msg = "任务已完成"
            elif "本期您已申请过此任务" in res.content.decode("gbk"):
                msg = "签到过了"
            elif "需要先登录" in res.content.decode("gbk"):
                msg = "未登录，请检查 Cookies"
            else:
                print("（52）签到错误信息", res.content.decode("gbk"))
                msg = "未知错误，检查日志"
        except Exception as e:
            print("错误信息", str(e))
            msg = "未知错误，检查日志"
        return msg

    def main(self):
        msg_list = []
        for pojie_cookie in self.pojie_cookie_list:
            pojie_cookie = pojie_cookie.get("pojie_cookie")
            uid = re.findall(r"htVD_2132_lastcheckfeed=(.*?);", pojie_cookie)[0].split("%7C")[0]
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.60",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "Referer": "https://www.52pojie.cn/index.php",
                "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,fr;q=0.5,pl;q=0.4",
                "cookie": pojie_cookie
            }
            msg = self.sign(headers=headers)
            msg = f"【吾爱破解签到】\n帐号信息: {uid}\n签到状态: {msg}"
            print(msg)
            msg_list.append(msg)
        return msg_list


if __name__ == "__main__":
    with open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "config.json"), "r", encoding="utf-8") as f:
        datas = json.loads(f.read())
    _pojie_cookie_list = datas.get("POJIE_COOKIE_LIST", [])
    PojieCheckIn(pojie_cookie_list=_pojie_cookie_list).main()
