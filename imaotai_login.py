import hashlib
import json
import time

import requests

"""
获取地点信息,这里用的高德 api,需要自己去高德开发者平台申请自己的 key
"""
AMAP_KEY = ""


SALT = "2af72f100c356273d46284f6fd1dfc08"

CURRENT_TIME = str(int(time.time() * 1000))
headers = {}


mt_version = json.loads(
    requests.get("https://itunes.apple.com/cn/lookup?id=1600482450").text
)["results"][0]["version"]


header_context = """
MT-Lat: 28.499562
MT-K: 1675213490331
MT-Lng: 102.182324
Host: app.moutai519.com.cn
MT-User-Tag: 0
Accept: */*
MT-Network-Type: WIFI
MT-Token: 1
MT-Team-ID: 1
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


# 初始化请求头
def init_headers(
    user_id: str = "1", token: str = "2", lat: str = "29.83826", lng: str = "119.74375"
):
    for k in header_context.strip().split("\n"):
        temp_l = k.split(": ")
        dict.update(headers, {temp_l[0]: temp_l[1]})
    dict.update(headers, {"userId": user_id})
    dict.update(headers, {"MT-Token": token})
    dict.update(headers, {"MT-Lat": lat})
    dict.update(headers, {"MT-Lng": lng})
    dict.update(headers, {"MT-APP-Version": mt_version})


# 用高德api获取地图信息
def select_geo(i: str):
    # 校验高德api是否配置
    if AMAP_KEY is None:
        print("!!!!请配置 AMAP_KEY (高德地图的MapKey)")
        raise ValueError
    resp = requests.get(
        f"https://restapi.amap.com/v3/geocode/geo?key={AMAP_KEY}&output=json&address={i}"
    )
    geocodes: list = resp.json()["geocodes"]
    return geocodes


def signature(data: dict):
    keys = sorted(data.keys())
    temp_v = ""
    for item in keys:
        temp_v += data[item]
    text = SALT + temp_v + CURRENT_TIME
    hl = hashlib.md5()
    hl.update(text.encode(encoding="utf8"))
    md5 = hl.hexdigest()
    return md5


# 获取登录手机验证码
def get_vcode(mobile: str):
    params = {"mobile": mobile}
    md5 = signature(params)
    dict.update(
        params, {"md5": md5, "timestamp": CURRENT_TIME, "MT-APP-Version": mt_version}
    )
    responses = requests.post(
        "https://app.moutai519.com.cn/xhr/front/user/register/vcode",
        json=params,
        headers=headers,
    )
    if responses.status_code != 200:
        print(
            f"get v_code : params : {params}, response code : {responses.status_code}, response body : {responses.text}"
        )


# 执行登录操作
def login(mobile: str, v_code: str):
    params = {"mobile": mobile, "vCode": v_code, "ydToken": "", "ydLogId": ""}
    md5 = signature(params)
    dict.update(
        params, {"md5": md5, "timestamp": CURRENT_TIME, "MT-APP-Version": mt_version}
    )
    responses = requests.post(
        "https://app.moutai519.com.cn/xhr/front/user/register/login",
        json=params,
        headers=headers,
    )
    if responses.status_code != 200:
        print(
            f"login : params : {params}, response code : {responses.status_code}, response body : {responses.text}"
        )
    dict.update(headers, {"MT-Token": responses.json()["data"]["token"]})
    dict.update(headers, {"userId": responses.json()["data"]["userId"]})
    return responses.json()["data"]["token"], responses.json()["data"]["userId"]


def get_location():
    while 1:
        location = input("请输入精确小区位置，例如[小区名称]，为你自动预约附近的门店:").strip()
        selects = select_geo(location)

        a = 0
        for item in selects:
            formatted_address = item["formatted_address"]
            province = item["province"]
            print(f"{a} : [地区:{province},位置:{formatted_address}]")
            a += 1
        user_select = input("请选择位置序号,重新输入请输入[-]:").strip()
        if user_select == "-":
            continue
        select = selects[int(user_select)]
        formatted_address = select["formatted_address"]
        province = select["province"]
        print(f"已选择 地区:{province},[{formatted_address}]附近的门店")
        return select


if __name__ == "__main__":
    items = []
    while 1:
        init_headers()
        location_select: dict = get_location()
        province = location_select["province"]
        city = location_select["city"]
        location: str = location_select["location"]

        mobile = input("输入手机号[18888888888]:").strip()
        get_vcode(mobile)
        code = input(f"输入 [{mobile}] 验证码[8888]:").strip()
        token, userId = login(mobile, code)
        item = {
            "province": province,
            "city": str(city),
            "lat": location.split(",")[1],
            "lng": location.split(",")[0],
            "mobile": str(mobile),
            "token": str(token),
            "userid": str(userId),
            "reserve_rule": 0,
            "item_codes": ["11318", "11319"],
        }
        items.append(item)
        condition = input("是否继续添加账号[y/n]:").strip()
        with open("account.json", "w") as f:
            f.write(json.dumps(items, ensure_ascii=False, indent=4))
        if condition.lower() == "n":
            break
