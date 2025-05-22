import hashlib
import json
import os
import random
import time
from typing import Optional, Union

import requests

from dailycheckin import CheckIn


class Tieba(CheckIn):
    name = "百度贴吧"

    def __init__(self, check_item: dict):
        self.TBS_URL = "http://tieba.baidu.com/dc/common/tbs"
        self.LIKE_URL = "http://c.tieba.baidu.com/c/f/forum/like"
        self.SIGN_URL = "http://c.tieba.baidu.com/c/c/forum/sign"
        self.LOGIN_INFO_URL = "https://zhidao.baidu.com/api/loginInfo"
        self.SIGN_KEY = "tiebaclient!!!"

        self.HEADERS = {
            "Host": "tieba.baidu.com",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36",
            "Connection": "keep-alive",
            "Accept-Encoding": "gzip, deflate",
            "Cache-Control": "no-cache",
        }

        self.SIGN_DATA = {
            "_client_type": "2",
            "_client_version": "9.7.8.0",
            "_phone_imei": "000000000000000",
            "model": "MI+5",
            "net_type": "1",
        }

        self.session = requests.Session()
        self.session.headers.update(self.HEADERS)

        cookie = check_item.get("cookie")
        if not cookie:
            raise ValueError("必须提供 BDUSS 或完整 Cookie")

        cookie_dict = {
            item.split("=")[0]: item.split("=")[1]
            for item in cookie.split("; ")
            if "=" in item
        }
        requests.utils.add_dict_to_cookiejar(self.session.cookies, cookie_dict)
        self.bduss = cookie_dict.get("BDUSS", "")
        if not self.bduss:
            raise ValueError("Cookie 中未找到 BDUSS")

    def request(
        self, url: str, method: str = "get", data: Optional[dict] = None, retry: int = 3
    ) -> dict:
        for i in range(retry):
            try:
                if method.lower() == "get":
                    response = self.session.get(url, timeout=10)
                else:
                    response = self.session.post(url, data=data, timeout=10)

                response.raise_for_status()
                if not response.text.strip():
                    raise ValueError("空响应内容")

                return response.json()

            except Exception as e:
                if i == retry - 1:
                    raise Exception(f"请求失败: {str(e)}")

                wait_time = 1.5 * (2**i) + random.uniform(0, 1)
                time.sleep(wait_time)

        raise Exception(f"请求失败，已达最大重试次数 {retry}")

    def encode_data(self, data: dict) -> dict:
        s = ""
        for key in sorted(data.keys()):
            s += f"{key}={data[key]}"
        sign = hashlib.md5((s + self.SIGN_KEY).encode("utf-8")).hexdigest().upper()
        data.update({"sign": sign})
        return data

    def get_user_info(self) -> tuple[Union[str, bool], str]:
        try:
            result = self.request(self.TBS_URL)
            if result.get("is_login", 0) == 0:
                return False, "登录失败，Cookie 异常"
            tbs = result.get("tbs", "")
            try:
                user_info = self.request(self.LOGIN_INFO_URL)
                user_name = user_info.get("userName", "未知用户")
            except Exception:
                user_name = "未知用户"
            return tbs, user_name
        except Exception as e:
            return False, f"登录验证异常: {e}"

    def get_favorite(self) -> list[dict]:
        forums = []
        page_no = 1

        while True:
            data = {
                "BDUSS": self.bduss,
                "_client_type": "2",
                "_client_id": "wappc_1534235498291_488",
                "_client_version": "9.7.8.0",
                "_phone_imei": "000000000000000",
                "from": "1008621y",
                "page_no": str(page_no),
                "page_size": "200",
                "model": "MI+5",
                "net_type": "1",
                "timestamp": str(int(time.time())),
                "vcode_tag": "11",
            }
            data = self.encode_data(data)

            try:
                res = self.request(self.LIKE_URL, "post", data)

                if "forum_list" in res:
                    for forum_type in ["non-gconforum", "gconforum"]:
                        if forum_type in res["forum_list"]:
                            items = res["forum_list"][forum_type]
                            if isinstance(items, list):
                                forums.extend(items)
                            elif isinstance(items, dict):
                                forums.append(items)

                if res.get("has_more") != "1":
                    break

                page_no += 1
                time.sleep(random.uniform(1, 2))

            except Exception as e:
                print(f"获取贴吧列表出错: {e}")
                break

        print(f"共获取到 {len(forums)} 个关注的贴吧")
        return forums

    def sign_forums(self, forums, tbs: str) -> dict:
        success_count, error_count, exist_count, shield_count = 0, 0, 0, 0
        total = len(forums)
        print(f"开始签到 {total} 个贴吧")
        last_request_time = time.time()
        for idx, forum in enumerate(forums):
            elapsed = time.time() - last_request_time
            delay = max(0, 1.0 + random.uniform(0.5, 1.5) - elapsed)
            time.sleep(delay)
            last_request_time = time.time()
            if (idx + 1) % 10 == 0:
                extra_delay = random.uniform(5, 10)
                print(f"已签到 {idx + 1}/{total} 个贴吧，休息 {extra_delay:.2f} 秒")
                time.sleep(extra_delay)

            forum_name = forum.get("name", "")
            forum_id = forum.get("id", "")
            log_prefix = f"【{forum_name}】吧({idx + 1}/{total})"

            try:
                data = self.SIGN_DATA.copy()
                data.update(
                    {
                        "BDUSS": self.bduss,
                        "fid": forum_id,
                        "kw": forum_name,
                        "tbs": tbs,
                        "timestamp": str(int(time.time())),
                    }
                )
                data = self.encode_data(data)
                result = self.request(self.SIGN_URL, "post", data)
                error_code = result.get("error_code", "")
                if error_code == "0":
                    success_count += 1
                    if "user_info" in result:
                        rank = result["user_info"]["user_sign_rank"]
                        print(f"{log_prefix} 签到成功，第{rank}个签到")
                    else:
                        print(f"{log_prefix} 签到成功")
                elif error_code == "160002":
                    exist_count += 1
                    print(f"{log_prefix} {result.get('error_msg', '今日已签到')}")
                elif error_code == "340006":
                    shield_count += 1
                    print(f"{log_prefix} 贴吧已被屏蔽")
                else:
                    error_count += 1
                    print(
                        f"{log_prefix} 签到失败，错误: {result.get('error_msg', '未知错误')}"
                    )

            except Exception as e:
                error_count += 1
                print(f"{log_prefix} 签到异常: {str(e)}")
        return {
            "total": total,
            "success": success_count,
            "exist": exist_count,
            "shield": shield_count,
            "error": error_count,
        }

    def main(self) -> str:
        try:
            tbs, user_name = self.get_user_info()
            if not tbs:
                return f"账号: {user_name}\n登录状态: Cookie可能已过期"
            forums = self.get_favorite()

            if forums:
                stats = self.sign_forums(forums, tbs)
                msg = [
                    {"name": "帐号信息", "value": user_name},
                    {"name": "贴吧总数", "value": stats["total"]},
                    {"name": "签到成功", "value": stats["success"]},
                    {"name": "已经签到", "value": stats["exist"]},
                    {"name": "被屏蔽的", "value": stats["shield"]},
                    {"name": "签到失败", "value": stats["error"]},
                ]
            else:
                msg = [
                    {"name": "帐号信息", "value": user_name},
                    {"name": "获取贴吧列表失败，无法完成签到", "value": ""},
                ]
        except Exception as e:
            msg = [
                {"name": "帐号信息", "value": user_name},
                {"name": "签到失败", "value": str(e)},
            ]
        msg = "\n".join([f"{one.get('name')}: {one.get('value')}" for one in msg])
        return msg


if __name__ == "__main__":
    with open(
        os.path.join(os.path.dirname(os.path.dirname(__file__)), "config.json"),
        encoding="utf-8",
    ) as f:
        datas = json.loads(f.read())
    _check_item = datas.get("TIEBA", [])[0]
    print(Tieba(check_item=_check_item).main())
