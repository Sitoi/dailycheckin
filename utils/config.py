# -*- coding: utf-8 -*-
import json
import os
from baidu_url_submit import BaiduUrlSubmit
from bilibili import BiliBiliCheckIn
from fmapp import FMAPPCheckIn
from iqiyi import IQIYICheckIn
from kgqq import KGQQCheckIn
from liantong import LianTongCheckIn
from music163 import Music163CheckIn
from oneplusbbs import OnePlusBBSCheckIn
from smzdm import SmzdmCheckIn
from tieba import TiebaCheckIn
from v2ex import V2exCheckIn
from vqq import VQQCheckIn
from weather import Weather
from www2nzz import WWW2nzzCheckIn
from youdao import YouDaoCheckIn

checkin_map = {
    "IQIYI_COOKIE_LIST": IQIYICheckIn,
    "VQQ_COOKIE_LIST": VQQCheckIn,
    "KGQQ_COOKIE_LIST": KGQQCheckIn,
    "MUSIC163_ACCOUNT_LIST": Music163CheckIn,
    "BILIBILI_COOKIE_LIST": BiliBiliCheckIn,
    "YOUDAO_COOKIE_LIST": YouDaoCheckIn,
    "FMAPP_ACCOUNT_LIST": FMAPPCheckIn,
    "BAIDU_URL_SUBMIT_LIST": BaiduUrlSubmit,
    "LIANTONG_ACCOUNT_LIST": LianTongCheckIn,
    "ONEPLUSBBS_COOKIE_LIST": OnePlusBBSCheckIn,
    "SMZDM_COOKIE_LIST": SmzdmCheckIn,
    "TIEBA_COOKIE_LIST": TiebaCheckIn,
    "V2EX_COOKIE_LIST": V2exCheckIn,
    "WWW2NZZ_COOKIE_LIST": WWW2nzzCheckIn,
    "CITY_NAME_LIST": Weather,
}


def env2json(key):
    value = json.loads(os.getenv(key, [])) if os.getenv(key) else []
    return value


def get_checkin_info(data):
    result = {}
    if isinstance(data, dict):
        for one in checkin_map.keys():
            result[one.lower()] = data.get(one, [])
    else:
        for one in checkin_map.keys():
            result[one.lower()] = env2json(one)
    return result
