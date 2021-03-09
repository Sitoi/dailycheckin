# -*- coding: utf-8 -*-
import json
import os
import sys
import time
from datetime import datetime, timedelta

from config import checkin_map, get_checkin_info, get_notice_info, env2config
from motto import Motto
from utils.message import push_message


def main_handler(event, context):
    start_time = time.time()
    utc_time = datetime.utcnow() + timedelta(hours=8)
    if "IS_GITHUB_ACTION" in os.environ:
        message = os.getenv("ONLY_MESSAGE")
        data = env2config()
    else:
        if isinstance(event, dict):
            message = event.get("Message")
        else:
            message = None
        with open(os.path.join(os.path.dirname(__file__), "config/config.json"), "r", encoding="utf-8") as f:
            data = json.loads(f.read())
    try:
        motto = data.get("MOTTO")
        notice_info = get_notice_info(data=data)
        check_info = get_checkin_info(data=data)
    except Exception as e:
        raise e
    content_list = [f"当前时间: {utc_time}"]
    if message == "xmly":
        if check_info.get("xmly_cookie_list"):
            check_name, check_func = checkin_map.get("XMLY_COOKIE_LIST")
            for check_item in check_info.get("xmly_cookie_list", []):
                if "xxxxxx" not in str(check_item) and "多账号" not in str(check_item):
                    try:
                        msg = check_func(check_item).main()
                        content_list.append(f"【{check_name}】\n{msg}")
                    except Exception as e:
                        content_list.append(f"【{check_name}】\n{e}")
                        print(check_name, e)
                else:
                    print(f"检测【{check_name}】脚本到配置文件包含模板配置,进行跳过")
    else:
        for one_check, check_tuple in checkin_map.items():
            check_name, check_func = check_tuple
            if one_check not in ["XMLY_COOKIE_LIST"]:
                if check_info.get(one_check.lower()):
                    print(f"----------已检测到正确的配置，并开始执行 {one_check} 签到----------")
                    for check_item in check_info.get(one_check.lower(), []):
                        if "xxxxxx" not in str(check_item) and "多账号" not in str(check_item):
                            try:
                                msg = check_func(check_item).main()
                                content_list.append(f"【{check_name}】\n{msg}")
                            except Exception as e:
                                content_list.append(f"【{check_name}】\n{e}")
                                print(check_name, e)
                        else:
                            print(f"检测【{check_name}】脚本到配置文件包含模板配置,进行跳过")
                else:
                    print(f"----------未检测到正确的配置，并跳过执行 {one_check} 签到----------")
        if motto:
            try:
                msg_list = Motto().main()
            except Exception as e:
                print(e)
                msg_list = []
            content_list += msg_list
    content_list.append(f"任务使用时间: {int(time.time() - start_time)} 秒")
    if message == "xmly":
        if utc_time.hour in [9, 18] and utc_time.minute == 0:
            flag = True
        else:
            flag = False
    else:
        flag = True
    if flag:
        push_message(content_list=content_list, notice_info=notice_info)
    return


if __name__ == "__main__":
    args = sys.argv
    if len(args) > 1:
        event = {"Message": args[1]}
    else:
        event = None
    main_handler(event=event, context=None)
