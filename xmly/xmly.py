# -*- coding: utf-8 -*-
import base64
import hashlib
import json
import os
import re
import time
from datetime import datetime, timedelta
from itertools import groupby

import requests

import rsa


class XMLYCheckIn:
    def __init__(self, check_item):
        self.check_item = check_item
        self.useragent = "Mozilla/5.0 (iPhone; CPU iPhone OS 13_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 iting/1.0.12 kdtunion_iting/1.0 iting(main)/1.0.12/ios_1"
        self.pubkey_str = "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCVhaR3Or7suUlwHUl2Ly36uVmboZ3+HhovogDjLgRE9CbaUokS2eqGaVFfbxAUxFThNDuXq/fBD+SdUgppmcZrIw4HMMP4AtE2qJJQH/KxPWmbXH7Lv+9CisNtPYOlvWJ/GHRqf9x3TBKjjeJ2CjuVxlPBDX63+Ecil2JR9klVawIDAQAB"

    @staticmethod
    def parse_cookie(str_cookie):
        if isinstance(str_cookie, dict):
            return str_cookie
        tmp = str_cookie.split(";")
        dict_cookie = {}
        try:
            for i in tmp:
                j = i.split("=")
                if not j[0]:
                    continue
                dict_cookie[j[0].strip()] = j[1].strip()

            assert dict_cookie.get("1&_token").split("&")[0]
            regex = r"&\d\.\d\.\d+"
            appid = "&1.1.9"
            dict_cookie["1&_device"] = re.sub(regex, appid, dict_cookie["1&_device"], 0, re.MULTILINE)
        except (IndexError, KeyError):
            print("cookie填写出错 ❌,仔细查看说明")
            raise
        return dict_cookie

    @staticmethod
    def get_time():
        time_stamp = int(time.time())
        date_stamp = (time_stamp - 57600) % 86400
        utc_time = datetime.utcnow() + timedelta(hours=8)  # 北京时间
        _datatime = utc_time.strftime("%Y%m%d")
        print(f"\n当前时间戳: {time_stamp}")
        print(f"北京时间: {utc_time}\n\n")
        return time_stamp, date_stamp, _datatime, utc_time

    @staticmethod
    def get_uid(cookies):
        return cookies["1&_token"].split("&")[0]

    @staticmethod
    def _str2key(s):
        b_str = base64.b64decode(s)
        if len(b_str) < 162:
            return False
        hex_str = ""
        for x in b_str:
            h = hex(x)[2:]
            h = h.rjust(2, "0")
            hex_str += h
        m_start = 29 * 2
        e_start = 159 * 2
        m_len = 128 * 2
        e_len = 3 * 2
        modulus = hex_str[m_start: m_start + m_len]
        exponent = hex_str[e_start: e_start + e_len]
        return modulus, exponent

    def rsa_encrypt(self, s, pubkey_str):
        key = self._str2key(pubkey_str)
        modulus = int(key[0], 16)
        exponent = int(key[1], 16)
        pubkey = rsa.PublicKey(modulus, exponent)
        return base64.b64encode(rsa.encrypt(s.encode(), pubkey)).decode()

    def checkin(self, cookies, _datatime):
        """
        连续签到
        :param cookies:
        :param _datatime:
        :return:
        """
        headers = {
            "Host": "m.ximalaya.com",
            "Accept": "application/json, text/plain, */*",
            "Connection": "keep-alive",
            "User-Agent": self.useragent,
            "Accept-Language": "zh-cn",
            "Referer": "https://m.ximalaya.com/growth-ssr-speed-welfare-center/page/welfare",
            "Accept-Encoding": "gzip, deflate, br",
        }
        params = {"time": str(int(time.time() * 1000))}
        try:
            response = requests.get(
                url="https://m.ximalaya.com/speed/task-center/check-in/record",
                headers=headers,
                params=params,
                cookies=cookies,
            )
        except Exception as e:
            print(f"网络请求异常: {e}")
            return 0
        result = response.json()
        # print(f"""连续签到{result["continuousDays"]}/{result["historyDays"]}天""")
        # print(result["isTickedToday"])
        if not result["isTickedToday"]:
            print("!!!开始签到")
            headers = {
                "User-Agent": self.useragent,
                "Content-Type": "application/json;charset=utf-8",
                "Host": "m.ximalaya.com",
                "Origin": "https://m.ximalaya.com",
                "Referer": "https://m.ximalaya.com/growth-ssr-speed-welfare-center/page/welfare",
            }
            uid = self.get_uid(cookies)
            params = {"checkData": self.rsa_encrypt(f"date={_datatime}&uid={uid}", self.pubkey_str), "makeUp": False}

            response = requests.post(
                url="https://m.ximalaya.com/speed/task-center/check-in/check",
                headers=headers,
                cookies=cookies,
                data=json.dumps(params),
            )
            # print(response.text)
        return result["continuousDays"]

    def save_listen_time(self, cookies, date_stamp):
        """
        刷时长
        :param cookies:
        :param date_stamp:
        :return:
        """
        headers = {
            "User-Agent": self.useragent,
            "Host": "mobile.ximalaya.com",
            "Content-Type": "application/x-www-form-urlencoded",
        }
        listentime = date_stamp
        print(f"上传本地收听时长1: {listentime // 60}分钟")
        currenttimemillis = int(time.time() * 1000) - 2
        uid = self.get_uid(cookies)
        sign = hashlib.md5(
            f"currenttimemillis={currenttimemillis}&listentime={listentime}&uid={uid}&23627d1451047b8d257a96af5db359538f081d651df75b4aa169508547208159".encode()
        ).hexdigest()
        data = {
            "activtyId": "listenAward",
            "currentTimeMillis": currenttimemillis,
            "listenTime": str(listentime),
            "nativeListenTime": str(listentime),
            "signature": sign,
            "uid": uid,
        }
        try:
            response = requests.post(
                url="http://mobile.ximalaya.com/pizza-category/ball/saveListenTime",
                headers=headers,
                cookies=cookies,
                data=data,
            )
        except Exception as e:
            print(f"网络请求异常: {e}")
            return
        listen_msg = int(response.json().get("nativeListenTime", 0) / 60)
        return listen_msg

    def listen_data(self, cookies, date_stamp):
        """
        刷时长
        :param cookies:
        :param date_stamp:
        :return:
        """
        headers = {
            "User-Agent": "ting_v1.1.9_c5(CFNetwork, iOS 14.0.1, iPhone9,2)",
            "Host": "m.ximalaya.com",
            "Content-Type": "application/json",
        }
        listentime = date_stamp - 1
        print(f"上传本地收听时长2: {listentime // 60}分钟")
        currenttimemillis = int(time.time() * 1000)
        uid = self.get_uid(cookies)
        sign = hashlib.md5(
            f"currenttimemillis={currenttimemillis}&listentime={listentime}&uid={uid}&23627d1451047b8d257a96af5db359538f081d651df75b4aa169508547208159".encode()
        ).hexdigest()
        data = {"currentTimeMillis": currenttimemillis, "listenTime": str(listentime), "signature": sign, "uid": uid}
        try:
            response = requests.post(
                url="http://m.ximalaya.com/speed/web-earn/listen/client/data",
                headers=headers,
                cookies=cookies,
                data=json.dumps(data),
            )
        except Exception as e:
            print(f"网络请求异常: {e}")
            return
        # print(response.text)

    def read(self, cookies):
        """
        阅读
        :param cookies:
        :return:
        """
        headers = {
            "Host": "51gzdhh.xyz",
            "accept": "application/json, text/plain, */*",
            "origin": "http://xiaokuohao.work",
            "user-agent": "Mozilla/5.0 (Linux; Android 6.0.1; MI 6 Plus Build/V417IR; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.100 Mobile Safari/537.36 iting(main)/1.8.18/android_1 kdtUnion_iting/1.8.18",
            "referer": "http://xiaokuohao.work/static/web/dxmly/index.html",
            "accept-encoding": "gzip, deflate",
            "accept-language": "zh-CN,en-US;q=0.8",
            "x-requested-with": "com.ximalaya.ting.lite",
        }
        params = {"hid": "233"}
        try:
            response = requests.get(url="https://51gzdhh.xyz/api/new/newConfig", headers=headers, params=params)
        except Exception as e:
            print(f"网络请求异常: {e}")
            return "网络请求异常"
        result = response.json()
        pid = str(result["pid"])
        headers = {
            "Host": "51gzdhh.xyz",
            "content-length": "37",
            "accept": "application/json, text/plain, */*",
            "origin": "http://xiaokuohao.work",
            "user-agent": "Mozilla/5.0 (Linux; Android 6.0.1; MI 6 Plus Build/V417IR; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.100 Mobile Safari/537.36 iting(main)/1.8.18/android_1 kdtUnion_iting/1.8.18",
            "content-type": "application/x-www-form-urlencoded",
            "referer": "http://xiaokuohao.work/static/web/dxmly/index.html",
            "accept-encoding": "gzip, deflate",
            "accept-language": "zh-CN,en-US;q=0.8",
            "x-requested-with": "com.ximalaya.ting.lite",
        }
        uid = self.get_uid(cookies)
        data = {"pid": str(pid), "mtuserid": uid}
        try:
            response = requests.post(
                url="https://51gzdhh.xyz/api/new/hui/complete", headers=headers, data=json.dumps(data)
            )
        except Exception as e:
            print(f"网络请求异常: {e}")
            return "网络请求异常"
        result = response.json()
        if result["status"] == -2:
            return "无法阅读,尝试从安卓端手动开启"
        if result["isComplete"] or result["count_finish"] == 9:
            return "今日完成阅读"
        headers = {
            "Host": "51gzdhh.xyz",
            "accept": "application/json, text/plain, */*",
            "origin": "http://xiaokuohao.work",
            "user-agent": "Mozilla/5.0 (Linux; Android 6.0.1; MI 6 Plus Build/V417IR; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.100 Mobile Safari/537.36 iting(main)/1.8.18/android_1 kdtUnion_iting/1.8.18",
            "referer": "http://xiaokuohao.work/static/web/dxmly/index.html",
            "accept-encoding": "gzip, deflate",
            "accept-language": "zh-CN,en-US;q=0.8",
            "x-requested-with": "com.ximalaya.ting.lite",
        }
        task_ids = {"242", "239", "241", "240", "238", "236", "237", "235", "234"} - set(result["completeList"])
        params = {
            "userid": str(uid),
            "pid": pid,
            "taskid": task_ids.pop(),
            "imei": "",
        }
        try:
            response = requests.get(url="https://51gzdhh.xyz/new/userCompleteNew", headers=headers, params=params)
            result = response.text
            return result
        except Exception as e:
            print(f"网络请求异常: {e}")
            return "网络请求异常"

    def receive(self, cookies, task_id):
        """
        收金币气泡收听
        :param cookies:
        :param task_id:
        :return:
        """
        headers = {
            "Host": "m.ximalaya.com",
            "Accept": "application/json, text/plain, */*",
            "Connection": "keep-alive",
            "User-Agent": self.useragent,
            "Accept-Language": "zh-cn",
            "Referer": "https://m.ximalaya.com/xmds-node-spa/apps/speed-growth-open-components/bubble",
            "Accept-Encoding": "gzip, deflate, br",
        }
        try:
            response = requests.get(
                url=f"https://m.ximalaya.com/speed/web-earn/listen/receive/{task_id}", headers=headers, cookies=cookies
            )
        except Exception as e:
            print(f"网络请求异常: {e}")
            return
        # print("receive: ", response.text)
        return response.json()

    def ad_score(self, cookies, business_type, task_id):
        """
        收金币气泡广告分数
        :param cookies:
        :param business_type:
        :param task_id:
        :return:
        """
        headers = {
            "Host": "m.ximalaya.com",
            "Accept": "application/json, text/plain ,*/*",
            "Connection": "keep-alive",
            "User-Agent": self.useragent,
            "Accept-Language": "zh-cn",
            "Content-Type": "application/json;charset=utf-8",
            "Accept-Encoding": "gzip, deflate, br",
        }
        try:
            response = requests.get(
                url="https://m.ximalaya.com/speed/task-center/ad/token", headers=headers, cookies=cookies
            )
        except Exception as e:
            print(f"网络请求异常: {e}")
            return
        result = response.json()
        token = result["id"]
        uid = self.get_uid(cookies)
        data = {
            "taskId": task_id,
            "businessType": business_type,
            "rsaSign": self.rsa_encrypt(f"""businessType={business_type}&token={token}&uid={uid}""", self.pubkey_str),
        }
        try:
            response = requests.post(
                url=f"https://m.ximalaya.com/speed/task-center/ad/score",
                headers=headers,
                cookies=cookies,
                data=json.dumps(data),
            )
        except Exception as e:
            print(f"网络请求异常: {e}")
            return
        # print(response.text)
        return response.json()

    def bubble(self, cookies):
        """
        收金币气泡
        :param cookies:
        :return:
        """
        headers = {
            "User-Agent": self.useragent,
            "Content-Type": "application/json;charset=utf-8",
            "Host": "m.ximalaya.com",
            "Origin": "https://m.ximalaya.com",
            "Referer": "https://m.ximalaya.com/xmds-node-spa/apps/speed-growth-open-components/bubble",
        }
        uid = self.get_uid(cookies)
        data = {
            "listenTime": "41246",
            "signature": "2b1cc9e8831cff8874d9c",
            "currentTimeMillis": "1596695606145",
            "uid": uid,
            "expire": False,
        }
        try:
            response = requests.post(
                url="https://m.ximalaya.com/speed/web-earn/listen/bubbles",
                headers=headers,
                cookies=cookies,
                data=json.dumps(data),
            )
        except Exception as e:
            print(f"网络请求异常: {e}")
            return
        result = response.json()
        # print(result)
        coin_count = 0
        if not result["data"]["effectiveBubbles"]:
            return "暂无有效气泡"
        for i in result["data"]["effectiveBubbles"]:
            # print(i["id"])
            tmp = self.receive(cookies, i["id"])
            if "errorCode" in tmp:
                print("❌ 每天手动收听一段时间，暂无其他方法")
                return
            time.sleep(1)
            res = self.ad_score(cookies, 7, i["id"])
            coin_count += res.get("coin", 0)
        for i in result["data"]["expiredBubbles"]:
            res = self.ad_score(cookies, 6, i["id"])
            coin_count += res.get("coin", 0)
        return coin_count

    def ans_get_times(self, cookies):
        """
        获取答题时间
        :param cookies:
        :return:
        """
        headers = {
            "Host": "m.ximalaya.com",
            "Accept": "application/json, text/plain, */*",
            "Connection": "keep-alive",
            "User-Agent": self.useragent,
            "Accept-Language": "zh-cn",
            "Referer": "https://m.ximalaya.com/growth-ssr-speed-welfare-center/page/quiz",
            "Accept-Encoding": "gzip, deflate, br",
        }
        try:
            response = requests.get(
                url="https://m.ximalaya.com/speed/web-earn/topic/user", headers=headers, cookies=cookies
            )
        except Exception as e:
            print(f"网络请求异常: {e}")
            return {"stamina": 0, "remainingTimes": 0}
        # print(response.text)
        result = response.json()
        stamina = result["data"]["stamina"]
        remaining_times = result["data"]["remainingTimes"]
        return {"stamina": stamina, "remainingTimes": remaining_times}

    def ans_start(self, cookies):
        """
        开始答题
        :param cookies:
        :return:
        """
        headers = {
            "Host": "m.ximalaya.com",
            "Accept": "application/json, text/plain, */*",
            "Connection": "keep-alive",
            "User-Agent": self.useragent,
            "Accept-Language": "zh-cn",
            "Referer": "https://m.ximalaya.com/growth-ssr-speed-welfare-center/page/quiz",
            "Accept-Encoding": "gzip, deflate, br",
        }
        try:
            response = requests.get(
                url="https://m.ximalaya.com/speed/web-earn/topic/start", headers=headers, cookies=cookies
            )
        except Exception as e:
            print(f"网络请求异常: {e}")
            return 0, 0, 0
        result = response.json()

        try:
            paper_id = result["data"]["paperId"]
            date_str = result["data"]["dateStr"]
            last_topic_id = result["data"]["topics"][2]["topicId"]
            # print(paper_id, date_str, last_topic_id)
            return paper_id, date_str, last_topic_id
        except Exception as e:
            print(f"❌1 重新抓包 2 手动答题，错误信息: {e}")
            return 0, 0, 0

    def ans_receive(self, cookies, paper_id, last_topic_id, receive_type):
        """

        :param cookies:
        :param paper_id:
        :param last_topic_id:
        :param receive_type:
        :return:
        """
        headers = {
            "User-Agent": self.useragent,
            "Content-Type": "application/json;charset=utf-8",
            "Host": "m.ximalaya.com",
            "Origin": "https://m.ximalaya.com",
            "Referer": "https://m.ximalaya.com/growth-ssr-speed-welfare-center/page/quiz",
        }
        check_data = self.rsa_encrypt(
            f"lastTopicId={last_topic_id}&numOfAnswers=3&receiveType={receive_type}", self.pubkey_str
        )
        data = {
            "paperId": paper_id,
            "checkData": check_data,
            "lastTopicId": last_topic_id,
            "numOfAnswers": 3,
            "receiveType": receive_type,
        }
        try:
            response = requests.post(
                url="https://m.ximalaya.com/speed/web-earn/topic/receive",
                headers=headers,
                cookies=cookies,
                data=json.dumps(data),
            )
        except Exception as e:
            print(f"网络请求异常: {e}")
            return 0
        return response.json()

    def ans_restore(self, cookies):
        """
        看视频回复体力
        :param cookies:
        :return:
        """
        headers = {
            "User-Agent": self.useragent,
            "Content-Type": "application/json;charset=utf-8",
            "Host": "m.ximalaya.com",
            "Origin": "https://m.ximalaya.com",
            "Referer": "https://m.ximalaya.com/growth-ssr-speed-welfare-center/page/quiz",
        }
        check_data = self.rsa_encrypt("restoreType=2", self.pubkey_str)

        data = {
            "restoreType": 2,
            "checkData": check_data,
        }
        try:
            response = requests.post(
                url="https://m.ximalaya.com/speed/web-earn/topic/restore",
                headers=headers,
                cookies=cookies,
                data=json.dumps(data),
            )
        except Exception as e:
            print(f"网络请求异常: {e}")
            return 0
        result = response.json()
        if "errorCode" in result:
            return 0
        return 1

    def answer(self, cookies):
        """
        答题
        :param cookies:
        :return:
        """
        ans_times = self.ans_get_times(cookies)
        if not ans_times:
            return
        if ans_times["stamina"] == 0:
            return "时间未到"
        for _ in range(ans_times["stamina"]):
            paper_id, _, last_topic_id = self.ans_start(cookies)
            if paper_id == 0:
                return
            tmp = self.ans_receive(cookies, paper_id, last_topic_id, 1)
            # print(tmp)
            if "errorCode" in tmp:
                print("❌ 每天手动收听一段时间，暂无其他方法")
                return
            time.sleep(1)
            tmp = self.ans_receive(cookies, paper_id, last_topic_id, 2)
            # print(tmp)
            if tmp == 0:
                return
            time.sleep(1)

        if ans_times["remainingTimes"] > 0:
            print("[看视频回复体力]")
            if self.ans_restore(cookies) == 0:
                return
            for _ in range(5):
                paper_id, _, last_topic_id = self.ans_start(cookies)
                if paper_id == 0:
                    return
                tmp = self.ans_receive(cookies, paper_id, last_topic_id, 1)
                # print(tmp)
                if "errorCode" in tmp:
                    print("❌ 每天手动收听一段时间，暂无其他方法")
                    return
                time.sleep(1)
                tmp = self.ans_receive(cookies, paper_id, last_topic_id, 2)
                # print(tmp)
                if tmp == 0:
                    return
                time.sleep(1)
        return ""

    def card_report_time(self, cookies, mins, date_stamp, _datatime):
        """
        收听获得抽卡机会 卡牌
        :param cookies:
        :param mins:
        :param date_stamp:
        :param _datatime:
        :return:
        """
        headers = {
            "User-Agent": self.useragent,
            "Content-Type": "application/json;charset=utf-8",
            "Host": "m.ximalaya.com",
            "Origin": "https://m.ximalaya.com",
            "Referer": "https://m.ximalaya.com/xmds-node-spa/apps/speed-growth-activities/card-collection/home",
        }
        listen_time = mins - date_stamp
        uid = self.get_uid(cookies)
        data = {
            "listenTime": listen_time,
            "signData": self.rsa_encrypt(f"{_datatime}{listen_time}{uid}", self.pubkey_str),
        }
        try:
            response = requests.post(
                url="https://m.ximalaya.com/speed/web-earn/card/reportTime",
                headers=headers,
                cookies=cookies,
                data=json.dumps(data),
            ).json()
            if response["data"]["upperLimit"]:
                # print(response["data"]["upperLimit"])
                print("今日已达上限")
                card_report_time_msg = "今日已达上限"
            else:
                card_report_time_msg = "完成抽卡"
            return card_report_time_msg
        except Exception as e:
            print(f"网络请求异常: {e}")
            return

    def get_omnipotent_card(self, cookies, mins, date_stamp, _datatime):
        """
        领取万能卡
        :param cookies:
        :param mins:
        :param date_stamp:
        :param _datatime:
        :return:
        """
        headers = {
            "User-Agent": self.useragent,
            "Content-Type": "application/json;charset=utf-8",
            "Host": "m.ximalaya.com",
            "Origin": "https://m.ximalaya.com",
            "Referer": "https://m.ximalaya.com/xmds-node-spa/apps/speed-growth-activities/card-collection/home",
        }
        try:
            count = requests.get(
                url="https://m.ximalaya.com/speed/web-earn/card/omnipotentCardInfo", headers=headers, cookies=cookies,
            ).json()["data"]["count"]
        except Exception as e:
            print(f"网络请求异常: {e}")
            return
        if count == 5:
            print("今日已满")
            return

        token = requests.get(
            "https://m.ximalaya.com/speed/web-earn/card/token/1", headers=headers, cookies=cookies,
        ).json()["data"]["id"]
        uid = self.get_uid(cookies)
        data = {
            "listenTime": mins - date_stamp,
            "signData": self.rsa_encrypt(f"{_datatime}{token}{uid}", self.pubkey_str),
            "token": token,
        }
        try:
            response = requests.post(
                url="https://m.ximalaya.com/speed/web-earn/card/getOmnipotentCard",
                headers=headers,
                cookies=cookies,
                data=json.dumps(data),
            )
        except Exception as e:
            print(f"网络请求异常: {e}")
            return
        # print(response.text)

    def index_baoxiang_award(self, cookies):
        """
        首页、宝箱奖励及翻倍
        :param cookies:
        :return:
        """
        headers = {
            "User-Agent": self.useragent,
            "Host": "mobile.ximalaya.com",
        }
        currenttimemillis = int(time.time() * 1000) - 2
        try:
            response = requests.post(
                url="https://mobile.ximalaya.com/pizza-category/activity/getAward?activtyId=baoxiangAward",
                headers=headers,
                cookies=cookies,
            )
        except Exception as e:
            print(f"网络请求异常: {e}")
            return
        result = response.json()
        try:
            baoxiang_award = int(result.get("msg", 0))
        except Exception as e:
            baoxiang_award = 0
        if "ret" in result and result["ret"] == 0:
            award_receive_id = result["awardReceiveId"]
            headers = {
                "Host": "mobile.ximalaya.com",
                "Accept": "*/*",
                "User-Agent": self.useragent,
                "Accept-Language": "zh-Hans-CN;q=1, en-CN;q=0.9",
                "Accept-Encoding": "gzip, deflate",
                "Connection": "keep-alive",
            }
            params = (
                ("activtyId", "baoxiangAward"),
                ("awardReceiveId", award_receive_id),
            )
            try:
                response = requests.get(
                    url="http://mobile.ximalaya.com/pizza-category/activity/awardMultiple",
                    headers=headers,
                    params=params,
                    cookies=cookies,
                )
                print("宝箱奖励翻倍 ", response.text)
                baoxiang_award += int(response.json().get("amount", 0))
            except Exception as e:
                print(f"网络请求异常: {e}")
                return
        index_baoxiang_award_msg = f"宝箱奖励: {baoxiang_award}"
        uid = self.get_uid(cookies)
        params = {
            "activtyId": "indexSegAward",
            "ballKey": str(uid),
            "currentTimeMillis": str(currenttimemillis),
            "sawVideoSignature": f"{currenttimemillis}+{uid}",
            "version": "2",
        }
        try:
            response = requests.get(
                url="https://mobile.ximalaya.com/pizza-category/activity/getAward",
                headers=headers,
                cookies=cookies,
                params=params,
            )
        except Exception as e:
            print(f"网络请求异常: {e}")
            return
        result = response.json()
        try:
            index_award = int(result.get("msg", 0))
        except Exception as e:
            index_award = 0
        if "ret" in result and result["ret"] == 0:
            award_receive_id = result["awardReceiveId"]
            headers = {
                "Host": "mobile.ximalaya.com",
                "Accept": "*/*",
                "User-Agent": self.useragent,
                "Accept-Language": "zh-Hans-CN;q=1, en-CN;q=0.9",
                "Accept-Encoding": "gzip, deflate",
                "Connection": "keep-alive",
            }

            params = {"activtyId": "indexSegAward", "awardReceiveId": award_receive_id}
            try:
                response = requests.get(
                    url="http://mobile.ximalaya.com/pizza-category/activity/awardMultiple",
                    headers=headers,
                    params=params,
                    cookies=cookies,
                )
                print("首页奖励翻倍: ", response.text)
                index_award = int(response.json().get("amount", 0))

            except Exception as e:
                print(f"网络请求异常: {e}")
                return
        index_baoxiang_award_msg += f"\n首页奖励: {index_award}"

        return index_baoxiang_award_msg

    def card_exchange_card(self, cookies, to_card_award_id, from_record_id_list):
        """
        万能卡兑换稀有卡
        :param cookies:
        :param to_card_award_id:
        :param from_record_id_list:
        :return:
        """
        from_record_id_list = sorted(from_record_id_list)
        headers = {
            "User-Agent": self.useragent,
            "Content-Type": "application/json;charset=utf-8",
            "Host": "m.ximalaya.com",
            "Origin": "https://m.ximalaya.com",
            "Referer": "https://m.ximalaya.com/xmds-node-spa/apps/speed-growth-activities/card-collection/home",
        }
        data = {
            "toCardAwardId": to_card_award_id,
            "fromRecordIdList": from_record_id_list,
            "exchangeType": 1,
        }
        try:
            response = requests.post(
                url="https://m.ximalaya.com/speed/web-earn/card/exchangeCard",
                headers=headers,
                cookies=cookies,
                data=json.dumps(data),
            )
        except Exception as e:
            print(f"网络请求异常: {e}")
            return
        # print(response.text)

    def draw_5card(self, cookies, draw_record_id_list):
        """
        五连抽
        :param cookies:
        :param draw_record_id_list:
        :return:
        """
        draw_record_id_list = sorted(draw_record_id_list)
        headers = {
            "User-Agent": self.useragent,
            "Content-Type": "application/json;charset=utf-8",
            "Host": "m.ximalaya.com",
            "Origin": "https://m.ximalaya.com",
            "Referer": "https://m.ximalaya.com/xmds-node-spa/apps/speed-growth-activities/card-collection/home",
        }
        uid = self.get_uid(cookies)
        data = {
            "signData": self.rsa_encrypt(f"{''.join(str(i) for i in draw_record_id_list)}{uid}", self.pubkey_str),
            "drawRecordIdList": draw_record_id_list,
            "drawType": 2,
        }
        try:
            response = requests.post(
                url="https://m.ximalaya.com/speed/web-earn/card/draw",
                headers=headers,
                cookies=cookies,
                data=json.dumps(data),
            )
        except Exception as e:
            print(f"网络请求异常: {e}")
            return
        # print("五连抽: ", response.text)

    def card(self, cookies, _datatime):
        """
        抽卡
        :param cookies:
        :param _datatime:
        :return:
        """
        headers = {
            "Host": "m.ximalaya.com",
            "Accept": "application/json, text/plain, */*",
            "Connection": "keep-alive",
            "User-Agent": self.useragent,
            "Accept-Language": "zh-cn",
            "Referer": "https://m.ximalaya.com/xmds-node-spa/apps/speed-growth-activities/card-collection/home",
            "Accept-Encoding": "gzip, deflate, br",
        }
        try:
            response = requests.get(
                url="https://m.ximalaya.com/speed/web-earn/card/userCardInfo", headers=headers, cookies=cookies
            )
        except Exception as e:
            print(f"网络请求异常: {e}")
            return
        data = response.json()["data"]
        # 5 连抽
        drawr_record_id_list = data["drawRecordIdList"]
        card_mag = f"抽卡机会: {len(drawr_record_id_list)}次"
        for _ in range(len(drawr_record_id_list) // 5):
            tmp = []
            for _ in range(5):
                tmp.append(drawr_record_id_list.pop())
            self.draw_5card(cookies, tmp)
        # 手牌兑换金币
        # 1 万能卡  10 碎片
        print("检查手牌，卡牌兑金币")
        theme_id_map = {
            2: [2, 3],
            3: [4, 5, 6, 7],
            4: [8, 9, 10, 11, 12],
            5: [13, 14, 15, 16, 17, 18],
            6: [19, 20, 21, 22],
            7: [23, 24, 25, 26, 27],
            8: [28, 29, 30, 31, 32],
            9: [33, 34, 35, 36, 37],
        }
        try:
            response = requests.get(
                url="https://m.ximalaya.com/speed/web-earn/card/userCardInfo", headers=headers, cookies=cookies
            )
        except Exception as e:
            print(f"网络请求异常: {e}")
            return
        data = response.json()["data"]
        user_cards_list = data["userCardsList"]  # 手牌
        lstg = groupby(user_cards_list, key=lambda x: x["themeId"])
        for key, group in lstg:
            if key in [1, 10]:
                continue
            theme_id = key
            ids = list(group)
            tmp_record_id = []
            tmp_id = []
            for i in ids:
                if i["id"] in tmp_id:
                    continue
                tmp_record_id.append(i["recordId"])
                tmp_id.append(i["id"])
            if len(tmp_record_id) == len(theme_id_map[key]):
                print("可以兑换")
                self.card_exchange_card(cookies, theme_id, tmp_record_id)
        # 万能卡兑换稀有卡
        response = requests.get(
            url="https://m.ximalaya.com/speed/web-earn/card/userCardInfo", headers=headers, cookies=cookies
        )
        data = response.json()["data"]
        user_cards_list = data["userCardsList"]
        omnipotent_card = [i for i in user_cards_list if i["id"] == 1]
        city_card_id = [i["id"] for i in user_cards_list if i["themeId"] == 9]
        need = set(theme_id_map[9]) - set(city_card_id)
        print("万能卡: ", [i["recordId"] for i in omnipotent_card])
        card_mag += f"\n万能卡: {len(omnipotent_card)}张"
        for _ in range(len(omnipotent_card) // 4):
            tmp = []
            for _ in range(4):
                tmp.append(omnipotent_card.pop())
            from_record_id_list = [i["recordId"] for i in tmp]
            if need:
                print("万能卡兑换稀有卡:")
                self.card_exchange_card(cookies, need.pop(), from_record_id_list)
        # print(card_mag)
        return card_mag

    def account(self, cookies):
        """
        打印账号信息
        :param cookies:
        :return:
        """
        headers = {
            "Host": "m.ximalaya.com",
            "Content-Type": "application/json;charset=utf-8",
            "Connection": "keep-alive",
            "Accept": "application/json, text/plain, */*",
            "User-Agent": self.useragent,
            "Referer": "https://m.ximalaya.com/speed/web-earn/wallet",
            "Accept-Language": "zh-cn",
            "Accept-Encoding": "gzip, deflate, br",
        }
        try:
            response = requests.get(
                url="https://m.ximalaya.com/speed/web-earn/account/coin", headers=headers, cookies=cookies
            )
        except Exception as e:
            print(f"网络请求异常: {e}")
            return "", "", ""
        result = response.json()
        total = result["total"] / 10000
        today_total = result["todayTotal"] / 10000
        history_total = result["historyTotal"] / 10000
        return total, today_total, history_total

    def main(self):
        mins, date_stamp, _datatime, utc_time = self.get_time()
        xmly_cookie = self.check_item.get("xmly_cookie")
        cookies = self.parse_cookie(xmly_cookie)
        device_model = cookies.get("device_model", "未获取到设备信息")
        listen_msg = self.save_listen_time(cookies, date_stamp)
        self.listen_data(cookies, date_stamp)
        print("*" * 10, "阅读", "*" * 10)
        self.read(cookies)  # 阅读
        print("*" * 10, "收金币气泡", "*" * 10)
        bubble_msg = self.bubble(cookies)  # 收金币气泡
        print("*" * 10, "自动签到", "*" * 10)
        continuous_days = self.checkin(cookies, _datatime)  # 自动签到
        print("*" * 10, "答题赚金币", "*" * 10)
        answer_msg = self.answer(cookies)  # 答题赚金币
        print("*" * 10, "卡牌", "*" * 10)
        card_report_time_msg = self.card_report_time(cookies, mins, date_stamp, _datatime)  # 卡牌
        print("*" * 10, "领取万能卡", "*" * 10)
        self.get_omnipotent_card(cookies, mins, date_stamp, _datatime)  # 领取万能卡
        print("*" * 10, "抽卡", "*" * 10)
        card_msg = self.card(cookies, _datatime)  # 抽卡
        print("*" * 10, "首页、宝箱奖励及翻倍", "*" * 10)
        index_baoxiang_award_msg = self.index_baoxiang_award(cookies)  # 首页、宝箱奖励及翻倍
        total, today_total, history_total = self.account(cookies)
        msg = (
            f"北京时间: {utc_time}\n设备信息: {device_model}\n连续签到: {continuous_days}天\n收听时长: {listen_msg}分钟\n"
            f"金币气泡: {bubble_msg}\n答题奖励: {answer_msg}\n卡牌奖励: {card_report_time_msg}\n"
            f"{card_msg}\n{index_baoxiang_award_msg}\n"
            f"当前剩余: {total}元\n今日获得: {today_total}元\n累计获得: {history_total}元"
        )
        return msg


if __name__ == "__main__":
    with open(
        os.path.join(os.path.dirname(os.path.dirname(__file__)), "config/config.json"), "r", encoding="utf-8"
    ) as f:
        datas = json.loads(f.read())
    _check_item = datas.get("XMLY_COOKIE_LIST")[0]
    print(XMLYCheckIn(check_item=_check_item).main())
