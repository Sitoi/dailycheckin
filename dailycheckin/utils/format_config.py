# -*- coding: utf-8 -*-

name_map = {
    "IQIYI_COOKIE_LIST": "IQIYI",
    "VQQ_COOKIE_LIST": "VQQ",
    "MGTV_PARAMS_LIST": "MGTV",
    "KGQQ_COOKIE_LIST": "KGQQ",
    "MUSIC163_ACCOUNT_LIST": "MUSIC163",
    "BILIBILI_COOKIE_LIST": "BILIBILI",
    "YOUDAO_COOKIE_LIST": "YOUDAO",
    "FMAPP_ACCOUNT_LIST": "FMAPP",
    "BAIDU_URL_SUBMIT_LIST": "BAIDU",
    "ONEPLUSBBS_COOKIE_LIST": "ONEPLUSBBS",
    "SMZDM_COOKIE_LIST": "SMZDM",
    "TIEBA_COOKIE_LIST": "TIEBA",
    "V2EX_COOKIE_LIST": "V2EX",
    "WWW2NZZ_COOKIE_LIST": "WWW2NZZ",
    "ACFUN_ACCOUNT_LIST": "ACFUN",
    "MIMOTION_ACCOUNT_LIST": "MIMOTION",
    "CLOUD189_ACCOUNT_LIST": "CLOUD189",
    "POJIE_COOKIE_LIST": "POJIE",
    "MEIZU_COOKIE_LIST": "MEIZU",
    "PICACOMIC_ACCOUNT_LIST": "PICACOMIC",
    "ZHIYOO_COOKIE_LIST": "ZHIYOO",
    "WEIBO_COOKIE_LIST": "WEIBO",
    "DUOKAN_COOKIE_LIST": "DUOKAN",
    "CSDN_COOKIE_LIST": "CSDN",
    "WZYD_DATA_LIST": "WZYD",
    "WOMAIL_URL_LIST": "WOMAIL",
}

change_key_map = {
    "ACFUN_ACCOUNT_LIST": {"acfun_password": "password", "acfun_phone": "phone"},
    "BAIDU_URL_SUBMIT_LIST": {
        "data_url": "data_url",
        "submit_url": "submit_url",
        "times": "times",
    },
    "BILIBILI_COOKIE_LIST": {
        "bilibili_cookie": "cookie",
        "coin_num": "coin_num",
        "coin_type": "coin_type",
        "silver2coin": "silver2coin",
    },
    "CLOUD189_ACCOUNT_LIST": {
        "cloud189_password": "password",
        "cloud189_phone": "phone",
    },
    "CSDN_COOKIE_LIST": {"csdn_cookie": "cookie"},
    "DUOKAN_COOKIE_LIST": {"duokan_cookie": "cookie"},
    "FMAPP_ACCOUNT_LIST": {
        "fmapp_blackbox": "blackbox",
        "fmapp_cookie": "cookie",
        "fmapp_device_id": "device_id",
        "fmapp_fmversion": "fmversion",
        "fmapp_os": "os",
        "fmapp_token": "token",
        "fmapp_useragent": "useragent",
    },
    "HEYTAP": {"cookie": "cookie", "useragent": "useragent"},
    "IQIYI_COOKIE_LIST": {"iqiyi_cookie": "cookie"},
    "KGQQ_COOKIE_LIST": {"kgqq_cookie": "cookie"},
    "MEIZU_COOKIE_LIST": {"draw_count": "draw_count", "meizu_cookie": "cookie"},
    "MGTV_PARAMS_LIST": {"mgtv_params": "params"},
    "MIMOTION_ACCOUNT_LIST": {
        "mimotion_max_step": "max_step",
        "mimotion_min_step": "min_step",
        "mimotion_password": "password",
        "mimotion_phone": "phone",
    },
    "MUSIC163_ACCOUNT_LIST": {
        "music163_password": "password",
        "music163_phone": "phone",
    },
    "ONEPLUSBBS_COOKIE_LIST": {"oneplusbbs_cookie": "cookie"},
    "PICACOMIC_ACCOUNT_LIST": {
        "picacomic_email": "email",
        "picacomic_password": "password",
    },
    "POJIE_COOKIE_LIST": {"pojie_cookie": "cookie"},
    "SMZDM_COOKIE_LIST": {"smzdm_cookie": "cookie"},
    "TIEBA_COOKIE_LIST": {"tieba_cookie": "cookie"},
    "UNICOM": {"app_id": "app_id", "mobile": "mobile", "password": "password"},
    "V2EX_COOKIE_LIST": {"v2ex_cookie": "cookie", "v2ex_proxy": "proxy"},
    "VQQ_COOKIE_LIST": {"auth_refresh": "auth_refresh", "vqq_cookie": "cookie"},
    "WEIBO_COOKIE_LIST": {"weibo_show_url": "url"},
    "WOMAIL_URL_LIST": {"womail_url": "url"},
    "WWW2NZZ_COOKIE_LIST": {"www2nzz_cookie": "cookie"},
    "WZYD_DATA_LIST": {"wzyd_data": "data"},
    "YOUDAO_COOKIE_LIST": {"youdao_cookie": "cookie"},
    "ZHIYOO_COOKIE_LIST": {"zhiyoo_cookie": "cookie"},
}


def format_data(data):
    flag = False
    new_data = {}
    for key, value in data.items():
        if name_map.get(key):
            flag = True
            if isinstance(value, list):
                for one in value:
                    if isinstance(one, dict):
                        if name_map.get(key) not in new_data.keys():
                            new_data[name_map.get(key)] = []
                        for k2, v2 in change_key_map[key].items():
                            try:
                                one[v2] = one.pop(k2)
                            except Exception as e:
                                print(e)
                        new_data[name_map.get(key)].append(one)
            if not new_data.get(name_map.get(key)):
                new_data[name_map.get(key)] = value
        else:
            new_data[key] = value
    return flag, new_data
