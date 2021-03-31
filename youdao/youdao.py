# -*- coding: utf-8 -*-
import json
import os

import requests


class YouDaoCheckIn:
    def __init__(self, check_item):
        self.check_item = check_item

    @staticmethod
    def sign(cookies):
        ad_space = 0
        refresh_cookies_res = requests.get("http://note.youdao.com/login/acc/pe/getsess?product=YNOTE", cookies=cookies)
        cookies = dict(refresh_cookies_res.cookies)
        url = "https://note.youdao.com/yws/api/daupromotion?method=sync"
        res = requests.post(url=url, cookies=cookies)
        if "error" not in res.text:
            checkin_response = requests.post(
                url="https://note.youdao.com/yws/mapi/user?method=checkin", cookies=cookies
            )
            for i in range(3):
                ad_response = requests.post(
                    url="https://note.youdao.com/yws/mapi/user?method=adRandomPrompt", cookies=cookies
                )
                ad_space += ad_response.json().get("space", 0) // 1048576
            if "reward" in res.text:
                sync_space = res.json().get("rewardSpace", 0) // 1048576
                checkin_space = checkin_response.json().get("space", 0) // 1048576
                space = sync_space + checkin_space + ad_space
                youdao_message = "+{0}M".format(space)
            else:
                youdao_message = "获取失败"
        else:
            youdao_message = "Cookie 可能过期"
        return youdao_message

    def main(self):
        youdao_cookie = {
            item.split("=")[0]: item.split("=")[1] for item in self.check_item.get("youdao_cookie").split("; ")
        }
        try:
            ynote_pers = youdao_cookie.get("YNOTE_PERS", "")
            uid = ynote_pers.split("||")[-2]
        except Exception as e:
            print(f"获取用户信息失败: {e}")
            uid = "未获取到用户信息"
        msg = self.sign(cookies=youdao_cookie)
        msg = f"帐号信息: {uid}\n获取空间: {msg}"
        return msg


if __name__ == "__main__":
    with open(
        os.path.join(os.path.dirname(os.path.dirname(__file__)), "config/config.json"), "r", encoding="utf-8"
    ) as f:
        datas = json.loads(f.read())
    _check_item = datas.get("YOUDAO_COOKIE_LIST", [])[0]
    print(YouDaoCheckIn(check_item=_check_item).main())
