import json
import os
import re

import requests
import urllib3

from dailycheckin import CheckIn

urllib3.disable_warnings()


class EnShan(CheckIn):
    name = "恩山无线论坛"

    def __init__(self, check_item):
        self.check_item = check_item

    @staticmethod
    def get_formhash_from_page(session):
        """GET 签到页面并提取 formhash Discuz 常见的 CSRF 字段"""
        response = session.get("https://www.right.com.cn/forum/forum.php", timeout=15)
        response.raise_for_status()
        html = response.text
        # 常见两种位置：隐藏 input name="formhash" value="..." 或 js var formhash = '...'
        m = re.search(r'name=["\']formhash["\']\s+value=["\']([0-9a-fA-F]+)["\']', html)
        if not m:
            m = re.search(r"formhash\s*[:=]\s*['\"]([0-9a-fA-F]+)['\"]", html)
        if not m:
            # 有时 formhash 包含非十六进制字符，放宽匹配
            m = re.search(r'name=["\']formhash["\']\s+value=["\']([^"\']+)["\']', html)

        if not m:
            raise RuntimeError("无法在页面中找到 formhash，请检查页面或手动查看 HTML")
        return m.group(1)

    @staticmethod
    def sign(session, form_hash):
        msg = []
        payload = {"formhash": form_hash}
        response = session.post(
            "https://www.right.com.cn/forum/plugin.php?id=erling_qd:action&action=sign", data=payload, timeout=15
        )
        try:
            data = response.json()
            if data.get("success"):
                continuous_days = data.get("continuous_days")
                msg = [
                    {
                        "name": "签到结果",
                        "value": data.get("message", "签到成功"),
                    },
                    {
                        "name": "连续签到",
                        "value": f"已连续签到{continuous_days}天",
                    },
                ]
            else:
                msg = [
                    {
                        "name": "签到结果",
                        "value": data.get("message", "签到失败"),
                    },
                ]
        except ValueError:
            msg = [
                {
                    "name": "签到结果",
                    "value": f"签到异常：{response.status_code}",
                }
            ]
            # print(f'status_code: {response.status_code}, text: {response.text[:2000]}')
        return msg

    @staticmethod
    def get_info(session):
        msg = []
        response = session.get("https://www.right.com.cn/FORUM/home.php?mod=spacecp&ac=credit&showcredit=1", timeout=15)
        response.raise_for_status()
        html = response.text
        try:
            coin = re.findall("恩山币: </em>(.*?)&nbsp;", html)[0]
            point = re.findall("<em>积分: </em>(.*?)<span", html)[0]
            msg = [
                {
                    "name": "恩山币",
                    "value": coin,
                },
                {
                    "name": "积分",
                    "value": point,
                },
            ]
        except Exception as e:
            msg = [
                {
                    "name": "获取代币失败",
                    "value": str(e),
                }
            ]
        return msg

    def main(self):
        cookie = self.check_item.get("cookie")
        session = requests.Session()
        session.headers.update(
            {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36",
                "Accept": "application/json, text/javascript, */*; q=0.01",
                "Referer": "https://www.right.com.cn/forum/",
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                "Cookie": cookie,
            }
        )
        form_hash = self.get_formhash_from_page(session=session)
        msg = self.sign(session=session, form_hash=form_hash)
        msg += self.get_info(session=session)
        msg = "\n".join([f"{one.get('name')}: {one.get('value')}" for one in msg])
        return msg


if __name__ == "__main__":
    with open(
        os.path.join(os.path.dirname(os.path.dirname(__file__)), "config.json"),
        encoding="utf-8",
    ) as f:
        datas = json.loads(f.read())
    _check_item = datas.get("ENSHAN", [])[0]
    print(EnShan(check_item=_check_item).main())
