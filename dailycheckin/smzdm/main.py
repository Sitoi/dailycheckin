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
    name = "SMZDM"

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
        return result

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
        result = self.all_reward(headers, data)
        msg.append(
            {
                "name": "什么值得买",
                "value": json.dumps(result["data"], ensure_ascii=False),
            },
        )
        msg = "\n".join([f"{one.get('name')}: {one.get('value')}" for one in msg])
        return msg


if __name__ == "__main__":
    with open(
        os.path.join(os.path.dirname(os.path.dirname(__file__)), "config.json"),
        encoding="utf-8",
    ) as f:
        datas = json.loads(f.read())
    # _check_item = datas.get("SMZDM", [])[0]
    _check_item = {
        "cookie": """__ckguid=syS3E6T5OCJLT2E2LtVRkn7; device_id=188331107416928912791221025b946eae97755d38628197ea52594f71; homepage_sug=d; r_sort_type=score; footer_floating_layer=0; ad_date=12; ad_json_feed=%7B%7D; _zdmA.vid=*; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2218a282eeded81d-0de23c34e957fb-4f641475-2304000-18a282eedee1f08%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.google.com%2F%22%7D%2C%22%24device_id%22%3A%2218a282eeded81d-0de23c34e957fb-4f641475-2304000-18a282eedee1f08%22%7D; sess=BA-13x0dQd4qdaZ4D80mDJAjqYFq9dT%2BR50CBfBp0Jnd41uWsf0FTKL%2FVdoJeSxRpXZMjc8EqTPS8hHhlyOAUmmX6RtU51votM3vyQB%2BhygL6cVeuCChgalixWu; user=user%3A9072273596%7C9072273596; smzdm_id=9072273596; _zdmA.uid=ZDMA.z9bFuVR0E.1704990066.2419200; bannerCounter=%5B%7B%22number%22%3A1%2C%22surplus%22%3A1%7D%2C%7B%22number%22%3A0%2C%22surplus%22%3A2%7D%2C%7B%22number%22%3A0%2C%22surplus%22%3A1%7D%2C%7B%22number%22%3A0%2C%22surplus%22%3A1%7D%2C%7B%22number%22%3A1%2C%22surplus%22%3A1%7D%5D; _zdmA.time=1704990066978.0.https%3A%2F%2Fwww.smzdm.com%2F"""
    }
    print(SMZDM(check_item=_check_item).main())
