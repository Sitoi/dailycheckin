import json
import os

import requests

from dailycheckin import CheckIn


class KGQQ(CheckIn):
    name = "全民K歌"

    def __init__(self, check_item):
        self.check_item = check_item

    @staticmethod
    def sign(kgqq_cookie):
        headers = {"Cookie": kgqq_cookie}
        uid = kgqq_cookie.split("; ")
        t_uuid = ""
        for i in uid:
            if i.find("uid=") >= 0:
                t_uuid = i.split("=")[1]
        proto_profile_url = "https://node.kg.qq.com/webapp/proxy?ns=proto_profile&cmd=profile.getProfile&mapExt=JTdCJTIyZmlsZSUyMiUzQSUyMnByb2ZpbGVfd2ViYXBwSmNlJTIyJTJDJTIyY21kTmFtZSUyMiUzQSUyMlByb2ZpbGVHZXQlMjIlMkMlMjJhcHBpZCUyMiUzQTEwMDA2MjYlMkMlMjJkY2FwaSUyMiUzQSU3QiUyMmludGVyZmFjZUlkJTIyJTNBMjA1MzU5NTk3JTdEJTJDJTIybDVhcGklMjIlM0ElN0IlMjJtb2RpZCUyMiUzQTI5NDAxNyUyQyUyMmNtZCUyMiUzQTI2MjE0NCU3RCUyQyUyMmlwJTIyJTNBJTIyMTAwLjExMy4xNjIuMTc4JTIyJTJDJTIycG9ydCUyMiUzQSUyMjEyNDA2JTIyJTdE&t_uUid={}".format(
            t_uuid
        )

        url_list = (
            [
                "https://node.kg.qq.com/webapp/proxy?ns=KG_TASK&cmd=task.getLottery&ns_inbuf=&mapExt=JTdCJTIyZmlsZSUyMiUzQSUyMnRhc2tKY2UlMjIlMkMlMjJjbWROYW1lJTIyJTNBJTIyTG90dGVyeVJlcSUyMiUyQyUyMnduc0NvbmZpZyUyMiUzQSU3QiUyMmFwcGlkJTIyJTNBMTAwMDU1NyU3RCUyQyUyMmw1YXBpJTIyJTNBJTdCJTIybW9kaWQlMjIlM0E1MDM5MzclMkMlMjJjbWQlMjIlM0E1ODk4MjQlN0QlN0Q%3D&t_uid={}&t_iShowEntry=1&t_type={}".format(
                    t_uuid, one
                )
                for one in ["1", "2"]
            ]
            + [
                "https://node.kg.qq.com/webapp/proxy?ns=KG_TASK&cmd=task.signinGetAward&mapExt=JTdCJTIyZmlsZSUyMiUzQSUyMnRhc2tKY2UlMjIlMkMlMjJjbWROYW1lJTIyJTNBJTIyR2V0U2lnbkluQXdhcmRSZXElMjIlMkMlMjJ3bnNDb25maWclMjIlM0ElN0IlMjJhcHBpZCUyMiUzQTEwMDA2MjYlN0QlMkMlMjJsNWFwaSUyMiUzQSU3QiUyMm1vZGlkJTIyJTNBNTAzOTM3JTJDJTIyY21kJTIyJTNBNTg5ODI0JTdEJTdE&t_uid={}&t_iShowEntry={}".format(
                    t_uuid, one
                )
                for one in ["1", "2", "4", "16", "128", "512"]
            ]
            + [
                "https://node.kg.qq.com/webapp/proxy?ns=KG_TASK&cmd=task.getLottery&mapExt=JTdCJTIyZmlsZSUyMiUzQSUyMnRhc2tKY2UlMjIlMkMlMjJjbWROYW1lJTIyJTNBJTIyTG90dGVyeVJlcSUyMiUyQyUyMnduc0NvbmZpZyUyMiUzQSU3QiUyMmFwcGlkJTIyJTNBMTAwMDU1NyU3RCUyQyUyMmw1YXBpJTIyJTNBJTdCJTIybW9kaWQlMjIlM0E1MDM5MzclMkMlMjJjbWQlMjIlM0E1ODk4MjQlN0QlN0Q&t_uid={}&t_iShowEntry=4&t_type=104".format(
                    t_uuid
                ),
                "https://node.kg.qq.com/webapp/proxy?ns=KG_TASK&cmd=task.getLottery&mapExt=JTdCJTIyZmlsZSUyMiUzQSUyMnRhc2tKY2UlMjIlMkMlMjJjbWROYW1lJTIyJTNBJTIyTG90dGVyeVJlcSUyMiUyQyUyMmw1YXBpJTIyJTNBJTdCJTIybW9kaWQlMjIlM0E1MDM5MzclMkMlMjJjbWQlMjIlM0E1ODk4MjQlN0QlMkMlMjJsNWFwaV9leHAxJTIyJTNBJTdCJTIybW9kaWQlMjIlM0E4MTcwODklMkMlMjJjbWQlMjIlM0EzODAxMDg4JTdEJTdE&t_uid={}&t_type=103".format(
                    t_uuid
                ),
            ]
        )

        proto_music_station_url = "https://node.kg.qq.com/webapp/proxy?ns=proto_music_station&cmd=message.batch_get_music_cards&mapExt=JTdCJTIyY21kTmFtZSUyMiUzQSUyMkdldEJhdGNoTXVzaWNDYXJkc1JlcSUyMiUyQyUyMmZpbGUlMjIlM0ElMjJwcm90b19tdXNpY19zdGF0aW9uSmNlJTIyJTJDJTIyd25zRGlzcGF0Y2hlciUyMiUzQXRydWUlN0Q&t_uUid={}&g_tk_openkey=".format(
            t_uuid
        )

        url_10 = "https://node.kg.qq.com/webapp/proxy?t_stReward%3Aobject=%7B%22uInteractiveType%22%3A1%2C%22uRewardType%22%3A0%2C%22uFlowerNum%22%3A15%7D&ns=proto_music_station&cmd=message.get_reward&mapExt=JTdCJTIyY21kTmFtZSUyMiUzQSUyMkdldFJld2FyZFJlcSUyMiUyQyUyMmZpbGUlMjIlM0ElMjJwcm90b19tdXNpY19zdGF0aW9uSmNlJTIyJTJDJTIyd25zRGlzcGF0Y2hlciUyMiUzQXRydWUlN0Q&t_uUid={}&t_strUgcId=".format(
            t_uuid
        )

        url_15 = "https://node.kg.qq.com/webapp/proxy?t_stReward%3Aobject=%7B%22uInteractiveType%22%3A0%2C%22uRewardType%22%3A0%2C%22uFlowerNum%22%3A10%7D&ns=proto_music_station&cmd=message.get_reward&mapExt=JTdCJTIyY21kTmFtZSUyMiUzQSUyMkdldFJld2FyZFJlcSUyMiUyQyUyMmZpbGUlMjIlM0ElMjJwcm90b19tdXNpY19zdGF0aW9uSmNlJTIyJTJDJTIyd25zRGlzcGF0Y2hlciUyMiUzQXRydWUlN0Q&t_uUid={}&t_strUgcId=".format(
            t_uuid
        )
        try:
            old_proto_profile_response = requests.get(
                url=proto_profile_url, headers=headers
            )
            old_num = old_proto_profile_response.json()["data"]["profile.getProfile"][
                "uFlowerNum"
            ]
            nickname = old_proto_profile_response.json()["data"]["profile.getProfile"][
                "stPersonInfo"
            ]["sKgNick"]
            for url in url_list:
                try:
                    requests.get(url=url, headers=headers)
                except Exception as e:
                    print(e)
            for g_tk_openkey in range(16):
                try:
                    proto_music_station_resp = requests.get(
                        url=proto_music_station_url + str(g_tk_openkey), headers=headers
                    )
                    if proto_music_station_resp.json().get("code") in [1000]:
                        return proto_music_station_resp.json().get("msg")
                    vct_music_cards = proto_music_station_resp.json()["data"][
                        "message.batch_get_music_cards"
                    ]["vctMusicCards"]
                    vct_music_cards_list = sorted(
                        vct_music_cards,
                        key=lambda x: x["stReward"]["uFlowerNum"],
                        reverse=True,
                    )[0]
                    str_ugc_id = vct_music_cards_list["strUgcId"]
                    str_key = vct_music_cards_list["strKey"]
                    url = str_ugc_id + "&t_strKey=" + str_key
                    u_flower_num = vct_music_cards_list["stReward"]["uFlowerNum"]
                    if u_flower_num > 10:
                        requests.get(url=url_10 + url, headers=headers)
                    elif 1 < u_flower_num < 10:
                        requests.get(url=url_15 + url, headers=headers)
                except Exception as e:
                    print(e)
            # VIP 签到
            try:
                getinfourl = (
                    "https://node.kg.qq.com/webapp/proxy?ns=proto_vip_webapp&cmd=vip.get_vip_info&t_uUid="
                    + t_uuid
                    + "&t_uWebReq=1&t_uGetDataFromC4B=1"
                )
                inforequest = requests.get(url=getinfourl, headers=headers)
                vip_status = inforequest.json()["data"]["vip.get_vip_info"][
                    "stVipCoreInfo"
                ]["uStatus"]
                if vip_status == 1:
                    vipurl = (
                        "https://node.kg.qq.com/webapp/proxy?t_uUid="
                        + t_uuid
                        + "&ns=proto_vip_webapp&cmd=vip.get_vip_day_reward&ns_inbuf=&nocache=1613719349184&mapExt=JTdCJTIyY21kTmFtZSUyMiUzQSUyMkdldFZpcERheVJld2FyZCUyMiU3RA%3D%3D&g_tk_openkey=642424811"
                    )
                    viprequest = requests.get(url=vipurl, headers=headers)
                    str_tips = viprequest.json()["data"]["vip.get_vip_day_reward"][
                        "strTips"
                    ]
                    u_cur_reward_num = viprequest.json()["data"][
                        "vip.get_vip_day_reward"
                    ]["uCurRewardNum"]
                    vip_message = f"{str_tips} 获取VIP福利道具：{u_cur_reward_num}个"
                else:
                    vip_message = "非 VIP 用户"
            except Exception as e:
                print(e)
                vip_message = "VIP 签到失败"
            new_proto_profile_response = requests.get(
                url=proto_profile_url, headers=headers
            )
            new_num = new_proto_profile_response.json()["data"]["profile.getProfile"][
                "uFlowerNum"
            ]
            get_num = int(new_num) - int(old_num)
            msg = [
                {"name": "帐号信息", "value": nickname},
                {"name": "获取鲜花", "value": get_num},
                {"name": "当前鲜花", "value": new_num},
                {"name": "VIP 签到", "value": vip_message},
            ]
        except Exception as e:
            msg = [
                {"name": "帐号信息", "value": str(e)},
            ]
        return msg

    def main(self):
        kgqq_cookie = self.check_item.get("cookie")
        msg = self.sign(kgqq_cookie=kgqq_cookie)
        msg = "\n".join([f"{one.get('name')}: {one.get('value')}" for one in msg])
        return msg


if __name__ == "__main__":
    with open(
        os.path.join(os.path.dirname(os.path.dirname(__file__)), "config.json"),
        encoding="utf-8",
    ) as f:
        datas = json.loads(f.read())
    _check_item = datas.get("KGQQ", [])[0]
    print(KGQQ(check_item=_check_item).main())
