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
        self.check_item = check_item
        self.cookie = check_item.get("cookie", "")
        self.cookie_values = self._parse_cookie(self.cookie)
        self.session = requests.Session()
        self.session.headers.update(
            {
                "User-Agent": "Mozilla/5.0 (Linux; Android 11; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.91 Mobile Safari/537.36",
                "Referer": "https://pan.baidu.com/wap/svip/growth/task",
                "Accept": "application/json, text/plain, */*",
                "X-Requested-With": "XMLHttpRequest",
                "Connection": "keep-alive",
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
            }
        )
        # Let Session build the Cookie header. This allows cookies returned in
        # Set-Cookie to take effect on the following request.
        for name, value in self.cookie_values.items():
            self.session.cookies.set(name, value, domain=".baidu.com", path="/")

    @staticmethod
    def _parse_cookie(cookie_header: str) -> dict:
        result = {}
        for item in cookie_header.split(";"):
            name, separator, value = item.strip().partition("=")
            if separator and name:
                result[name] = value
        return result

    def _get(self, url: str):
        resp = self.session.get(url)
        cookie_changed = False
        now = time.time()

        # requests can retain both the old and new cookie when their domains or
        # paths differ. A browser resolves this using its persistent cookie jar;
        # normalize cookies with the same name before the next request instead.
        for updated_cookie in resp.cookies:
            for current_cookie in list(self.session.cookies):
                if current_cookie.name == updated_cookie.name:
                    self.session.cookies.clear(
                        domain=current_cookie.domain,
                        path=current_cookie.path,
                        name=current_cookie.name,
                    )

            expired = updated_cookie.expires is not None and updated_cookie.expires <= now
            if expired:
                if updated_cookie.name in self.cookie_values:
                    self.cookie_values.pop(updated_cookie.name)
                    cookie_changed = True
                continue

            self.session.cookies.set_cookie(updated_cookie)
            if self.cookie_values.get(updated_cookie.name) != updated_cookie.value:
                self.cookie_values[updated_cookie.name] = updated_cookie.value
                cookie_changed = True

        if cookie_changed:
            self.cookie = "; ".join(f"{name}={value}" for name, value in self.cookie_values.items())
            # check_item is the same dict loaded from config.json. The main
            # runner persists it atomically after this account finishes.
            self.check_item["cookie"] = self.cookie

        return resp

    def signin(self):
        url = "https://pan.baidu.com/rest/2.0/membership/level?app_id=250528&web=5&method=signin"
        resp = self._get(url)
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
            signin_error_msg = f"签到请求失败: {resp.status_code}"
        return sign_point, signin_error_msg

    def get_question(self):
        url = "https://pan.baidu.com/act/v2/membergrowv2/getdailyquestion?app_id=250528&web=5"
        resp = self._get(url)
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
        resp = self._get(url)
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
        resp = self._get(url)
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
