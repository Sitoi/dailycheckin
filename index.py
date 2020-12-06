# -*- coding: utf-8 -*-
import json

from baidu_url_submit import BaiduUrlSubmit
from iqiyi import IQIYICheckIn
from kgqq import KGQQCheckIn
from music163 import Music163CheckIn
from pojie import PojieCheckIn
from vqq import VQQCheckIn
from youdao import YouDaoCheckIn


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

    vqq_cookie_list = data.get("vqq", [])
    if vqq_cookie_list:
        VQQCheckIn(
            dingtalk_secret=dingtalk_secret,
            dingtalk_access_token=dingtalk_access_token,
            vqq_cookie_list=vqq_cookie_list,
        ).main()

    youdao_cookie_list = data.get("youdao", [])
    if youdao_cookie_list:
        YouDaoCheckIn(
            dingtalk_secret=dingtalk_secret,
            dingtalk_access_token=dingtalk_access_token,
            youdao_cookie_list=youdao_cookie_list,
        ).main()

    pojie_cookie_list = data.get("52pojie", [])
    if pojie_cookie_list:
        PojieCheckIn(
            dingtalk_secret=dingtalk_secret,
            dingtalk_access_token=dingtalk_access_token,
            pojie_cookie_list=pojie_cookie_list,
        ).main()

    kgqq_cookie_list = data.get("kgqq", [])
    if kgqq_cookie_list:
        KGQQCheckIn(
            dingtalk_secret=dingtalk_secret,
            dingtalk_access_token=dingtalk_access_token,
            kgqq_cookie_list=kgqq_cookie_list,
        ).main()

    music163_account_list = data.get("music163", [])
    if music163_account_list:
        Music163CheckIn(
            dingtalk_secret=dingtalk_secret,
            dingtalk_access_token=dingtalk_access_token,
            music163_account_list=music163_account_list,
        ).main()
    return


if __name__ == '__main__':
    main_handler(event=None, context=None)
