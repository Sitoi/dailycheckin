import json
import os
import re

import requests
import urllib3

from dailycheckin import CheckIn

urllib3.disable_warnings()


class AcFun(CheckIn):
    name = "AcFun"

    def __init__(self, check_item: dict):
        self.check_item = check_item
        self.contentid = "27259341"
        self.st = None

    @staticmethod
    def login(phone, password, session):
        url = "https://id.app.acfun.cn/rest/web/login/signin"
        body = f"username={phone}&password={password}&key=&captcha="
        res = session.post(url=url, data=body).json()
        return (True, res) if res.get("result") == 0 else (False, res.get("err_msg"))

    @staticmethod
    def get_cookies(session, phone, password):
        url = "https://id.app.acfun.cn/rest/app/login/signin"
        headers = {
            "Host": "id.app.acfun.cn",
            "user-agent": "AcFun/6.39.0 (iPhone; iOS 14.3; Scale/2.00)",
            "devicetype": "0",
            "accept-language": "zh-Hans-CN;q=1, en-CN;q=0.9, ja-CN;q=0.8, zh-Hant-HK;q=0.7, io-Latn-CN;q=0.6",
            "accept": "application/json",
            "content-type": "application/x-www-form-urlencoded",
        }
        data = f"password={password}&username={phone}"
        response = session.post(url=url, data=data, headers=headers, verify=False)
        acpasstoken = response.json().get("acPassToken")
        auth_key = str(response.json().get("auth_key"))
        if acpasstoken and auth_key:
            cookies = {"acPasstoken": acpasstoken, "auth_key": auth_key}
            return cookies
        else:
            return False

    def get_token(self, session):
        url = "https://id.app.acfun.cn/rest/web/token/get?sid=acfun.midground.api"
        res = session.post(url=url).json()
        self.st = res.get("acfun.midground.api_st") if res.get("result") == 0 else ""
        return self.st

    def get_video(self, session):
        url = "https://www.acfun.cn/rest/pc-direct/rank/channel"
        res = session.get(url=url).json()
        self.contentid = res.get("rankList")[0].get("contentId")
        return self.contentid

    @staticmethod
    def sign(session):
        url = "https://www.acfun.cn/rest/pc-direct/user/signIn"
        response = session.post(url=url)
        return {"name": "签到信息", "value": response.json().get("msg")}

    def danmu(self, session):
        url = "https://www.acfun.cn/rest/pc-direct/new-danmaku/add"
        data = {
            "mode": "1",
            "color": "16777215",
            "size": "25",
            "body": "123321",
            "videoId": "26113662",
            "position": "2719",
            "type": "douga",
            "id": "31224739",
            "subChannelId": "1",
            "subChannelName": "动画",
        }
        response = session.get(url=f"https://www.acfun.cn/v/ac{self.contentid}")
        videoId = re.findall(r'"currentVideoId":(\d+),', response.text)
        subChannel = re.findall(
            r'{subChannelId:(\d+),subChannelName:"([\u4e00-\u9fa5]+)"}', response.text
        )
        if videoId:
            data["videoId"] = videoId[0]
            data["subChannelId"] = subChannel[0][0]
            data["subChannelName"] = subChannel[0][1]
        res = session.post(url=url, data=data).json()
        msg = "弹幕成功" if res.get("result") == 0 else "弹幕失败"
        return {"name": "弹幕任务", "value": msg}

    def throwbanana(self, session):
        url = "https://www.acfun.cn/rest/pc-direct/banana/throwBanana"
        data = {"resourceId": self.contentid, "count": "1", "resourceType": "2"}
        res = session.post(url=url, data=data).json()
        msg = "投🍌成功" if res.get("result") == 0 else "投🍌失败"
        return {"name": "香蕉任务", "value": msg}

    def like(self, session):
        like_url = "https://kuaishouzt.com/rest/zt/interact/add"
        unlike_url = "https://kuaishouzt.com/rest/zt/interact/delete"
        body = (
            f"kpn=ACFUN_APP&kpf=PC_WEB&subBiz=mainApp&interactType=1&"
            f"objectType=2&objectId={self.contentid}&acfun.midground.api_st={self.st}&"
            f"extParams%5BisPlaying%5D=false&extParams%5BshowCount%5D=1&extParams%5B"
            f"otherBtnClickedCount%5D=10&extParams%5BplayBtnClickedCount%5D=0"
        )
        res = session.post(url=like_url, data=body).json()
        session.post(url=unlike_url, data=body)
        msg = "点赞成功" if res.get("result") == 1 else "点赞失败"
        return {"name": "点赞任务", "value": msg}

    def share(self, session, cookies):
        url = "https://api-ipv6.acfunchina.com/rest/app/task/reportTaskAction?taskType=1&market=tencent&product=ACFUN_APP&appMode=0"
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
        }
        response = session.get(url=url, headers=headers, cookies=cookies, verify=False)
        if response.json().get("result") == 0:
            msg = "分享成功"
        else:
            msg = "分享失败"
        return {"name": "分享任务", "value": msg}

    @staticmethod
    def get_info(session):
        url = "https://www.acfun.cn/rest/pc-direct/user/personalInfo"
        res = session.get(url=url).json()
        if res.get("result") != 0:
            return [{"name": "当前等级", "value": "查询失败"}]
        info = res.get("info")
        return [
            {"name": "当前等级", "value": info.get("level")},
            {"name": "持有香蕉", "value": info.get("banana")},
        ]

    def main(self):
        phone = self.check_item.get("phone")
        password = self.check_item.get("password")
        session = requests.session()
        session.headers.update(
            {
                "accept": "*/*",
                "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
                "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.70",
                "Referer": "https://www.acfun.cn/",
            }
        )
        flag, res = self.login(phone, password, session)
        if flag is True:
            self.get_video(session=session)
            self.get_token(session=session)
            sign_msg = self.sign(session=session)
            like_msg = self.like(session=session)
            danmu_msg = self.danmu(session=session)
            throwbanana_msg = self.throwbanana(session=session)
            info_msg = self.get_info(session=session)
            msg = [
                {"name": "帐号信息", "value": phone},
                sign_msg,
                like_msg,
                danmu_msg,
                throwbanana_msg,
            ] + info_msg
        else:
            msg = [
                {"name": "帐号信息", "value": phone},
                {"name": "错误信息", "value": res},
            ]
        msg = "\n".join([f"{one.get('name')}: {one.get('value')}" for one in msg])
        return msg


if __name__ == "__main__":
    with open(
        os.path.join(os.path.dirname(os.path.dirname(__file__)), "config.json"),
        encoding="utf-8",
    ) as f:
        datas = json.loads(f.read())
    _check_item = datas.get("ACFUN", [])[0]
    print(AcFun(check_item=_check_item).main())
