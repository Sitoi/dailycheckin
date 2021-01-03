# -*- coding: utf-8 -*-
import json
import os
from datetime import datetime

import requests


class LianTongCheckIn:

    def __init__(self, liantong_account_list):
        self.liantong_account_list = liantong_account_list

    @staticmethod
    def sign(liantong_data):
        session = requests.session()
        headers = {
            'Host': 'm.client.10010.com',
            'Accept': '*/*',
            'User-Agent': 'ChinaUnicom4.x/810 CFNetwork/1209 Darwin/20.2.0',
            'Accept-Language': 'zh-cn',
        }
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        data = f"reqtime={timestamp}&{liantong_data}"
        req1 = session.post(url="http://m.client.10010.com/mobileService/login.htm", headers=headers, data=data)
        a_token = req1.cookies.get("a_token")
        if a_token and req1.status_code == 200:
            phone = req1.json().get("default")
            req3 = session.post("https://act.10010.com/SigninApp/signin/querySigninActivity.htm?token=" + a_token)
            if req3.status_code == 200:
                req4 = session.post("https://act.10010.com/SigninApp/signin/daySign", "btnPouplePost".encode("utf-8"))
                if req4.status_code == 200:
                    req5 = session.post("https://act.10010.com/SigninApp/signin/getIntegral")
                    return f"帐号信息: {phone}\n签到信息: {json.dumps(req5.json())}"
        return f"帐号信息: 获取失败\n签到信息: 请检查参数是否过期"

    def main(self):
        msg_list = []
        for liantong_account in self.liantong_account_list:
            liantong_data = liantong_account.get("data")
            sign_msg = self.sign(liantong_data=liantong_data)
            msg = f"【联通营业厅】\n{sign_msg}"
            print(msg)
            msg_list.append(msg)
        return msg_list


if __name__ == "__main__":
    with open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "config.json"), "r", encoding="utf-8") as f:
        datas = json.loads(f.read())
    _liantong_account_list = datas.get("LIANTONG_ACCOUNT_LIST", [])
    LianTongCheckIn(liantong_account_list=_liantong_account_list).main()
