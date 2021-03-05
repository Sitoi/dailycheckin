# -*- coding: utf-8 -*-
import json
import os
from datetime import datetime

import requests


class Weather:
    def __init__(self, check_item):
        self.check_item = check_item

    def main(self):
        """
        获取天气信息。网址：https://www.sojson.com/blog/305.html
        :return:
        """
        with open(os.path.join(os.path.dirname(__file__), "city.json"), "r", encoding="utf-8") as city_file:
            city_map = json.loads(city_file.read())
        city_code = city_map.get(self.check_item, "101020100")
        weather_url = f"http://t.weather.itboy.net/api/weather/city/{city_code}"
        today_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        resp = requests.get(url=weather_url)
        if resp.status_code == 200 and resp.json().get("status") == 200:
            weather_json = resp.json()
            today_weather = weather_json.get("data").get("forecast")[1]
            notice = today_weather.get("notice")
            high = today_weather.get("high")
            low = today_weather.get("low")
            temperature = f"温度: {low[low.find(' ') + 1:]}/{high[high.find(' ') + 1:]}"
            wind = f"{today_weather.get('fx')}: {today_weather.get('fl')}"
            aqi = f"空气: {today_weather.get('aqi')}"
            msg = f"城市: {self.check_item}\n时间: {today_time}\n{notice}\n{temperature}\n{wind}\n{aqi}\n"
        else:
            msg = f"城市: {self.check_item}\n时间: {today_time}天气情况: 获取失败"
        return msg


if __name__ == "__main__":
    with open(
        os.path.join(os.path.dirname(os.path.dirname(__file__)), "config/config.json"), "r", encoding="utf-8"
    ) as f:
        datas = json.loads(f.read())
    _check_item = datas.get("CITY_NAME_LIST")[0]
    print(Weather(check_item=_check_item).main())
