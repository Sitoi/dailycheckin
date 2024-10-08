import json
import os
from urllib import parse

import requests

from dailycheckin import CheckIn


class Baidu(CheckIn):
    name = "百度站点提交"

    def __init__(self, check_item: dict):
        self.check_item = check_item

    @staticmethod
    def url_submit(data_url: str, submit_url: str, times: int = 100) -> str:
        site = parse.parse_qs(parse.urlsplit(submit_url).query).get("site")[0]
        urls_data = requests.get(url=data_url)
        remain = 100000
        success_count = 0
        error_count = 0
        for one in range(times):
            try:
                response = requests.post(url=submit_url, data=urls_data)
                if response.json().get("success"):
                    remain = response.json().get("remain")
                    success_count += response.json().get("success")
                else:
                    error_count += 1
            except Exception as e:
                print(e)
                error_count += 1
        msg = [
            {"name": "站点地址", "value": site},
            {"name": "剩余条数", "value": remain},
            {"name": "成功条数", "value": success_count},
            {"name": "成功次数", "value": times - error_count},
            {"name": "失败次数", "value": error_count},
        ]
        return msg

    def main(self):
        data_url = self.check_item.get("data_url")
        submit_url = self.check_item.get("submit_url")
        times = int(self.check_item.get("times", 100))
        if data_url and submit_url:
            msg = self.url_submit(data_url=data_url, submit_url=submit_url, times=times)
        else:
            msg = {"name": "站点配置", "value": "配置错误"}
        msg = "\n".join([f"{one.get('name')}: {one.get('value')}" for one in msg])
        return msg


if __name__ == "__main__":
    with open(
        os.path.join(os.path.dirname(os.path.dirname(__file__)), "config.json"),
        encoding="utf-8",
    ) as f:
        datas = json.loads(f.read())
    _check_item = datas.get("BAIDU", [])[0]
    print(Baidu(check_item=_check_item).main())
