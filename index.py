# -*- coding: utf-8 -*-
import base64
import hashlib
import hmac
import json
import time
import urllib.parse
from datetime import datetime

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
    if isinstance(event, dict):
        message = event.get("Message")
    else:
        message = None
    start_time = time.time()
    with open("config.json", "r", encoding="utf-8") as f:
        data = json.loads(f.read())
    dingtalk_secret = data.get("dingtalk", {}).get("dingtalk_secret")
    dingtalk_access_token = data.get("dingtalk", {}).get("dingtalk_access_token")
    sckey = data.get("server", {}).get("sckey")
    tg_bot_token = data.get("telegram", {}).get("tg_bot_token")
    tg_user_id = data.get("telegram", {}).get("tg_user_id")
    qmsg_key = data.get("qmsg", {}).get("qmsg_key")
    content_list = [f'当前时间: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}']
    if message != "xmly":
        iqiyi_cookie_list = data.get("iqiyi", [])
        if iqiyi_cookie_list:
            msg_list = IQIYICheckIn(iqiyi_cookie_list=iqiyi_cookie_list).main()
            content_list += msg_list

        baidu_url_submit_list = data.get("baidu_url_submit", [])
        if baidu_url_submit_list:
            msg_list = BaiduUrlSubmit(baidu_url_submit_list=baidu_url_submit_list).main()
            content_list += msg_list

        vqq_cookie_list = data.get("vqq", [])
        if vqq_cookie_list:
            msg_list = VQQCheckIn(vqq_cookie_list=vqq_cookie_list).main()
            content_list += msg_list

        youdao_cookie_list = data.get("youdao", [])
        if youdao_cookie_list:
            msg_list = YouDaoCheckIn(youdao_cookie_list=youdao_cookie_list).main()
            content_list += msg_list

        pojie_cookie_list = data.get("52pojie", [])
        if pojie_cookie_list:
            msg_list = PojieCheckIn(pojie_cookie_list=pojie_cookie_list).main()
            content_list += msg_list

        kgqq_cookie_list = data.get("kgqq", [])
        if kgqq_cookie_list:
            msg_list = KGQQCheckIn(kgqq_cookie_list=kgqq_cookie_list).main()
            content_list += msg_list

        music163_account_list = data.get("music163", [])
        if music163_account_list:
            msg_list = Music163CheckIn(music163_account_list=music163_account_list).main()
            content_list += msg_list

        city_name_list = data.get("weather", [])
        if city_name_list:
            msg_list = Weather(city_name_list=city_name_list).main()
            content_list += msg_list

        motto = data.get("motto")
        if motto:
            msg_list = Motto().main()
            content_list += msg_list
    else:
        xmly_cookie_list = data.get("xmly")
        if xmly_cookie_list:
            msg_list = XMLYCheckIn(xmly_cookie_list=xmly_cookie_list).main()
            content_list += msg_list
    use_time_info = f"本次任务使用时间: {time.time() - start_time} 秒"
    content_list.append(use_time_info)
    content = "\n-----------------------------\n\n".join(content_list)
    print(content)
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
