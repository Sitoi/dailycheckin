# -*- coding: utf-8 -*-
import json
import os

import requests
import urllib3

urllib3.disable_warnings()


class AcFunCheckIn:
    def __init__(self, acfun_account_list):
        self.acfun_account_list = acfun_account_list

    @staticmethod
    def sign(session, phone, password):
        url = "https://id.app.acfun.cn/rest/app/login/signin"
        headers = {
            "Host": "id.app.acfun.cn",
            "user-agent": "AcFun/6.39.0 (iPhone; iOS 14.3; Scale/2.00)",
            "devicetype": "0",
            "accept-language": "zh-Hans-CN;q=1, en-CN;q=0.9, ja-CN;q=0.8, zh-Hant-HK;q=0.7, io-Latn-CN;q=0.6",
            "accept": "application/json",
            "content-type": "application/x-www-form-urlencoded",
        }
        data = f"password={password}&username={phone}"
        response = session.post(url=url, data=data, headers=headers, verify=False)
        acpasstoken = response.json().get("acPassToken")
        auth_key = str(response.json().get("auth_key"))
        if acpasstoken and auth_key:
            cookies = {"acPasstoken": acpasstoken, "auth_key": auth_key}
            headers = {"acPlatform": "IPHONE"}
            response = session.post(
                url="https://api-ipv6.acfunchina.com/rest/app/user/signIn", headers=headers, cookies=cookies
            )
            return response.json().get("msg")
        else:
            return "登录失败！请检查密码是否正确！"

    def main(self):
        msg_list = []
        for acfun_account in self.acfun_account_list:
            phone = acfun_account.get("acfun_phone")
            password = acfun_account.get("acfun_password")
            session = requests.session()
            sign_msg = self.sign(session=session, phone=phone, password=password)
            msg = f"【AcFun 签到】\n帐号信息: {phone}\n签到状态: {sign_msg}"
            msg_list.append(msg)
        return msg_list


if __name__ == "__main__":
    with open(
        os.path.join(os.path.dirname(os.path.dirname(__file__)), "config/config.json"), "r", encoding="utf-8"
    ) as f:
        datas = json.loads(f.read())
    _acfun_account_list = datas.get("ACFUN_ACCOUNT_LIST", [])
    AcFunCheckIn(acfun_account_list=_acfun_account_list).main()
