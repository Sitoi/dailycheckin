import json
import os

from dailycheckin import CheckIn


def checkin_map():
    result = {}
    for cls in CheckIn.__subclasses__():
        check_name = cls.__name__.upper()
        if check_name:
            result[check_name] = (cls.name, cls)
    return result


checkin_map = checkin_map()

notice_map = {
    "BARK_URL": "",
    "COOLPUSHEMAIL": "",
    "COOLPUSHQQ": "",
    "COOLPUSHSKEY": "",
    "COOLPUSHWX": "",
    "DINGTALK_ACCESS_TOKEN": "",
    "DINGTALK_SECRET": "",
    "FSKEY": "",
    "PUSHPLUS_TOKEN": "",
    "PUSHPLUS_TOPIC": "",
    "QMSG_KEY": "",
    "QMSG_TYPE": "",
    "QYWX_AGENTID": "",
    "QYWX_CORPID": "",
    "QYWX_CORPSECRET": "",
    "QYWX_KEY": "",
    "QYWX_TOUSER": "",
    "QYWX_MEDIA_ID": "",
    "QYWX_ORIGIN": "",
    "SCKEY": "",
    "SENDKEY": "",
    "TG_API_HOST": "",
    "TG_BOT_TOKEN": "",
    "TG_PROXY": "",
    "TG_USER_ID": "",
    "MERGE_PUSH": "",
    "GOTIFY_URL": "",
    "GOTIFY_TOKEN": "",
    "GOTIFY_PRIORITY": "",
    "NTFY_URL": "",
    "NTFY_TOPIC": "",
    "NTFY_PRIORITY": "",
}


def env2list(key):
    try:
        value = json.loads(os.getenv(key, []).strip()) if os.getenv(key) else []
        if isinstance(value, list):
            value = value
        else:
            value = []
    except Exception as e:
        print(e)
        value = []
    return value


def env2str(key):
    try:
        value = os.getenv(key, "") if os.getenv(key) else ""
        if isinstance(value, str):
            value = value.strip()
        elif isinstance(value, bool):
            value = value
        else:
            value = None
    except Exception as e:
        print(e)
        value = None
    return value


def get_checkin_info(data):
    result = {}
    if isinstance(data, dict):
        for one in checkin_map.keys():
            result[one.lower()] = data.get(one, [])
    else:
        for one in checkin_map.keys():
            result[one.lower()] = env2list(one)
    return result


def get_notice_info(data):
    result = {}
    if isinstance(data, dict):
        for one in notice_map.keys():
            result[one.lower()] = data.get(one, None)
    else:
        for one in notice_map.keys():
            result[one.lower()] = env2str(one)
    return result
