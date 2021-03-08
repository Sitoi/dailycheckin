# -*- coding: utf-8 -*-
import json
import os

from acfun import AcFunCheckIn
from baidu_url_submit import BaiduUrlSubmit
from bilibili import BiliBiliCheckIn
from caiyun import CaiYunCheckIn
from cloud189 import Cloud189CheckIn
from fmapp import FMAPPCheckIn
from iqiyi import IQIYICheckIn
from kgqq import KGQQCheckIn
from liantong import LianTongCheckIn
from meizu import MeizuCheckIn
from mgtv import MgtvCheckIn
from mimotion import MiMotion
from music163 import Music163CheckIn
from oneplusbbs import OnePlusBBSCheckIn
from picacomic import PicacomicCheckIn
from pojie import PojieCheckIn
from smzdm import SmzdmCheckIn
from tieba import TiebaCheckIn
from v2ex import V2exCheckIn
from vqq import VQQCheckIn
from weather import Weather
from wps import WPSCheckIn
from www2nzz import WWW2nzzCheckIn
from xmly import XMLYCheckIn
from youdao import YouDaoCheckIn

checkin_map = {
    "IQIYI_COOKIE_LIST": ("爱奇艺", IQIYICheckIn),
    "VQQ_COOKIE_LIST": ("腾讯视频", VQQCheckIn),
    "MGTV_PARAMS_LIST": ("芒果TV", MgtvCheckIn),
    "KGQQ_COOKIE_LIST": ("全民K歌", KGQQCheckIn),
    "MUSIC163_ACCOUNT_LIST": ("网易云音乐", Music163CheckIn),
    "BILIBILI_COOKIE_LIST": ("Bilibili", BiliBiliCheckIn),
    "YOUDAO_COOKIE_LIST": ("有道云笔记", YouDaoCheckIn),
    "FMAPP_ACCOUNT_LIST": ("Fa米家 APP", FMAPPCheckIn),
    "BAIDU_URL_SUBMIT_LIST": ("百度站点提交", BaiduUrlSubmit),
    "LIANTONG_ACCOUNT_LIST": ("联通营业厅", LianTongCheckIn),
    "ONEPLUSBBS_COOKIE_LIST": ("一加手机社区官方论坛", OnePlusBBSCheckIn),
    "SMZDM_COOKIE_LIST": ("什么值得买", SmzdmCheckIn),
    "TIEBA_COOKIE_LIST": ("百度贴吧", TiebaCheckIn),
    "V2EX_COOKIE_LIST": ("V2EX 论坛", V2exCheckIn),
    "WWW2NZZ_COOKIE_LIST": ("咔叽网单", WWW2nzzCheckIn),
    "ACFUN_ACCOUNT_LIST": ("AcFun", AcFunCheckIn),
    "MIMOTION_ACCOUNT_LIST": ("小米运动", MiMotion),
    "CLOUD189_ACCOUNT_LIST": ("天翼云盘", Cloud189CheckIn),
    "WPS_COOKIE_LIST": ("WPS", WPSCheckIn),
    "POJIE_COOKIE_LIST": ("吾爱破解", PojieCheckIn),
    "MEIZU_COOKIE_LIST": ("MEIZU社区", MeizuCheckIn),
    "PICACOMIC_ACCOUNT_LIST": ("哔咔漫画", PicacomicCheckIn),
    "CAIYUN_COOKIE_LIST": ("和彩云", CaiYunCheckIn),
    "CITY_NAME_LIST": ("天气预报", Weather),
    "XMLY_COOKIE_LIST": ("喜马拉雅极速版", XMLYCheckIn),
}

notice_map = {
    "DINGTALK_SECRET": "",
    "DINGTALK_ACCESS_TOKEN": "",
    "BARK_URL": "",
    "SCKEY": "",
    "SENDKEY": "",
    "TG_BOT_TOKEN": "",
    "TG_USER_ID": "",
    "QMSG_KEY": "",
    "COOLPUSHSKEY": "",
    "COOLPUSHQQ": "",
    "COOLPUSHWX": "",
    "COOLPUSHEMAIL": "",
    "QYWX_KEY": "",
    "QYWX_CORPID": "",
    "QYWX_AGENTID": "",
    "QYWX_CORPSECRET": "",
    "QYWX_TOUSER": "",
}


def env2list(key):
    try:
        value = json.loads(os.getenv(key, []).strip()) if os.getenv(key) else []
        if isinstance(value, list):
            value = value
        else:
            value = []
    except Exception as e:
        print(e)
        value = []
    return value


def env2str(key):
    try:
        value = os.getenv(key, "") if os.getenv(key) else ""
        if isinstance(value, str):
            value = value.strip()
        else:
            value = None
    except Exception as e:
        print(e)
        value = None
    return value


def get_checkin_info(data):
    result = {}
    if isinstance(data, dict):
        for one in checkin_map.keys():
            result[one.lower()] = data.get(one, [])
    else:
        for one in checkin_map.keys():
            result[one.lower()] = env2list(one)
    return result


def get_notice_info(data):
    result = {}
    if isinstance(data, dict):
        for one in notice_map.keys():
            result[one.lower()] = data.get(one, None)
    else:
        for one in notice_map.keys():
            result[one.lower()] = env2str(one)
    return result
