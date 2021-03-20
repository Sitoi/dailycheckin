# 配置说明

## 参数说明

> ⚠️️ _**斜体加粗大写英文字母**_ 表示 GitHub Actions Secrets 环境变量名称，内容直接复制 _**斜体加粗大写英文字母 key**_  对应的 value 是 List 格式的直接复制全部 List 内容

### 推送配置

|Name|归属|属性|说明|
|:---:|:---:|:---:|:---|
|_**DINGTALK_SECRET**_|钉钉推送|推送|钉钉推送[官方文档](https://ding-doc.dingtalk.com/doc#/serverapi2/qf2nxq) 密钥，机器人安全设置页面，加签一栏下面显示的 `SEC` 开头的字符串, 注:填写了 `DD_BOT_TOKEN` 和 `DD_BOT_SECRET`，钉钉机器人安全设置只需勾选`加签`即可，其他选项不要勾选|
|_**DINGTALK_ACCESS_TOKEN**_|钉钉推送|推送|钉钉推送[官方文档](https://ding-doc.dingtalk.com/doc#/serverapi2/qf2nxq) ,只需 `https://oapi.dingtalk.com/robot/send?access_token=XXX` 等于符号后面的 `XXX`|
|_**SCKEY**_|server 酱推送|推送|server 酱推送[官方文档](https://sc.ftqq.com/3.version) ,填写 `SCKEY` 代码即可|
|_**SENDKEY**_|server 酱 TURBO 推送|推送|server 酱 TURBO 推送[官方文档](https://sct.ftqq.com/sendkey) ,填写 `SENDKEY` 代码即可|
|_**BARK_URL**_|BARK 推送|推送|BARK 推送[使用](https://github.com/Sitoi/dailycheckin/issues/29) ,填写 `BARK_URL` 即可，例如: `https://api.day.app/DxHcxxxxxRxxxxxxcm/` |
|_**QMSG_KEY**_|qmsg 酱推送|推送|qmsg 酱推送[官方文档](https://qmsg.zendee.cn/index.html) ,填写 `KEY` 代码即可|
|_**QMSG_TYPE**_|qmsg 酱推送|推送|qmsg 酱推送[官方文档](https://qmsg.zendee.cn/index.html) ,如果需要推送到群填写 `group`,其他的都推送到 QQ |
|_**TG_BOT_TOKEN**_|telegram 推送|推送|telegram 推送 `TG_BOT_TOKEN`|
|_**TG_USER_ID**_|telegram 推送|推送|telegram 推送 `TG_USER_ID`|
|_**COOLPUSHSKEY**_|Cool Push 推送|推送|[Cool Push](https://cp.xuthus.cc/) 推送的 `SKEY`|
|_**COOLPUSHQQ**_|Cool Push 推送|推送|[Cool Push](https://cp.xuthus.cc/) 是否开启 QQ 推送，默认开启|
|_**COOLPUSHWX**_|Cool Push 推送|推送|[Cool Push](https://cp.xuthus.cc/) 是否开启 微信 推送，默认关闭|
|_**COOLPUSHEMAIL**_|Cool Push 推送|推送|[Cool Push](https://cp.xuthus.cc/) 是否开启 邮件 推送，默认关闭|
|_**QYWX_KEY**_|企业微信群机器人推送|推送|密钥，企业微信推送 `webhook` 后面的 `key` 详见[官方说明文档](https://work.weixin.qq.com/api/doc/90000/90136/91770) |
|_**QYWX_CORPID**_|企业微信应用消息推送|推送|corpid [参考文档1](https://note.youdao.com/ynoteshare1/index.html?id=351e08a72378206f9dd64d2281e9b83b&type=note)  [参考文档2](https://note.youdao.com/ynoteshare1/index.html?id=1a0c8aff284ad28cbd011b29b3ad0191&type=note) |
|_**QYWX_AGENTID**_|企业微信应用消息推送|推送|agentid [参考文档1](https://note.youdao.com/ynoteshare1/index.html?id=351e08a72378206f9dd64d2281e9b83b&type=note)  [参考文档2](https://note.youdao.com/ynoteshare1/index.html?id=1a0c8aff284ad28cbd011b29b3ad0191&type=note) |
|_**QYWX_CORPSECRET**_|企业微信应用消息推送|推送|corpsecret [参考文档1](https://note.youdao.com/ynoteshare1/index.html?id=351e08a72378206f9dd64d2281e9b83b&type=note)  [参考文档2](https://note.youdao.com/ynoteshare1/index.html?id=1a0c8aff284ad28cbd011b29b3ad0191&type=note) |
|_**QYWX_TOUSER**_|企业微信应用消息推送|推送|touser [参考文档1](https://note.youdao.com/ynoteshare1/index.html?id=351e08a72378206f9dd64d2281e9b83b&type=note)  [参考文档2](https://note.youdao.com/ynoteshare1/index.html?id=1a0c8aff284ad28cbd011b29b3ad0191&type=note) |
|_**PUSHPLUS_TOKEN**_|pushplus 推送|推送|用户令牌，可直接加到请求地址后，如：http://pushplus.hxtrip.com/send/{token} [官方文档](https://pushplus.hxtrip.com/doc/)|
|_**PUSHPLUS_TOPIC**_|pushplus 推送|推送|群组编码，不填仅发送给自己 [官方文档](https://pushplus.hxtrip.com/doc/)|

### Web 签到配置

|Name|归属|属性|说明|
|:---:|:---:|:---:|:---|
|_**IQIYI_COOKIE_LIST**_.iqiyi_cookie|[爱奇艺](https://www.iqiyi.com/)|Web|爱奇艺 帐号的 cookie 信息|
|_**KGQQ_COOKIE_LIST**_.kgqq_cookie|[全民K歌](https://kg.qq.com/index-pc.html)|Web|全民K歌 帐号的 cookie 信息|
|_**VQQ_COOKIE_LIST**_.auth_refresh|[腾讯视频](https://v.qq.com/)|Web|腾讯视频 搜索 带有 `auth_refresh` 的 url，填写其完整的 URL|
|_**VQQ_COOKIE_LIST**_.vqq_cookie|[腾讯视频](https://v.qq.com/)|Web|腾讯视频 搜索 带有 `auth_refresh` 的 url，填写其对应的 cookie|
|_**YOUDAO_COOKIE_LIST**_.youdao_cookie|[有道云笔记](https://note.youdao.com/web/)|Web|有道云笔记 帐号的 cookie 信息|
|_**MUSIC163_ACCOUNT_LIST**_.music163_phone|[网易云音乐](https://music.163.com/)|账号|网易云音乐 帐号的手机号|
|_**MUSIC163_ACCOUNT_LIST**_.music163_password|[网易云音乐](https://music.163.com/)|账号|网易云音乐 帐号的密码|
|_**ONEPLUSBBS_COOKIE_LIST**_.oneplusbbs_cookie|[一加手机社区官方论坛](https://www.oneplusbbs.com/)|Web|一加手机社区官方论坛 账户的 cookie|
|_**TIEBA_COOKIE_LIST**_.tieba_cookie|[百度贴吧](https://tieba.baidu.com/index.html)|Web|百度贴吧 cookie|
|_**BILIBILI_COOKIE_LIST**_.bilibili_cookie|[Bilibili](https://www.bilibili.com)|Web|Bilibili cookie|
|_**BILIBILI_COOKIE_LIST**_.coin_num|[Bilibili](https://www.bilibili.com)|Web|Bilibili 每日投币数量|
|_**BILIBILI_COOKIE_LIST**_.coin_type|[Bilibili](https://www.bilibili.com)|Web|Bilibili 投币方式 默认为 0 ；1: 为关注用户列表视频投币 0: 为随机投币。如果关注用户发布的视频不足配置的投币数，则剩余部分使用随机投币|
|_**BILIBILI_COOKIE_LIST**_.silver2coin|[Bilibili](https://www.bilibili.com)|Web|Bilibili 是否开启银瓜子换硬币，默认为 True 开启|
|_**V2EX_COOKIE_LIST**_.v2ex_cookie|[V2EX](https://www.v2ex.com/)|Web|V2EX 每日签到|
|_**WWW2NZZ_COOKIE_LIST**_.www2nzz_cookie|[咔叽网单](https://www.2nzz.com/)|Web|咔叽网单 每日签到|
|_**SMZDM_COOKIE_LIST**_.smzdm_cookie|[什么值得买](https://www.smzdm.com)|Web|什么值得买 每日签到|
|_**CLOUD189_ACCOUNT_LIST**_.cloud189_phone|[天翼云盘](https://cloud.189.cn/)|Web| 天翼云盘 手机号|
|_**CLOUD189_ACCOUNT_LIST**_.cloud189_password|[天翼云盘](https://cloud.189.cn/)|Web| 天翼云盘 手机号对应的密码|
|_**WPS_COOKIE_LIST**_.wps_cookie|[WPS](https://www.wps.cn/)|Web| WPS cookie|
|_**POJIE_COOKIE_LIST**_.pojie_cookie|[吾爱破解](https://www.52pojie.cn/index.php)|Web| 吾爱破解 cookie|
|_**MEIZU_COOKIE_LIST**_.meizu_cookie|[MEIZU 社区](https://bbs.meizu.cn)|Web| MEIZU 社区 cookie|
|_**MEIZU_COOKIE_LIST**_.draw_count|[MEIZU 社区](https://bbs.meizu.cn)|Web| MEIZU 社区 抽奖次数|
|_**CAIYUN_COOKIE_LIST**_.caiyun_cookie|[和彩云](https://caiyun.feixin.10086.cn:7071/portal/newsignin/index.jsp)|Web| 和彩云 cookie|
|_**ZHIYOO_COOKIE_LIST**_.zhiyoo_cookie|[智友邦](http://zhizhiyoo.net/)|Web| 智友邦 WEB Cookie|

### APP 签到配置

|Name|归属|属性|说明|
|:---:|:---:|:---:|:---|
|_**LIANTONG_ACCOUNT_LIST**_.data|联通营业厅|APP|联通营业厅 每日签到|
|_**FMAPP_ACCOUNT_LIST**_.fmapp_token|Fa米家|APP|Fa米家 APP headers 中的 token|
|_**FMAPP_ACCOUNT_LIST**_.fmapp_cookie|Fa米家|APP|Fa米家 APP headers 中的 cookie|
|_**FMAPP_ACCOUNT_LIST**_.fmapp_device_id|Fa米家|APP|Fa米家 APP headers 中的 deviceId|
|_**XMLY_COOKIE_LIST**_.xmly_cookie|喜马拉雅极速版|APP|喜马拉雅极速版 cookie|
|_**ACFUN_ACCOUNT_LIST**_.acfun_phone|[AcFun](https://www.acfun.cn/)|APP|AcFun 手机账号|
|_**ACFUN_ACCOUNT_LIST**_.acfun_password|[AcFun](https://www.acfun.cn/)|APP|AcFun 账号密码|
|_**MGTV_PARAMS_LIST**_.mgtv_params|芒果 TV|APP|芒果 TV 请求参数|
|_**PICACOMIC_ACCOUNT_LIST**_.picacomic_email|[哔咔漫画](https://www.picacomic.com)|APP| 哔咔漫画 账号|
|_**PICACOMIC_ACCOUNT_LIST**_.picacomic_password|[哔咔漫画](https://www.picacomic.com)|APP| 哔咔漫画 密码|

### 其他任务配置

|Name|归属|属性|说明|
|:---:|:---:|:---:|:---|
|_**MIMOTION_ACCOUNT_LIST**_.mimotion_phone|小米运动|其他|小米运动刷步数的手机账号|
|_**MIMOTION_ACCOUNT_LIST**_.mimotion_password|小米运动|其他|小米运动刷步数的手机账号密码|
|_**MIMOTION_ACCOUNT_LIST**_.mimotion_min_step|小米运动|其他|小米运动刷步数的最小步数|
|_**MIMOTION_ACCOUNT_LIST**_.mimotion_max_step|小米运动|其他|小米运动刷步数的最大步数|
|_**BAIDU_URL_SUBMIT_LIST**_.data_url|[百度搜索资源平台](https://ziyuan.baidu.com/site/index#/)|其他|提交网站的 URL 链接|
|_**BAIDU_URL_SUBMIT_LIST**_.submit_url|[百度搜索资源平台](https://ziyuan.baidu.com/site/index#/)|其他|百度搜索资源平台 提交百度网站的目标 URL|
|_**BAIDU_URL_SUBMIT_LIST**_.times|[百度搜索资源平台](https://ziyuan.baidu.com/site/index#/)|其他|每日对同一个网站提交次数|
|_**CITY_NAME_LIST**_|每日天气|其他|填写城市名称，点击查看[城市名称列表](https://cdn.jsdelivr.net/gh/Sitoi/dailycheckin/weather/city.json)|
|_**MOTTO**_|每日一句|其他|是否开启默认为 false|

## 参数获取方法

### 网页 Cookie 获取

获取 Cookie 教程（以爱奇艺为例）

![获取 cookie 教程](https://cdn.jsdelivr.net/gh/Sitoi/dailycheckin/docs/img/iqiyi_cookie.png)

1. 进入[爱奇艺官网](https://www.iqiyi.com/)
2. 按 `F12` 打开开发者工具，刷新页面
3. 点击 `Network` 标签
4. 选择 `Doc` 标签
5. 选中 `www.iqiyi.com`
6. 下滑找到 `cookie` 全选复制即可


### APP 抓包

#### 芒果 TV 请求参数

抓包 APP 中获取 url 关键词 `credits.bz.mgtv.com/user/creditsTake`，提取 `?` 后所有参数

**示例**

```json
[
  {
    "mgtv_params": "uuid=xxx&uid=xxx&ticket=xxx&token=xxx&device=iPhone&did=xxx&deviceId=xxx&appVersion=6.8.2&osType=ios&platform=iphone&abroad=0&aid=xxx&nonce=xxx&timestamp=1614595550&appid=xxx&type=1&sign=xxx&callback=__jp18"
  }
]
```

#### 喜马拉雅极速版 Cookie 参数获取

抓包 APP 中域名为 `m.ximalaya.com` 中的 `cookie` 即可

#### Fa米家 Cookie 等参数获取

抓包 APP 的请求中的 `headers` 信息中提取 `token`、`deviceId`、`cookie` 即可

#### 联通营业厅参数获取

1. 退出手机营业厅登录，然后开启抓包软件，登录手机营业厅

查找网址为 `https://m.client.10010.com/mobileService/login.htm` 的记录，找到请求内容，将 `simCount` 开始到最后的内容按要求填入 `config/config.json` 文件。

**样例**

```json
{
  "LIANTONG_ACCOUNT_LIST": [
    {
      "data": "simCount=1&version=iphone_c@8.0100&mobile=xxxxxx&netWay=wifi&isRemberPwd=false&appId=xxxxxx&deviceId=xxxxxx&pip=192.168.1.1&password=xxxxxx&deviceOS=14.3&deviceBrand=iphone&deviceModel=iPhone&remark4=&keyVersion=2&deviceCode=xxxxxx"
    }
  ]
}
```

### 其他参数

#### 百度站点提交参数获取

[百度搜索资源平台](https://ziyuan.baidu.com/site/index#/)

![获取百度云提交链接教程](https://cdn.jsdelivr.net/gh/Sitoi/dailycheckin/docs/img/submit_url.png)

- _**BAIDU_URL_SUBMIT_LIST**_.data_url: 提交网站的 URL
  链接，参考链接：[https://cdn.jsdelivr.net/gh/Sitoi/Sitoi.github.io/baidu_urls.txt](https://cdn.jsdelivr.net/gh/Sitoi/Sitoi.github.io/baidu_urls.txt)
- _**BAIDU_URL_SUBMIT_LIST**_.submit_url: 提交百度网站的目标
  URL，参考格式：`http://data.zz.baidu.com/urls?site=https://sitoi.cn&token=xxxxx`
- _**BAIDU_URL_SUBMIT_LIST**_.times: 单次任务执行对同一个网站提交次数

#### 城市天气列表

[城市名称列表](https://cdn.jsdelivr.net/gh/Sitoi/dailycheckin/weather/city.json)

#### 每日一句 是否开启

默认为 false。false: 表示关闭；true: 表示开启

## 示例

> ⚠️ 请务必到 [http://www.json.cn](http://www.json.cn) 网站检查 `config.json` 文件格式是否正确！

配置文件：`config/config.json`

```json
{
  "DINGTALK_SECRET": "",
  "DINGTALK_ACCESS_TOKEN": "",
  "SCKEY": "",
  "SENDKEY": "",
  "BARK_URL": "",
  "QMSG_KEY": "",
  "QMSG_TYPE": "",
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
      "caiyun_cookie": "WAPJSESSIONID=xxxxxx; bc_mo=xxxxxx; bc_ps=xxxxxx; bc_to=xxxxxx; JSESSIONID=xxxxxx; sensorsdata2015jssdkcross=xxxxxx; sajssdk_2015_cross_new_user=1"
    },
    {
      "caiyun_cookie": "多账号 cookie 填写，请参考上面，cookie 以实际获取为准（遇到特殊字符如双引号\" 请加反斜杠转义）"
    }
  ],
  "ZHIYOO_COOKIE_LIST": [
    {
      "zhiyoo_cookie": "ikdQ_9242_saltkey=xxxxxx; ikdQ_9242_lastvisit=xxxxxx; ikdQ_9242_onlineusernum=xxxxxx; ikdQ_9242_sendmail=1; ikdQ_9242_seccode=xxxxxx; ikdQ_9242_ulastactivity=xxxxxx; ikdQ_9242_auth=xxxxxx; ikdQ_9242_connect_is_bind=xxxxxx; ikdQ_9242_nofavfid=xxxxxx; ikdQ_9242_checkpm=xxxxxx; ikdQ_9242_noticeTitle=1; ikdQ_9242_sid=xxxxxx; ikdQ_9242_lip=xxxxxx; ikdQ_9242_lastact=xxxxxx"
    },
    {
      "zhiyoo_cookie": "多账号 cookie 填写，请参考上面，cookie 以实际获取为准（遇到特殊字符如双引号\" 请加反斜杠转义）"
    }
  ]
}
```