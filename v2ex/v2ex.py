# -*- coding: utf-8 -*-
import json
import os
import re

import requests
import urllib3
from requests import utils

urllib3.disable_warnings()


class V2exCheckIn:
    def __init__(self, v2ex_cookie_list):
        self.v2ex_cookie_list = v2ex_cookie_list

    @staticmethod
    def sign(session):
        msg = ""
        response = session.get(url="https://www.v2ex.com/mission/daily", verify=False)
        pattern = (
            r"<input type=\"button\" class=\"super normal button\""
            r" value=\".*?\" onclick=\"location\.href = \'(.*?)\';\" />"
        )
        urls = re.findall(pattern=pattern, string=response.text)
        url = urls[0] if urls else None
        if url != "/balance":
            headers = {"Referer": "https://www.v2ex.com/mission/daily"}
            data = {"once": url.split("=")[-1]}
            _ = session.get(url="https://www.v2ex.com" + url, verify=False, headers=headers, params=data)
        response = session.get(url="https://www.v2ex.com/balance", verify=False)
        total = re.findall(
            pattern=r"<td class=\"d\" style=\"text-align: right;\">(\d+\.\d+)</td>", string=response.text
        )
        total = total[0] if total else "签到失败"
        today = re.findall(pattern=r'<td class="d"><span class="gray">(.*?)</span></td>', string=response.text)
        today = today[0] if today else "签到失败"
        username = re.findall(pattern=r"<a href=\"/member/.*?\" class=\"top\">(.*?)</a>", string=response.text)
        username = username[0] if username else "用户名获取失败"
        msg += f"帐号信息: {username}\n今日签到: {today}\n帐号余额: {total}"
        response = session.get(url="https://www.v2ex.com/mission/daily", verify=False)
        data = re.findall(pattern=r"<div class=\"cell\">(.*?)天</div>", string=response.text)
        data = data[0] + "天" if data else "获取连续签到天数失败"
        msg += f"\n签到天数: {data}"
        msg = msg.strip()
        return msg

    def main(self):
        msg_list = []
        for v2ex_cookie in self.v2ex_cookie_list:
            v2ex_cookie = {
                item.split("=")[0]: item.split("=")[1] for item in v2ex_cookie.get("v2ex_cookie").split("; ")
            }
            session = requests.session()
            requests.utils.add_dict_to_cookiejar(session.cookies, v2ex_cookie)
            session.headers.update(
                {
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.66",
                    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
                }
            )
            sign_msg = self.sign(session=session)
            msg = f"【V2EX 论坛】\n{sign_msg}"
            msg_list.append(msg)
        return msg_list


if __name__ == "__main__":
    with open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "config.json"), "r", encoding="utf-8") as f:
        datas = json.loads(f.read())
    _v2ex_cookie_list = datas.get("V2EX_COOKIE_LIST", [])
    V2exCheckIn(v2ex_cookie_list=_v2ex_cookie_list).main()
