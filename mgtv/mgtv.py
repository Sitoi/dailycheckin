# -*- coding: utf-8 -*-
import json
import os
import time
from urllib import parse

import requests


class MgtvCheckIn:
    def __init__(self, mgtv_params_list):
        self.mgtv_params_list = mgtv_params_list

    @staticmethod
    def sign(params):
        url = "https://credits.bz.mgtv.com/user/creditsTake"
        user_params = {
            "abroad": params.get("abroad"),
            "ageMode": "0",
            "appVersion": params.get("appVersion"),
            "artistId": params.get("uuid"),
            "device": params.get("device"),
            "did": params.get("did"),
            "mac": params.get("did"),
            "osType": params.get("osType"),
            "src": "mgtv",
            "testversion": "",
            "ticket": params.get("ticket"),
            "uuid": params.get("uuid"),
        }
        try:
            user_info = requests.get(
                url="https://homepage.bz.mgtv.com/v2/user/userInfo",
                params=user_params
            ).json()
            username = user_info.get("data", {}).get("nickName")
        except Exception as e:
            print("获取用户信息失败", e)
            username = params.get("uuid")
        res = requests.get(url=url, params=params)
        res_json = json.loads(res.text.replace(f"{params.get('callback')}(", "").replace(");", ""))
        if res_json["code"] == 200:
            cur_day = res_json["data"]["curDay"]
            _credits = res_json["data"]["credits"]
            msg = f"帐号信息: {username}\n签到积分: +{_credits}积分\n已经签到: {cur_day}天/21天"
        else:
            msg = f"帐号信息: {username}\n签到状态: 已完成签到 or 签到失败"
        return msg

    def main(self):
        msg_list = []
        for mgtv_cookie in self.mgtv_params_list:
            mgtv_params = mgtv_cookie.get("mgtv_params")
            params = parse.parse_qs(mgtv_params)
            params["timestamp"] = [round(time.time())]
            params = {key: value[0] for key, value in params.items()}
            sign_msg = self.sign(params=params)
            msg = f"【芒果TV】\n{sign_msg}"
            msg_list.append(msg)
        return msg_list


if __name__ == '__main__':
    with open(
        os.path.join(os.path.dirname(os.path.dirname(__file__)), "config/config.json"), "r", encoding="utf-8"
    ) as f:
        datas = json.loads(f.read())
    _mgtv_params_list = datas.get("MGTV_PARAMS_LIST", [])
    MgtvCheckIn(mgtv_params_list=_mgtv_params_list).main()
