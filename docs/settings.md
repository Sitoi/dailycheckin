# 配置说明

## 参数说明

> _**斜体加粗大写英文字母**_ 表示 GitHub Actions Secrets 环境变量名称，内容直接复制 _**斜体加粗大写英文字母 key**_  对应的 value 是 List 格式的直接复制全部 List 内容

> _**斜体加粗大写英文字母**_ 表示 GitHub Actions Secrets 环境变量名称，内容直接复制 _**斜体加粗大写英文字母 key**_  对应的 value 是 List 格式的直接复制全部 List 内容

> _**斜体加粗大写英文字母**_ 表示 GitHub Actions Secrets 环境变量名称，内容直接复制 _**斜体加粗大写英文字母 key**_  对应的 value 是 List 格式的直接复制全部 List 内容

### 推送配置

|Name|归属|属性|说明|
|:---:|:---:|:---:|:---|
|_**DINGTALK_SECRET**_|钉钉推送|推送|钉钉推送[官方文档](https://ding-doc.dingtalk.com/doc#/serverapi2/qf2nxq) 密钥，机器人安全设置页面，加签一栏下面显示的 `SEC` 开头的字符串, 注:填写了 `DD_BOT_TOKEN` 和 `DD_BOT_SECRET`，钉钉机器人安全设置只需勾选`加签`即可，其他选项不要勾选|
|_**DINGTALK_ACCESS_TOKEN**_|钉钉推送|推送|钉钉推送[官方文档](https://ding-doc.dingtalk.com/doc#/serverapi2/qf2nxq) ,只需 `https://oapi.dingtalk.com/robot/send?access_token=XXX` 等于符号后面的 `XXX`|
|_**SCKEY**_|server 酱推送|推送|server 酱推送[官方文档](https://sc.ftqq.com/3.version) ,填写 `SCKEY` 代码即可|
|_**SENDKEY**_|server 酱 TURBO 推送|推送|server 酱 TURBO 推送[官方文档](https://sct.ftqq.com/sendkey) ,填写 `SENDKEY` 代码即可|
|_**BARK_URL**_|BARK 推送|推送|BARK 推送[使用](https://github.com/Sitoi/dailycheckin/issues/29) ,填写 `BARK_URL` 即可，例如: `https://api.day.app/DxHcxxxxxRxxxxxxcm/` |
|_**QMSG_KEY**_|qmsg 酱推送|推送|qmsg 酱推送[官方文档](https://qmsg.zendee.cn/index.html) ,填写 `KEY` 代码即可|
|_**TG_BOT_TOKEN**_|telegram 推送|推送|telegram 推送 `TG_BOT_TOKEN`|
|_**TG_USER_ID**_|telegram 推送|推送|telegram 推送 `TG_USER_ID`|
|_**COOLPUSHSKEY**_|Cool Push 推送|推送|[Cool Push](https://cp.xuthus.cc/) 推送的 `SKEY`|
|_**COOLPUSHQQ**_|Cool Push 推送|推送|[Cool Push](https://cp.xuthus.cc/) 是否开启 QQ 推送，默认开启|
|_**COOLPUSHWX**_|Cool Push 推送|推送|[Cool Push](https://cp.xuthus.cc/) 是否开启 微信 推送，默认关闭|
|_**COOLPUSHEMAIL**_|Cool Push 推送|推送|[Cool Push](https://cp.xuthus.cc/) 是否开启 邮件 推送，默认关闭|

### Web 签到配置

|Name|归属|属性|说明|
|:---:|:---:|:---:|:---|
|_**IQIYI_COOKIE_LIST**_.iqiyi_cookie|[爱奇艺](https://www.iqiyi.com/)|Web|爱奇艺 帐号的 cookie 信息|
|_**KGQQ_COOKIE_LIST**_.kgqq_cookie|[全民K歌](https://kg.qq.com/index-pc.html)|Web|全民K歌 帐号的 cookie 信息|
|_**VQQ_COOKIE_LIST**_.vqq_cookie|[腾讯视频](https://v.qq.com/)|Web|腾讯视频 帐号的 cookie 信息|
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

### APP 签到配置

|Name|归属|属性|说明|
|:---:|:---:|:---:|:---|
|_**LIANTONG_ACCOUNT_LIST**_.data|联通营业厅|APP|联通营业厅 每日签到|
|_**FMAPP_ACCOUNT_LIST**_.fmapp_token|Fa米家|APP|Fa米家 APP headers 中的 token|
|_**FMAPP_ACCOUNT_LIST**_.fmapp_cookie|Fa米家|APP|Fa米家 APP headers 中的 cookie|
|_**FMAPP_ACCOUNT_LIST**_.fmapp_device_id|Fa米家|APP|Fa米家 APP headers 中的 deviceId|
|_**XMLY_COOKIE_LIST**_.xmly_cookie|喜马拉雅极速版|APP|喜马拉雅极速版 cookie|
|_**ACFUN_ACCOUNT_LIST**_.acfun_phone|[AcFun](https://www.acfun.cn/)|APP|AcFun 每日签到|
|_**ACFUN_ACCOUNT_LIST**_.acfun_password|[AcFun](https://www.acfun.cn/)|APP|AcFun 每日签到|

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

### 帐号参数

#### 网易云音乐帐号信息

[网易云音乐](https://music.163.com/)

- _**MUSIC163_ACCOUNT_LIST**_.music163_phone: 网易云音乐手机号
- _**MUSIC163_ACCOUNT_LIST**_.music163_password: 网易云音乐手机号对应的密码

#### AcFun 帐号信息

[AcFun](https://www.acfun.cn/)

- _**ACFUN_ACCOUNT_LIST**_.acfun_phone: AcFun 手机号
- _**ACFUN_ACCOUNT_LIST**_.acfun_password: AcFun 手机号对应的密码

#### 天翼云盘 帐号信息

[天翼云盘](https://cloud.189.cn/)

- _**CLOUD189_ACCOUNT_LIST**_.cloud189_phone: 天翼云盘 手机号
- _**CLOUD189_ACCOUNT_LIST**_.cloud189_password: 天翼云盘 手机号对应的密码

### APP 抓包

#### 喜马拉雅极速版 Cookie 参数获取

抓包 APP 中域名为 `m.ximalaya.com` 中的 `cookie` 即可

#### Fa米家 Cookie 等参数获取

抓包 APP 的请求中的 `headers` 信息中提取 `token`、`deviceId`、`cookie` 即可

#### 联通营业厅参数获取

1. 退出手机营业厅登录，然后开启抓包软件，登录手机营业厅

查找网址为 `https://m.client.10010.com/mobileService/login.htm` 的记录，找到请求内容，将 `simCount` 开始到最后的内容按要求填入 `config.json` 文件。

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

> 请务必到 [http://www.json.cn](http://www.json.cn) 网站检查 `config.json` 文件格式是否正确！

> 请务必到 [http://www.json.cn](http://www.json.cn) 网站检查 `config.json` 文件格式是否正确！

> 请务必到 [http://www.json.cn](http://www.json.cn) 网站检查 `config.json` 文件格式是否正确！


配置文件：`config.json`

```json
{
  "DINGTALK_SECRET": "xxxxxx",
  "DINGTALK_ACCESS_TOKEN": "xxxxxx",
  "SCKEY": "xxxxxx",
  "SENDKEY": "xxxxxx",
  "BARK_URL": "xxxxxx",
  "QMSG_KEY": "xxxxxx",
  "TG_BOT_TOKEN": "xxxxxx",
  "TG_USER_ID": "xxxxxx",
  "COOLPUSHSKEY": "xxxxxx",
  "COOLPUSHQQ": true,
  "COOLPUSHWX": true,
  "COOLPUSHEMAIL": true,
  "CITY_NAME_LIST": [
    "上海"
  ],
  "MOTTO": true,
  "IQIYI_COOKIE_LIST": [
    {
      "iqiyi_cookie": "帐号1 cookie"
    },
    {
      "iqiyi_cookie": "帐号2 cookie"
    }
  ],
  "VQQ_COOKIE_LIST": [
    {
      "vqq_cookie": "帐号1 cookie"
    },
    {
      "vqq_cookie": "帐号2 cookie"
    }
  ],
  "YOUDAO_COOKIE_LIST": [
    {
      "youdao_cookie": "帐号1 cookie"
    },
    {
      "youdao_cookie": "帐号2 cookie"
    }
  ],
  "KGQQ_COOKIE_LIST": [
    {
      "kgqq_cookie": "帐号1 cookie"
    },
    {
      "kgqq_cookie": "帐号2 cookie"
    }
  ],
  "MUSIC163_ACCOUNT_LIST": [
    {
      "music163_phone": "帐号1 手机号",
      "music163_password": "帐号1 密码"
    },
    {
      "music163_phone": "帐号2 手机号",
      "music163_password": "帐号2 密码"
    }
  ],
  "XMLY_COOKIE_LIST": [
    {
      "xmly_cookie": "帐号1 cookie"
    },
    {
      "xmly_cookie": "帐号2 cookie"
    }
  ],
  "ONEPLUSBBS_COOKIE_LIST": [
    {
      "oneplusbbs_cookie": "帐号1 cookie"
    },
    {
      "oneplusbbs_cookie": "帐号2 cookie"
    }
  ],
  "BAIDU_URL_SUBMIT_LIST": [
    {
      "data_url": "https://cdn.jsdelivr.net/gh/Sitoi/Sitoi.github.io/baidu_urls.txt",
      "submit_url": "http://data.zz.baidu.com/urls?site=https://sitoi.cn&token=xxxxxx",
      "times": 10
    },
    {
      "data_url": "帐号2 data_url",
      "submit_url": "帐号2 submit_url",
      "times": 10
    }
  ],
  "FMAPP_ACCOUNT_LIST": [
    {
      "fmapp_token": "帐号1 token",
      "fmapp_cookie": "帐号1 cookie",
      "fmapp_device_id": "帐号1 device_id"
    },
    {
      "fmapp_token": "帐号2 token",
      "fmapp_cookie": "帐号2 cookie",
      "fmapp_device_id": "帐号2 device_id"
    }
  ],
  "TIEBA_COOKIE_LIST": [
    {
      "tieba_cookie": "帐号1 cookie"
    },
    {
      "tieba_cookie": "帐号2 cookie"
    }
  ],
  "BILIBILI_COOKIE_LIST": [
    {
      "bilibili_cookie": "帐号1 cookie",
      "coin_num": 0,
      "coin_type": 1,
      "silver2coin": true
    },
    {
      "bilibili_cookie": "帐号2 cookie",
      "coin_num": 0,
      "coin_type": 1,
      "silver2coin": true
    }
  ],
  "LIANTONG_ACCOUNT_LIST": [
    {
      "data": "simCount=1&version=iphone_c@8.0100&mobile=xxxxxx&netWay=wifi&isRemberPwd=false&appId=xxxxxx&deviceId=xxxxxx&pip=192.168.1.1&password=xxxxxx&deviceOS=14.3&deviceBrand=iphone&deviceModel=iPhone&remark4=&keyVersion=2&deviceCode=xxxxxx"
    },
    {
      "data": "帐号2 信息"
    }
  ],
  "V2EX_COOKIE_LIST": [
    {
      "v2ex_cookie": "帐号1 cookie"
    },
    {
      "v2ex_cookie": "帐号2 cookie"
    }
  ],
  "WWW2NZZ_COOKIE_LIST": [
    {
      "www2nzz_cookie": "帐号1 cookie"
    },
    {
      "www2nzz_cookie": "帐号2 cookie"
    }
  ],
  "SMZDM_COOKIE_LIST": [
    {
      "smzdm_cookie": "账号1 cookie"
    },
    {
      "smzdm_cookie": "账号2 cookie"
    }
  ],
  "MIMOTION_ACCOUNT_LIST": [
    {
      "mimotion_phone": "账号1",
      "mimotion_password": "账号1 密码",
      "mimotion_min_step": "账号1 最小步数",
      "mimotion_max_step": "账号1 最大步数"
    },
    {
      "mimotion_phone": "账号2",
      "mimotion_password": "账号2 密码",
      "mimotion_min_step": "账号2 最小步数",
      "mimotion_max_step": "账号2 最大步数"
    }
  ],
  "ACFUN_ACCOUNT_LIST": [
    {
      "acfun_phone": "帐号1 手机号",
      "acfun_password": "帐号1 密码"
    },
    {
      "acfun_phone": "帐号2 手机号",
      "acfun_password": "帐号2 密码"
    }
  ],
  "CLOUD189_ACCOUNT_LIST": [
    {
      "cloud189_phone": "帐号1 手机号",
      "cloud189_password": "帐号1 密码"
    },
    {
      "cloud189_phone": "帐号2 手机号",
      "cloud189_password": "帐号2 密码"
    }
  ],
  "WPS_COOKIE_LIST": [
    {
      "wps_cookie": "帐号1 cookie"
    },
    {
      "wps_cookie": "帐号2 cookie"
    }
  ],
  "POJIE_COOKIE_LIST": [
    {
      "pojie_cookie": "帐号1 cookie"
    },
    {
      "pojie_cookie": "帐号2 cookie"
    }
  ]
}
```