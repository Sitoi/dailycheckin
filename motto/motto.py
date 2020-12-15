# -*- coding: utf-8 -*-
import json
import os

import requests


class Motto:
    @staticmethod
    def main():
        """
        从词霸中获取每日一句，带英文。
        :return:
        """
        resp = requests.get(url="http://open.iciba.com/dsapi")
        if resp.status_code == 200:
            content_json = resp.json()
            content = content_json.get("content")
            note = content_json.get("note")
            msg = [f"{content}\n{note}\n"]
        else:
            msg = []
        print(msg)
        return msg


if __name__ == "__main__":
    with open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "config.json"), "r", encoding="utf-8") as f:
        datas = json.loads(f.read())
    motto = datas.get("MOTTO")
    if motto:
        Motto().main()
