import base64
import datetime
import json
import math
import os
import random
import time

import requests
from Crypto.Cipher import AES

from dailycheckin import CheckIn


class Encrypt:
    def __init__(self, key, iv):
        self.key = key.encode("utf-8")
        self.iv = iv.encode("utf-8")

    def pkcs7padding(self, text):
        """明文使用PKCS7填充"""
        bs = 16
        length = len(text)
        bytes_length = len(text.encode("utf-8"))
        padding_size = length if (bytes_length == length) else bytes_length
        padding = bs - padding_size % bs
        padding_text = chr(padding) * padding
        self.coding = chr(padding)
        return text + padding_text

    def aes_encrypt(self, content):
        """AES加密"""
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        content_padding = self.pkcs7padding(content)
        encrypt_bytes = cipher.encrypt(content_padding.encode("utf-8"))
        result = str(base64.b64encode(encrypt_bytes), encoding="utf-8")
        return result

    def aes_decrypt(self, content):
        """AES解密"""
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        content = base64.b64decode(content)
        text = cipher.decrypt(content).decode("utf-8")
        return text.rstrip(self.coding)


class IMAOTAI(CheckIn):
    name = "i茅台"

    def __init__(self, check_item):
        self.check_item = check_item
        self.RESERVE_RULE = 0
        self.mt_r = "clips_OlU6TmFRag5rCXwbNAQ/Tz1SKlN8THcecBp/"
        self.ITEM_MAP = {
            "11318": "53%vol 500ml贵州茅台酒（乙巳蛇年）",
            "11317": "53%vol 500ml贵州茅台酒（笙乐飞天）",
            "11319": "53%vol 375mlx2贵州茅台酒（乙巳蛇年）",
            "2478": "53%vol 500ml贵州茅台酒（珍品）",
            "11240": "53%vol 500ml 茅台1935·中国国家地理文创酒（喜逢大运河）",
        }
        self.ITEM_CODES = ["11318", "11319"]
        AES_KEY = "qbhajinldepmucsonaaaccgypwuvcjaa"
        AES_IV = "2018534749963515"
        self.encrypt = Encrypt(key=AES_KEY, iv=AES_IV)

        self.mt_version = json.loads(
            requests.get("https://itunes.apple.com/cn/lookup?id=1600482450").text
        )["results"][0]["version"]
        self.headers = {}
        self.header_context = """
MT-Lat: 28.499562
MT-K: 1675213490331
MT-Lng: 102.182324
Host: app.moutai519.com.cn
MT-User-Tag: 0
Accept: */*
MT-Network-Type: WIFI
MT-Token: 1
MT-Info: 028e7f96f6369cafe1d105579c5b9377
MT-Device-ID: 2F2075D0-B66C-4287-A903-DBFF6358342A
MT-Bundle-ID: com.moutai.mall
Accept-Language: en-CN;q=1, zh-Hans-CN;q=0.9
MT-Request-ID: 167560018873318465
MT-APP-Version: 1.3.7
User-Agent: iOS;16.3;Apple;?unrecognized?
MT-R: clips_OlU6TmFRag5rCXwbNAQ/Tz1SKlN8THcecBp/HGhHdw==
Content-Length: 93
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Content-Type: application/json
userId: 2
"""

    def init_headers(
        self,
        user_id: str = "1",
        token: str = "2",
        lat: str = "29.83826",
        lng: str = "119.74375",
    ):
        for k in self.header_context.strip().split("\n"):
            temp_l = k.split(": ")
            dict.update(self.headers, {temp_l[0]: temp_l[1]})
        dict.update(self.headers, {"userId": user_id})
        dict.update(self.headers, {"MT-Token": token})
        dict.update(self.headers, {"MT-Lat": lat})
        dict.update(self.headers, {"MT-Lng": lng})
        dict.update(self.headers, {"MT-APP-Version": self.mt_version})

    def get_current_session_id(self):
        day_time = int(time.mktime(datetime.date.today().timetuple())) * 1000
        my_url = f"https://static.moutai519.com.cn/mt-backend/xhr/front/mall/index/session/get/{day_time}"
        responses = requests.get(my_url)
        if responses.status_code != 200:
            print(
                f"get_current_session_id : params : {day_time}, response code : {responses.status_code}, response body : {responses.text}"
            )
        current_session_id = responses.json()["data"]["sessionId"]
        dict.update(self.headers, {"current_session_id": str(current_session_id)})

    def get_map(self, lat: str = "28.499562", lng: str = "102.182324"):
        p_c_map = {}
        url = "https://static.moutai519.com.cn/mt-backend/xhr/front/mall/resource/get"
        headers = {
            "X-Requested-With": "XMLHttpRequest",
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_0_1 like Mac OS X)",
            "Referer": "https://h5.moutai519.com.cn/gux/game/main?appConfig=2_1_2",
            "Client-User-Agent": "iOS;16.0.1;Apple;iPhone 14 ProMax",
            "MT-R": "clips_OlU6TmFRag5rCXwbNAQ/Tz1SKlN8THcecBp/HGhHdw==",
            "Origin": "https://h5.moutai519.com.cn",
            "MT-APP-Version": self.mt_version,
            "MT-Request-ID": f"{int(time.time() * 1000)}{random.randint(1111111, 999999999)}{int(time.time() * 1000)}",
            "Accept-Language": "zh-CN,zh-Hans;q=1",
            "MT-Device-ID": f"{int(time.time() * 1000)}{random.randint(1111111, 999999999)}{int(time.time() * 1000)}",
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "mt-lng": f"{lng}",
            "mt-lat": f"{lat}",
        }
        res = requests.get(url, headers=headers)
        mtshops = res.json().get("data", {}).get("mtshops_pc", {})
        urls = mtshops.get("url")
        r = requests.get(urls)
        for k, v in dict(r.json()).items():
            provinceName = v.get("provinceName")
            cityName = v.get("cityName")
            if not p_c_map.get(provinceName):
                p_c_map[provinceName] = {}
            if not p_c_map[provinceName].get(cityName, None):
                p_c_map[provinceName][cityName] = [k]
            else:
                p_c_map[provinceName][cityName].append(k)

        return p_c_map, dict(r.json())

    def max_shop(self, city, item_code, p_c_map, province, shops):
        max_count = 0
        max_shop_id = "0"
        shop_ids = p_c_map[province][city]
        for shop in shops:
            shopId = shop["shopId"]
            items = shop["items"]

            if shopId not in shop_ids:
                continue
            for item in items:
                if item["itemId"] != str(item_code):
                    continue
                if item["inventory"] > max_count:
                    max_count = item["inventory"]
                    max_shop_id = shopId
        print(
            f"item code {item_code}, max shop id : {max_shop_id}, max count : {max_count}"
        )
        return max_shop_id

    def distance_shop(
        self,
        item_code,
        shops,
        source_data,
        lat: str = "28.499562",
        lng: str = "102.182324",
    ):
        temp_list = []
        for shop in shops:
            shopId = shop["shopId"]
            items = shop["items"]
            item_ids = [i["itemId"] for i in items]
            if str(item_code) not in item_ids:
                continue
            shop_info = source_data.get(shopId)
            d = math.sqrt(
                (float(lat) - shop_info["lat"]) ** 2
                + (float(lng) - shop_info["lng"]) ** 2
            )
            temp_list.append((d, shopId))

        temp_list = sorted(temp_list, key=lambda x: x[0])
        if len(temp_list) > 0:
            return temp_list[0][1]
        else:
            return "0"

    def get_location_count(
        self,
        province: str,
        city: str,
        item_code: str,
        p_c_map: dict,
        source_data: dict,
        lat: str = "29.83826",
        lng: str = "102.182324",
        reserve_rule: int = 0,
    ):
        day_time = int(time.mktime(datetime.date.today().timetuple())) * 1000
        session_id = self.headers["current_session_id"]
        responses = requests.get(
            f"https://static.moutai519.com.cn/mt-backend/xhr/front/mall/shop/list/slim/v3/{session_id}/{province}/{item_code}/{day_time}"
        )
        if responses.status_code != 200:
            print(
                f"get_location_count : params : {day_time}, response code : {responses.status_code}, response body : {responses.text}"
            )
        shops = responses.json()["data"]["shops"]

        if reserve_rule == 0:
            return self.distance_shop(item_code, shops, source_data, lat, lng)
        if reserve_rule == 1:
            return self.max_shop(city, item_code, p_c_map, province, shops)

    def act_params(self, shop_id: str, item_id: str):
        session_id = self.headers["current_session_id"]
        userId = self.headers["userId"]
        params = {
            "itemInfoList": [{"count": 1, "itemId": item_id}],
            "sessionId": int(session_id),
            "userId": userId,
            "shopId": shop_id,
        }
        s = json.dumps(params)
        act = self.encrypt.aes_encrypt(s)
        params.update({"actParam": act})
        return params

    def reservation(self, params: dict):
        params.pop("userId")
        responses = requests.post(
            "https://app.moutai519.com.cn/xhr/front/mall/reservation/add",
            json=params,
            headers=self.headers,
        ).json()
        if responses.get("code") == 401:
            msg = {
                "name": "申购结果",
                "value": "token失效, 请重新抓包获取",
            }
        elif responses.get("code") != 2000:
            msg = {
                "name": "申购结果",
                "value": responses.get("message"),
            }
        else:
            msg = {
                "name": "申购结果",
                "value": responses.get("data", {}).get("successDesc"),
            }
        return msg

    def getUserEnergyAward(self):
        """
        耐力值
        """
        cookies = {
            "MT-Device-ID-Wap": self.headers["MT-Device-ID"],
            "MT-Token-Wap": self.headers["MT-Token"],
            "YX_SUPPORT_WEBP": "1",
        }
        response = requests.post(
            url="https://h5.moutai519.com.cn/game/isolationPage/getUserEnergyAward",
            cookies=cookies,
            headers=self.headers,
            json={},
        ).json()
        if response.get("code") == 200:
            msg = {
                "name": "耐力",
                "value": "✅领取耐力成功",
            }
        else:
            msg = {
                "name": "耐力",
                "value": response.get("message"),
            }
        return msg

    def main(self):
        msg = []
        mobile = self.check_item.get("mobile")
        province = self.check_item.get("province")
        city = self.check_item.get("city")
        token = self.check_item.get("token")
        userId = self.check_item.get("userid")
        lat = self.check_item.get("lat")
        lng = self.check_item.get("lng")
        item_codes = self.check_item.get("item_codes", self.ITEM_CODES)
        reserve_rule = self.check_item.get("reserve_rule", 0)
        msg = [
            {
                "name": "手机号",
                "value": f"{mobile}",
            },
            {
                "name": "省份城市",
                "value": f"{province}{city}",
            },
        ]
        p_c_map, source_data = self.get_map(lat=lat, lng=lng)
        self.get_current_session_id()
        self.init_headers(user_id=userId, token=token, lng=lng, lat=lat)
        try:
            for item in item_codes:
                max_shop_id = self.get_location_count(
                    province=province,
                    city=city,
                    item_code=item,
                    p_c_map=p_c_map,
                    source_data=source_data,
                    lat=lat,
                    lng=lng,
                    reserve_rule=reserve_rule,
                )
                if max_shop_id == "0":
                    continue
                reservation_params = self.act_params(max_shop_id, item)
                reservation_msg = self.reservation(reservation_params)
                time.sleep(20)
                award_msg = self.getUserEnergyAward()
                msg.append(reservation_msg)
                msg.append(award_msg)
        except BaseException as e:
            msg.append(
                {
                    "name": "申购结果",
                    "value": e,
                }
            )
        msg = "\n".join([f"{one.get('name')}: {one.get('value')}" for one in msg])
        return msg


if __name__ == "__main__":
    with open(
        os.path.join(os.path.dirname(os.path.dirname(__file__)), "config.json"),
        encoding="utf-8",
    ) as f:
        datas = json.loads(f.read())
    _check_item = datas.get("IMAOTAI", [])[0]
    print(IMAOTAI(check_item=_check_item).main())
