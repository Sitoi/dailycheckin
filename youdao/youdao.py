# -*- coding: utf-8 -*-
import json
import os
import re

import requests


class YouDaoCheckIn:
    def __init__(self, youdao_cookie_list):
        self.youdao_cookie_list = youdao_cookie_list

    @staticmethod
    def sign(headers):
        ad_space = 0
        url = "https://note.youdao.com/yws/api/daupromotion?method=sync"
        res = requests.post(url=url, headers=headers)
        if "error" not in res.text:
            checkin_response = requests.post(
                url="https://note.youdao.com/yws/mapi/user?method=checkin", headers=headers
            )
            for i in range(3):
                ad_response = requests.post(
                    url="https://note.youdao.com/yws/mapi/user?method=adRandomPrompt", headers=headers
                )
                ad_space += ad_response.json()["space"] // 1048576
            if "reward" in res.text:
                sync_space = res.json()["rewardSpace"] // 1048576
                checkin_space = checkin_response.json()["space"] // 1048576
                space = sync_space + checkin_space + ad_space
                youdao_message = "+{0}M".format(space)
            else:
                youdao_message = "获取失败"
        else:
            youdao_message = "Cookie 可能过期"
        return youdao_message

    def main(self):
        msg_list = []
        for youdao_cookie in self.youdao_cookie_list:
            youdao_cookie = youdao_cookie.get("youdao_cookie")
            ynote_pers = re.findall(r"YNOTE_PERS=(.*?);", youdao_cookie)[0]
            uid = ynote_pers.split("||")[-2]
            headers = {"Cookie": youdao_cookie}
            msg = self.sign(headers=headers)
            msg = f"【有道云笔记签到】\n帐号信息: {uid}\n获取空间: {msg}"
            print(msg)
            msg_list.append(msg)
        return msg_list


if __name__ == "__main__":
    with open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "config.json"), "r", encoding="utf-8") as f:
        datas = json.loads(f.read())
    _youdao_cookie_list = datas.get("YOUDAO_COOKIE_LIST", [])
    YouDaoCheckIn(youdao_cookie_list=_youdao_cookie_list).main()
