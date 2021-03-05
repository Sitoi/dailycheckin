# -*- coding: utf-8 -*-
import json
import os
import re
import time
from urllib import parse

import requests


class OnePlusBBSCheckIn:
    def __init__(self, check_item):
        self.check_item = check_item

    @staticmethod
    def sign(cookie):
        headers = {
            "Origin": "https://www.oneplusbbs.com",
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.57",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Referer": "https://www.oneplusbbs.com/plugin-dsu_paulsign:sign.html",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,fr;q=0.5,pl;q=0.4",
            "cookie": cookie,
        }
        params = (
            ("id", "dsu_paulsign:sign"),
            ("operation", "qiandao"),
            ("infloat", "1"),
            ("inajax", "1"),
        )
        formhash = re.findall(r"bbs_formhash=(.*?);", cookie)[0]
        data = {"formhash": formhash, "qdxq": "kx", "qdmode": "1", "todaysay": "努力奋斗"}
        response = requests.post(
            url="https://www.oneplusbbs.com/plugin.php", headers=headers, params=params, data=data
        ).text
        msg = re.findall(r'<div class="c">(.*?)</div>', response, re.S)
        msg = msg[0].strip() if msg else "Cookie 可能过期"
        return msg

    @staticmethod
    def draw(cookie):
        headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.57",
            "X-Requested-With": "XMLHttpRequest",
            "Origin": "https://www.oneplusbbs.com",
            "Referer": "https://www.oneplusbbs.com/plugin-choujiang.html",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,fr;q=0.5,pl;q=0.4",
            "cookie": cookie,
        }
        params = (
            ("id", "choujiang"),
            ("do", "draw"),
        )
        sum_list = []
        success_count = 0
        error_count = 0
        for i in range(10):
            try:
                data = requests.post(url="https://www.oneplusbbs.com/plugin.php", headers=headers, params=params).json()
                if data["ret"] != "":
                    ret_map = {
                        "2": 18,
                        "4": 188,
                        "5": 88,
                        "7": 8,
                    }
                    ret = data["ret"]
                    sum_list.append(ret_map.get(ret, 0))
                    one_msg = data["msg"]
                    if str(ret) in ["-1", "-6", "-7"]:
                        break
                    else:
                        success_count += 1
                else:
                    error_count += 1
                    one_msg = "抽奖失败"
            except Exception as e:
                one_msg = f"抽奖失败: {e}"
                error_count += 1
            print(f"第{i + 1}次抽奖结果：" + str(one_msg))
            time.sleep(5)
        msg = f"成功抽奖 {success_count} 次"
        draw_msg = "抽奖状态: " + str(msg)
        draw_msg += f"\n抽奖结果: 获得 {sum(sum_list) - success_count * 10} 加油"
        print(draw_msg)
        return draw_msg

    def main(self):
        oneplusbbs_cookie = self.check_item.get("oneplusbbs_cookie")
        bbs_uname = re.findall(r"bbs_uname=(.*?);", oneplusbbs_cookie)
        bbs_uname = bbs_uname[0].split("%7C")[0] if bbs_uname else "未获取到用户信息"
        try:
            bbs_uname = parse.unquote(bbs_uname)
        except Exception as e:
            print(f"bbs_uname 转换失败: {e}")
            bbs_uname = bbs_uname
        sign_msg = self.sign(cookie=oneplusbbs_cookie)
        draw_msg = self.draw(cookie=oneplusbbs_cookie)
        msg = f"帐号信息: {bbs_uname}\n签到信息: {sign_msg}\n{draw_msg}"
        return msg


if __name__ == "__main__":
    with open(
        os.path.join(os.path.dirname(os.path.dirname(__file__)), "config/config.json"), "r", encoding="utf-8"
    ) as f:
        datas = json.loads(f.read())
    _check_item = datas.get("ONEPLUSBBS_COOKIE_LIST", [])[0]
    print(OnePlusBBSCheckIn(check_item=_check_item).main())
