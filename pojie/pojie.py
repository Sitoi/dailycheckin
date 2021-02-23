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
            msg = ""
            session = requests.session()
            session.get(url="https://www.52pojie.cn/home.php?mod=task&do=apply&id=2", headers=headers)
            resp = session.get(url="https://www.52pojie.cn/home.php?mod=task&do=draw&id=2", headers=headers)
            content = re.findall(r'<div id="messagetext".*?\n<p>(.*?)</p>', resp.text)[0]
            if "您需要先登录才能继续本操作" in resp.text:
                msg += "吾爱破解 cookie 失效"
            elif "恭喜" in resp.text:
                msg += "吾爱破解签到成功"
            else:
                msg += content
        except Exception as e:
            if "安域防护节点" in resp.text:
                print("触发吾爱破解安全防护，访问出错。自行修改脚本运行时间和次数，总有能访问到的时间")
            print("吾爱破解出错")
            msg += "吾爱破解出错"
        return msg

    def main(self):
        msg_list = []
        for pojie_cookie in self.pojie_cookie_list:
            pojie_cookie = pojie_cookie.get("pojie_cookie")
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36",
                "Cookie": pojie_cookie,
                "ContentType": "text/html;charset=gbk",
            }
            uid = re.findall(r"htVD_2132_lastcheckfeed=(.*?);", pojie_cookie)[0].split("%7C")[0]
            sign_msg = self.sign(headers=headers)
            msg = f"【吾爱破解】\n帐号信息: {uid}\n签到状态: {sign_msg}"
            msg_list.append(msg)
        return msg_list


if __name__ == "__main__":
    with open(
        os.path.join(os.path.dirname(os.path.dirname(__file__)), "config/config.json"), "r", encoding="utf-8"
    ) as f:
        datas = json.loads(f.read())
    _pojie_cookie_list = datas.get("POJIE_COOKIE_LIST", [])
    PojieCheckIn(pojie_cookie_list=_pojie_cookie_list).main()
