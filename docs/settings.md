# 配置说明

配置文件：`config.json`

**示例**:

```json
{
  "DINGTALK_SECRET": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
  "DINGTALK_ACCESS_TOKEN": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
  "SCKEY": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
  "QMSG_KEY": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
  "TG_BOT_TOKEN": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
  "TG_USER_ID": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
  "CITY_NAME_LIST": [
    "上海"
  ],
  "MOTTO": true,
  "IQIYI_COOKIE_LIST": [
    {
      "iqiyi_cookie": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    }
  ],
  "VQQ_COOKIE_LIST": [
    {
      "vqq_cookie": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    }
  ],
  "POJIE_COOKIE_LIST": [
    {
      "pojie_cookie": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    }
  ],
  "YOUDAO_COOKIE_LIST": [
    {
      "youdao_cookie": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    }
  ],
  "KGQQ_COOKIE_LIST": [
    {
      "kgqq_cookie": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    }
  ],
  "MUSIC163_ACCOUNT_LIST": [
    {
      "music163_phone": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
      "music163_password": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    }
  ],
  "XMLY_COOKIE_LIST": [
    {
      "xmly_cookie": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    }
  ],
  "ONEPLUSBBS_COOKIE_LIST": [
    {
      "oneplusbbs_cookie": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    }
  ],
  "QQREAD_ACCOUNT_LIST": [
    {
      "qqread_bodys": {
        "common": {
          "appid": "xxxxxxxxxx",
          "areaid": "xxxxxxxxxx",
          "qq_ver": "xxxxxxxxxx",
          "os_ver": "xxxxxxxxxx",
          "mp_ver": "xxxxxxxxxx",
          "mpos_ver": "xxxxxxxxxx",
          "brand": "xxxxxxxxxx",
          "model": "xxxxxxxxxx",
          "screenWidth": "xxxxxxxxxx",
          "screenHeight": "xxxxxxxxxx",
          "windowWidth": "xxxxxxxxxx",
          "windowHeight": "xxxxxxxxxx",
          "openid": "xxxxxxxxxx",
          "guid": "xxxxxxxxxx",
          "session": "xxxxxxxxxx",
          "scene": "xxxxxxxxxx",
          "source": "xxxxxxxxxx",
          "hasRedDot": "xxxxxxxxxx",
          "missions": "xxxxxxxxxx",
          "caseID": "xxxxxxxxxx"
        },
        "dataList": [
          {
            "click1": "xxxxxxxxxx",
            "click2": "xxxxxxxxxx",
            "route": "xxxxxxxxxx",
            "refer": "xxxxxxxxxx",
            "options": {
              "bid": "xxxxxxxxxx",
              "cid": "xxxxxxxxxx"
            },
            "dis": 1607589409986,
            "ext6": 26,
            "eventID": "xxxxxxxxxx",
            "type": "xxxxxxxxxx",
            "ccid": 1,
            "bid": "xxxxxxxxxx",
            "bookStatus": 1,
            "bookPay": 0,
            "chapterStatus": 0,
            "ext1": {
              "font": 18,
              "bg": 0,
              "pageMode": 1
            },
            "from": "xxxxxxxxxx"
          }
        ]
      },
      "qqread_headers": {
        "Accept": "*/*",
        "ywsession": "xxxxxxxxxx",
        "Connection": "keep-alive",
        "Content-Type": "application/json",
        "Cookie": "ywguid=xxxxxxxxxx",
        "Host": "mqqapi.reader.qq.com",
        "User-Agent": "xxxxxxxxxx",
        "Referer": "xxxxxxxxxx",
        "Accept-Language": "zh-cn",
        "Accept-Encoding": "gzip, deflate, br",
        "mpversion": "0.32.5"
      },
      "qqread_timeurl": "https://mqqapi.reader.qq.com/mqq/addReadTimeWithBid?xxxxxxxxxx"
    }
  ],
  "BAIDU_URL_SUBMIT_LIST": [
    {
      "data_url": "https://cdn.jsdelivr.net/gh/Sitoi/Sitoi.github.io/baidu_urls.txt",
      "submit_url": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
      "times": 10
    }
  ]
}
```

## 参数说明

> _**斜体加粗大写英文字母**_ 表示 GitHub Actions Secrets 环境变量名称，内容直接复制 _**斜体加粗大写英文字母 key**_  对应的 value

> _**斜体加粗大写英文字母**_ 表示 GitHub Actions Secrets 环境变量名称，内容直接复制 _**斜体加粗大写英文字母 key**_  对应的 value

> _**斜体加粗大写英文字母**_ 表示 GitHub Actions Secrets 环境变量名称，内容直接复制 _**斜体加粗大写英文字母 key**_  对应的 value

|Name|归属|属性|说明|
|:---:|:---:|:---:|:---|
|_**DINGTALK_SECRET**_|钉钉推送|非必须|钉钉推送[官方文档](https://ding-doc.dingtalk.com/doc#/serverapi2/qf2nxq) 密钥，机器人安全设置页面，加签一栏下面显示的 `SEC` 开头的字符串, 注:填写了 `DD_BOT_TOKEN` 和 `DD_BOT_SECRET`，钉钉机器人安全设置只需勾选`加签`即可，其他选项不要勾选|
|_**DINGTALK_ACCESS_TOKEN**_|钉钉推送|非必须|钉钉推送[官方文档](https://ding-doc.dingtalk.com/doc#/serverapi2/qf2nxq) ,只需 `https://oapi.dingtalk.com/robot/send?access_token=XXX` 等于符号后面的 `XXX`|
|_**SCKEY**_|server 酱推送|非必须|server 酱推送[官方文档](https://sc.ftqq.com/3.version) ,填写 `SCKEY` 代码即可|
|_**QMSG_KEY**_|qmsg 酱推送|非必须|qmsg 酱推送[官方文档](https://qmsg.zendee.cn/index.html) ,填写 `KEY` 代码即可|
|_**TG_BOT_TOKEN**_|telegram 推送|非必须|telegram 推送 `TG_BOT_TOKEN`|
|_**TG_USER_ID**_|telegram 推送|非必须|telegram 推送 `TG_USER_ID`|
|_**CITY_NAME_LIST**_|每日天气|非必须|填写城市名称，点击查看[城市名称列表](https://cdn.jsdelivr.net/gh/Sitoi/dailycheckin/weather/city.json)|
|_**MOTTO**_|每日一句|非必须|是否开启默认为 false|
|_**IQIYI_COOKIE_LIST**_.iqiyi_cookie|爱奇艺|非必须|[爱奇艺](https://www.iqiyi.com/) 帐号的 cookie 信息|
|_**VQQ_COOKIE_LIST**_.vqq_cookie|腾讯视频|非必须|[腾讯视频](https://v.qq.com/) 帐号的 cookie 信息|
|_**POJIE_COOKIE_LIST**_.pojie_cookie|吾爱破解|非必须|[吾爱破解](https://www.52pojie.cn/index.php) 帐号的 cookie 信息|
|_**YOUDAO_COOKIE_LIST**_.youdao_cookie|有道云笔记|非必须|[有道云笔记](https://note.youdao.com/web/) 帐号的 cookie 信息|
|_**KGQQ_COOKIE_LIST**_.kgqq_cookie|全民K歌|非必须|[全民K歌](https://kg.qq.com/index-pc.html) 帐号的 cookie 信息|
|_**MUSIC163_ACCOUNT_LIST**_.music163_phone|网易云音乐|非必须|[网易云音乐](https://music.163.com/) 帐号的手机号|
|_**MUSIC163_ACCOUNT_LIST**_.music163_password|网易云音乐|非必须|[网易云音乐](https://music.163.com/) 帐号的密码|
|_**XMLY_COOKIE_LIST**_.xmly_cookie|喜马拉雅极速版|非必须|喜马拉雅极速版 cookie|
|_**ONEPLUSBBS_COOKIE_LIST**_.oneplusbbs_cookie|一加手机社区官方论坛|非必须|[一加手机社区官方论坛](https://www.oneplusbbs.com/) 账户的 cookie|
|_**QQREAD_ACCOUNT_LIST**_.qqread_bodys|企鹅读书|非必须|企鹅读书 的请求体|
|_**QQREAD_ACCOUNT_LIST**_.qqread_headers|企鹅读书|非必须|企鹅读书 的请求头|
|_**QQREAD_ACCOUNT_LIST**_.qqread_timeurl|企鹅读书|非必须|企鹅读书 上传阅读时长功能需要的 URL|
|_**BAIDU_URL_SUBMIT_LIST**_.data_url|百度搜索资源平台|非必须|提交网站的 URL 链接|
|_**BAIDU_URL_SUBMIT_LIST**_.submit_url|百度搜索资源平台|非必须|[百度搜索资源平台](https://ziyuan.baidu.com/site/index#/) 提交百度网站的目标 URL|
|_**BAIDU_URL_SUBMIT_LIST**_.times|百度搜索资源平台|非必须|每日对同一个网站提交次数|

## 参数获取方法

### 推送参数

#### 钉钉推送参数获取

[钉钉推送官方文档](https://ding-doc.dingtalk.com/doc#/serverapi2/qf2nxq)

#### Server 酱推送参数获取

[Server 酱官方文档](https://sc.ftqq.com/3.version)

#### Qmsg 酱推送参数获取

[Qmsg 酱官方文档](https://qmsg.zendee.cn/index.html)

#### Telegram 推送参数获取

### 其他参数

#### 城市天气列表

[城市名称列表](https://cdn.jsdelivr.net/gh/Sitoi/dailycheckin/weather/city.json)

#### 每日一句 是否开启

默认为 false。false: 表示关闭；true: 表示开启

### 帐号参数

#### 网易云音乐帐号信息

[网易云音乐](https://music.163.com/)

- _**MUSIC163_ACCOUNT_LIST**_.music163_phone: 网易云音乐手机号
- _**MUSIC163_ACCOUNT_LIST**_.music163_password: 网易云音乐手机号对应的密码

#### 百度站点提交参数获取

[百度搜索资源平台](https://ziyuan.baidu.com/site/index#/)


![获取百度云提交链接教程](https://cdn.jsdelivr.net/gh/Sitoi/dailycheckin/docs/img/submit_url.png)


- _**BAIDU_URL_SUBMIT_LIST**_.data_url: 提交网站的 URL
  链接，参考链接：[https://cdn.jsdelivr.net/gh/Sitoi/Sitoi.github.io/baidu_urls.txt](https://cdn.jsdelivr.net/gh/Sitoi/Sitoi.github.io/baidu_urls.txt)
- _**BAIDU_URL_SUBMIT_LIST**_.submit_url: 提交百度网站的目标
  URL，参考格式：`http://data.zz.baidu.com/urls?site=https://sitoi.cn&token=xxxxx`
- _**BAIDU_URL_SUBMIT_LIST**_.times: 单次任务执行对同一个网站提交次数

### 网页 Cookie 获取

获取 Cookie 教程（以爱奇艺为例）

![获取 cookie 教程](https://cdn.jsdelivr.net/gh/Sitoi/dailycheckin/docs/img/iqiyi_cookie.png)

1. 进入[爱奇艺官网](https://www.iqiyi.com/)
2. 按 `F12` 打开开发者工具，刷新页面
3. 点击 `Network` 标签
4. 选择 `Doc` 标签
5. 选中 `www.iqiyi.com`
6. 下滑找到 `cookie` 全选复制即可

#### 爱奇艺 Cookie 参数获取

[爱奇艺官网](https://www.iqiyi.com/)

#### 腾讯视频 Cookie 参数获取

[腾讯视频官网](https://v.qq.com/)

#### 吾爱破解 Cookie 参数获取

[吾爱破解](https://www.52pojie.cn/index.php)

#### 有道云笔记 Cookie 参数获取

[有道云笔记](https://note.youdao.com/web/)

#### 全民K歌 Cookie 参数获取

[全民K歌](https://kg.qq.com/index-pc.html)

#### 一加手机社区官方论坛 Cookie 参数获取

[一加手机社区官方论坛](https://www.oneplusbbs.com/)

### APP抓包

#### 喜马拉雅极速版 Cookie 参数获取

抓包 APP 中域名为 `m.ximalaya.com` 中的 `cookie` 即可

#### 企鹅读书参数获取

> ⚠️注意: `qqread_bodys` 中的 三个 `bid` 和 `qqread_timeurl` 中的 `bid` 必须是一致的

> ⚠️注意: `qqread_bodys` 中的 三个 `bid` 和 `qqread_timeurl` 中的 `bid` 必须是一致的

> ⚠️注意: `qqread_bodys` 中的 三个 `bid` 和 `qqread_timeurl` 中的 `bid` 必须是一致的

进入 [https://m.q.qq.com/a/s/6fb00f7035f82425df91a5b668f6be8b](https://m.q.qq.com/a/s/6fb00f7035f82425df91a5b668f6be8b) >>
进一本书阅读一会儿 >> 然后退出 >> 获取`qqread_headers` `qqread_bodys` 和 `qqread_timeurl`

##### `qqread_headers`参数格式

匹配链接为 `https://mqqapi.reader.qq.com/mqq/addReadTimeWithBid?.......`

```json
{
  "Accept": "*/*",
  "ywsession": "xxxxxx",
  "Connection": "keep-alive",
  "Content-Type": "application/json",
  "Cookie": "xxxxxx",
  "Host": "mqqapi.reader.qq.com",
  "User-Agent": "QQ/8.4.17.638 CFNetwork/1206 Darwin/20.1.0",
  "Referer": "https://appservice.qq.com/xxxxxx/0.32.5/page-frame.html",
  "Accept-Language": "zh-cn",
  "Accept-Encoding": "gzip, deflate, br",
  "mpversion": "0.32.5"
}
```

##### `qqread_bodys` 参数格式

匹配链接为 `https://mqqapi.reader.qq.com/log/v4/mqq/track`

```json
{
  "common": {
    "appid": 1111111111,
    "areaid": 5,
    "qq_ver": "8.4.17",
    "os_ver": "iOS 14.2",
    "mp_ver": "0.32.5",
    "mpos_ver": "1.21.0",
    "brand": "iPhone",
    "model": "iPhone 11<iPhone12,1>",
    "screenWidth": 414,
    "screenHeight": 896,
    "windowWidth": 414,
    "windowHeight": 813,
    "openid": "xxxxxx",
    "guid": 111111111111,
    "session": "xxxxxx",
    "scene": 2016,
    "source": "xxxxxx",
    "hasRedDot": "false",
    "missions": -1,
    "caseID": -1
  },
  "dataList": [
    {
      "click1": "bookDetail_bottomBar_read_C",
      "click2": "bookLib2_bookList_bookClick_C",
      "route": "pages/book-read/index",
      "refer": "pages/book-detail/index",
      "options": {
        "bid": "888888",
        "cid": "1"
      },
      "dis": 1666666666666,
      "ext6": 26,
      "eventID": "bookRead_show_I",
      "type": "shown",
      "ccid": 1,
      "bid": "888888",
      "bookStatus": 1,
      "bookPay": 0,
      "chapterStatus": 0,
      "ext1": {
        "font": 18,
        "bg": 0,
        "pageMode": 1
      },
      "from": "bookLib2_bookList_bookClick_C_2_888888"
    }
  ]
}
```

##### `qqread_timeurl` 参数格式

匹配链接为 `https://mqqapi.reader.qq.com/mqq/addReadTimeWithBid?.......`

```text
https://mqqapi.reader.qq.com/mqq/addReadTimeWithBid?scene=2016&refer=pages%2Fbook-category%2Findex&bid=888888&readTime=8888&read_type=0&conttype=1&read_status=0&chapter_info=xxxxxx&sp=-1
```