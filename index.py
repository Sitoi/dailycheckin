# -*- coding: utf-8 -*-
import json
import os
import time
from datetime import datetime, timedelta

from config import checkin_map, env2config, get_checkin_info, get_notice_info
from motto import Motto
from utils.message import push_message


def main_handler(event, context):
    start_time = time.time()
    utc_time = datetime.utcnow() + timedelta(hours=8)
    if "IS_GITHUB_ACTION" in os.environ:
        data = env2config()
    else:
        with open(os.path.join(os.path.dirname(__file__), "config/config.json"), "r", encoding="utf-8") as f:
            data = json.loads(f.read())
    try:
        motto = data.get("MOTTO")
        notice_info = get_notice_info(data=data)
        check_info = get_checkin_info(data=data)
    except Exception as e:
        raise e
    content_list = [f"当前时间: {utc_time}"]
    for one_check, check_tuple in checkin_map.items():
        check_name, check_func = check_tuple
        if check_info.get(one_check.lower()):
            print(f"----------已检测到正确的配置，并开始执行【{check_name}】签到----------")
            for index, check_item in enumerate(check_info.get(one_check.lower(), [])):
                print(f"----------开始执行【{check_name}】签到 : 第 {index + 1} 个账号----------")
                if "xxxxxx" not in str(check_item) and "多账号" not in str(check_item):
                    try:
                        msg = check_func(check_item).main()
                        content_list.append(f"【{check_name}】\n{msg}")
                        print(f"----------执行完成 【{check_name}】签到 : 第 {index + 1} 个账号----------")
                    except Exception as e:
                        content_list.append(f"【{check_name}】\n{e}")
                        print(f"----------执行失败 【{check_name}】签到 : 错误日志如下:----------\n{e}")

                else:
                    print(f"----------跳过执行【{check_name}】签到 : 配置文件包含自带的默认配置----------")
        else:
            print(f"----------未检测到正确的配置，并跳过执行【{check_name}】签到----------")
    if motto:
        try:
            msg_list = Motto().main()
        except Exception as e:
            print(e)
            msg_list = []
        content_list += msg_list
    content_list.append(f"任务使用时间: {int(time.time() - start_time)} 秒")
    push_message(content_list=content_list, notice_info=notice_info)
    return


if __name__ == "__main__":
    main_handler(event=None, context=None)
