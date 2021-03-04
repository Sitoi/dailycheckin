# -*- coding: utf-8 -*-
import json
import os
import re

import requests


class YouDaoCheckIn:
    def __init__(self, check_item):
        self.check_item = check_item

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
        youdao_cookie = self.check_item.get("youdao_cookie")
        ynote_pers = re.findall(r"YNOTE_PERS=(.*?);", youdao_cookie)[0]
        uid = ynote_pers.split("||")[-2]
        headers = {"Cookie": youdao_cookie}
        msg = self.sign(headers=headers)
        msg = f"帐号信息: {uid}\n获取空间: {msg}"
        return msg


if __name__ == "__main__":
    with open(
        os.path.join(os.path.dirname(os.path.dirname(__file__)), "config/config.json"), "r", encoding="utf-8"
    ) as f:
        datas = json.loads(f.read())
    _check_item = datas.get("YOUDAO_COOKIE_LIST", [])
    YouDaoCheckIn(check_item=_check_item).main()
