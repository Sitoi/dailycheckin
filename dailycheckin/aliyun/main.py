import json
import os

import requests
import urllib3

from dailycheckin import CheckIn

urllib3.disable_warnings()


class AliYun(CheckIn):
    name = "阿里云盘"

    def __init__(self, check_item: dict):
        self.check_item = check_item

    def update_token(self, refresh_token):
        url = "https://auth.aliyundrive.com/v2/account/token"
        data = {"grant_type": "refresh_token", "refresh_token": refresh_token}
        response = requests.post(url=url, json=data).json()
        access_token = response.get("access_token")
        return access_token

    def sign(self, access_token):
        url = "https://member.aliyundrive.com/v1/activity/sign_in_list"
        headers = {"Authorization": access_token, "Content-Type": "application/json"}
        result = requests.post(url=url, headers=headers, json={}).json()
        sign_days = result["result"]["signInCount"]
        data = {"signInDay": sign_days}
        url_reward = "https://member.aliyundrive.com/v1/activity/sign_in_reward"
        requests.post(url=url_reward, headers=headers, data=json.dumps(data))
        if "success" in result:
            print("签到成功")
            for i, j in enumerate(result["result"]["signInLogs"]):
                if j["status"] == "miss":
                    day_json = result["result"]["signInLogs"][i - 1]
                    if not day_json["isReward"]:
                        msg = [
                            {
                                "name": "阿里云盘",
                                "value": "签到成功，今日未获得奖励",
                            }
                        ]
                    else:
                        msg = [
                            {
                                "name": "累计签到",
                                "value": result["result"]["signInCount"],
                            },
                            {
                                "name": "阿里云盘",
                                "value": "获得奖励：{}{}".format(
                                    day_json["reward"]["name"],
                                    day_json["reward"]["description"],
                                ),
                            },
                        ]

                    return msg

    def main(self):
        refresh_token = self.check_item.get("refresh_token")
        access_token = self.update_token(refresh_token)
        if not access_token:
            return [{"name": "阿里云盘", "value": "token 过期"}]
        msg = self.sign(access_token)
        msg = "\n".join([f"{one.get('name')}: {one.get('value')}" for one in msg])
        return msg


if __name__ == "__main__":
    with open(
        os.path.join(os.path.dirname(os.path.dirname(__file__)), "config.json"),
        encoding="utf-8",
    ) as f:
        datas = json.loads(f.read())
    _check_item = datas.get("ALIYUN", [])[0]
    print(AliYun(check_item=_check_item).main())
