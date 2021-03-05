# -*- coding: utf-8 -*-
import datetime
import json
import os
import time

import requests
from requests import utils


class WPSCheckIn:
    def __init__(self, check_item):
        self.check_item = check_item
        self.invite_sid = [
            "V02S2UBSfNlvEprMOn70qP3jHPDqiZU00a7ef4a800341c7c3b",
            "V02S2oI49T-Jp0_zJKZ5U38dIUSIl8Q00aa679530026780e96",
            "V02S7tldy5ltYcikCzJ8PJQDSy_ElEs00a327c3c0026782526",
            "V02SBpDdos7QiFOs_5TOLF0a80pWt-U00a94ce2c003a814a17",
            "V02SBsNOf4sJZNFo4jOHdgHg7-2Tn1s00a338776000b669579",
            "V02SC1mOHS0RiUBxeoA8NTliH2h2NGc00a803c35002693584d",
            "V02SFiqdXRGnH5oAV2FmDDulZyGDL3M00a61660c0026781be1",
            "V02SPoOluAnWda0dTBYTXpdetS97tyI00a16135e002684bb5c",
            "V02SWIvKWYijG6Rggo4m0xvDKj1m7ew00a8e26d3002508b828",
            "V02Sb8gxW2inr6IDYrdHK_ywJnayd6s00ab7472b0026849b17",
            "V02ScVbtm2pQD49ArcgGLv360iqQFLs014c8062e000b6c37b6",
            "V02SfEpW1yy4wUUh_eEnEHpiJJuoDnE00ae12710000179aa7f",
            "V02ShotJqqiWyubCX0VWTlcbgcHqtSQ00a45564e002678124c",
            "V02Sr3nJ9IicoHWfeyQLiXgvrRpje6E00a240b890023270f97",
            "V02StVuaNcoKrZ3BuvJQ1FcFS_xnG2k00af250d4002664c02f",
            "V02SwV15KQ_8n6brU98_2kLnnFUDUOw00adf3fda0026934a7f",
        ]

        self.invite_limit = 10

    @staticmethod
    def web_sign(session, sid):
        response = session.post(url="https://vip.wps.cn/sigin/do", headers={"sid": sid})
        resp = response.json()
        if resp["msg"] == "已完成签到":
            web_sign_msg = "网页签到: 今日已完成签到"
        elif resp["msg"] == "need_captcha":
            question_response = session.get(
                url="https://vip.wps.cn/checkcode/signin/question", headers={"sid": sid}
            ).json()
            answer_set = {
                "WPS会员全文检索",
                "100G",
                "WPS会员数据恢复",
                "WPS会员PDF转doc",
                "WPS会员PDF转图片",
                "WPS图片转PDF插件",
                "金山PDF转WORD",
                "WPS会员拍照转文字",
                "使用WPS会员修复",
                "WPS全文检索功能",
                "有，且无限次",
                "文档修复",
            }
            while question_response["data"]["multi_select"] == 1:
                question_response = session.get(
                    url="https://vip.wps.cn/checkcode/signin/question", headers={"sid": sid}
                ).json()
            answer_id = 3
            for i in range(4):
                opt = question_response["data"]["options"][i]
                if opt in answer_set:
                    answer_id = i + 1
                    break
            print("选项: {}".format(question_response["data"]["options"]))
            print("选择答案: {}".format(answer_id))
            answer_response = session.post(
                url="https://vip.wps.cn/sigin/do",
                headers={"sid": sid},
                data={"platform": 2, "answer": answer_id, "auth_type": "answer"},
            ).json()
            if answer_response["msg"] == "wrong answer":
                for i in range(4):
                    answer_response = session.post(
                        url="https://vip.wps.cn/sigin/do",
                        headers={"sid": sid},
                        data={"platform": 2, "answer": i + 1, "auth_type": "answer"},
                    ).json()
                    if answer_response["result"] == "ok":
                        break
            web_sign_msg = f"网页签到: 签到成功\n获得奖品{answer_response.get('gift_name')}\n领取地址: {answer_response.get('url')}"
        elif resp["result"] == "ok":
            web_sign_msg = "网页签到: {}".format(resp["msg"])
        else:
            web_sign_msg = "网页签到: {}".format(resp["msg"])
        return web_sign_msg

    def docer_sign(self, session, sid):
        response = session.post(url="https://zt.wps.cn/2018/docer_check_in/api/checkin_today", headers={"sid": sid})
        resp = response.json()
        if resp["result"] == "ok":
            docer_sign_msg = f'稻壳签到: {resp["result"]}'
        elif resp["msg"] == "recheckin":
            docer_sign_msg = "稻壳签到: 重复签到"
        else:
            return "稻壳签到: 签到失败"
        checkin_record_response = session.get(
            url="https://zt.wps.cn/2018/docer_check_in/api/checkin_record", headers={"sid": sid}
        ).json()
        docer_sign_msg += "\n本期连续签到: {} 天".format(checkin_record_response["data"]["max_days"])
        checkin_early_times_response = session.get(
            url="https://zt.wps.cn/2018/docer_check_in/api/checkin_early_times", headers={"sid": sid}
        ).json()
        docer_sign_msg += f"\n拥有补签卡: {checkin_early_times_response['data']} 张"
        max_days = checkin_record_response["data"]["max_days"]
        if checkin_early_times_response["data"] > 0 and len(checkin_record_response["data"]["records"]) > 0:
            max_days = self.docer_webpage_early_sign(
                session=session,
                sid=sid,
                checkinearly_times=checkin_early_times_response["data"],
                checkinrecord=checkin_record_response["data"]["records"],
                max_days=max_days,
            )
            docer_sign_msg += f"\n补签后连续签到: {max_days} 天"
        if len(checkin_record_response["data"]["records"]) > 0:
            gift_msg = self.docer_webpage_gift_receive(session=session, sid=sid, max_days=max_days)
            docer_sign_msg += f"\n{gift_msg}"
        return docer_sign_msg

    @staticmethod
    def docer_webpage_early_sign(session, sid, checkinearly_times, checkinrecord, max_days):
        now = datetime.datetime.utcnow()
        this_month_start = datetime.datetime(now.year, now.month, 1).date()
        checkin_earliestdate = datetime.datetime.strptime(checkinrecord[0]["checkin_date"], "%Y-%m-%d").date()
        for i in range(checkinearly_times):
            if checkin_earliestdate.day > this_month_start.day:
                checkin_date = checkin_earliestdate - datetime.timedelta(days=(i + 1))
                checkin_date = datetime.datetime.strptime(str(checkin_date), "%Y-%m-%d").strftime("%Y%m%d")
                session.post(
                    url="https://zt.wps.cn/2018/docer_check_in/api/checkin_early",
                    data={"date": checkin_date},
                    headers={"sid": sid},
                )
            else:
                if i == 0:
                    print("无需补签")
                    return max_days
                else:
                    print("使用补签卡{} 张".format(i))
                    resp = session.get(
                        url="https://zt.wps.cn/2018/docer_check_in/api/checkin_record", headers={"sid": sid}
                    ).json()
                    print("补签后连续签到: {}天".format(resp["data"]["max_days"]))
                    return resp["data"]["max_days"]
        print("使用补签卡{} 张".format(i))
        resp = session.get(url="https://zt.wps.cn/2018/docer_check_in/api/checkin_record", headers={"sid": sid}).json()
        return resp["data"]["max_days"]

    @staticmethod
    def docer_webpage_gift_receive(session, sid, max_days):
        gift_msg = ""
        resp = session.get(url="https://vip.wps.cn/userinfo", headers={"sid": sid}).json()
        memberid = [0]
        if len(resp["data"]["vip"]["enabled"]) > 0:
            for i in range(len(resp["data"]["vip"]["enabled"])):
                memberid.append(resp["data"]["vip"]["enabled"][i]["memberid"])
        resp = session.get(url="https://zt.wps.cn/2018/docer_check_in/api/reward_record", headers={"sid": sid}).json()
        reward_record_list = resp["data"]
        if len(reward_record_list) > 0:
            for i in reward_record_list:
                if i["reward_type"] == "vip" or i["reward_type"] == "code":
                    if (
                        int(i["limit_days"]) <= max_days
                        and int(i["limit_vip"]) in memberid
                        and i["status"] == "unreceived"
                    ):
                        receive_reward_resp = session.post(
                            url="https://zt.wps.cn/2018/docer_check_in/api/receive_reward",
                            data={"reward_id": i["id"], "receive_from": "pc_client"},
                            headers={"sid": sid},
                        )
                        gift_msg = "领取礼物: {} ".format(i["reward_name"])
                        if "reward_info" in receive_reward_resp.text:
                            resp1 = json.loads(receive_reward_resp.text)
                            gift_msg += "\n礼物信息: {}".format(resp1["data"]["reward_info"])
                        else:
                            gift_msg += "领取信息: {}".format(receive_reward_resp.text)
                    elif i["status"] == "received":
                        gift_msg = "已领取礼物: {} ".format(i["reward_name"])
                        if "reward_info" in i:
                            gift_msg += "\n礼物信息: {}".format(i["reward_info"])
        return gift_msg

    @staticmethod
    def miniprogram_sign(session, sid):
        resp = session.get(url="http://zt.wps.cn/2018/clock_in/api/clock_in", headers={"sid": sid}).json()
        if resp["msg"] == "已打卡":
            return f"小程序签到: {resp['msg']}"
        elif resp["msg"] == "未绑定手机":
            return f"小程序签到: {resp['msg']}"
        elif resp["msg"] == "前一天未报名":
            resp = session.get(url="http://zt.wps.cn/2018/clock_in/api/sign_up", headers={"sid": sid}).json()
            if resp["result"] == "ok":
                return "小程序报名: 已自动报名, 报名后第二天签到"
            else:
                return "小程序报名: 报名失败: 请手动报名, 报名后第二天签到"
        elif resp["msg"] == "答题未通过":
            resp = session.get(
                url="http://zt.wps.cn/2018/clock_in/api/get_question?member=wps", headers={"sid": sid}
            ).json()
            answer_set = {
                "WPS会员全文检索",
                "100G",
                "WPS会员数据恢复",
                "WPS会员PDF转doc",
                "WPS会员PDF转图片",
                "WPS图片转PDF插件",
                "金山PDF转WORD",
                "WPS会员拍照转文字",
                "使用WPS会员修复",
                "WPS全文检索功能",
                "有，且无限次",
                "文档修复",
            }
            while resp["data"]["multi_select"] == 1:
                resp = session.get(
                    url="http://zt.wps.cn/2018/clock_in/api/get_question?member=wps", headers={"sid": sid}
                ).json()
            answer_id = 3
            for i in range(4):
                opt = resp["data"]["options"][i]
                if opt in answer_set:
                    answer_id = i + 1
                    break
            print("选项: {}".format(resp["data"]["options"]))
            print("选择答案: {}".format(answer_id))
            resp = session.post(
                url="http://zt.wps.cn/2018/clock_in/api/answer?member=wps",
                headers={"sid": sid},
                data={"answer": answer_id},
            ).json()
            if resp["msg"] == "wrong answer":
                for i in range(4):
                    resp = session.post(
                        url="http://zt.wps.cn/2018/clock_in/api/answer?member=wps",
                        headers={"sid": sid},
                        data={"answer": i + 1},
                    ).json()
                    if resp["result"] == "ok":
                        break
            r = session.get(url="http://zt.wps.cn/2018/clock_in/api/clock_in?member=wps", headers={"sid": sid})
            return "小程序签到: {}".format(r.text)
        elif resp["msg"] == "ParamData Empty":
            session.get(url="http://zt.wps.cn/2018/clock_in/api/sign_up", headers={"sid": sid}).json()
            return f"小程序签到: {resp['msg']}"
        elif resp["msg"] == "不在打卡时间内":
            print("签到失败: 不在打卡时间内")
            resp = session.get(url="http://zt.wps.cn/2018/clock_in/api/sign_up", headers={"sid": sid}).json()
            if resp["result"] == "ok":
                return "小程序签到: 已自动报名, 报名后请设置在规定时间内签到"
            else:
                return "小程序签到: 报名失败: 请手动报名, 报名后第二天签到"
        elif resp["result"] == "error":
            signup_url = "http://zt.wps.cn/2018/clock_in/api/sign_up"
            resp = session.get(signup_url, headers={"sid": sid}).json()
            if resp["result"] == "ok":
                return "小程序签到: 已自动报名, 报名后请设置在规定时间内签到"
            else:
                return "小程序签到: 报名失败: 请手动报名, 报名后第二天签到"
        # member_url = "https://zt.wps.cn/2018/clock_in/api/get_data?member=wps"
        # resp = session.get(member_url, headers={"sid": sid})
        # total_add_day = re.search(r'"total_add_day":(\d+)', resp.text).group(1)
        # print("小程序打卡中累计获得会员: {} 天".format(total_add_day))

    @staticmethod
    def user_info(session, sid):
        resp1 = session.post(url="https://vip.wps.cn/2019/user/summary", headers={"sid": sid}).json()
        resp = session.get(url="https://vip.wps.cn/userinfo", headers={"sid": sid}).json()
        nickname = resp["data"]["nickname"]
        userid = resp["data"]["userid"]
        user_info = f'用户名称: {nickname}\n会员积分: {resp1["data"]["integral"]}\n稻米数量: {resp1["data"]["wealth"]}'
        if len(resp["data"]["vip"]["enabled"]) > 0:
            for one_vip in resp["data"]["vip"]["enabled"]:
                user_info += f"\n{one_vip.get('name')}: {datetime.datetime.fromtimestamp(one_vip.get('expire_time')).strftime('%Y-%m-%d %H:%M:%S')}"
        return user_info, userid

    def miniprogram_invite(self, session, invite_userid: int):
        k = 0
        for index, i in enumerate(self.invite_sid):
            time.sleep(5)
            if k < self.invite_limit:
                headers = {"sid": i}
                resp = session.post(
                    url="http://zt.wps.cn/2018/clock_in/api/invite",
                    headers=headers,
                    data={"invite_userid": invite_userid},
                )
                if resp.status_code == 200:
                    try:
                        resp_json = resp.json()
                        print("邀请对象ID={}, Result: {}".format(str(index + 1).zfill(2), resp_json["result"]))
                        k += 1
                    except Exception as e:
                        print("邀请对象ID={0}, Result: ID已失效, 错误信息{1}".format(str(index + 1).zfill(2), e))
                else:
                    print(
                        "邀请对象ID={}, 状态码: {}, 请求信息{}".format(str(index + 1).zfill(2), resp.status_code, resp.text[:25])
                    )
        return f"邀请用户: 成功邀请 {k} 人"

    def main(self):
        wps_cookie = {item.split("=")[0]: item.split("=")[1] for item in self.check_item.get("wps_cookie").split("; ")}
        session = requests.session()
        requests.utils.add_dict_to_cookiejar(session.cookies, wps_cookie)
        session.headers.update(
            {
                "Accept": "*/*",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36 Edg/88.0.705.74",
                "X-Requested-With": "XMLHttpRequest",
                "Origin": "http://www.wpsmembers.cn",
                "Referer": "http://www.wpsmembers.cn/",
                "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
            }
        )
        sid = wps_cookie.get("wps_sid")
        web_sign_msg = self.web_sign(session=session, sid=sid)
        docer_sign_msg = self.docer_sign(session=session, sid=sid)
        miniprogram_sign_msg = self.miniprogram_sign(session=session, sid=sid)
        user_info_msg, userid = self.user_info(session=session, sid=sid)
        miniprogram_invite_msg = self.miniprogram_invite(session=session, invite_userid=userid)
        msg = (
            f"{user_info_msg}\n{web_sign_msg}\n{docer_sign_msg}\n{miniprogram_sign_msg}"
            f"\n{miniprogram_invite_msg}"
        )
        return msg


if __name__ == "__main__":
    with open(
        os.path.join(os.path.dirname(os.path.dirname(__file__)), "config/config.json"), "r", encoding="utf-8"
    ) as f:
        datas = json.loads(f.read())
    _check_item = datas.get("WPS_COOKIE_LIST", [])[0]
    print(WPSCheckIn(check_item=_check_item).main())
