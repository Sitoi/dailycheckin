# -*- coding: utf-8 -*-
import json
import os
import re
import time

import requests
from requests import utils


class VQQCheckIn:
    def __init__(self, vqq_cookie_list):
        self.vqq_cookie_list = vqq_cookie_list

    @staticmethod
    def sign_once(session):
        url = "http://v.qq.com/x/bu/mobile_checkin?isDarkMode=0&uiType=REGULAR"
        res = session.get(url=url)
        match = re.search(r'isMultiple" />\s+(.*?)\s+<', res.text)
        if match:
            value = match.group(1)
            msg = f"成长值{value}"
        else:
            msg = "签到失败(可能已签到)"
        return msg

    @staticmethod
    def sign_twice(session):
        this_time = int(round(time.time() * 1000))
        url = "https://vip.video.qq.com/fcgi-bin/comm_cgi?name=hierarchical_task_system&cmd=2&_=" + str(this_time)
        res = session.get(url=url)
        ret = re.search('ret": (.*?),|}', res.text).group(1)
        if ret == "0":
            value = re.search('checkin_score": (.*?),', res.text).group(1)
            msg = f"成长值x{value}"
        else:
            msg = res.text
        return msg

    def main(self):
        msg_list = []
        for vqq_cookie in self.vqq_cookie_list:
            vqq_cookie = {item.split("=")[0]: item.split("=")[1] for item in vqq_cookie.get("vqq_cookie").split("; ")}
            _tmp = vqq_cookie.pop("ptag", None)
            session = requests.session()
            requests.utils.add_dict_to_cookiejar(session.cookies, vqq_cookie)
            o_cookie = (
                vqq_cookie.get("o_cookie") if vqq_cookie.get("o_cookie") else vqq_cookie.get("qq_nick", "未获取到用户信息")
            )
            sign_once_msg = self.sign_once(session=session)
            sign_twice_msg = self.sign_twice(session=session)
            msg = f"【腾讯视频签到】\n用户信息: {o_cookie}\n签到奖励1: {sign_once_msg}\n签到奖励2: {sign_twice_msg}"
            msg_list.append(msg)
        return msg_list


if __name__ == "__main__":
    with open(
        os.path.join(os.path.dirname(os.path.dirname(__file__)), "config/config.json"), "r", encoding="utf-8"
    ) as f:
        datas = json.loads(f.read())
    _vqq_cookie_list = datas.get("VQQ_COOKIE_LIST", [])
    VQQCheckIn(vqq_cookie_list=_vqq_cookie_list).main()
