import json
import os
import re
import time
from hashlib import md5
from random import randint
from urllib.parse import unquote
from uuid import uuid4

import requests

from dailycheckin import CheckIn


class IQIYI(CheckIn):
    name = "爱奇艺"

    def __init__(self, check_item):
        self.check_item = check_item

    @staticmethod
    def parse_cookie(cookie):
        p00001 = (
            re.findall(r"P00001=(.*?);", cookie)[0]
            if re.findall(r"P00001=(.*?);", cookie)
            else ""
        )
        p00002 = (
            re.findall(r"P00002=(.*?);", cookie)[0]
            if re.findall(r"P00002=(.*?);", cookie)
            else ""
        )
        p00003 = (
            re.findall(r"P00003=(.*?);", cookie)[0]
            if re.findall(r"P00003=(.*?);", cookie)
            else ""
        )
        __dfp = (
            re.findall(r"__dfp=(.*?);", cookie)[0]
            if re.findall(r"__dfp=(.*?);", cookie)
            else ""
        )
        __dfp = __dfp.split("@")[0]
        qyid = (
            re.findall(r"QC005=(.*?);", cookie)[0]
            if re.findall(r"QC005=(.*?);", cookie)
            else ""
        )
        return p00001, p00002, p00003, __dfp, qyid

    @staticmethod
    def user_information(p00001):
        """
        账号信息查询
        """
        time.sleep(3)
        url = "http://serv.vip.iqiyi.com/vipgrowth/query.action"
        params = {"P00001": p00001}
        res = requests.get(url=url, params=params).json()
        if res["code"] == "A00000":
            try:
                res_data = res.get("data", {})
                level = res_data.get("level", 0)
                growthvalue = res_data.get("growthvalue", 0)
                distance = res_data.get("distance", 0)
                deadline = res_data.get("deadline", "非 VIP 用户")
                today_growth_value = res_data.get("todayGrowthValue", 0)
                msg = [
                    {"name": "VIP 等级", "value": level},
                    {"name": "当前成长", "value": growthvalue},
                    {"name": "今日成长", "value": today_growth_value},
                    {"name": "升级还需", "value": distance},
                    {"name": "VIP 到期", "value": deadline},
                ]
            except Exception as e:
                msg = [
                    {"name": "账号信息", "value": str(e)},
                ]
        else:
            msg = [
                {"name": "账号信息", "value": res.get("msg")},
            ]
        return msg

    def k(self, secret_key, data, split="|"):
        result_string = split.join(f"{key}={data[key]}" for key in sorted(data))
        return md5((result_string + split + secret_key).encode("utf-8")).hexdigest()

    def sign(self, p00001, p00003, dfp, qyid):
        """
        VIP 签到
        """
        time_stamp = int(time.time() * 1000)
        sign_date = {
            "agenttype": 20,
            "agentversion": "15.4.6",
            "appKey": "lequ_rn",
            "appver": "15.4.6",
            "authCookie": p00001,
            "qyid": qyid,
            "srcplatform": 20,
            "task_code": "natural_month_sign",
            "timestamp": time_stamp,
            "userId": p00003,
        }
        sign = self.k("cRcFakm9KSPSjFEufg3W", sign_date)
        sign_date["sign"] = sign
        data = {
            "natural_month_sign": {
                "verticalCode": "iQIYI",
                "taskCode": "iQIYI_mofhr",
                "authCookie": p00001,
                "qyid": qyid,
                "agentType": 20,
                "agentVersion": "15.4.6",
                "dfp": dfp,
                "signFrom": 1,
            }
        }
        url = "https://community.iqiyi.com/openApi/task/execute"
        res = requests.post(
            url=url,
            params=sign_date,
            data=json.dumps(data),
            headers={"Content-Type": "application/json"},
        ).json()
        if res["code"] == "A00000":
            _msg = res["data"]["msg"]
            if _msg:
                msg = [{"name": "签到天数", "value": _msg}]
            else:
                try:
                    msg = [{"name": "签到天数", "value": res["data"]["data"]["signDays"]}]
                except Exception as e:
                    msg = [{"name": "签到天数", "value": str(e)}]
        else:
            msg = [{"name": "签到天数", "value": res.get("msg")}]
        return msg

    @staticmethod
    def query_user_task(p00001):
        """
        获取 VIP 日常任务 和 taskCode(任务状态)
        """
        url = "https://tc.vip.iqiyi.com/taskCenter/task/queryUserTask"
        params = {"P00001": p00001}
        task_list = []
        res = requests.get(url=url, params=params).json()
        if res["code"] == "A00000":
            for item in res["data"].get("tasks", {}).get("daily", []):
                task_list.append(
                    {
                        "taskTitle": item["taskTitle"],
                        "taskCode": item["taskCode"],
                        "status": item["status"],
                        "taskReward": item["taskReward"]["task_reward_growth"],
                    }
                )
        return task_list

    @staticmethod
    def join_task(p00001, task_list):
        """
        遍历完成任务
        """
        url = "https://tc.vip.iqiyi.com/taskCenter/task/joinTask"
        params = {
            "P00001": p00001,
            "taskCode": "",
            "platform": "bb136ff4276771f3",
            "lang": "zh_CN",
        }
        for item in task_list:
            if item["status"] == 2:
                params["taskCode"] = item["taskCode"]
                requests.get(url=url, params=params)

    @staticmethod
    def get_task_rewards(p00001, task_list):
        """
        获取任务奖励
        :return: 返回信息
        """
        url = "https://tc.vip.iqiyi.com/taskCenter/task/getTaskRewards"
        params = {
            "P00001": p00001,
            "taskCode": "",
            "platform": "bb136ff4276771f3",
            "lang": "zh_CN",
        }
        growth_task = 0
        for item in task_list:
            if item["status"] == 0:
                params["taskCode"] = item.get("taskCode")
                requests.get(url=url, params=params)
            elif item["status"] == 4:
                params["taskCode"] = item.get("taskCode")
                requests.get(
                    url="https://tc.vip.iqiyi.com/taskCenter/task/notify", params=params
                )
                requests.get(url=url, params=params)
            elif item["status"] == 1:
                growth_task += item["taskReward"]
        msg = {"name": "任务奖励", "value": f"+{growth_task}成长值"}
        return msg

    def lottery(self, p00001, award_list=[]):
        url = "https://act.vip.iqiyi.com/shake-api/lottery"
        params = {
            "P00001": p00001,
            "lotteryType": "0",
            "actCode": "0k9GkUcjqqj4tne8",
        }
        params = {
            "P00001": p00001,
            "deviceID": str(uuid4()),
            "version": "15.3.0",
            "platform": str(uuid4())[:16],
            "lotteryType": "0",
            "actCode": "0k9GkUcjqqj4tne8",
            "extendParams": json.dumps(
                {
                    "appIds": "iqiyi_pt_vip_iphone_video_autorenew_12m_348yuan_v2",
                    "supportSk2Identity": True,
                    "testMode": "0",
                    "iosSystemVersion": "17.4",
                    "bundleId": "com.qiyi.iphone",
                }
            ),
        }
        res = requests.get(url, params=params).json()
        msgs = []
        if res.get("code") == "A00000":
            award_info = res.get("data", {}).get("title")
            award_list.append(award_info)
            time.sleep(3)
            return self.lottery(p00001=p00001, award_list=award_list)
        elif res.get("msg") == "抽奖次数用完":
            if award_list:
                msgs = [{"name": "每天摇一摇", "value": "、".join(award_list)}]
            else:
                msgs = [{"name": "每天摇一摇", "value": res.get("msg")}]
        else:
            msgs = [{"name": "每天摇一摇", "value": res.get("msg")}]
        return msgs

    @staticmethod
    def draw(draw_type, p00001, p00003):
        """
        查询抽奖次数(必),抽奖
        :param draw_type: 类型。0 查询次数；1 抽奖
        :param p00001: 关键参数
        :param p00003: 关键参数
        :return: {status, msg, chance}
        """
        url = "https://iface2.iqiyi.com/aggregate/3.0/lottery_activity"
        params = {
            "lottery_chance": 1,
            "app_k": "b398b8ccbaeacca840073a7ee9b7e7e6",
            "app_v": "11.6.5",
            "platform_id": 10,
            "dev_os": "8.0.0",
            "dev_ua": "FRD-AL10",
            "net_sts": 1,
            "qyid": "2655b332a116d2247fac3dd66a5285011102",
            "psp_uid": p00003,
            "psp_cki": p00001,
            "psp_status": 3,
            "secure_v": 1,
            "secure_p": "GPhone",
            "req_sn": round(time.time() * 1000),
        }
        if draw_type == 1:
            del params["lottery_chance"]
        res = requests.get(url=url, params=params).json()
        if not res.get("code"):
            chance = int(res.get("daysurpluschance"))
            msg = res.get("awardName")
            return {"status": True, "msg": msg, "chance": chance}
        else:
            try:
                msg = res.get("kv", {}).get("msg")
            except Exception as e:
                print(e)
                msg = res["errorReason"]
        return {"status": False, "msg": msg, "chance": 0}

    def get_watch_time(self, p00001):
        url = "https://tc.vip.iqiyi.com/growthAgency/watch-film-duration"
        data = requests.get(
            url=url,
            headers={
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0",
                "Cookie": f"P00001={p00001}",
                "Content-Type": "application/json",
            },
        ).json()
        watch_time = data["data"]["viewtime"]["time"]
        return watch_time

    def level_right(self, p00001):
        data = {"code": "k8sj74234c683f", "P00001": p00001}
        res = requests.post(
            url="https://act.vip.iqiyi.com/level-right/receive", data=data
        ).json()
        msg = res["msg"]
        return [{"name": "V7 免费升级星钻", "value": msg}]

    def start_watch(self, p00001, p00003, dfp):
        total_time = self.get_watch_time(p00001=p00001)
        print(f"现在已经刷到了 {total_time}秒, 数据同步有延迟, 仅供参考")
        if total_time >= 7200:
            return {
                "name": "视频时长",
                "value": f"已经刷了 {total_time}秒, 数据同步有延迟, 仅供参考",
            }
        for _ in range(150):
            tm = randint(60, 120)
            watch_time_url = "https://msg.qy.net/b"
            params = {
                "u": "f600a23f03c26507f5482e6828cfc6c5",
                "pu": p00003,
                "p1": "1_10_101",
                "v": "5.2.66",
                "ce": uuid4().hex,
                "de": "1616773143.1639632721.1639653680.29",
                "c1": "2",
                "ve": uuid4().hex,
                "ht": "0",
                "pt": randint(1000000000, 9999999999) / 1000000,
                "isdm": "0",
                "duby": "0",
                "ra": "5",
                "clt": "",
                "ps2": "DIRECT",
                "ps3": "",
                "ps4": "",
                "br": "mozilla/5.0 (windows nt 10.0; win64; x64) applewebkit/537.36 (khtml, like gecko) chrome/96.0.4664.110 safari/537.36",
                "mod": "cn_s",
                "purl": "https://www.iqiyi.com/v_1eldg8u3r08.html?vfrm=pcw_home&vfrmblk=712211_cainizaizhui&vfrmrst=712211_cainizaizhui_image1&r_area=rec_you_like&r_source=62%40128&bkt=MBA_PW_T3_53&e=b3ec4e6c74812510c7719f7ecc8fbb0f&stype=2",
                "tmplt": "2",
                "ptid": "01010031010000000000",
                "os": "window",
                "nu": "0",
                "vfm": "",
                "coop": "",
                "ispre": "0",
                "videotp": "0",
                "drm": "",
                "plyrv": "",
                "rfr": "https://www.iqiyi.com/",
                "fatherid": f"{randint(1000000000000000, 9999999999999999)}",
                "stauto": "1",
                "algot": "abr_v12-rl",
                "vvfrom": "",
                "vfrmtp": "1",
                "pagev": "playpage_adv_xb",
                "engt": "2",
                "ldt": "1",
                "krv": "1.1.85",
                "wtmk": "0",
                "duration": f"{randint(1000000, 9999999)}",
                "bkt": "",
                "e": "",
                "stype": "",
                "r_area": "",
                "r_source": "",
                "s4": f"{randint(100000, 999999)}_dianshiju_tbrb_image2",
                "abtest": "1707_B,1550_B",
                "s3": f"{randint(100000, 999999)}_dianshiju_tbrb",
                "vbr": f"{randint(100000, 999999)}",
                "mft": "0",
                "ra1": "2",
                "wint": "3",
                "s2": "pcw_home",
                "bw": "10",
                "ntwk": "18",
                "dl": f"{randint(10, 999)}.27999999999997",
                "rn": f"0.{randint(1000000000000000, 9999999999999999)}",
                "dfp": dfp,
                "stime": str(time.time() * 1000),
                "r": f"{randint(1000000000000000, 9999999999999999)}",
                "hu": "1",
                "t": "2",
                "tm": str(tm),
                "_": str(time.time() * 1000),
            }
            requests.get(
                url=watch_time_url,
                headers={
                    "User-Agent": "mozilla/5.0 (windows nt 10.0; win64; x64) applewebkit/537.36 (khtml, like gecko) chrome/96.0.4664.110 safari/537.36",
                    "Cookie": f"P00001={p00001}",
                    "Content-Type": "application/json",
                },
                params=params,
            )
            total_time += tm
            print(f"现在已经刷到了 {total_time}秒, 数据同步有延迟, 仅供参考")
            if total_time >= 7600:
                break
        return {
            "name": "视频时长",
            "value": f"已经刷了 {total_time}秒, 数据同步有延迟, 仅供参考",
        }

    def give_times(self, p00001):
        url = "https://pcell.iqiyi.com/lotto/giveTimes"
        times_code_list = ["browseWeb", "browseWeb", "bookingMovie"]
        for times_code in times_code_list:
            params = {
                "actCode": "bcf9d354bc9f677c",
                "timesCode": times_code,
                "P00001": p00001,
            }
            response = requests.get(url, params=params)
            print(response.json())

    def lotto_lottery(self, p00001):
        self.give_times(p00001=p00001)
        gift_list = []
        for _ in range(5):
            url = "https://pcell.iqiyi.com/lotto/lottery"
            params = {"actCode": "bcf9d354bc9f677c", "P00001": p00001}
            response = requests.get(url, params=params)
            gift_name = response.json()["data"]["giftName"]
            if gift_name and "未中奖" not in gift_name:
                gift_list.append(gift_name)
        if gift_list:
            return [{"name": "白金抽奖", "value": "、".join(gift_list)}]
        else:
            return [{"name": "白金抽奖", "value": "未中奖"}]

    def main(self):
        p00001, p00002, p00003, dfp, qyid = self.parse_cookie(
            self.check_item.get("cookie")
        )
        try:
            user_info = json.loads(unquote(p00002, encoding="utf-8"))
            user_name = user_info.get("user_name")
            user_name = user_name.replace(user_name[3:7], "****")
            nickname = user_info.get("nickname")
        except Exception as e:
            print(f"获取账号信息失败，错误信息: {e}")
            nickname = "未获取到，请检查 Cookie 中 P00002 字段"
            user_name = "未获取到，请检查 Cookie 中 P00002 字段"
        sign_msg = self.sign(p00001=p00001, p00003=p00003, dfp=dfp, qyid=qyid)
        _user_msg = self.user_information(p00001=p00001)
        lotto_lottery_msg = self.lotto_lottery(p00001=p00001)
        if _user_msg[4].get("value") != "非 VIP 用户":
            watch_msg = self.start_watch(p00001=p00001, p00003=p00003, dfp=dfp)
            level_right_msg = self.level_right(p00001=p00001)
        else:
            watch_msg = {"name": "视频时长", "value": "非 VIP 用户"}
            level_right_msg = [
                {
                    "name": "V7 免费升级星钻",
                    "value": "非 VIP 用户",
                }
            ]
        chance = self.draw(draw_type=0, p00001=p00001, p00003=p00003)["chance"]
        lottery_msgs = self.lottery(p00001=p00001, award_list=[])
        if chance:
            draw_msg = ""
            for _ in range(chance):
                ret = self.draw(draw_type=1, p00001=p00001, p00003=p00003)
                draw_msg += ret["msg"] + ";" if ret["status"] else ""
        else:
            draw_msg = "抽奖机会不足"
        task_msg = ""
        for _ in range(3):
            task_list = self.query_user_task(p00001=p00001)
            self.join_task(p00001=p00001, task_list=task_list)
            task_msg = self.get_task_rewards(p00001=p00001, task_list=task_list)

        user_msg = self.user_information(p00001=p00001)

        msg = (
            [
                {"name": "用户账号", "value": user_name},
                {"name": "用户昵称", "value": nickname},
            ]
            + user_msg
            + sign_msg
            + [
                task_msg,
                {"name": "抽奖奖励", "value": draw_msg},
            ]
            + [watch_msg]
            + lottery_msgs
            + level_right_msg
            + lotto_lottery_msg
        )
        msg = "\n".join([f"{one.get('name')}: {one.get('value')}" for one in msg])
        return msg


if __name__ == "__main__":
    with open(
        os.path.join(os.path.dirname(os.path.dirname(__file__)), "config.json"),
        encoding="utf-8",
    ) as f:
        datas = json.loads(f.read())
    _check_item = datas.get("IQIYI", [])[0]
    print(IQIYI(check_item=_check_item).main())
