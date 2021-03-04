# -*- coding: utf-8 -*-
import json
import os

import requests
from requests import utils


class SmzdmCheckIn:
    def __init__(self, check_item):
        self.check_item = check_item

    @staticmethod
    def sign(session):
        try:
            current = session.get(url="https://zhiyou.smzdm.com/user/info/jsonp_get_current").json()
            if current["checkin"]["has_checkin"]:
                msg = (
                    f"用户信息: {current.get('nickname', '')}\n目前积分: {current.get('point', '')}\n"
                    f"经验值: {current.get('exp', '')}\n金币: {current.get('gold', '')}\n"
                    f"碎银子: {current.get('silver', '')}\n威望: {current.get('prestige', '')}\n"
                    f"等级: {current.get('level', '')}\n"
                    f"已经签到: {current.get('checkin', {}).get('daily_checkin_num', '')} 天"
                )
            else:
                response = session.get(url="https://zhiyou.smzdm.com/user/checkin/jsonp_checkin").json().get("data", {})
                msg = (
                    f"用户信息: {current.get('nickname', '')}\n目前积分: {response.get('point', '')}\n"
                    f"增加积分: {response.get('add_point', '')}\n经验值: {response.get('exp', '')}\n"
                    f"金币: {response.get('gold', '')}\n威望: {response.get('prestige', '')}\n"
                    f"等级: {response.get('rank', '')}\n"
                    f"已经签到: {response.get('checkin_num', {})} 天"
                )
        except Exception as e:
            msg = f"签到状态: 签到失败\n错误信息: {e}"
        return msg

    def main(self):
        smzdm_cookie = {
            item.split("=")[0]: item.split("=")[1] for item in self.check_item.get("smzdm_cookie").split("; ")
        }
        session = requests.session()
        requests.utils.add_dict_to_cookiejar(session.cookies, smzdm_cookie)
        session.headers.update(
            {
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "zh-CN,zh;q=0.9",
                "Connection": "keep-alive",
                "Host": "zhiyou.smzdm.com",
                "Referer": "https://www.smzdm.com/",
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "same-site",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36",
            }
        )
        sign_msg = self.sign(session=session)
        msg = f"{sign_msg}"
        return msg


if __name__ == "__main__":
    with open(
        os.path.join(os.path.dirname(os.path.dirname(__file__)), "config/config.json"), "r", encoding="utf-8"
    ) as f:
        datas = json.loads(f.read())
    _check_item = datas.get("SMZDM_COOKIE_LIST", [])[0]
    print(SmzdmCheckIn(check_item=_check_item).main())
