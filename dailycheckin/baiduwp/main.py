import json
import os
import re
import time

import requests

from dailycheckin import CheckIn


class BaiduWP(CheckIn):
    name = "百度网盘"
    """
    百度网盘会员成长值签到和答题功能。
    传入cookie 自动完成签到、答题和会员信息查询。
    """

    def __init__(self, check_item: dict):
        self.cookie = check_item.get("cookie")
        self.session = requests.Session()
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 11; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.91 Mobile Safari/537.36",
            "Referer": "https://pan.baidu.com/wap/svip/growth/task",
            "Accept": "application/json, text/plain, */*",
            "X-Requested-With": "XMLHttpRequest",
            "Connection": "keep-alive",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
            "Cookie": self.cookie,
        }

    def signin(self):
        url = "https://pan.baidu.com/rest/2.0/membership/level?app_id=250528&web=5&method=signin"
        resp = self.session.get(url, headers=self.headers)
        sign_point = None
        signin_error_msg = ""
        if resp.status_code == 200:
            m = re.search(r'points":(\d+)', resp.text)
            if m:
                sign_point = m.group(1)
            m2 = re.search(r'"error_msg":"(.*?)",', resp.text)
            if m2:
                signin_error_msg = m2.group(1)
        else:
            signin_error_msg = f"签到请求失败: {resp.status_code} {self.cookie}"
        return sign_point, signin_error_msg

    def get_question(self):
        url = "https://pan.baidu.com/act/v2/membergrowv2/getdailyquestion?app_id=250528&web=5"
        resp = self.session.get(url, headers=self.headers)
        answer = None
        ask_id = None
        if resp.status_code == 200:
            m = re.search(r'"answer":(\d+),', resp.text)
            if m:
                answer = m.group(1)
            m2 = re.search(r'"ask_id":(\d+),', resp.text)
            if m2:
                ask_id = m2.group(1)
        return ask_id, answer

    def answer_question(self, ask_id, answer):
        url = f"https://pan.baidu.com/act/v2/membergrowv2/answerquestion?app_id=250528&web=5&ask_id={ask_id}&answer={answer}"
        resp = self.session.get(url, headers=self.headers)
        answer_score = None
        answer_msg = ""
        if resp.status_code == 200:
            m = re.search(r'"score":(\d+)', resp.text)
            if m:
                answer_score = m.group(1)
            m2 = re.search(r'"show_msg":"(.*?)"', resp.text)
            if m2:
                answer_msg = m2.group(1)
        return answer_score, answer_msg

    def get_userinfo(self):
        url = "https://pan.baidu.com/rest/2.0/membership/user?app_id=250528&web=5&method=query"
        resp = self.session.get(url, headers=self.headers)
        current_value = None
        current_level = None
        if resp.status_code == 200:
            m = re.search(r'current_value":(\d+),', resp.text)
            if m:
                current_value = m.group(1)
            m2 = re.search(r'current_level":(\d+),', resp.text)
            if m2:
                current_level = m2.group(1)
        return current_level, current_value

    def main(self):
        sign_point, signin_error_msg = self.signin()
        time.sleep(3)
        ask_id, answer = self.get_question()
        answer_score, answer_msg = (None, "")
        if ask_id and answer:
            answer_score, answer_msg = self.answer_question(ask_id, answer)
        current_level, current_value = self.get_userinfo()
        msg = f"签到获得{sign_point or ''}{signin_error_msg}\n答题获得{answer_score or ''}{answer_msg}\n当前会员等级{current_level or ''}，成长值{current_value or ''}"
        return msg


if __name__ == "__main__":
    with open(
        os.path.join(os.path.dirname(os.path.dirname(__file__)), "config.json"),
        encoding="utf-8",
    ) as f:
        datas = json.loads(f.read())
    _check_item = datas.get("BAIDUWP", [])[0]
    print(BaiduWP(check_item=_check_item).main())
