import base64
import hashlib
import hmac
import json
import re
import time
from urllib.parse import quote_plus

import requests


def message2server(sckey, content):
    print("server 酱推送开始")
    data = {"text": "每日签到", "desp": content.replace("\n", "\n\n")}
    requests.post(url=f"https://sc.ftqq.com/{sckey}.send", data=data)
    return


def message2server_turbo(sendkey, content):
    data = {"text": "每日签到", "desp": content.replace("\n", "\n\n")}
    if match := re.match(r"^sctp(\d+)t", sendkey):
        sc3uid = match.group(1)
        print("Server 酱³ 推送开始")
        url = f"https://{sc3uid}.push.ft07.com/send/{sendkey}.send?tags=DailyCheckin"
    else:
        print("server 酱 Turbo 推送开始")
        url = f"https://sctapi.ftqq.com/{sendkey}.send"
    requests.post(url=url, data=data)
    return


def message2coolpush(
    coolpushskey,
    content,
    coolpushqq: bool = True,
    coolpushwx: bool = False,
    coolpushemail: bool = False,
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


def message2qmsg(qmsg_key, qmsg_type, content):
    print("qmsg 酱推送开始")
    params = {"msg": content}
    if qmsg_type == "group":
        requests.get(url=f"https://qmsg.zendee.cn/group/{qmsg_key}", params=params)
    else:
        requests.get(url=f"https://qmsg.zendee.cn/send/{qmsg_key}", params=params)
    return


def message2telegram(tg_api_host, tg_proxy, tg_bot_token, tg_user_id, content):
    print("Telegram 推送开始")
    send_data = {
        "chat_id": tg_user_id,
        "text": content,
        "disable_web_page_preview": "true",
    }
    if tg_api_host:
        url = f"https://{tg_api_host}/bot{tg_bot_token}/sendMessage"
    else:
        url = f"https://api.telegram.org/bot{tg_bot_token}/sendMessage"
    if tg_proxy:
        proxies = {
            "http": tg_proxy,
            "https": tg_proxy,
        }
    else:
        proxies = None
    requests.post(url=url, data=send_data, proxies=proxies)
    return


def message2feishu(fskey, content):
    print("飞书 推送开始")
    data = {"msg_type": "text", "content": {"text": content}}
    requests.post(
        url=f"https://open.feishu.cn/open-apis/bot/v2/hook/{fskey}", json=data
    )
    return


def message2dingtalk(dingtalk_secret, dingtalk_access_token, content):
    print("Dingtalk 推送开始")
    timestamp = str(round(time.time() * 1000))
    secret_enc = dingtalk_secret.encode("utf-8")
    string_to_sign = f"{timestamp}\n{dingtalk_secret}"
    string_to_sign_enc = string_to_sign.encode("utf-8")
    hmac_code = hmac.new(
        secret_enc, string_to_sign_enc, digestmod=hashlib.sha256
    ).digest()
    sign = quote_plus(base64.b64encode(hmac_code))
    send_data = {"msgtype": "text", "text": {"content": content}}
    requests.post(
        url="https://oapi.dingtalk.com/robot/send?access_token={}&timestamp={}&sign={}".format(
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
    content = quote_plus(content)
    url = f"{bark_url}{content}"
    headers = {"Content-type": "application/x-www-form-urlencoded"}
    requests.get(url=url, headers=headers)
    return


def message2qywxrobot(qywx_key, content):
    print("企业微信群机器人推送开始")
    requests.post(
        url=f"https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={qywx_key}",
        data=json.dumps({"msgtype": "text", "text": {"content": content}}),
    )
    return


def message2qywxapp(
    qywx_corpid,
    qywx_agentid,
    qywx_corpsecret,
    qywx_touser,
    qywx_media_id,
    qywx_origin,
    content,
):
    print("企业微信应用消息推送开始")
    base_url = "https://qyapi.weixin.qq.com"
    if qywx_origin:
        base_url = qywx_origin
    res = requests.get(
        f"{base_url}/cgi-bin/gettoken?corpid={qywx_corpid}&corpsecret={qywx_corpsecret}"
    )
    token = res.json().get("access_token", False)
    if qywx_media_id:
        data = {
            "touser": qywx_touser,
            "msgtype": "mpnews",
            "agentid": int(qywx_agentid),
            "mpnews": {
                "articles": [
                    {
                        "title": "Dailycheckin 签到通知",
                        "thumb_media_id": qywx_media_id,
                        "author": "Sitoi",
                        "content_source_url": "https://github.com/Sitoi/dailycheckin",
                        "content": content.replace("\n", "<br>"),
                        "digest": content,
                    }
                ]
            },
        }
    else:
        data = {
            "touser": qywx_touser,
            "agentid": int(qywx_agentid),
            "msgtype": "textcard",
            "textcard": {
                "title": "Dailycheckin 签到通知",
                "description": content,
                "url": "https://github.com/Sitoi/dailycheckin",
                "btntxt": "开源项目",
            },
        }
    requests.post(
        url=f"{base_url}/cgi-bin/message/send?access_token={token}",
        data=json.dumps(data),
    )
    return


def message2pushplus(pushplus_token, content, pushplus_topic=None):
    print("Pushplus 推送开始")
    data = {
        "token": pushplus_token,
        "title": "签到通知",
        "content": content.replace("\n", "<br>"),
        "template": "json",
    }
    if pushplus_topic:
        data["topic"] = pushplus_topic
    requests.post(url="http://www.pushplus.plus/send", data=json.dumps(data))
    return


def message2gotify(
    gotify_url: str, gotify_token: str, gotify_priority: str, content: str
) -> None:
    print("Gotify 服务启动")
    if not gotify_priority:
        gotify_priority = "3"
    url = f"{gotify_url}/message?token={gotify_token}"
    data = {
        "title": "Dailycheckin签到通知",
        "message": content,
        "priority": gotify_priority,
    }
    response = requests.post(url, data=data).json()

    if response.get("id"):
        print("Gotify 推送成功！")
    else:
        print("Gotify 推送失败！")
    return


def message2ntfy(
    ntfy_url: str, ntfy_topic: str, ntfy_priority: str, content: str
) -> None:
    def encode_rfc2047(text: str) -> str:
        """将文本编码为符合 RFC 2047 标准的格式"""
        encoded_bytes = base64.b64encode(text.encode("utf-8"))
        encoded_str = encoded_bytes.decode("utf-8")
        return f"=?utf-8?B?{encoded_str}?="

    print("Ntfy 服务启动")
    if not ntfy_url:
        ntfy_url = "https://ntfy.sh"
    if not ntfy_priority:
        ntfy_priority = "3"
    # 使用 RFC 2047 编码 title
    encoded_title = encode_rfc2047("Dailycheckin签到通知")

    data = content.encode(encoding="utf-8")
    headers = {"Title": encoded_title, "Priority": ntfy_priority}  # 使用编码后的 title
    url = f"{ntfy_url}/{ntfy_topic}"
    response = requests.post(url, data=data, headers=headers)
    if response.status_code == 200:  # 使用 response.status_code 进行检查
        print("Ntfy 推送成功！")
    else:
        print("Ntfy 推送失败！错误信息：", response.text)


def important_notice():
    datas = requests.get(
        url="https://api.github.com/repos/Sitoi/dailycheckin/issues?state=open&labels=通知"
    ).json()
    if datas:
        data = datas[0]
        title = data.get("title")
        body = data.get("body")
        url = data.get("html_url")
        notice = f"{title}\n{body}\n详细地址: {url}"
    else:
        notice = None
    return notice


def push_message(content_list: list, notice_info: dict):
    dingtalk_secret = notice_info.get("dingtalk_secret")
    dingtalk_access_token = notice_info.get("dingtalk_access_token")
    fskey = notice_info.get("fskey")
    bark_url = notice_info.get("bark_url")
    sckey = notice_info.get("sckey")
    sendkey = notice_info.get("sendkey")
    qmsg_key = notice_info.get("qmsg_key")
    qmsg_type = notice_info.get("qmsg_type")
    tg_bot_token = notice_info.get("tg_bot_token")
    tg_user_id = notice_info.get("tg_user_id")
    tg_api_host = notice_info.get("tg_api_host")
    tg_proxy = notice_info.get("tg_proxy")
    coolpushskey = notice_info.get("coolpushskey")
    coolpushqq = notice_info.get("coolpushqq")
    coolpushwx = notice_info.get("coolpushwx")
    coolpushemail = notice_info.get("coolpushemail")
    qywx_key = notice_info.get("qywx_key")
    qywx_corpid = notice_info.get("qywx_corpid")
    qywx_agentid = notice_info.get("qywx_agentid")
    qywx_corpsecret = notice_info.get("qywx_corpsecret")
    qywx_touser = notice_info.get("qywx_touser")
    qywx_media_id = notice_info.get("qywx_media_id")
    qywx_origin = notice_info.get("qywx_origin")
    pushplus_token = notice_info.get("pushplus_token")
    pushplus_topic = notice_info.get("pushplus_topic")
    gotify_url = notice_info.get("gotify_url")
    gotify_token = notice_info.get("gotify_token")
    gotify_priority = notice_info.get("gotify_priority")
    ntfy_url = notice_info.get("ntfy_url")
    ntfy_topic = notice_info.get("ntfy_topic")
    ntfy_priority = notice_info.get("ntfy_priority")
    content_str = "\n————————————\n\n".join(content_list)
    merge_push = notice_info.get("merge_push")
    message_list = [content_str]
    try:
        notice = important_notice()
        if notice:
            message_list.append(notice)
            content_list.append(notice)
    except Exception as e:
        print("获取重要通知失败:", e)
    if merge_push is None:
        if (
            qmsg_key
            or coolpushskey
            or qywx_touser
            or qywx_corpsecret
            or qywx_agentid
            or bark_url
            or pushplus_token
            or ntfy_topic
            or (gotify_url and gotify_token)
        ):
            merge_push = False
        else:
            merge_push = True
    if not merge_push:
        message_list = content_list
    for message in message_list:
        if qmsg_key:
            try:
                message2qmsg(qmsg_key=qmsg_key, qmsg_type=qmsg_type, content=message)
            except Exception as e:
                print("qmsg 推送失败", e)
        if coolpushskey:
            try:
                message2coolpush(
                    coolpushskey=coolpushskey,
                    coolpushqq=coolpushqq,
                    coolpushwx=coolpushwx,
                    coolpushemail=coolpushemail,
                    content=message,
                )
            except Exception as e:
                print("coolpush 推送失败", e)
        if qywx_touser and qywx_corpid and qywx_corpsecret and qywx_agentid:
            try:
                message2qywxapp(
                    qywx_corpid=qywx_corpid,
                    qywx_agentid=qywx_agentid,
                    qywx_corpsecret=qywx_corpsecret,
                    qywx_touser=qywx_touser,
                    qywx_media_id=qywx_media_id,
                    qywx_origin=qywx_origin,
                    content=message,
                )
            except Exception as e:
                print("企业微信应用消息推送失败", e)
        if bark_url:
            try:
                message2bark(bark_url=bark_url, content=message)
            except Exception as e:
                print("Bark 推送失败", e)
        if dingtalk_access_token and dingtalk_secret:
            try:
                message2dingtalk(
                    dingtalk_secret=dingtalk_secret,
                    dingtalk_access_token=dingtalk_access_token,
                    content=message,
                )
            except Exception as e:
                print("钉钉推送失败", e)
        if fskey:
            try:
                message2feishu(fskey=fskey, content=message)
            except Exception as e:
                print("飞书推送失败", e)
        if sckey:
            try:
                message2server(sckey=sckey, content=message)
            except Exception as e:
                print("Server 推送失败", e)
        if sendkey:
            try:
                message2server_turbo(sendkey=sendkey, content=message)
            except Exception as e:
                print("Server Turbo 推送失败", e)
        if qywx_key:
            try:
                message2qywxrobot(qywx_key=qywx_key, content=message)
            except Exception as e:
                print("企业微信群机器人推送失败", e)
        if pushplus_token:
            try:
                message2pushplus(
                    pushplus_token=pushplus_token,
                    content=message,
                    pushplus_topic=pushplus_topic,
                )
            except Exception as e:
                print("Pushplus 推送失败", e)
        if tg_user_id and tg_bot_token:
            try:
                message2telegram(
                    tg_api_host=tg_api_host,
                    tg_proxy=tg_proxy,
                    tg_user_id=tg_user_id,
                    tg_bot_token=tg_bot_token,
                    content=message,
                )
            except Exception as e:
                print("Telegram 推送失败", e)
        if gotify_url and gotify_token:
            try:
                message2gotify(
                    gotify_url=gotify_url,
                    gotify_token=gotify_token,
                    gotify_priority=gotify_priority,
                    content=message,
                )
            except Exception as e:
                print("Gotify 推送失败", e)
        if ntfy_topic:
            try:
                message2ntfy(
                    ntfy_url=ntfy_url,
                    ntfy_topic=ntfy_topic,
                    ntfy_priority=ntfy_priority,
                    content=message,
                )
            except Exception as e:
                print("Ntfy 推送失败", e)


if __name__ == "__main__":
    print(important_notice())
