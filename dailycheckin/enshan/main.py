import json
import os
import re

import requests
import urllib3

from dailycheckin import CheckIn

urllib3.disable_warnings()


class EnShan(CheckIn):
    name = "恩山无线论坛"

    def __init__(self, check_item):
        self.check_item = check_item

    @staticmethod
    def sign(cookie):
        msg = []
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.125 Safari/537.36",
            "Cookie": cookie,
        }
        response = requests.get(
            url="https://www.right.com.cn/FORUM/home.php?mod=spacecp&ac=credit&showcredit=1",
            headers=headers,
            verify=False,
        )
        try:
            coin = re.findall("恩山币: </em>(.*?)&nbsp;", response.text)[0]
            point = re.findall("<em>积分: </em>(.*?)<span", response.text)[0]
            msg = [
                {
                    "name": "恩山币",
                    "value": coin,
                },
                {
                    "name": "积分",
                    "value": point,
                },
            ]
        except Exception as e:
            msg = [
                {
                    "name": "签到失败",
                    "value": str(e),
                }
            ]
        return msg

    def main(self):
        cookie = self.check_item.get("cookie")
        msg = self.sign(cookie=cookie)
        msg = "\n".join([f"{one.get('name')}: {one.get('value')}" for one in msg])
        return msg


if __name__ == "__main__":
    with open(
        os.path.join(os.path.dirname(os.path.dirname(__file__)), "config.json"),
        encoding="utf-8",
    ) as f:
        datas = json.loads(f.read())
    _check_item = datas.get("ENSHAN", [])[0]
    print(EnShan(check_item=_check_item).main())
