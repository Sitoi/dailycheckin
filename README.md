# 每日签到集合

基于腾讯云函数的每日签到脚本（支持多账号使用）

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

## TODO

- [ ] 添加其他通知服务
- [ ] 添加 GitHub Actions 使用
- [ ] 添加新的签到脚本，请到 [ISSUE](https://github.com/Sitoi/DailyCheckIn/issues) 中提交

## 使用方法

### 方法一: 本地使用

1. 根据各个使用文档获取对应的参数，并修改 `config.json`
2. 安装 Pypi 依赖包
3. 运行 `index.py` 即可

### 方法二: 腾讯云函数使用

> （腾讯云函数相关教程请自行百度）

1. [点击下载代码](https://github.com/Sitoi/DailyCheckIn/archive/main.zip)
2. 解压代码压缩包
3. 根据各个使用文档获取对应的参数，并修改 `config.json`
4. 上传至【腾讯云函数】
5. 配置定时触发器

### 方法三: GitHub Action 使用

TODO

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
  "baidu_url_submit": [
    {
      "data_url": "https://cdn.jsdelivr.net/gh/Sitoi/Sitoi.github.io/baidu_urls.txt",
      "submit_url": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
      "times": 10
    }
  ]
}
```

### dingtalk

|Name|归属|属性|说明|
|:---:|:---:|:---:|:---|
|dingtalk.`dingtalk_secret`|钉钉推送|非必须|钉钉推送[官方文档](https://ding-doc.dingtalk.com/doc#/serverapi2/qf2nxq) 密钥，机器人安全设置页面，加签一栏下面显示的 `SEC` 开头的字符串, 注:填写了 `DD_BOT_TOKEN` 和 `DD_BOT_SECRET`，钉钉机器人安全设置只需勾选`加签`即可，其他选项不要勾选|
|dingtalk.`dingtalk_access_token`|钉钉推送|非必须|钉钉推送[官方文档](https://ding-doc.dingtalk.com/doc#/serverapi2/qf2nxq) ,只需 `https://oapi.dingtalk.com/robot/send?access_token=XXX` 等于符号后面的 `XXX`， 注：如果钉钉推送只填写 `DD_BOT_TOKEN`，那么安全设置需勾选`自定义关键词`，内容输入输入`账号`即可，其他安全设置不要勾选|
|iqiyi.`iqiyi_cookie`|爱奇艺|非必须|[爱奇艺](https://www.iqiyi.com/) 帐号的 cookie 信息|
|vqq.`vqq_cookie`|腾讯视频|非必须|[腾讯视频](https://v.qq.com/) 帐号的 cookie 信息|
|52pojie.`pojie_cookie`|吾爱破解|非必须|[吾爱破解](https://www.52pojie.cn/index.php) 帐号的 cookie 信息|
|youdao.`youdao_cookie`|有道云笔记|非必须|[有道云笔记](https://note.youdao.com/web/) 帐号的 cookie 信息|
|kgqq.`kgqq_cookie`|全民K歌|非必须|[全民K歌](https://kg.qq.com/index-pc.html) 帐号的 cookie 信息|
|music163.`music163_phone`|网易云音乐|非必须|[网易云音乐](https://music.163.com/) 帐号的手机号|
|music163.`music163_password`|网易云音乐|非必须|[网易云音乐](https://music.163.com/) 帐号的密码|
|baidu_url_submit.`data_url`|百度搜索资源平台|非必须|提交网站的 URL 链接，参考：[baidu_urls.txt](https://cdn.jsdelivr.net/gh/Sitoi/Sitoi.github.io/baidu_urls.txt)|
|baidu_url_submit.`submit_url`|百度搜索资源平台|非必须|[百度搜索资源平台](https://ziyuan.baidu.com/site/index#/) 提交百度网站的目标 URL，参考格式：`http://data.zz.baidu.com/urls?site=https://sitoi.cn&token=xxxxx`|
|`weather`|每日天气|非必须|填写城市名称，点击查看[城市名称列表](./weather/city.json)|
|`motto`|每日一句|非必须|是否开启默认为 false|