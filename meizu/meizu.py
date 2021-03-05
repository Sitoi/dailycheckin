# -*- coding: utf-8 -*-
import json
import os
import time

import requests


class MeizuCheckIn:
    def __init__(self, check_item):
        self.check_item = check_item

    @staticmethod
    def sign(cookie):
        headers = {
            "authority": "bbs-act.meizu.cn",
            "pragma": "no-cache",
            "cache-control": "no-cache",
            "accept": "application/json, text/javascript, */*; q=0.01",
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36 Edg/88.0.705.74",
            "origin": "https://bbs.meizu.cn",
            "referer": "https://bbs.meizu.cn/",
            "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
            "cookie": cookie,
        }
        params = (
            ("mod", "signin"),
            ("action", "sign"),
        )
        response = requests.get(url="https://bbs-act.meizu.cn/index.php", headers=headers, params=params).json()
        msg = response.get("message")
        return msg

    @staticmethod
    def draw(cookie, count: int = 0):
        headers = {
            "authority": "bbs-act.meizu.cn",
            "accept": "application/json, text/javascript, */*; q=0.01",
            "x-requested-with": "XMLHttpRequest",
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36 Edg/88.0.705.74",
            "content-type": "application/x-www-form-urlencoded",
            "origin": "https://bbs-act.meizu.cn",
            "referer": "https://bbs-act.meizu.cn/2/index.html",
            "accept-language": "zh-CN,zh;q=0.9",
            "cookie": cookie,
        }
        data = {"mod": "index", "action": "draw", "id": "2"}
        award_list = []
        success_count = 0
        error_count = 0
        if count:
            for i in range(count):
                try:
                    data = requests.post(url="https://bbs-act.meizu.cn/index.php", headers=headers, data=data).json()
                    if data["code"] == 200:
                        one_msg = data.get("data", {}).get("award_name")
                        award_list.append(one_msg)
                        success_count += 1
                    else:
                        error_count += 1
                        print(data.get("code"), data.get("message"))
                        one_msg = "抽奖失败"
                except Exception as e:
                    one_msg = f"抽奖失败: {e}"
                    error_count += 1
                print(f"第{i + 1}次抽奖结果：" + str(one_msg))
                time.sleep(5)
            msg = f"成功抽奖 {success_count} 次"
            draw_msg = "抽奖状态: " + str(msg)
            draw_msg += f"\n抽奖结果: {';'.join(award_list)}"
        else:
            draw_msg = "抽奖结果: 未开启抽奖"
        data = {"mod": "index", "action": "get_user_count", "id": "2"}
        user_info = requests.post("https://bbs-act.meizu.cn/index.php", headers=headers, data=data).json()
        uid = user_info.get("data", {}).get("uid")
        return draw_msg, uid

    def main(self):
        meizu_cookie = self.check_item.get("meizu_cookie")
        try:
            draw_count = int(self.check_item.get("draw_count", 0))
        except Exception as e:
            print("初始化抽奖次数失败: 重置为 0 ", str(e))
            draw_count = 0
        sign_msg = self.sign(cookie=meizu_cookie)
        draw_msg, uid = self.draw(cookie=meizu_cookie, count=draw_count)
        msg = f"帐号信息: {uid}\n签到信息: {sign_msg}\n{draw_msg}"
        return msg


if __name__ == "__main__":
    with open(
        os.path.join(os.path.dirname(os.path.dirname(__file__)), "config/config.json"), "r", encoding="utf-8"
    ) as f:
        datas = json.loads(f.read())
    _check_item = datas.get("MEIZU_COOKIE_LIST", [])[0]
    print(MeizuCheckIn(check_item=_check_item).main())
