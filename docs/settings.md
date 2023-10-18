# 配置说明

## 参数说明

### 推送配置

|            Name             |       归属       | 属性 | 说明                                                                                                                                                                                                                                          |
| :-------------------------: | :--------------: | :--: | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|    _**DINGTALK_SECRET**_    |       钉钉       | 推送 | 钉钉推送[官方文档](https://ding-doc.dingtalk.com/doc#/serverapi2/qf2nxq) 密钥，机器人安全设置页面，加签一栏下面显示的 `SEC` 开头的字符串, 注:填写了 `DD_BOT_TOKEN` 和 `DD_BOT_SECRET`，钉钉机器人安全设置只需勾选`加签`即可，其他选项不要勾选 |
| _**DINGTALK_ACCESS_TOKEN**_ |       钉钉       | 推送 | 钉钉推送[官方文档](https://ding-doc.dingtalk.com/doc#/serverapi2/qf2nxq) ,只需 `https://oapi.dingtalk.com/robot/send?access_token=XXX` 等于符号后面的 `XXX`                                                                                   |
|         _**SCKEY**_         |    server 酱     | 推送 | server 酱推送[官方文档](https://sc.ftqq.com/3.version) ,填写 `SCKEY` 代码即可                                                                                                                                                                 |
|        _**SENDKEY**_        | server 酱 TURBO  | 推送 | server 酱 TURBO 推送[官方文档](https://sct.ftqq.com/sendkey) ,填写 `SENDKEY` 代码即可                                                                                                                                                         |
|       _**BARK_URL**_        |       BARK       | 推送 | BARK 推送[使用](https://github.com/Sitoi/dailycheckin/issues/29) ,填写 `BARK_URL` 即可，例如: `https://api.day.app/DxHcxxxxxRxxxxxxcm/`                                                                                                       |
|       _**QMSG_KEY**_        |     qmsg 酱      | 推送 | qmsg 酱推送[官方文档](https://qmsg.zendee.cn/index.html) ,填写 `KEY` 代码即可                                                                                                                                                                 |
|       _**QMSG_TYPE**_       |     qmsg 酱      | 推送 | qmsg 酱推送[官方文档](https://qmsg.zendee.cn/index.html) ,如果需要推送到群填写 `group`,其他的都推送到 QQ                                                                                                                                      |
|     _**TG_BOT_TOKEN**_      |     telegram     | 推送 | telegram 推送 `TG_BOT_TOKEN`                                                                                                                                                                                                                  |
|      _**TG_USER_ID**_       |     telegram     | 推送 | telegram 推送 `TG_USER_ID`                                                                                                                                                                                                                    |
|      _**TG_API_HOST**_      |     telegram     | 推送 | Telegram api 自建的反向代理地址 例子：反向代理地址 http://aaa.bbb.ccc 则填写 aaa.bbb.ccc [简略搭建教程](https://shimo.im/docs/JD38CJDQtYy3yTd8/read)                                                                                          |
|       _**TG_PROXY**_        |     telegram     | 推送 | Telegram 代理的信息，无密码例子: http://127.0.0.1:1080 有密码例子: http://username:password@127.0.0.1:1080                                                                                                                                    |
|     _**COOLPUSHSKEY**_      |    Cool Push     | 推送 | [Cool Push](https://cp.xuthus.cc/) 推送的 `SKEY`                                                                                                                                                                                              |
|      _**COOLPUSHQQ**_       |    Cool Push     | 推送 | [Cool Push](https://cp.xuthus.cc/) 是否开启 QQ 推送，默认开启                                                                                                                                                                                 |
|      _**COOLPUSHWX**_       |    Cool Push     | 推送 | [Cool Push](https://cp.xuthus.cc/) 是否开启 微信 推送，默认关闭                                                                                                                                                                               |
|     _**COOLPUSHEMAIL**_     |    Cool Push     | 推送 | [Cool Push](https://cp.xuthus.cc/) 是否开启 邮件 推送，默认关闭                                                                                                                                                                               |
|       _**QYWX_KEY**_        | 企业微信群机器人 | 推送 | 密钥，企业微信推送 `webhook` 后面的 `key` 详见[官方说明文档](https://work.weixin.qq.com/api/doc/90000/90136/91770)                                                                                                                            |
|      _**QYWX_CORPID**_      | 企业微信应用消息 | 推送 | corpid                                                                                                                                                                                                                                        |
|     _**QYWX_AGENTID**_      | 企业微信应用消息 | 推送 | agentid                                                                                                                                                                                                                                       |
|    _**QYWX_CORPSECRET**_    | 企业微信应用消息 | 推送 | corpsecret                                                                                                                                                                                                                                    |
|      _**QYWX_TOUSER**_      | 企业微信应用消息 | 推送 | touser                                                                                                                                                                                                                                        |
|     _**QYWX_MEDIA_ID**_     | 企业微信应用消息 | 推送 | media_id [参考文档 1](https://note.youdao.com/ynoteshare1/index.html?id=351e08a72378206f9dd64d2281e9b83b&type=note) [参考文档 2](https://note.youdao.com/ynoteshare1/index.html?id=1a0c8aff284ad28cbd011b29b3ad0191&type=note)                |
|    _**PUSHPLUS_TOKEN**_     |     pushplus     | 推送 | 用户令牌，可直接加到请求地址后，如：http://www.pushplus.plus/send/{token} [官方文档](https://www.pushplus.plus/doc/)                                                                                                                          |
|    _**PUSHPLUS_TOPIC**_     |     pushplus     | 推送 | 群组编码，不填仅发送给自己 [官方文档](https://www.pushplus.plus/doc/)                                                                                                                                                                         |
|         _**FSKEY**_         |       飞书       | 推送 | `https://open.feishu.cn/open-apis/bot/v2/hook/xxxxxx` **xxxxxx** 部分就是需要填写的 FSKEY                                                                                                                                                     |
|      _**MERGE_PUSH**_       |     合并推送     | 配置 | **true**: 将推送消息合并；**false**: 分开推送                                                                                                                                                                                                 |

### Web 签到配置

|            Name            |                      归属                      | 属性 | 说明                                                                                                                                 |
| :------------------------: | :--------------------------------------------: | :--: | :----------------------------------------------------------------------------------------------------------------------------------- |
|     _**IQIYI**_.cookie     |                     爱奇艺                     | WEB  | 爱奇艺 APP headers 中的 token                                                                                                        |
|     _**KGQQ**_.cookie      |  [全民 K 歌](https://kg.qq.com/index-pc.html)  | Web  | 全民 K 歌 帐号的 cookie 信息                                                                                                         |
|    _**YOUDAO**_.cookie     |   [有道云笔记](https://note.youdao.com/web/)   | Web  | 有道云笔记 帐号的 cookie 信息                                                                                                        |
|     _**TIEBA**_.cookie     | [百度贴吧](https://tieba.baidu.com/index.html) | Web  | 百度贴吧 cookie                                                                                                                      |
|   _**BILIBILI**_.cookie    |      [Bilibili](https://www.bilibili.com)      | Web  | Bilibili cookie                                                                                                                      |
|  _**BILIBILI**_.coin_num   |      [Bilibili](https://www.bilibili.com)      | Web  | Bilibili 每日投币数量                                                                                                                |
|  _**BILIBILI**_.coin_type  |      [Bilibili](https://www.bilibili.com)      | Web  | Bilibili 投币方式 默认为 0 ；1: 为关注用户列表视频投币 0: 为随机投币。如果关注用户发布的视频不足配置的投币数，则剩余部分使用随机投币 |
| _**BILIBILI**_.silver2coin |      [Bilibili](https://www.bilibili.com)      | Web  | Bilibili 是否开启银瓜子换硬币，默认为 True 开启                                                                                      |
|     _**V2EX**_.cookie      |         [V2EX](https://www.v2ex.com/)          | Web  | V2EX 每日签到                                                                                                                        |
|      _**V2EX**_.proxy      |         [V2EX](https://www.v2ex.com/)          | Web  | V2EX 代理的信息，无密码例子: http://127.0.0.1:1080 有密码例子: http://username:password@127.0.0.1:1080                               |
|    _**CLOUD189**_.phone    |       [天翼云盘](https://cloud.189.cn/)        | Web  | 天翼云盘 手机号                                                                                                                      |
|  _**CLOUD189**_.password   |       [天翼云盘](https://cloud.189.cn/)        | Web  | 天翼云盘 手机号对应的密码                                                                                                            |

### APP 签到配置

|         Name          |              归属              | 属性 | 说明                                |
| :-------------------: | :----------------------------: | :--: | :---------------------------------- |
|   _**FMAPP**_.token   |            Fa 米家             | APP  | Fa 米家 APP headers 中的 token      |
| _**FMAPP**_.blackbox  |            Fa 米家             | APP  | Fa 米家 APP headers 中的 blackBox   |
| _**FMAPP**_.device_id |            Fa 米家             | APP  | Fa 米家 APP headers 中的 deviceId   |
| _**FMAPP**_.fmversion |            Fa 米家             | APP  | Fa 米家 APP headers 中的 fmVersion  |
|    _**FMAPP**_.os     |            Fa 米家             | APP  | Fa 米家 APP headers 中的 os         |
| _**FMAPP**_.useragent |            Fa 米家             | APP  | Fa 米家 APP headers 中的 User-Agent |
|   _**ACFUN**_.phone   | [AcFun](https://www.acfun.cn/) | APP  | AcFun 手机账号                      |
| _**ACFUN**_.password  | [AcFun](https://www.acfun.cn/) | APP  | AcFun 账号密码                      |

### 其他任务配置

|          Name           |                           归属                            | 属性 | 说明                                    |
| :---------------------: | :-------------------------------------------------------: | :--: | :-------------------------------------- |
|  _**MIMOTION**_.phone   |                         小米运动                          | 其他 | 小米运动刷步数的手机账号                |
| _**MIMOTION**_.password |                         小米运动                          | 其他 | 小米运动刷步数的手机账号密码            |
| _**MIMOTION**_.min_step |                         小米运动                          | 其他 | 小米运动刷步数的最小步数                |
| _**MIMOTION**_.max_step |                         小米运动                          | 其他 | 小米运动刷步数的最大步数                |
|  _**BAIDUT**_.data_url  | [百度搜索资源平台](https://ziyuan.baidu.com/site/index#/) | 其他 | 提交网站的 URL 链接                     |
| _**BAIDUT**_.submit_url | [百度搜索资源平台](https://ziyuan.baidu.com/site/index#/) | 其他 | 百度搜索资源平台 提交百度网站的目标 URL |
|   _**BAIDUT**_.times    | [百度搜索资源平台](https://ziyuan.baidu.com/site/index#/) | 其他 | 每日对同一个网站提交次数                |

## 参数获取方法

### 网页 Cookie 获取

获取 Cookie 教程（以爱奇艺为例）

![获取 cookie 教程](img/iqiyi_cookie.png)

1. 进入[爱奇艺官网](https://www.iqiyi.com/)
2. 按 `F12` 打开开发者工具，刷新页面
3. 点击 `Network` 标签
4. 选择 `Doc` 标签
5. 选中 `www.iqiyi.com`
6. 下滑找到 `cookie` 全选复制即可

### APP 抓包

#### Fa 米家 Cookie 等参数获取

抓包 APP 的请求中的 `headers` 信息中提取 `token`、`deviceId`、`cookie` 即可

### 其他参数

#### 百度站点提交参数获取

[百度搜索资源平台](https://ziyuan.baidu.com/site/index#/)

![获取百度云提交链接教程](img/submit_url.png)

- _**BAIDUT**_.data_url: 提交网站的 URL 链接，参考链接：[https://cdn.jsdelivr.net/gh/Sitoi/Sitoi.github.io/baidu_urls.txt](https://cdn.jsdelivr.net/gh/Sitoi/Sitoi.github.io/baidu_urls.txt)
- _**BAIDUT**_.submit_url: 提交百度网站的目标 URL，参考格式：`http://data.zz.baidu.com/urls?site=https://sitoi.cn&token=xxxxx`
- _**BAIDUT**_.times: 单次任务执行对同一个网站提交次数

## 示例

> ⚠️ 请务必到 [http://www.json.cn](http://www.json.cn) 网站检查 `config.json` 文件格式是否正确！

配置文件：`config/config.json`

```json
{
  "BARK_URL": "",
  "COOLPUSHEMAIL": true,
  "COOLPUSHQQ": true,
  "COOLPUSHSKEY": "",
  "COOLPUSHWX": true,
  "DINGTALK_ACCESS_TOKEN": "",
  "DINGTALK_SECRET": "",
  "FSKEY": "",
  "PUSHPLUS_TOKEN": "",
  "PUSHPLUS_TOPIC": "",
  "QMSG_KEY": "",
  "QMSG_TYPE": "",
  "QYWX_AGENTID": "",
  "QYWX_CORPID": "",
  "QYWX_CORPSECRET": "",
  "QYWX_KEY": "",
  "QYWX_MEDIA_ID": "",
  "QYWX_TOUSER": "",
  "SCKEY": "",
  "SENDKEY": "",
  "TG_API_HOST": "",
  "TG_BOT_TOKEN": "",
  "TG_PROXY": "",
  "TG_USER_ID": "",
  "MERGE_PUSH": "",
  "ACFUN": [
    {
      "password": "Sitoi",
      "phone": "18888xxxxxx"
    },
    {
      "password": "多账号 密码填写，请参考上面",
      "phone": "多账号 手机号填写，请参考上面"
    }
  ],
  "BAIDU": [
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
  "BILIBILI": [
    {
      "cookie": "_uuid=xxxxxx; rpdid=xxxxxx; LIVE_BUVID=xxxxxx; PVID=xxxxxx; blackside_state=xxxxxx; CURRENT_FNVAL=xxxxxx; buvid3=xxxxxx; fingerprint3=xxxxxx; fingerprint=xxxxxx; buivd_fp=xxxxxx; buvid_fp_plain=xxxxxx; DedeUserID=xxxxxx; DedeUserID__ckMd5=xxxxxx; SESSDATA=xxxxxx; bili_jct=xxxxxx; bsource=xxxxxx; finger=xxxxxx; fingerprint_s=xxxxxx;",
      "coin_num": 0,
      "coin_type": 1,
      "silver2coin": true
    },
    {
      "cookie": "多账号 cookie 填写，请参考上面，cookie 以实际获取为准（遇到特殊字符如双引号\" 请加反斜杠转义）",
      "coin_num": 0,
      "coin_type": 1,
      "silver2coin": true
    }
  ],
  "FMAPP": [
    {
      "blackbox": "eyJlcnJxxxxxx",
      "device_id": "xxxxxx-xxxx-xxxx-xxxx-xxxxxx",
      "fmversion": "xxxxxx",
      "os": "xxxxxx",
      "token": "xxxxxx.xxxxxx-xxxxxx-xxxxxx.xxxxxx-xxxxxx",
      "useragent": "xxxxxx"
    },
    {
      "blackbox": "多账号 blackbox 填写，请参考上面，blackbox 以实际获取为准（遇到特殊字符如双引号\" 请加反斜杠转义）",
      "device_id": "多账号 device_id 填写，请参考上面，以实际获取为准",
      "fmversion": "多账号 fmVersion 填写，请参考上面，以实际获取为准",
      "os": "多账号 os 填写，请参考上面，以实际获取为准",
      "token": "多账号 token 填写，请参考上面，以实际获取为准",
      "useragent": "多账号 User-Agent 填写，请参考上面，以实际获取为准"
    }
  ],
  "IQIYI": [
    {
      "cookie": "__dfp=xxxxxx; QP0013=xxxxxx; QP0022=xxxxxx; QYABEX=xxxxxx; P00001=xxxxxx; P00002=xxxxxx; P00003=xxxxxx; P00007=xxxxxx; QC163=xxxxxx; QC175=xxxxxx; QC179=xxxxxx; QC170=xxxxxx; P00010=xxxxxx; P00PRU=xxxxxx; P01010=xxxxxx; QC173=xxxxxx; QC180=xxxxxx; P00004=xxxxxx; QP0030=xxxxxx; QC006=xxxxxx; QC007=xxxxxx; QC008=xxxxxx; QC010=xxxxxx; nu=xxxxxx; __uuid=xxxxxx; QC005=xxxxxx;"
    },
    {
      "cookie": "多账号 cookie 填写，请参考上面，cookie 以实际获取为准（遇到特殊字符如双引号\" 请加反斜杠转义）"
    }
  ],
  "KGQQ": [
    {
      "cookie": "muid=xxxxxx; uid=xxxxxx; userlevel=xxxxxx; openid=xxxxxx; openkey=xxxxxx; opentype=xxxxxx; qrsig=xxxxxx; pgv_pvid=xxxxxx;"
    },
    {
      "cookie": "多账号 cookie 填写，请参考上面，cookie 以实际获取为准（遇到特殊字符如双引号\" 请加反斜杠转义）"
    }
  ],
  "MIMOTION": [
    {
      "max_step": "20000",
      "min_step": "10000",
      "password": "Sitoi",
      "phone": "18888xxxxxx"
    },
    {
      "max_step": "多账号 最大步数填写，请参考上面",
      "min_step": "多账号 最小步数填写，请参考上面",
      "password": "多账号 密码填写，请参考上面",
      "phone": "多账号 手机号填写，请参考上面"
    }
  ],
  "TIEBA": [
    {
      "cookie": "BIDUPSID=xxxxxx; PSTM=xxxxxx; BAIDUID=xxxxxx; BAIDUID_BFESS=xxxxxx; delPer=xxxxxx; PSINO=xxxxxx; H_PS_PSSID=xxxxxx; BA_HECTOR=xxxxxx; BDORZ=xxxxxx; TIEBA_USERTYPE=xxxxxx; st_key_id=xxxxxx; BDUSS=xxxxxx; BDUSS_BFESS=xxxxxx; STOKEN=xxxxxx; TIEBAUID=xxxxxx; ab_sr=xxxxxx; st_data=xxxxxx; st_sign=xxxxxx;"
    },
    {
      "cookie": "多账号 cookie 填写，请参考上面，cookie 以实际获取为准（遇到特殊字符如双引号\" 请加反斜杠转义）"
    }
  ],
  "V2EX": [
    {
      "cookie": "_ga=xxxxxx; __cfduid=xxxxxx; PB3_SESSION=xxxxxx; A2=xxxxxx; V2EXSETTINGS=xxxxxx; V2EX_REFERRER=xxxxxx; V2EX_LANG=xxxxxx; _gid=xxxxxx; V2EX_TAB=xxxxxx;",
      "proxy": "使用代理的信息，无密码例子: http://127.0.0.1:1080 有密码例子: http://username:password@127.0.0.1:1080"
    },
    {
      "cookie": "多账号 cookie 填写，请参考上面，cookie 以实际获取为准（遇到特殊字符如双引号\" 请加反斜杠转义）",
      "proxy": "使用代理的信息，无密码例子: http://127.0.0.1:1080 有密码例子: http://username:password@127.0.0.1:1080"
    }
  ],
  "YOUDAO": [
    {
      "cookie": "JSESSIONID=xxxxxx; __yadk_uid=xxxxxx; OUTFOX_SEARCH_USER_ID_NCOO=xxxxxx; YNOTE_SESS=xxxxxx; YNOTE_PERS=xxxxxx; YNOTE_LOGIN=xxxxxx; YNOTE_CSTK=xxxxxx; _ga=xxxxxx; _gid=xxxxxx; _gat=xxxxxx; PUBLIC_SHARE_18a9dde3de846b6a69e24431764270c4=xxxxxx;"
    },
    {
      "cookie": "多账号 cookie 填写，请参考上面，cookie 以实际获取为准（遇到特殊字符如双引号\" 请加反斜杠转义）"
    }
  ]
}
```
