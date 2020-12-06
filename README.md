# 每日签到集合

基于腾讯云函数的每日签到脚本

## 一、功能

- [x] [爱奇艺每日签到使用文档](./iqiyi/README.md): 签7天奖1天，14天奖2天，28天奖7天；日常任务；随机成长值
- [x] [百度站点每日提交使用文档](./baidu_url_submit/README.md): 每日提交网站页面供百度收录

## 二、使用

> 腾讯云函数使用（腾讯云函数相关教程请自行百度）

1. 根据各个使用文档获取对应的参数，并修改 `config.json`
2. 上传至【腾讯云函数】
3. 配置定时触发器

> 本地使用

1. 根据各个使用文档获取对应的参数，并修改 `config.json`
2. 运行 `index.py` 即可

> GitHub Action 使用

TODO

## 配置说明

配置文件：`config.json`

**示例**:

```json
{
  "iqiyi": [
    {
      "iqyi_cookie": "QC005=5e8c9fd4e1235215c70796ebdfb1d944; QC142=zz_"
    }
  ],
  "BaiduUrlSubmit": [
    {
      "data_url": "https://cdn.jsdelivr.net/gh/Sitoi/Sitoi.github.io/baidu_urls.txt",
      "submit_url": "http://data.zz.baidu.com/urls?site=https://sitoi.cn&token=bJIOyR1kxxxxxwu",
      "times": 100
    }
  ],
  "dingtalk": {
    "dingtalk_secret": "SECb7ee6efb290d5497fe1xxx38fd0aa1d18ae47",
    "dingtalk_access_token": "c4eb939ba9e3xxx105448661ffb78eb8155e"
  }
}
```

### dingtalk

钉钉推送配置信息

```json
{
  "dingtalk_secret": "SECb7ee6efb290d5497fe1xxx38fd0aa1d18ae47",
  "dingtalk_access_token": "c4eb939ba9e3xxx105448661ffb78eb8155e"
}
```

> 配置相关文档，请自行百度

- dingtalk_secret: 密钥
- dingtalk_access_token: 只需 `https://oapi.dingtalk.com/robot/send?access_token=XXX` 等于符号后面的 `XXX`

### iqiyi

> 支持多账号

```json
[
  {
    "iqyi_cookie": "QC005=5e8c9fd4e1235215c70796ebdfb1d944; QC142=zz_"
  }
]
```

- iqyi_cookie: iqiyi 帐号的 cookie 信息

### BaiduUrlSubmit

> 支持多账号

```json
[
  {
    "data_url": "https://cdn.jsdelivr.net/gh/Sitoi/Sitoi.github.io/baidu_urls.txt",
    "submit_url": "http://data.zz.baidu.com/urls?site=https://sitoi.cn&token=bJIOyR1kxxxxxwu",
    "times": 100
  }
]
```

- data_url: 获取待提交网站的 URL 链接
- submit_url: 提交百度网站的目标 URL
- times: 每日对同一个网站提交次数