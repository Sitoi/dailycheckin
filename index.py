# -*- coding: utf-8 -*-
# -*- coding: utf8 -*-
import json

from baidu_url_submit.baidu_url_submit import BaiduUrlSubmit
from iqiyi.iqiyi import IQIYICheckIn


def main_handler(event, context):
    with open("config.json", "r", encoding="utf-8") as f:
        data = json.loads(f.read())
    dingtalk_secret = data.get("dingtalk", {}).get("dingtalk_secret")
    dingtalk_access_token = data.get("dingtalk", {}).get("dingtalk_access_token")

    iqiyi_cookie_list = data.get("iqiyi", [])
    if iqiyi_cookie_list:
        IQIYICheckIn(
            dingtalk_secret=dingtalk_secret,
            dingtalk_access_token=dingtalk_access_token,
            iqiyi_cookie_list=iqiyi_cookie_list,
        ).main()

    baidu_url_submit_list = data.get("BaiduUrlSubmit", [])
    if baidu_url_submit_list:
        BaiduUrlSubmit(
            dingtalk_secret=dingtalk_secret,
            dingtalk_access_token=dingtalk_access_token,
            baidu_url_submit_list=baidu_url_submit_list,
        ).main()
    return


if __name__ == '__main__':
    main_handler(event=None, context=None)
