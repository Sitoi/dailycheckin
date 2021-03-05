# -*- coding: utf-8 -*-
import hashlib
import json
import os
import re

import requests
from requests import utils


class TiebaCheckIn:
    def __init__(self, check_item):
        self.check_item = check_item

    @staticmethod
    def login_info(session):
        return session.get(url="https://zhidao.baidu.com/api/loginInfo").json()

    def valid(self, session):
        try:
            content = session.get(url="http://tieba.baidu.com/dc/common/tbs")
        except Exception as e:
            return False, f"登录验证异常,错误信息: {e}"
        data = json.loads(content.text)
        if data["is_login"] == 0:
            return False, "登录失败,cookie 异常"
        tbs = data["tbs"]
        user_name = self.login_info(session=session)["userName"]
        return tbs, user_name

    @staticmethod
    def tieba_list(session):
        data = session.get(url="https://tieba.baidu.com/mo/q/newmoindex").json()
        if data["no"] == 0:
            return [x["forum_name"] for x in data["data"]["like_forum"]]
        else:
            return []

    @staticmethod
    def tieba_list_more(session):
        content = session.get(url="http://tieba.baidu.com/f/like/mylike?&pn=1", timeout=(5, 20))
        pn = int(re.match(r".*/f/like/mylike\?&pn=(.*?)\">尾页.*", content.text, re.S | re.I).group(1))
        next_page = 1
        pattern = re.compile(r".*?<a href=\"/f\?kw=.*?title=\"(.*?)\">")
        while next_page <= pn:
            tbname = pattern.findall(content.text)
            for x in tbname:
                yield x
            next_page += 1
            content = session.get(url=f"http://tieba.baidu.com/f/like/mylike?&pn={next_page}", timeout=(5, 20))

    def get_tieba_list(self, session):
        try:
            session.get(url="https://tieba.baidu.com/f/user/json_userinfo", allow_redirects=False).json()
        except Exception as e:
            print(e)
            tieba_list = self.tieba_list(session=session)
        else:
            tieba_list = self.tieba_list_more(session=session)
        return tieba_list

    @staticmethod
    def sign(session, tb_name_list, tbs):
        success_count, error_count, exist_count = 0, 0, 0
        for tb_name in tb_name_list:
            md5 = hashlib.md5(f"kw={tb_name}tbs={tbs}tiebaclient!!!".encode("utf-8")).hexdigest()
            data = {"kw": tb_name, "tbs": tbs, "sign": md5}
            try:
                response = session.post(url="http://c.tieba.baidu.com/c/c/forum/sign", data=data).json()
                if response["error_code"] == "0":
                    success_count += 1
                elif response["error_code"] == "160002":
                    exist_count += 1
                else:
                    error_count += 1
            except Exception as e:
                print(f"贴吧 {tb_name} 签到异常,原因{str(e)}")
        msg = f"贴吧总数: {len(tb_name_list)}\n签到成功: {success_count}\n已经签到: {exist_count}\n签到失败: {error_count}"
        return msg

    def main(self):
        tieba_cookie = {
            item.split("=")[0]: item.split("=")[1] for item in self.check_item.get("tieba_cookie").split("; ")
        }
        session = requests.session()
        requests.utils.add_dict_to_cookiejar(session.cookies, tieba_cookie)
        session.headers.update({"Referer": "https://www.baidu.com/"})
        tbs, user_name = self.valid(session=session)
        if tbs:
            tb_name_list = self.get_tieba_list(session=session)
            msg = self.sign(session=session, tb_name_list=tb_name_list, tbs=tbs)
            msg = f"帐号信息: {user_name}\n{msg}"
        else:
            msg = f"帐号信息: {user_name}\n签到状态: Cookie 可能过期"
        return msg


if __name__ == "__main__":
    with open(
        os.path.join(os.path.dirname(os.path.dirname(__file__)), "config/config.json"), "r", encoding="utf-8"
    ) as f:
        datas = json.loads(f.read())
    _check_item = datas.get("TIEBA_COOKIE_LIST", [])[0]
    print(TiebaCheckIn(check_item=_check_item).main())
