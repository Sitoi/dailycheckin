# -*- coding: utf-8 -*-
import json
import os

import requests


class SmzdmCheckIn:
    def __init__(self, smzdm_cookie_list):
        self.smzdm_cookie_list = smzdm_cookie_list

    @staticmethod
    def sign(session):
        try:
            current = session.get(url='https://zhiyou.smzdm.com/user/info/jsonp_get_current').json()
            if current['checkin']['has_checkin']:
                print(current)
                msg = f"用户信息: {current['nickname']}\n目前积分: {current['point']}\n" \
                      f"经验值: {current['exp']}\n金币: {current['gold']}\n" \
                      f"碎银子: {current['silver']}\n威望: {current['prestige']}\n等级: {current['level']}\n" \
                      f"已经签到: {current['checkin']['daily_checkin_num']} 天"
            else:
                response = session.get(url="https://zhiyou.smzdm.com/user/checkin/jsonp_checkin").json()
                print(response)
                msg = f"用户信息: {current['nickname']}\n目前积分: {response['point']}\n" \
                      f"增加积分: {response['add_point']}\n经验值: {response['exp']}\n" \
                      f"金币: {response['gold']}\n威望: {response['prestige']}\n等级: {response['rank']}"
            print(msg)
        except Exception as e:
            msg = f"签到状态: 签到失败\n错误信息: {e}"
        return msg

    def main(self):
        msg_list = []
        for smzdm_cookie in self.smzdm_cookie_list:
            smzdm_cookie = {
                item.split("=")[0]: item.split("=")[1] for item in smzdm_cookie.get("smzdm_cookie").split("; ")
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
            msg = f"【什么值得买】\n{sign_msg}"
            print(msg)
            msg_list.append(msg)
        return msg_list


if __name__ == "__main__":
    with open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "config.json"), "r", encoding="utf-8") as f:
        datas = json.loads(f.read())
    _smzdm_cookie_list = datas.get("SMZDM_COOKIE_LIST", [])
    SmzdmCheckIn(smzdm_cookie_list=_smzdm_cookie_list).main()
