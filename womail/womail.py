# -*- coding: utf-8 -*-
import json
import os
import re

import requests


class WoMailCheckIn:
    def __init__(self, check_item):
        self.check_item = check_item

    @staticmethod
    def login(womail_url):
        try:
            url = womail_url
            headers = {
                "User-Agent": "User-Agent: Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3868.400 QQBrowser/10.8.4394.400"
            }
            res = requests.get(url=url, headers=headers, allow_redirects=False)
            set_cookie = res.headers["Set-Cookie"]
            cookies = re.findall("YZKF_SESSION.*?;", set_cookie)[0]
            if "YZKF_SESSION" in cookies:
                return cookies
            else:
                print("沃邮箱获取 cookies 失败")
                return None
        except Exception as e:
            print("沃邮箱错误:", e)
            return None

    @staticmethod
    def dotask(cookies):
        msg = ""
        headers = {
            "User-Agent": "User-Agent: Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3868.400 QQBrowser/10.8.4394.400",
            "Cookie": cookies,
        }
        try:
            url = "https://nyan.mail.wo.cn/cn/sign/index/userinfo.do?rand=0.8897817905278955"
            res = requests.post(url=url, headers=headers)
            result = res.json()
            wxName = result.get("result").get("wxName")
            userMobile = result.get("result").get("userMobile")
            userdata = f"帐号信息: {wxName} - {userMobile[:3]}****{userMobile[-4:]}\n"
            msg += userdata
        except Exception as e:
            print("沃邮箱获取用户信息失败", e)
            msg += "沃邮箱获取用户信息失败\n"
        try:
            url = "https://nyan.mail.wo.cn/cn/sign/user/checkin.do?rand=0.913524814493383"
            res = requests.post(url=url, headers=headers).json()
            result = res.get("result")
            if result == -2:
                msg += "每日签到: 已签到\n"
            elif result is None:
                msg += f"每日签到: 签到失败\n"
            else:
                msg += f"每日签到: 签到成功~已签到{result}天！\n"
        except Exception as e:
            print("沃邮箱签到错误", e)
            msg += "沃邮箱签到错误\n"
        try:
            url = "https://nyan.mail.wo.cn/cn/sign/user/doTask.do?rand=0.8776674762904109"
            data_params = {
                "每日首次登录手机邮箱": {"taskName": "loginmail"},
                "和WOWO熊一起寻宝": {"taskName": "treasure"},
                "去用户俱乐部逛一逛": {"taskName": "club"},
            }
            for key, data in dict.items(data_params):
                try:
                    res = requests.post(url=url, data=data, headers=headers).json()
                    result = res.get("result")
                    if result == 1:
                        msg += f"{key}: 做任务成功\n"
                    elif result == -1:
                        msg += f"{key}: 任务已做过\n"
                    elif result == -2:
                        msg += f"{key}: 请检查登录状态\n"
                    else:
                        msg += f"{key}: 未知错误\n"
                except Exception as e:
                    print(f"沃邮箱执行任务【{key}】错误", e)
                    msg += f"沃邮箱执行任务【{key}】错误"

        except Exception as e:
            print("沃邮箱执行任务错误", e)
            msg += "沃邮箱执行任务错误错误"
        return msg

    @staticmethod
    def dotask2(womail_url):
        msg = ""
        userdata = re.findall("mobile.*", womail_url)[0]
        url = "https://club.mail.wo.cn/clubwebservice/?" + userdata
        headers = {
            "User-Agent": "User-Agent: Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3868.400 QQBrowser/10.8.4394.400"
        }
        try:
            res = requests.get(url=url, headers=headers, allow_redirects=False)
            set_cookie = res.headers["Set-Cookie"]
            cookies = re.findall("SESSION.*?;", set_cookie)[0]
            if "SESSION" in cookies:
                headers = {
                    "User-Agent": "User-Agent: Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3868.400 QQBrowser/10.8.4394.400",
                    "Cookie": cookies,
                }
                # 获取用户信息
                try:
                    url = "https://club.mail.wo.cn/clubwebservice/club-user/user-info/get-user-score-info/"
                    res = requests.get(url=url, headers=headers)
                    result = res.json()
                    integralTotal = result.get("integralTotal")
                    userMobile = result.get("userPhoneNum")
                    userdata = f"帐号信息: {userMobile[:3]}****{userMobile[-4:]}\n当前积分:{integralTotal}\n"
                    msg += userdata
                    url_params = {
                        "每日签到": "https://club.mail.wo.cn/clubwebservice/growth/userSign",
                        "参与活动": f"https://club.mail.wo.cn/clubwebservice/growth/addIntegral?phoneNum={userMobile}&resourceType=huodong",
                        "沃邮箱邮件查看": f"https://club.mail.wo.cn/clubwebservice/growth/addIntegral?phoneNum={userMobile}&resourceType=lookMail",
                        "沃门户": f"https://club.mail.wo.cn/clubwebservice/growth/addIntegral?phoneNum={userMobile}&resourceType=womenhuzhuye",
                    }
                    # 执行任务
                    for key, data in dict.items(url_params):
                        try:
                            res = requests.get(url=data, headers=headers).json()
                            result = res.get("description")
                            msg += f"{key}: {result}\n"
                        except Exception as e:
                            print(f"沃邮箱俱乐部执行任务【{key}】错误", e)
                            msg += f"沃邮箱俱乐部执行任务【{key}】错误"
                except Exception as e:
                    print("沃邮箱俱乐部获取用户信息失败", e)
                    msg += "沃邮箱俱乐部获取用户信息失败\n"
            else:
                msg += "沃邮箱俱乐部获取用户信息失败\n"
        except Exception as e:
            print("沃邮箱俱乐部获取cookies失败", e)
            msg += "沃邮箱俱乐部获取cookies失败\n"
        return msg

    def main(self):
        womail_url = self.check_item.get("womail_url")
        try:
            cookies = self.login(womail_url)
            if cookies:
                msg = self.dotask(cookies)
                msg += f"\n沃邮箱俱乐部\n{self.dotask2(womail_url)}"
            else:
                msg = "登录失败"
        except Exception as e:
            print(e)
            msg = "登录失败"
        return msg


if __name__ == "__main__":
    with open(
        os.path.join(os.path.dirname(os.path.dirname(__file__)), "config/config.json"), "r", encoding="utf-8"
    ) as f:
        datas = json.loads(f.read())
    _check_item = datas.get("WOMAIL_URL_LIST", [])[0]
    print(WoMailCheckIn(check_item=_check_item).main())
