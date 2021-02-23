# -*- coding: utf-8 -*-
import base64
import hashlib
import hmac
import json
import time
import urllib.parse

import requests


def message2server(sckey, content):
    print("server 酱推送开始")
    data = {"text": "每日签到", "desp": content.replace("\n", "\n\n")}
    requests.post(url=f"https://sc.ftqq.com/{sckey}.send", data=data)
    return


def message2server_turbo(sendkey, content):
    print("server 酱 Turbo 推送开始")
    data = {"text": "每日签到", "desp": content.replace("\n", "\n\n")}
    requests.post(url=f"https://sctapi.ftqq.com/{sendkey}.send", data=data)
    return


def message2coolpush(
    coolpushskey, content, coolpushqq: bool = True, coolpushwx: bool = False, coolpushemail: bool = False
):
    print("Cool Push 推送开始")
    params = {"c": content, "t": "每日签到"}
    if coolpushqq:
        requests.post(url=f"https://push.xuthus.cc/send/{coolpushskey}", params=params)
    if coolpushwx:
        requests.post(url=f"https://push.xuthus.cc/wx/{coolpushskey}", params=params)
    if coolpushemail:
        requests.post(url=f"https://push.xuthus.cc/email/{coolpushskey}", params=params)
    return


def message2qmsg(qmsg_key, content):
    print("qmsg 酱推送开始")
    params = {"msg": content}
    requests.get(url=f"https://qmsg.zendee.cn/send/{qmsg_key}", params=params)
    return


def message2telegram(tg_bot_token, tg_user_id, content):
    print("Telegram 推送开始")
    send_data = {"chat_id": tg_user_id, "text": content, "disable_web_page_preview": "true"}
    requests.post(url=f"https://api.telegram.org/bot{tg_bot_token}/sendMessage", data=send_data)
    return


def message2dingtalk(dingtalk_secret, dingtalk_access_token, content):
    print("Dingtalk 推送开始")
    timestamp = str(round(time.time() * 1000))
    secret_enc = dingtalk_secret.encode("utf-8")
    string_to_sign = "{}\n{}".format(timestamp, dingtalk_secret)
    string_to_sign_enc = string_to_sign.encode("utf-8")
    hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
    sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
    send_data = {"msgtype": "text", "text": {"content": content}}
    requests.post(
        url="https://oapi.dingtalk.com/robot/send?access_token={0}&timestamp={1}&sign={2}".format(
            dingtalk_access_token, timestamp, sign
        ),
        headers={"Content-Type": "application/json", "Charset": "UTF-8"},
        data=json.dumps(send_data),
    )
    return


def message2bark(bark_url: str, content):
    print("Bark 推送开始")
    if not bark_url.endswith("/"):
        bark_url += "/"
    url = f"{bark_url}{content}"
    headers = {"Content-type": "application/x-www-form-urlencoded"}
    requests.get(url=url, headers=headers)
    return


def important_notice():
    datas = requests.get(url="https://api.github.com/repos/Sitoi/dailycheckin/issues?state=open&labels=通知").json()
    if datas:
        data = datas[0]
        title = data.get("title")
        body = data.get("body")
        url = data.get("html_url")
        notice = f"重要通知: {title}\n通知内容: {body}\n详细地址: {url}"
    else:
        notice = None
    return notice


if __name__ == '__main__':
    print(important_notice())
