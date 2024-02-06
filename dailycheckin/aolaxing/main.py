import json
import os
import time

import requests

from dailycheckin import CheckIn


class AoLaXing(CheckIn):
    name = "奥拉星"

    def __init__(self, check_item: dict):
        self.check_item = check_item

    def user(self, headers):
        url = "http://service.100bt.com/creditmall/my/user_info.jsonp"
        user_json = requests.get(url, headers=headers).json()
        user_data = user_json["jsonResult"]["data"]
        try:
            credit = user_data["credit"]
            creditHistory = user_data["creditHistory"]
            phoneNum = user_data["phoneNum"]
            signInTotal = user_data["signInTotal"]
        except Exception as e:
            return [{"name": "签到", "value": str(e)}]
        msgs = [
            {"name": "用户", "value": phoneNum},
            {"name": "当前积分", "value": credit},
            {"name": "总共获得积分", "value": creditHistory},
            {"name": "总签到", "value": signInTotal},
        ]
        return msgs

    def practise(self, headers, task_id):
        url = f"http://service.100bt.com/creditmall/activity/do_task.jsonp?taskId={task_id}&gameId=2&_=1643440166690"
        task_json = requests.get(url, headers=headers).json()
        try:
            message = task_json["jsonResult"]["message"]
        except:
            message = "NO"
        return message

    def task(self, headers, msg: bool = False):
        url = "http://service.100bt.com/creditmall/activity/daily_task_list.jsonp?gameId=2&_=1643437206026"
        task_json = requests.get(url, headers=headers).json()
        task_data = task_json["jsonResult"]["data"]
        task_finish_count = 0
        for task_item in task_data:
            name = task_item["name"]
            status_desc = task_item["status_desc"]
            task_id = task_item["taskID"]
            if msg:
                if status_desc == "已完成":
                    task_finish_count += 1
            else:
                if status_desc == "未完成":
                    print(f"开始任务：{name}")
                    res = self.practise(task_id=task_id, headers=headers)
                    print(f"返回状态：{res}")
                    time.sleep(2.5)
        msgs = [
            {"name": "今日任务总数", "value": len(task_data)},
            {"name": "今日任务完成数", "value": task_finish_count},
        ]
        return msgs

    def main(self):
        cookie = self.check_item.get("cookie")
        headers = {
            "Host": "service.100bt.com",
            "Proxy-Connection": "keep-alive",
            "Accept": "*/*",
            "Referer": "http://www.100bt.com/",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cookie": cookie,
        }
        _ = self.task(headers)
        task_msgs = self.task(headers=headers, msg=True)
        user_msgs = self.user(headers=headers)
        msgs = task_msgs + user_msgs
        msg = "\n".join([f"{one.get('name')}: {one.get('value')}" for one in msgs])
        return msg


if __name__ == "__main__":
    with open(
        os.path.join(os.path.dirname(os.path.dirname(__file__)), "config.json"),
        encoding="utf-8",
    ) as f:
        datas = json.loads(f.read())
    _check_item = datas.get("AOLAXING", [])[0]
    print(AoLaXing(check_item=_check_item).main())
