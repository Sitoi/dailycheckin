import hashlib
import json
import os
import re
import time

import requests
import urllib3

from dailycheckin import CheckIn

urllib3.disable_warnings()


class SMZDM(CheckIn):
    name = "什么值得买"

    def __init__(self, check_item: dict):
        self.check_item = check_item

    def robot_token(self, headers):
        ts = int(round(time.time() * 1000))
        url = "https://user-api.smzdm.com/robot/token"
        data = {
            "f": "android",
            "v": "10.4.1",
            "weixin": 1,
            "time": ts,
            "sign": hashlib.md5(
                bytes(
                    f"f=android&time={ts}&v=10.4.1&weixin=1&key=apr1$AwP!wRRT$gJ/q.X24poeBInlUJC",
                    encoding="utf-8",
                )
            )
            .hexdigest()
            .upper(),
        }
        html = requests.post(url=url, headers=headers, data=data)
        result = html.json()
        token = result["data"]["token"]
        return token

    def sign(self, headers, token):
        Timestamp = int(round(time.time() * 1000))
        data = {
            "f": "android",
            "v": "10.4.1",
            "sk": "ierkM0OZZbsuBKLoAgQ6OJneLMXBQXmzX+LXkNTuKch8Ui2jGlahuFyWIzBiDq/L",
            "weixin": 1,
            "time": Timestamp,
            "token": token,
            "sign": hashlib.md5(
                bytes(
                    f"f=android&sk=ierkM0OZZbsuBKLoAgQ6OJneLMXBQXmzX+LXkNTuKch8Ui2jGlahuFyWIzBiDq/L&time={Timestamp}&token={token}&v=10.4.1&weixin=1&key=apr1$AwP!wRRT$gJ/q.X24poeBInlUJC",
                    encoding="utf-8",
                )
            )
            .hexdigest()
            .upper(),
        }
        url = "https://user-api.smzdm.com/checkin"
        resp = requests.post(url=url, headers=headers, data=data)
        error_msg = resp.json()["error_msg"]
        return error_msg, data

    def all_reward(self, headers, data):
        url2 = "https://user-api.smzdm.com/checkin/all_reward"
        resp = requests.post(url=url2, headers=headers, data=data)
        result = resp.json()
        msgs = []
        if normal_reward := result["data"]["normal_reward"]:
            msgs = [
                {
                    "name": "签到奖励",
                    "value": normal_reward["reward_add"]["content"],
                },
                {
                    "name": "连续签到",
                    "value": normal_reward["sub_title"],
                },
            ]
        return msgs

    def active(self, cookie):
        zdm_active_id = ["ljX8qVlEA7"]
        for active_id in zdm_active_id:
            url = f"https://zhiyou.smzdm.com/user/lottery/jsonp_draw?active_id={active_id}"
            rewardurl = f"https://zhiyou.smzdm.com/user/lottery/jsonp_get_active_info?active_id={active_id}"
            infourl = "https://zhiyou.smzdm.com/user/"
            headers = {
                "Host": "zhiyou.smzdm.com",
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": cookie,
                "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148/smzdm 10.4.6 rv:130.1 (iPhone 13; iOS 15.6; zh_CN)/iphone_smzdmapp/10.4.6/wkwebview/jsbv_1.0.0",
                "Accept-Language": "zh-CN,zh-Hans;q=0.9",
                "Referer": "https://m.smzdm.com/",
                "Accept-Encoding": "gzip, deflate, br",
            }
            response = requests.post(url=url, headers=headers).json()
            response_info = requests.get(url=infourl, headers=headers).text
            _ = requests.get(url=rewardurl, headers=headers).json()
            name = (
                str(
                    re.findall(
                        '<a href="https://zhiyou.smzdm.com/user"> (.*?) </a>',
                        str(response_info),
                        re.S,
                    )
                )
                .replace("[", "")
                .replace("]", "")
                .replace("'", "")
            )
            level = (
                str(
                    re.findall(
                        r'<img src="https://res.smzdm.com/h5/h5_user/dist/assets/level/(.*?).png\?v=1">',
                        str(response_info),
                        re.S,
                    )
                )
                .replace("[", "")
                .replace("]", "")
                .replace("'", "")
            )
            gold = (
                str(
                    re.findall(
                        '<div class="assets-part assets-gold">\n                    (.*?)</span>',
                        str(response_info),
                        re.S,
                    )
                )
                .replace("[", "")
                .replace("]", "")
                .replace("'’", "")
                .replace('<span class="assets-part-element assets-num">', "")
                .replace("'", "")
            )
            silver = (
                str(
                    re.findall(
                        '<div class="assets-part assets-prestige">\n                    (.*?)</span>',
                        str(response_info),
                        re.S,
                    )
                )
                .replace("[", "")
                .replace("]", "")
                .replace("'’", "")
                .replace('<span class="assets-part-element assets-num">', "")
                .replace("'", "")
            )
            msg = [
                {
                    "name": "签到结果",
                    "value": response["error_msg"],
                },
                {"name": "等级", "value": level},
                {"name": "昵称", "value": name},
                {"name": "金币", "value": gold},
                {"name": "碎银", "value": silver},
            ]
        return msg

    def main(self):
        cookie = self.check_item.get("cookie")
        headers = {
            "Host": "user-api.smzdm.com",
            "Content-Type": "application/x-www-form-urlencoded",
            "Cookie": cookie,
            "User-Agent": "smzdm_android_V10.4.1 rv:841 (22021211RC;Android12;zh)smzdmapp",
        }
        msg = self.active(cookie)
        token = self.robot_token(headers)
        error_msg, data = self.sign(headers, token)
        msg.append({"name": "签到结果", "value": error_msg})
        reward_msg = self.all_reward(headers, data)
        msg += reward_msg
        msg = "\n".join([f"{one.get('name')}: {one.get('value')}" for one in msg])
        return msg


if __name__ == "__main__":
    with open(
        os.path.join(os.path.dirname(os.path.dirname(__file__)), "config.json"),
        encoding="utf-8",
    ) as f:
        datas = json.loads(f.read())
    _check_item = datas.get("SMZDM", [])[0]
    print(SMZDM(check_item=_check_item).main())
