# -*- coding: utf-8 -*-
import base64
import hashlib
import hmac
import json
import os
import sys
import time
import urllib.parse
from datetime import datetime, timedelta

import requests

from baidu_url_submit import BaiduUrlSubmit
from bilibili import BiliBiliCheckIn
from fmapp import FMAPPCheckIn
from iqiyi import IQIYICheckIn
from kgqq import KGQQCheckIn
from motto import Motto
from music163 import Music163CheckIn
from oneplusbbs import OnePlusBBSCheckIn
from pojie import PojieCheckIn
from qqread import QQReadCheckIn
from tieba import TiebaCheckIn
from vqq import VQQCheckIn
from weather import Weather
from xmly import XMLYCheckIn
from youdao import YouDaoCheckIn


def message_to_server(sckey, content):
    print("server 酱推送开始")
    data = {"text": "每日签到", "desp": content.replace("\n", "\n\n")}
    response = requests.post(url=f"https://sc.ftqq.com/{sckey}.send", data=data)
    return response.text


def message_to_coolpush(
    coolpushskey, content, coolpushqq: bool = True, coolpushwx: bool = False, coolpushemail: bool = False
):
    print("Cool Push 推送开始")
    params = {"c": content, "t": "每日签到"}
    if coolpushqq:
        response = requests.post(url=f"https://push.xuthus.cc/send/{coolpushskey}", params=params)
    if coolpushwx:
        response = requests.post(url=f"https://push.xuthus.cc/wx/{coolpushskey}", params=params)
    if coolpushemail:
        response = requests.post(url=f"https://push.xuthus.cc/email/{coolpushskey}", params=params)
    return response.text


def message_to_qmsg(qmsg_key, content):
    print("qmsg 酱推送开始")
    params = {"msg": content}
    response = requests.get(url=f"https://qmsg.zendee.cn/send/{qmsg_key}", params=params)
    return response.text


def message_to_telegram(tg_bot_token, tg_user_id, content):
    print("Telegram 推送开始")
    send_data = {"chat_id": tg_user_id, "text": content, "disable_web_page_preview": "true"}
    response = requests.post(url=f"https://api.telegram.org/bot{tg_bot_token}/sendMessage", data=send_data)
    return response.text


def message_to_dingtalk(dingtalk_secret, dingtalk_access_token, content):
    print("Dingtalk 推送开始")
    timestamp = str(round(time.time() * 1000))
    secret_enc = dingtalk_secret.encode("utf-8")
    string_to_sign = "{}\n{}".format(timestamp, dingtalk_secret)
    string_to_sign_enc = string_to_sign.encode("utf-8")
    hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
    sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
    send_data = {"msgtype": "text", "text": {"content": content}}
    response = requests.post(
        url="https://oapi.dingtalk.com/robot/send?access_token={0}&timestamp={1}&sign={2}".format(
            dingtalk_access_token, timestamp, sign
        ),
        headers={"Content-Type": "application/json", "Charset": "UTF-8"},
        data=json.dumps(send_data),
    )
    return response.text


def main_handler(event, context):
    start_time = time.time()
    utc_time = datetime.utcnow() + timedelta(hours=8)
    if "IS_GITHUB_ACTION" in os.environ:
        message = os.getenv("ONLY_MESSAGE")
        dingtalk_secret = os.getenv("DINGTALK_SECRET")
        dingtalk_access_token = os.getenv("DINGTALK_ACCESS_TOKEN")
        sckey = os.getenv("SCKEY")
        tg_bot_token = os.getenv("TG_BOT_TOKEN")
        tg_user_id = os.getenv("TG_USER_ID")
        qmsg_key = os.getenv("QMSG_KEY")
        coolpushskey = os.getenv("COOLPUSHSKEY")
        coolpushqq = os.getenv("COOLPUSHQQ")
        coolpushwx = os.getenv("COOLPUSHWX")
        coolpushemail = os.getenv("COOLPUSHEMAIL")
        motto = os.getenv("MOTTO")
        iqiyi_cookie_list = json.loads(os.getenv("IQIYI_COOKIE_LIST", [])) if os.getenv("IQIYI_COOKIE_LIST") else []
        baidu_url_submit_list = (
            json.loads(os.getenv("BAIDU_URL_SUBMIT_LIST", [])) if os.getenv("BAIDU_URL_SUBMIT_LIST") else []
        )
        vqq_cookie_list = json.loads(os.getenv("VQQ_COOKIE_LIST", [])) if os.getenv("VQQ_COOKIE_LIST") else []
        youdao_cookie_list = json.loads(os.getenv("YOUDAO_COOKIE_LIST", [])) if os.getenv("YOUDAO_COOKIE_LIST") else []
        pojie_cookie_list = json.loads(os.getenv("POJIE_COOKIE_LIST", [])) if os.getenv("POJIE_COOKIE_LIST") else []
        kgqq_cookie_list = json.loads(os.getenv("KGQQ_COOKIE_LIST", [])) if os.getenv("KGQQ_COOKIE_LIST") else []
        music163_account_list = (
            json.loads(os.getenv("MUSIC163_ACCOUNT_LIST", [])) if os.getenv("MUSIC163_ACCOUNT_LIST") else []
        )
        city_name_list = json.loads(os.getenv("CITY_NAME_LIST", [])) if os.getenv("CITY_NAME_LIST") else []
        xmly_cookie_list = json.loads(os.getenv("XMLY_COOKIE_LIST", [])) if os.getenv("XMLY_COOKIE_LIST") else []
        oneplusbbs_cookie_list = (
            json.loads(os.getenv("ONEPLUSBBS_COOKIE_LIST", [])) if os.getenv("ONEPLUSBBS_COOKIE_LIST") else []
        )

        qqread_account_list = (
            json.loads(os.getenv("QQREAD_ACCOUNT_LIST", [])) if os.getenv("QQREAD_ACCOUNT_LIST") else []
        )

        fmapp_account_list = json.loads(os.getenv("FMAPP_ACCOUNT_LIST", [])) if os.getenv("FMAPP_ACCOUNT_LIST") else []
        tieba_cookie_list = json.loads(os.getenv("TIEBA_COOKIE_LIST", [])) if os.getenv("TIEBA_COOKIE_LIST") else []
        bilibili_cookie_list = (
            json.loads(os.getenv("BILIBILI_COOKIE_LIST", [])) if os.getenv("BILIBILI_COOKIE_LIST") else []
        )

    else:
        if isinstance(event, dict):
            message = event.get("Message")
        else:
            message = None
        with open(os.path.join(os.path.dirname(__file__), "config.json"), "r", encoding="utf-8") as f:
            data = json.loads(f.read())
        dingtalk_secret = data.get("DINGTALK_SECRET")
        dingtalk_access_token = data.get("DINGTALK_ACCESS_TOKEN")
        sckey = data.get("SCKEY")
        qmsg_key = data.get("QMSG_KEY")
        tg_bot_token = data.get("TG_BOT_TOKEN")
        tg_user_id = data.get("TG_USER_ID")
        coolpushskey = data.get("COOLPUSHSKEY")
        coolpushqq = data.get("COOLPUSHQQ")
        coolpushwx = data.get("COOLPUSHWX")
        coolpushemail = data.get("COOLPUSHEMAIL")
        city_name_list = data.get("CITY_NAME_LIST", [])
        motto = data.get("MOTTO")
        iqiyi_cookie_list = data.get("IQIYI_COOKIE_LIST", [])
        vqq_cookie_list = data.get("VQQ_COOKIE_LIST", [])
        pojie_cookie_list = data.get("POJIE_COOKIE_LIST", [])
        youdao_cookie_list = data.get("YOUDAO_COOKIE_LIST", [])
        kgqq_cookie_list = data.get("KGQQ_COOKIE_LIST", [])
        music163_account_list = data.get("MUSIC163_ACCOUNT_LIST", [])
        xmly_cookie_list = data.get("XMLY_COOKIE_LIST", [])
        oneplusbbs_cookie_list = data.get("ONEPLUSBBS_COOKIE_LIST", [])
        qqread_account_list = data.get("QQREAD_ACCOUNT_LIST", [])
        baidu_url_submit_list = data.get("BAIDU_URL_SUBMIT_LIST", [])
        fmapp_account_list = data.get("FMAPP_ACCOUNT_LIST", [])
        tieba_cookie_list = data.get("TIEBA_COOKIE_LIST", [])
        bilibili_cookie_list = data.get("BILIBILI_COOKIE_LIST", [])

    content_list = [f"当前时间: {utc_time}"]
    if message == "xmly":
        if xmly_cookie_list:
            msg_list = XMLYCheckIn(xmly_cookie_list=xmly_cookie_list).main()
            content_list += msg_list
    elif message == "qqread":
        if qqread_account_list:
            msg_list = QQReadCheckIn(qqread_account_list=qqread_account_list).main()
            content_list += msg_list
    else:
        if iqiyi_cookie_list:
            msg_list = IQIYICheckIn(iqiyi_cookie_list=iqiyi_cookie_list).main()
            content_list += msg_list

        if baidu_url_submit_list:
            msg_list = BaiduUrlSubmit(baidu_url_submit_list=baidu_url_submit_list).main()
            content_list += msg_list

        if vqq_cookie_list:
            msg_list = VQQCheckIn(vqq_cookie_list=vqq_cookie_list).main()
            content_list += msg_list

        if youdao_cookie_list:
            msg_list = YouDaoCheckIn(youdao_cookie_list=youdao_cookie_list).main()
            content_list += msg_list

        if pojie_cookie_list:
            msg_list = PojieCheckIn(pojie_cookie_list=pojie_cookie_list).main()
            content_list += msg_list

        if kgqq_cookie_list:
            msg_list = KGQQCheckIn(kgqq_cookie_list=kgqq_cookie_list).main()
            content_list += msg_list

        if music163_account_list:
            msg_list = Music163CheckIn(music163_account_list=music163_account_list).main()
            content_list += msg_list

        if oneplusbbs_cookie_list:
            msg_list = OnePlusBBSCheckIn(oneplusbbs_cookie_list=oneplusbbs_cookie_list).main()
            content_list += msg_list

        if fmapp_account_list:
            msg_list = FMAPPCheckIn(fmapp_account_list=fmapp_account_list).main()
            content_list += msg_list

        if tieba_cookie_list:
            msg_list = TiebaCheckIn(tieba_cookie_list=tieba_cookie_list).main()
            content_list += msg_list

        if bilibili_cookie_list:
            msg_list = BiliBiliCheckIn(bilibili_cookie_list=bilibili_cookie_list).main()
            content_list += msg_list

        if city_name_list:
            msg_list = Weather(city_name_list=city_name_list).main()
            content_list += msg_list

        if motto:
            msg_list = Motto().main()
            content_list += msg_list
    use_time_info = f"本次任务使用时间: {time.time() - start_time} 秒"
    content_list.append(use_time_info)
    content = "\n-----------------------------\n\n".join(content_list)
    print(content)
    if message == "xmly":
        if utc_time.hour in [9, 18] and utc_time.minute == 0:
            flag = True
        else:
            flag = False
    elif message == "qqread":
        if utc_time.hour in [9, 18] and utc_time.minute == 0:
            flag = True
        else:
            flag = False
    else:
        flag = True
    if flag:
        if dingtalk_access_token and dingtalk_secret:
            message_to_dingtalk(
                dingtalk_secret=dingtalk_secret, dingtalk_access_token=dingtalk_access_token, content=content
            )
        if sckey:
            message_to_server(sckey=sckey, content=content)
        if qmsg_key:
            for content in content_list:
                message_to_qmsg(qmsg_key=qmsg_key, content=content)
        if tg_user_id and tg_bot_token:
            message_to_telegram(tg_user_id=tg_user_id, tg_bot_token=tg_bot_token, content=content)
        if coolpushskey:
            for content in content_list:
                message_to_coolpush(
                    coolpushskey=coolpushskey,
                    content=content,
                    coolpushqq=coolpushqq,
                    coolpushwx=coolpushwx,
                    coolpushemail=coolpushemail,
                )
    return


if __name__ == "__main__":
    args = sys.argv
    if len(args) > 1:
        event = {"Message": args[1]}
    else:
        event = None
    main_handler(event=event, context=None)
