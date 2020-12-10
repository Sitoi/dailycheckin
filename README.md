# 每日签到集合

基于【腾讯云函数】/【GitHub Actions】的每日签到脚本（支持多账号使用）

## 签到列表

- [x] 爱奇艺每日签到: 签7天奖1天，14天奖2天，28天奖7天；日常任务；随机成长值
- [x] 全民K歌每日签到: 每日签到获取鲜花
- [x] 百度站点每日提交: 每日提交网站页面供百度收录
- [x] 腾讯视频每日签到: 每日两次腾讯视频签到获取成长值
- [x] 吾爱破解每日签到: 每日签到获取2枚吾爱币
- [x] 有道云笔记每日签到: 每日签到获取存储空间
- [x] 网易云音乐每日签到升级: 每日自动登录签到 + 刷歌 310 首
- [x] 每日天气预报: 可以获取指定的多个城市天气信息
- [x] 每日一句: 从词霸中获取每日一句，带英文
- [x] 一加手机社区官方论坛: 论坛每日签到 + 10 次抽奖

## 支持的通知列表

- [x] dingtalk（钉钉）
- [x] server 酱（微信）
- [x] qmsg 酱（QQ）
- [x] telegram（TG）

## TODO

- [ ] 如有签到脚本需求，请到 [ISSUE](https://github.com/Sitoi/DailyCheckIn/issues) 中提交

## 使用方法

### 方法一: 本地使用

1. 根据各个使用文档获取对应的参数，并修改 `config.json`
2. 安装 Pypi 依赖包
3. 运行 `index.py` 即可

> 对单个签到进行测试，配置好 `config.json` 进入对应的签到脚本目录运行即可

### 方法二: 腾讯云函数使用

> （腾讯云函数相关教程请自行百度）

1. [点击下载代码](https://github.com/Sitoi/DailyCheckIn/archive/main.zip)
2. 解压代码压缩包
3. 根据各个使用文档获取对应的参数，并修改 `config.json`
4. 上传至【腾讯云函数】
5. 配置定时触发器

#### TODO

喜马拉雅极速版脚本运行方式

### 方法三: GitHub Action 使用

#### 环境变量说明

> 可以将 json 类型的数据到 [Json.cn](http://www.json.cn/) 网站格式化一下，确保数据格式的准确性

|Secret|归属|属性|说明|例子|
|:---:|:---:|:---:|:---|:---|
|DINGTALK_SECRET|钉钉推送|非必须|钉钉推送[官方文档](https://ding-doc.dingtalk.com/doc#/serverapi2/qf2nxq) 密钥，机器人安全设置页面，加签一栏下面显示的 `SEC` 开头的字符串, 注:填写了 `DD_BOT_TOKEN` 和 `DD_BOT_SECRET`，钉钉机器人安全设置只需勾选`加签`即可，其他选项不要勾选|xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx|
|DINGTALK_ACCESS_TOKEN|钉钉推送|非必须|钉钉推送[官方文档](https://ding-doc.dingtalk.com/doc#/serverapi2/qf2nxq) ,只需 `https://oapi.dingtalk.com/robot/send?access_token=XXX` 等于符号后面的 `XXX`， 注：如果钉钉推送只填写 `DD_BOT_TOKEN`，那么安全设置需勾选`自定义关键词`，内容输入输入`账号`即可，其他安全设置不要勾选|xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx|
|SCKEY|server 酱推送|非必须|server 酱推送[官方文档](https://sc.ftqq.com/3.version) ,填写 `SCKEY` 代码即可|xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx|
|QMSG_KEY|qmsg 酱推送|非必须|qmsg 酱推送[官方文档](https://qmsg.zendee.cn/index.html) ,填写 `KEY` 代码即可|xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx|
|TG_BOT_TOKEN|telegram 推送|非必须|telegram 推送 `tg_bot_token`|xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx|
|TG_USER_ID|telegram 推送|非必须|telegram 推送 `tg_user_id`|xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx|
|IQIYI_COOKIE_LIST|爱奇艺|非必须|[爱奇艺](https://www.iqiyi.com/) 帐号的 cookie 信息列表 参考 `config.json`|[ { "iqiyi_cookie": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" } ]|
|VQQ_COOKIE_LIST|腾讯视频|非必须|[腾讯视频](https://v.qq.com/) 帐号的 cookie 信息|[ { "vqq_cookie": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" } ]|
|POJIE_COOKIE_LIST|吾爱破解|非必须|[吾爱破解](https://www.52pojie.cn/index.php) 帐号的 cookie 信息|[ { "pojie_cookie": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" } ]|
|YOUDAO_COOKIE_LIST|有道云笔记|非必须|[有道云笔记](https://note.youdao.com/web/) 帐号的 cookie 信息|[ { "youdao_cookie": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" } ]|
|KGQQ_COOKIE_LIST|全民K歌|非必须|[全民K歌](https://kg.qq.com/index-pc.html) 帐号的 cookie 信息|[ { "kgqq_cookie": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" } ]|
|MUSIC163_ACCOUNT_LIST|网易云音乐|非必须|[网易云音乐](https://music.163.com/) 帐号的手机号,密码|[ { "music163_phone": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", "music163_password": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" } ]|
|BAIDU_URL_SUBMIT_LIST|百度搜索资源平台|非必须|百度链接提交的相关参数|[ { "data_url": "https://cdn.jsdelivr.net/gh/Sitoi/Sitoi.github.io/baidu_urls.txt", "submit_url": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", "times": 10 } ]|
|CITY_NAME_LIST|每日天气|非必须|填写城市名称，点击查看[城市名称列表](./weather/city.json)|["上海"]|
|MOTTO|每日一句|非必须|是否开启默认为 false|true|
|XMLY_COOKIE_LIST|喜马拉雅极速版|非必须|喜马拉雅极速版 cookie|[ { "xmly_cookie": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" } ]|
|ONEPLUSBBS_COOKIE_LIST|一加手机社区官方论坛|非必须|[一加手机社区官方论坛](https://www.oneplusbbs.com/) 账户的 cookie|[ { "oneplusbbs_cookie": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" } ]|

## 获取 Cookie 教程（以爱奇艺为例）

![获取 cookie 教程](./img/iqiyi_cookie.png)

1. 进入[爱奇艺（IQIYI）官网](https://www.iqiyi.com/)
2. 按 `F12` 打开开发者工具，刷新页面
3. 点击 `Network` 标签
4. 选择 `Doc` 标签
5. 选中 `www.iqiyi.com`
6. 下滑找到 `cookie` 全选复制即可

## 配置说明

配置文件：`config.json`

**示例**:

```json
{
  "dingtalk": {
    "dingtalk_secret": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    "dingtalk_access_token": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
  },
  "server": {
    "sckey": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
  },
  "qmsg": {
    "qmsg_key": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
  },
  "telegram": {
    "tg_bot_token": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    "tg_user_id": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
  },
  "weather": [
    "上海"
  ],
  "motto": true,
  "iqiyi": [
    {
      "iqiyi_cookie": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    }
  ],
  "vqq": [
    {
      "vqq_cookie": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    }
  ],
  "52pojie": [
    {
      "pojie_cookie": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    }
  ],
  "youdao": [
    {
      "youdao_cookie": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    }
  ],
  "kgqq": [
    {
      "kgqq_cookie": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    }
  ],
  "music163": [
    {
      "music163_phone": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
      "music163_password": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    }
  ],
  "xmly": [
    {
      "xmly_cookie": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    }
  ],
  "oneplusbbs": [
    {
      "oneplusbbs_cookie": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    }
  ],
  "baidu_url_submit": [
    {
      "data_url": "https://cdn.jsdelivr.net/gh/Sitoi/Sitoi.github.io/baidu_urls.txt",
      "submit_url": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
      "times": 10
    }
  ]
}
```

### 参数说明

|Name|归属|属性|说明|
|:---:|:---:|:---:|:---|
|dingtalk.`dingtalk_secret`|钉钉推送|非必须|钉钉推送[官方文档](https://ding-doc.dingtalk.com/doc#/serverapi2/qf2nxq) 密钥，机器人安全设置页面，加签一栏下面显示的 `SEC` 开头的字符串, 注:填写了 `DD_BOT_TOKEN` 和 `DD_BOT_SECRET`，钉钉机器人安全设置只需勾选`加签`即可，其他选项不要勾选|
|dingtalk.`dingtalk_access_token`|钉钉推送|非必须|钉钉推送[官方文档](https://ding-doc.dingtalk.com/doc#/serverapi2/qf2nxq) ,只需 `https://oapi.dingtalk.com/robot/send?access_token=XXX` 等于符号后面的 `XXX`， 注：如果钉钉推送只填写 `DD_BOT_TOKEN`，那么安全设置需勾选`自定义关键词`，内容输入输入`账号`即可，其他安全设置不要勾选|
|server.`sckey`|server 酱推送|非必须|server 酱推送[官方文档](https://sc.ftqq.com/3.version) ,填写 `SCKEY` 代码即可|
|qmsg.`qmsg_key`|qmsg 酱推送|非必须|qmsg 酱推送[官方文档](https://qmsg.zendee.cn/index.html) ,填写 `KEY` 代码即可|
|telegram.`tg_bot_token`|telegram 推送|非必须|telegram 推送 `tg_bot_token`|
|telegram.`tg_user_id`|telegram 推送|非必须|telegram 推送 `tg_user_id`|
|iqiyi.`iqiyi_cookie`|爱奇艺|非必须|[爱奇艺](https://www.iqiyi.com/) 帐号的 cookie 信息|
|vqq.`vqq_cookie`|腾讯视频|非必须|[腾讯视频](https://v.qq.com/) 帐号的 cookie 信息|
|52pojie.`pojie_cookie`|吾爱破解|非必须|[吾爱破解](https://www.52pojie.cn/index.php) 帐号的 cookie 信息|
|youdao.`youdao_cookie`|有道云笔记|非必须|[有道云笔记](https://note.youdao.com/web/) 帐号的 cookie 信息|
|kgqq.`kgqq_cookie`|全民K歌|非必须|[全民K歌](https://kg.qq.com/index-pc.html) 帐号的 cookie 信息|
|music163.`music163_phone`|网易云音乐|非必须|[网易云音乐](https://music.163.com/) 帐号的手机号|
|music163.`music163_password`|网易云音乐|非必须|[网易云音乐](https://music.163.com/) 帐号的密码|
|baidu_url_submit.`data_url`|百度搜索资源平台|非必须|提交网站的 URL 链接，参考：[baidu_urls.txt](https://cdn.jsdelivr.net/gh/Sitoi/Sitoi.github.io/baidu_urls.txt)|
|baidu_url_submit.`submit_url`|百度搜索资源平台|非必须|[百度搜索资源平台](https://ziyuan.baidu.com/site/index#/) 提交百度网站的目标 URL，参考格式：`http://data.zz.baidu.com/urls?site=https://sitoi.cn&token=xxxxx`|
|baidu_url_submit.`times`|百度搜索资源平台|非必须|每日对同一个网站提交次数|
|`weather`|每日天气|非必须|填写城市名称，点击查看[城市名称列表](./weather/city.json)|
|`motto`|每日一句|非必须|是否开启默认为 false|
|xmly.`xmly_cookie`|喜马拉雅极速版|非必须|喜马拉雅极速版 cookie|
|oneplusbbs.`oneplusbbs_cookie`|一加手机社区官方论坛|非必须|[一加手机社区官方论坛](https://www.oneplusbbs.com/) 账户的 cookie|

## 鸣谢

[@Zero-S1](https://github.com/Zero-S1/xmly_speed) - 喜马拉雅极速版签到