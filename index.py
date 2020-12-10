# -*- coding: utf-8 -*-
import base64
import hashlib
import hmac
import json
import os
import time
import urllib.parse
from datetime import datetime, timedelta

import requests

from baidu_url_submit import BaiduUrlSubmit
from iqiyi import IQIYICheckIn
from kgqq import KGQQCheckIn
from motto.motto import Motto
from music163 import Music163CheckIn
from pojie import PojieCheckIn
from vqq import VQQCheckIn
from weather import Weather
from xmly.xmly import XMLYCheckIn
from youdao import YouDaoCheckIn


def message_to_server(sckey, content):
    print("server 酱推送开始")
    data = {"text": "每日签到", "desp": content.replace("\n", "\n\n")}
    response = requests.post(f"https://sc.ftqq.com/{sckey}.send", data=data)
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
    """
    判断是否运行自GitHub action,"XMLY_SPEED_COOKIE" 该参数与 repo里的Secrets的名称保持一致
    """
    if "IS_GITHUB_ACTION" in os.environ:
        message = os.environ["ONLY_XMLY"]
        dingtalk_secret = os.environ["DINGTALK_SECRET"]
        dingtalk_access_token = os.environ["DINGTALK_ACCESS_TOKEN"]
        sckey = os.environ["SCKEY"]
        tg_bot_token = os.environ["TG_BOT_TOKEN"]
        tg_user_id = os.environ["TG_USER_ID"]
        qmsg_key = os.environ["QMSG_KEY"]
        motto = os.environ["MOTTO"]
        iqiyi_cookie_list = json.loads(os.environ.get("IQIYI_COOKIE_LIST", [])) if os.environ.get("IQIYI_COOKIE_LIST") else []
        baidu_url_submit_list = json.loads(os.environ.get("BAIDU_URL_SUBMIT_LIST", [])) if os.environ.get("BAIDU_URL_SUBMIT_LIST") else []
        vqq_cookie_list = json.loads(os.environ.get("VQQ_COOKIE_LIST", [])) if os.environ.get("VQQ_COOKIE_LIST") else []
        youdao_cookie_list = json.loads(os.environ.get("YOUDAO_COOKIE_LIST", [])) if os.environ.get("YOUDAO_COOKIE_LIST") else []
        pojie_cookie_list = json.loads(os.environ.get("POJIE_COOKIE_LIST", [])) if os.environ.get("POJIE_COOKIE_LIST") else []
        kgqq_cookie_list = json.loads(os.environ.get("KGQQ_COOKIE_LIST", [])) if os.environ.get("KGQQ_COOKIE_LIST") else []
        music163_account_list = json.loads(os.environ.get("MUSIC163_ACCOUNT_LIST", [])) if os.environ.get("MUSIC163_ACCOUNT_LIST") else []
        city_name_list = json.loads(os.environ.get("CITY_NAME_LIST", [])) if os.environ.get("CITY_NAME_LIST") else []
        xmly_cookie_list = json.loads(os.environ.get("XMLY_COOKIE_LIST", [])) if os.environ.get("XMLY_COOKIE_LIST") else []
    else:
        if isinstance(event, dict):
            message = event.get("Message")
        else:
            message = None
        start_time = time.time()
        utc_time = datetime.utcnow() + timedelta(hours=8)
        with open("config.json", "r", encoding="utf-8") as f:
            data = json.loads(f.read())
        dingtalk_secret = data.get("dingtalk", {}).get("dingtalk_secret")
        dingtalk_access_token = data.get("dingtalk", {}).get("dingtalk_access_token")
        sckey = data.get("server", {}).get("sckey")
        tg_bot_token = data.get("telegram", {}).get("tg_bot_token")
        tg_user_id = data.get("telegram", {}).get("tg_user_id")
        qmsg_key = data.get("qmsg", {}).get("qmsg_key")
        iqiyi_cookie_list = data.get("iqiyi", [])
        baidu_url_submit_list = data.get("baidu_url_submit", [])
        vqq_cookie_list = data.get("vqq", [])
        youdao_cookie_list = data.get("youdao", [])
        pojie_cookie_list = data.get("52pojie", [])
        kgqq_cookie_list = data.get("kgqq", [])
        music163_account_list = data.get("music163", [])
        city_name_list = data.get("weather", [])
        motto = data.get("motto")
        xmly_cookie_list = data.get("xmly")

    content_list = [f'当前时间: {utc_time}']
    if message != "xmly":
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

        if city_name_list:
            msg_list = Weather(city_name_list=city_name_list).main()
            content_list += msg_list

        if motto:
            msg_list = Motto().main()
            content_list += msg_list
    else:
        if xmly_cookie_list:
            msg_list = XMLYCheckIn(xmly_cookie_list=xmly_cookie_list).main()
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
    return


if __name__ == "__main__":
    main_handler(event=None, context=None)
