# -*- coding: utf-8 -*-
import json
import os
import sys
import time
from datetime import datetime, timedelta

from motto import Motto
from utils.config import checkin_map, get_checkin_info
from utils.message import (
    message2bark,
    message2coolpush,
    message2dingtalk,
    message2qmsg,
    message2server,
    message2server_turbo,
    message2telegram,
    important_notice
)


def main_handler(event, context):
    start_time = time.time()
    utc_time = datetime.utcnow() + timedelta(hours=8)
    if "IS_GITHUB_ACTION" in os.environ:
        message = os.getenv("ONLY_MESSAGE")
        dingtalk_secret = os.getenv("DINGTALK_SECRET")
        dingtalk_access_token = os.getenv("DINGTALK_ACCESS_TOKEN")
        bark_url = os.getenv("BARK_URL")
        sckey = os.getenv("SCKEY")
        sendkey = os.getenv("SENDKEY")
        tg_bot_token = os.getenv("TG_BOT_TOKEN")
        tg_user_id = os.getenv("TG_USER_ID")
        qmsg_key = os.getenv("QMSG_KEY")
        coolpushskey = os.getenv("COOLPUSHSKEY")
        coolpushqq = os.getenv("COOLPUSHQQ")
        coolpushwx = os.getenv("COOLPUSHWX")
        coolpushemail = os.getenv("COOLPUSHEMAIL")
        motto = os.getenv("MOTTO")
        check_info = get_checkin_info(data=None)
    else:
        if isinstance(event, dict):
            message = event.get("Message")
        else:
            message = None
        try:
            with open(os.path.join(os.path.dirname(__file__), "config/config.json"), "r", encoding="utf-8") as f:
                data = json.loads(f.read())
            dingtalk_secret = data.get("DINGTALK_SECRET")
            dingtalk_access_token = data.get("DINGTALK_ACCESS_TOKEN")
            bark_url = data.get("BARK_URL")
            sckey = data.get("SCKEY")
            sendkey = data.get("SENDKEY")
            qmsg_key = data.get("QMSG_KEY")
            tg_bot_token = data.get("TG_BOT_TOKEN")
            tg_user_id = data.get("TG_USER_ID")
            coolpushskey = data.get("COOLPUSHSKEY")
            coolpushqq = data.get("COOLPUSHQQ")
            coolpushwx = data.get("COOLPUSHWX")
            coolpushemail = data.get("COOLPUSHEMAIL")
            motto = data.get("MOTTO")
            check_info = get_checkin_info(data=data)
        except Exception as e:
            raise e
    content_list = [f"当前时间: {utc_time}"]
    if message == "xmly":
        if check_info.get("xmly_cookie_list"):
            msg_list = checkin_map.get("XMLY_COOKIE_LIST")(xmly_cookie_list=check_info.get("xmly_cookie_list")).main()
            content_list += msg_list
    elif message == "qqread":
        return

    else:
        for one_check, check_func in checkin_map.items():
            if one_check not in ["XMLY_COOKIE_LIST"]:
                try:
                    if check_info.get(one_check.lower()):
                        print(f"----------已检测到正确的配置，并开始执行 {one_check} 签到----------")
                        msg_list = check_func(check_info.get(one_check.lower())).main()
                    else:
                        print(f"----------未检测到正确的配置，并跳过执行 {one_check} 签到----------")
                        msg_list = []
                except Exception as e:
                    print(e)
                    msg_list = []
                content_list += msg_list

        if motto:
            try:
                msg_list = Motto().main()
            except Exception as e:
                print(e)
                msg_list = []
            content_list += msg_list
    notice = important_notice()
    if notice:
        content_list.append(notice)
    use_time_info = f"本次任务使用时间: {time.time() - start_time} 秒"
    content_list.append(use_time_info)
    content = "\n-----------------------------\n\n".join(content_list)
    if message == "xmly":
        if utc_time.hour in [9, 18] and utc_time.minute == 0:
            flag = True
        else:
            flag = False
    else:
        flag = True
    if flag:
        if dingtalk_access_token and dingtalk_secret:
            message2dingtalk(
                dingtalk_secret=dingtalk_secret, dingtalk_access_token=dingtalk_access_token, content=content
            )
        if sckey:
            message2server(sckey=sckey, content=content)
        if sendkey:
            message2server_turbo(sendkey=sendkey, content=content)
        if qmsg_key:
            for content in content_list:
                message2qmsg(qmsg_key=qmsg_key, content=content)
        if tg_user_id and tg_bot_token:
            message2telegram(tg_user_id=tg_user_id, tg_bot_token=tg_bot_token, content=content)
        if coolpushskey:
            for content in content_list:
                message2coolpush(
                    coolpushskey=coolpushskey,
                    content=content,
                    coolpushqq=coolpushqq,
                    coolpushwx=coolpushwx,
                    coolpushemail=coolpushemail,
                )
        if bark_url:
            message2bark(bark_url=bark_url, content=content)
    return


if __name__ == "__main__":
    args = sys.argv
    if len(args) > 1:
        event = {"Message": args[1]}
    else:
        event = None
    main_handler(event=event, context=None)
