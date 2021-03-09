# GitHub Actions 使用教程

## 一、fork 本项目

项目地址: [https://github.com/Sitoi/dailycheckin](https://github.com/Sitoi/dailycheckin)

## 二、配置项目 Secrets

### 逐一配置

> ⚠️ ️_**斜体加粗大写英文字母**_ 表示 GitHub Actions Secrets 环境变量名称，内容直接复制 _**斜体加粗大写英文字母 key**_  对应的 value

参考[配置说明文档](https://sitoi.github.io/dailycheckin/settings/) ，`GitHub Actions Secrets` 环境变量

![Secret 教程](https://cdn.jsdelivr.net/gh/Sitoi/dailycheckin/docs/img/secret.png)

Secrets 填写教程，以 IQIYI_COOKIE_LIST 为例:

- name: 斜体加粗大写英文字母

```text
IQIYI_COOKIE_LIST
```

- value: 斜体加粗大写英文字母 对应的 value 是什么类型就填写什么类型，建议去 [http://www.json.cn](http://www.json.cn) 进行校验。

```json
[
  {
    "iqiyi_cookie": "QC005=xxxx; QC142=xxxx; T00404=xxxx; QC006=xxxx; __uuid=xxxx; QC173=0; P00004=xxxx; P00003=xxxx; P00010=xxxx; P01010=xxxx; P00PRU=xxxx"
  }
]
```

### 配置整个 config.json

> 如果同时配置了逐个配置，会自动合并到 CONFIG_JSON 配置中，如果全部使用 CONFIG_JSON 请删除其他的 Secrets 配置。

- name: 斜体加粗大写英文字母

```text
CONFIG_JSON
```

- value: 斜体加粗大写英文字母 对应的 value 是什么类型就填写什么类型，建议去 [http://www.json.cn](http://www.json.cn) 进行校验。

```json
{
  "DINGTALK_SECRET": "",
  "DINGTALK_ACCESS_TOKEN": "",
  "SCKEY": "",
  "SENDKEY": "",
  "BARK_URL": "",
  "QMSG_KEY": "",
  "TG_BOT_TOKEN": "",
  "TG_USER_ID": "",
  "COOLPUSHSKEY": "",
  "COOLPUSHQQ": true,
  "COOLPUSHWX": true,
  "COOLPUSHEMAIL": true,
  "QYWX_KEY": "",
  "QYWX_CORPID": "",
  "QYWX_AGENTID": "",
  "QYWX_CORPSECRET": "",
  "QYWX_TOUSER": "",
  "PUSHPLUS_TOKEN": "",
  "PUSHPLUS_TOPIC": "",
  "CITY_NAME_LIST": [
    "上海"
  ],
  "MOTTO": true,
  "IQIYI_COOKIE_LIST": [
    {
      "iqiyi_cookie": "__dfp=xxxxxx; QP0013=xxxxxx; QP0022=xxxxxx; QYABEX=xxxxxx; P00001=xxxxxx; P00002=xxxxxx; P00003=xxxxxx; P00007=xxxxxx; QC163=xxxxxx; QC175=xxxxxx; QC179=xxxxxx; QC170=xxxxxx; P00010=xxxxxx; P00PRU=xxxxxx; P01010=xxxxxx; QC173=xxxxxx; QC180=xxxxxx; P00004=xxxxxx; QP0030=xxxxxx; QC006=xxxxxx; QC007=xxxxxx; QC008=xxxxxx; QC010=xxxxxx; nu=xxxxxx; __uuid=xxxxxx; QC005=xxxxxx;"
    },
    {
      "iqiyi_cookie": "多账号 cookie 填写，请参考上面，cookie 以实际获取为准（遇到特殊字符如双引号\" 请加反斜杠转义）"
    }
  ],
  "VQQ_COOKIE_LIST": [
    {
      "auth_refresh": "https://access.video.qq.com/user/auth_refresh?vappid=xxxxxx&vsecret=xxxxxx&type=qq&g_tk=&g_vstk=xxxxxx&g_actk=xxxxxx&callback=xxxxxx&_=xxxxxx",
      "vqq_cookie": "pgv_pvid=xxxxxx; pac_uid=xxxxxx; RK=xxxxxx; ptcz=xxxxxx; tvfe_boss_uuid=xxxxxx; video_guid=xxxxxx; video_platform=xxxxxx; pgv_info=xxxxxx; main_login=xxxxxx; vqq_access_token=xxxxxx; vqq_appid=xxxxxx; vqq_openid=xxxxxx; vqq_vuserid=xxxxxx; vqq_refresh_token=xxxxxx; login_time_init=xxxxxx; uid=xxxxxx; vqq_vusession=xxxxxx; vqq_next_refresh_time=xxxxxx; vqq_login_time_init=xxxxxx; login_time_last=xxxxxx;"
    },
    {
      "auth_refresh": "多账号 refresh url，请参考上面，以实际获取为准",
      "vqq_cookie": "多账号 cookie 填写，请参考上面，cookie 以实际获取为准（遇到特殊字符如双引号\" 请加反斜杠转义）"
    }
  ],
  "YOUDAO_COOKIE_LIST": [
    {
      "youdao_cookie": "JSESSIONID=xxxxxx; __yadk_uid=xxxxxx; OUTFOX_SEARCH_USER_ID_NCOO=xxxxxx; YNOTE_SESS=xxxxxx; YNOTE_PERS=xxxxxx; YNOTE_LOGIN=xxxxxx; YNOTE_CSTK=xxxxxx; _ga=xxxxxx; _gid=xxxxxx; _gat=xxxxxx; PUBLIC_SHARE_18a9dde3de846b6a69e24431764270c4=xxxxxx;"
    },
    {
      "youdao_cookie": "多账号 cookie 填写，请参考上面，cookie 以实际获取为准（遇到特殊字符如双引号\" 请加反斜杠转义）"
    }
  ],
  "KGQQ_COOKIE_LIST": [
    {
      "kgqq_cookie": "muid=xxxxxx; uid=xxxxxx; userlevel=xxxxxx; openid=xxxxxx; openkey=xxxxxx; opentype=xxxxxx; qrsig=xxxxxx; pgv_pvid=xxxxxx;"
    },
    {
      "kgqq_cookie": "多账号 cookie 填写，请参考上面，cookie 以实际获取为准（遇到特殊字符如双引号\" 请加反斜杠转义）"
    }
  ],
  "MUSIC163_ACCOUNT_LIST": [
    {
      "music163_phone": "18888xxxxxx",
      "music163_password": "Sitoi"
    },
    {
      "music163_phone": "多账号 手机号",
      "music163_password": "多账号 密码"
    }
  ],
  "XMLY_COOKIE_LIST": [
    {
      "xmly_cookie": "1&_device=xxxxxx; 1&_token=xxxxxx; NSUP=xxxxxx; XUM=xxxxxx; ainr=xxxxxx; c-oper=xxxxxx; channel=xxxxxx; device_model=xxxxxx; idfa=xxxxxx; impl=xxxxxx; ip=xxxxxx; net-mode=xxxxxx; res=xxxxxx; _xmLog=xxxxxx;"
    },
    {
      "xmly_cookie": "多账号 cookie 填写，请参考上面，cookie 以实际获取为准（遇到特殊字符如双引号\" 请加反斜杠转义）"
    }
  ],
  "ONEPLUSBBS_COOKIE_LIST": [
    {
      "oneplusbbs_cookie": "acw_tc=xxxxxx; qKc3_0e8d_saltkey=xxxxxx; qKc3_0e8d_lastvisit=xxxxxx; bbs_avatar=xxxxxx; qKc3_0e8d_sendmail=xxxxxx; opcid=xxxxxx; opcct=xxxxxx; oppt=xxxxxx; opsid=xxxxxx; opsct=xxxxxx; opbct=xxxxxx; UM_distinctid=xxxxxx; CNZZDATA1277373783=xxxxxx; www_clear=xxxxxx; ONEPLUSID=xxxxxx; qKc3_0e8d_sid=xxxxxx; bbs_uid=xxxxxx; bbs_uname=xxxxxx; bbs_grouptitle=xxxxxx; opuserid=xxxxxx; bbs_sign=xxxxxx; bbs_formhash=xxxxxx; qKc3_0e8d_ulastactivity=xxxxxx; opsertime=xxxxxx; qKc3_0e8d_lastact=xxxxxx; qKc3_0e8d_checkpm=xxxxxx; qKc3_0e8d_noticeTitle=xxxxxx; optime_browser=xxxxxx; opnt=xxxxxx; opstep=xxxxxx; opstep_event=xxxxxx; fp=xxxxxx;"
    },
    {
      "oneplusbbs_cookie": "多账号 cookie 填写，请参考上面，cookie 以实际获取为准（遇到特殊字符如双引号\" 请加反斜杠转义）"
    }
  ],
  "BAIDU_URL_SUBMIT_LIST": [
    {
      "data_url": "https://cdn.jsdelivr.net/gh/Sitoi/Sitoi.github.io/baidu_urls.txt",
      "submit_url": "http://data.zz.baidu.com/urls?site=https://sitoi.cn&token=xxxxxx",
      "times": 10
    },
    {
      "data_url": "多账号 data_url 链接地址，以实际获取为准",
      "submit_url": "多账号 submit_url 链接地址，以实际获取为准",
      "times": 10
    }
  ],
  "FMAPP_ACCOUNT_LIST": [
    {
      "fmapp_token": "xxxxxx.xxxxxx-xxxxxx-xxxxxx.xxxxxx-xxxxxx",
      "fmapp_cookie": "sensorsdata2015jssdkcross=xxxxxx",
      "fmapp_device_id": "xxxxxx-xxxx-xxxx-xxxx-xxxxxx"
    },
    {
      "fmapp_token": "多账号 token 填写，请参考上面，以实际获取为准",
      "fmapp_cookie": "多账号 cookie 填写，请参考上面，cookie 以实际获取为准（遇到特殊字符如双引号\" 请加反斜杠转义）",
      "fmapp_device_id": "多账号 device_id 填写，请参考上面，以实际获取为准"
    }
  ],
  "TIEBA_COOKIE_LIST": [
    {
      "tieba_cookie": "BIDUPSID=xxxxxx; PSTM=xxxxxx; BAIDUID=xxxxxx; BAIDUID_BFESS=xxxxxx; delPer=xxxxxx; PSINO=xxxxxx; H_PS_PSSID=xxxxxx; BA_HECTOR=xxxxxx; BDORZ=xxxxxx; TIEBA_USERTYPE=xxxxxx; st_key_id=xxxxxx; BDUSS=xxxxxx; BDUSS_BFESS=xxxxxx; STOKEN=xxxxxx; TIEBAUID=xxxxxx; ab_sr=xxxxxx; st_data=xxxxxx; st_sign=xxxxxx;"
    },
    {
      "tieba_cookie": "多账号 cookie 填写，请参考上面，cookie 以实际获取为准（遇到特殊字符如双引号\" 请加反斜杠转义）"
    }
  ],
  "BILIBILI_COOKIE_LIST": [
    {
      "bilibili_cookie": "_uuid=xxxxxx; rpdid=xxxxxx; LIVE_BUVID=xxxxxx; PVID=xxxxxx; blackside_state=xxxxxx; CURRENT_FNVAL=xxxxxx; buvid3=xxxxxx; fingerprint3=xxxxxx; fingerprint=xxxxxx; buivd_fp=xxxxxx; buvid_fp_plain=xxxxxx; DedeUserID=xxxxxx; DedeUserID__ckMd5=xxxxxx; SESSDATA=xxxxxx; bili_jct=xxxxxx; bsource=xxxxxx; finger=xxxxxx; fingerprint_s=xxxxxx;",
      "coin_num": 0,
      "coin_type": 1,
      "silver2coin": true
    },
    {
      "bilibili_cookie": "多账号 cookie 填写，请参考上面，cookie 以实际获取为准（遇到特殊字符如双引号\" 请加反斜杠转义）",
      "coin_num": 0,
      "coin_type": 1,
      "silver2coin": true
    }
  ],
  "LIANTONG_ACCOUNT_LIST": [
    {
      "data": "simCount=1&version=xxxxxx@8.0100&mobile=xxxxxx&netWay=wifi&isRemberPwd=false&appId=xxxxxx&deviceId=xxxxxx&pip=xxxxxx&password=xxxxxx&deviceOS=14.3&deviceBrand=iphone&deviceModel=iPhone&remark4=&keyVersion=2&deviceCode=xxxxxx"
    },
    {
      "data": "多账号 请求 中的参数信息填写，请参考上面，以实际获取为准"
    }
  ],
  "V2EX_COOKIE_LIST": [
    {
      "v2ex_cookie": "_ga=xxxxxx; __cfduid=xxxxxx; PB3_SESSION=xxxxxx; A2=xxxxxx; V2EXSETTINGS=xxxxxx; V2EX_REFERRER=xxxxxx; V2EX_LANG=xxxxxx; _gid=xxxxxx; V2EX_TAB=xxxxxx;"
    },
    {
      "v2ex_cookie": "多账号 cookie 填写，请参考上面，cookie 以实际获取为准（遇到特殊字符如双引号\" 请加反斜杠转义）"
    }
  ],
  "WWW2NZZ_COOKIE_LIST": [
    {
      "www2nzz_cookie": "YPx9_2132_saltkey=xxxxxx; YPx9_2132_lastvisit=xxxxxx; YPx9_2132_sendmail=xxxxxx; YPx9_2132_con_request_uri=xxxxxx; YPx9_2132_sid=xxxxxx; YPx9_2132_client_created=xxxxxx; YPx9_2132_client_token=xxxxxx; YPx9_2132_ulastactivity=xxxxxx; YPx9_2132_auth=xxxxxx; YPx9_2132_connect_login=xxxxxx; YPx9_2132_connect_is_bind=xxxxxx; YPx9_2132_connect_uin=xxxxxx; YPx9_2132_stats_qc_login=xxxxxx; YPx9_2132_checkpm=xxxxxx; YPx9_2132_noticeTitle=xxxxxx; YPx9_2132_nofavfid=xxxxxx; YPx9_2132_lastact=xxxxxx;"
    },
    {
      "www2nzz_cookie": "多账号 cookie 填写，请参考上面，cookie 以实际获取为准（遇到特殊字符如双引号\" 请加反斜杠转义）"
    }
  ],
  "SMZDM_COOKIE_LIST": [
    {
      "smzdm_cookie": "__jsluid_s=xxxxxx; __ckguid=xxxxxx; device_id=xxxxxx; homepage_sug=xxxxxx; r_sort_type=xxxxxx; _zdmA.vid=xxxxxx; sajssdk_2015_cross_new_user=xxxxxx; sensorsdata2015jssdkcross=xxxxxx; footer_floating_layer=xxxxxx; ad_date=xxxxxx; ad_json_feed=xxxxxx; zdm_qd=xxxxxx; sess=xxxxxx; user=xxxxxx; _zdmA.uid=xxxxxx; smzdm_id=xxxxxx; userId=xxxxxx; bannerCounter=xxxxxx; _zdmA.time=xxxxxx;"
    },
    {
      "smzdm_cookie": "多账号 cookie 填写，请参考上面，cookie 以实际获取为准（遇到特殊字符如双引号\" 请加反斜杠转义）"
    }
  ],
  "MIMOTION_ACCOUNT_LIST": [
    {
      "mimotion_phone": "18888xxxxxx",
      "mimotion_password": "Sitoi",
      "mimotion_min_step": "10000",
      "mimotion_max_step": "20000"
    },
    {
      "mimotion_phone": "多账号 手机号填写，请参考上面",
      "mimotion_password": "多账号 密码填写，请参考上面",
      "mimotion_min_step": "多账号 最小步数填写，请参考上面",
      "mimotion_max_step": "多账号 最大步数填写，请参考上面"
    }
  ],
  "ACFUN_ACCOUNT_LIST": [
    {
      "acfun_phone": "18888xxxxxx",
      "acfun_password": "Sitoi"
    },
    {
      "acfun_phone": "多账号 手机号填写，请参考上面",
      "acfun_password": "多账号 密码填写，请参考上面"
    }
  ],
  "CLOUD189_ACCOUNT_LIST": [
    {
      "cloud189_phone": "18888xxxxxx",
      "cloud189_password": "Sitoi"
    },
    {
      "cloud189_phone": "多账号 手机号填写，请参考上面",
      "cloud189_password": "多账号 密码填写，请参考上面"
    }
  ],
  "WPS_COOKIE_LIST": [
    {
      "wps_cookie": "csrf=xxxxxx; wpsqing_autoLoginV1=xxxxxx; wps_sid=xxxxxx; uzone=xxxxxx; ulocale=xxxxxx; XSRF-TOKEN=xxxxxx; _session=xxxxxx; logined=xxxxxx;"
    },
    {
      "wps_cookie": "多账号 cookie 填写，请参考上面，cookie 以实际获取为准（遇到特殊字符如双引号\" 请加反斜杠转义）"
    }
  ],
  "POJIE_COOKIE_LIST": [
    {
      "pojie_cookie": "htVD_2132_client_token=xxxxxx; htVD_2132_connect_is_bind=xxxxxx; htVD_2132_connect_uin=xxxxxx; htVD_2132_nofavfid=xxxxxx; htVD_2132_smile=xxxxxx; Hm_lvt_46d556462595ed05e05f009cdafff31a=xxxxxx; htVD_2132_saltkey=xxxxxx; htVD_2132_lastvisit=xxxxxx; htVD_2132_client_created=xxxxxx; htVD_2132_auth=xxxxxx; htVD_2132_connect_login=xxxxxx; htVD_2132_home_diymode=xxxxxx; htVD_2132_visitedfid=xxxxxx; htVD_2132_viewid=xxxxxx; KF4=xxxxxx; htVD_2132_st_p=xxxxxx; htVD_2132_lastcheckfeed=xxxxxx; htVD_2132_sid=xxxxxx; htVD_2132_ulastactivity=xxxxxx; htVD_2132_noticeTitle=xxxxxx;"
    },
    {
      "pojie_cookie": "多账号 cookie 填写，请参考上面，cookie 以实际获取为准（遇到特殊字符如双引号\" 请加反斜杠转义）"
    }
  ],
  "MGTV_PARAMS_LIST": [
    {
      "mgtv_params": "uuid=xxxxxx&uid=xxxxxx&ticket=xxxxxx&token=xxxxxx&device=iPhone&did=xxxxxx&deviceId=xxxxxx&appVersion=6.8.2&osType=ios&platform=iphone&abroad=0&aid=xxxxxx&nonce=xxxxxx&timestamp=xxxxxx&appid=xxxxxx&type=1&sign=xxxxxx&callback=xxxxxx"
    },
    {
      "mgtv_params": "多账号 请求参数填写，请参考上面"
    }
  ],
  "PICACOMIC_ACCOUNT_LIST": [
    {
      "picacomic_email": "Sitoi",
      "picacomic_password": "Sitoi"
    },
    {
      "picacomic_email": "多账号 账号填写，请参考上面",
      "picacomic_password": "多账号 密码填写，请参考上面"
    }
  ],
  "MEIZU_COOKIE_LIST": [
    {
      "meizu_cookie": "aliyungf_tc=xxxxxx; logined_uid=xxxxxx; acw_tc=xxxxxx; LT=xxxxxx; MZBBS_2132_saltkey=xxxxxx; MZBBS_2132_lastvisit=xxxxxx; MZBBSUC_2132_auth=xxxxxx; MZBBSUC_2132_loginmember=xxxxxx; MZBBSUC_2132_ticket=xxxxxx; MZBBS_2132_sid=xxxxxx; MZBBS_2132_ulastactivity=xxxxxx; MZBBS_2132_auth=xxxxxx; MZBBS_2132_loginmember=xxxxxx; MZBBS_2132_lastcheckfeed=xxxxxx; MZBBS_2132_checkfollow=xxxxxx; MZBBS_2132_lastact=xxxxxx;",
      "draw_count": "1"
    },
    {
      "meizu_cookie": "多账号 cookie 填写，请参考上面，cookie 以实际获取为准（遇到特殊字符如双引号\" 请加反斜杠转义）",
      "draw_count": "多账号 抽奖次数设置"
    }
  ],
  "CAIYUN_COOKIE_LIST": [
    {
      "caiyun_cookie": "WAPJSESSIONID=xxxxxx; bc_mo=xxxxxx; bc_ps=xxxxxx; bc_to=xxxxxx; JSESSIONID=xxxxxx; sensorsdata2015jssdkcross=xxxxxx; sajssdk_2015_cross_new_user=1",
      "caiyun_referer": "https://caiyun.feixin.10086.cn:7071/portal/newsignin/index.jsp",
      "caiyun_draw": false
    },
    {
      "caiyun_cookie": "多账号 cookie 填写，请参考上面，cookie 以实际获取为准（遇到特殊字符如双引号\" 请加反斜杠转义）",
      "caiyun_referer": "多账号 请求重定向地址，填写，请参考上面，以实际获取为准",
      "caiyun_draw": "多账号 是否开启抽奖，填写 true or false 去掉双引号"
    }
  ]
}
```


## 三、Star 一下，立即执行，观察运行情况

点一下自己 fork 项目的 star 立即执行

## 四、开启定时运行

必须修改一次文件（比如自己库中的 `README.md` 文件）才能定时运行