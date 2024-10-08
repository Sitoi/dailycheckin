<div align="center">

<img src="https://socialify.git.ci/Sitoi/dailycheckin/image?font=Rokkitt&forks=1&issues=1&language=1&name=1&owner=1&pattern=Circuit%20Board&pulls=1&stargazers=1&theme=Dark">

<h1>DailyCheckIn</h1>

基于「Docker」/「青龙面板」/「群晖」/「本地」的每日签到脚本

<!-- SHIELD GROUP -->
<div id="shield">

[![][github-releases-shield]][github-releases-link]
[![][pypi-version-shield]][pypi-version-link]
[![][github-release-date-shield]][github-release-date-link]
[![][github-stars-shield]][github-stars-link]
[![][github-forks-shield]][github-forks-link]
[![][github-issues-shield]][github-issues-link]
[![][github-contributors-shield]][github-contributors-link]

[![][python-version-shield]][python-version-link]
[![][pypi-dm-shield]][pypi-dm-link]
[![][docker-pull-shield]][docker-pull-link]
[![][docker-size-shield]][docker-size-link]
[![][docker-stars-shield]][docker-stars-link]
[![][github-license-shield]][github-license-link]

<!-- SHIELD GROUP -->
</div>
</div>


## 如何使用本仓库内容

在青龙创建一个订阅

拉库命令 `ql repo https://github.com/Fansirsqi/dailycheckin.git null null null main`

配置执行后运行的命令
`pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple && pip install requests pycrypto pycryptodome && cd /ql/data/repo/Fansirsqi_dailycheckin_main && python setup.py develop`

在脚本管理根目录创建`config.json`配置文件可以参考官方配置，这里只是增加了一段

[配置示例](https://gist.githubusercontent.com/Fansirsqi/9e238bb3e432fdb7bee1caa46da81519/raw/5a7d599b526564c68b0120e9a275ce6f414757df/config.json)

```
,
    "TESTNOTICE": [
      {
        "test1": "test1mesg"
      }
    ]
```
强烈建议您在`https://www.json.cn/`这个网站检查您的配置

最后在定时任务里创建一个测试任务

`task dailycheckin --include TESTNOTICE`运行并查看日志

![1715763862230.png](https://pic2.ziyuan.wang/user/fansir/2024/05/1715763862230_5344cb6724871.png)

![1715763931708.png](https://pic2.ziyuan.wang/user/fansir/2024/05/1715763931708_ec7c766df87c4.png)

## ✨ 特性

- 📦 支持 Pypi 包安装
- 💻 支持多个平台部署
- ⚙️ 支持多个平台签到
- 📢 支持多个平台通知
- ♾️ 支持多个账号签到
- 🕙 支持定时任务设置
- 🆙 支持项目自动更新

## 🦄 教程

[https://sitoi.github.io/dailycheckin/](https://sitoi.github.io/dailycheckin/)

## 🧾 列表

🟢: 正常运行 🔴: 脚本暂不可用 🔵: 可以执行(需更新) 🟡: 待测试 🟤: 看脸

| 状态 | 任务名称 | 名称网站                                                   | 检查日期 | 备注                                                                                                                                           |
| ---- | -------- | ---------------------------------------------------------- | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| 🟢️  | KGQQ     | [全民 K 歌](https://kg.qq.com/index-pc.html)               | 24.02.20 | 每日签到获取鲜花 每日大约 120 鲜花左右                                                                                                         |
| 🟢️  | YOUDAO   | [有道云笔记](https://note.youdao.com/web/)                 | 24.02.20 | 每日签到获取存储空间                                                                                                                           |
| 🟢️  | TIEBA    | [百度贴吧](https://tieba.baidu.com/index.html)             | 24.02.20 | 贴吧每日签到                                                                                                                                   |
| 🟢️  | BILIBILI | [BiliBili](https://www.bilibili.com/)                      | 24.02.20 | 直播签到，漫画签到，每日经验任务，自动投币，银瓜子换硬币等功能                                                                                 |
| 🟢️  | V2EX     | [V2EX](https://www.v2ex.com/)                              | 24.02.20 | 铜币奖励                                                                                                                                       |
| 🟢️  | ACFUN    | [AcFun](https://www.acfun.cn/)                             | 24.02.20 | 每日签到香蕉                                                                                                                                   |
| 🟢️  | IQIYI    | [爱奇艺](https://www.iqiyi.com/)                           | 24.02.20 | ① 满签得 7 天会员；② 日常任务 4 成长值；③ 爱奇艺刷时长任务，10 成长值；④ 每日签到随机成长值；⑤ 抽白金会员 5 次；⑥ 摇一摇抽奖 3 次；⑦ 抽奖 3 次 |
| 🟢️  | SMZDM    | [什么值得买](https://www.smzdm.com/)                       | 24.02.20 | 签到和抽奖                                                                                                                                     |
| 🟢️  | ALIYUN   | [阿里云盘](https://www.aliyundrive.com/drive/)             | 24.02.20 | 签到获取免费会员和空间                                                                                                                         |
| 🟢️  | ENSHAN   | [恩山无线论坛](https://www.right.com.cn/forum/)            | 24.02.20 | 签到获取硬币和积分                                                                                                                             |
| 🟢️  | AOLAXING | [奥拉星](http://www.100bt.com/m/creditMall/?gameId=2#task) | 24.02.20 | 签到获取积分                                                                                                                                   |
| 🟢️  | IMAOTAI  | i 茅台                                                     | 24.02.20 | 申购生肖茅台                                                                                                                                   |
| 🟤   | MIMOTION | 小米运动                                                   | 24.02.20 | 每日小米运动刷步数                                                                                                                             |
| 🟢️  | BAIDU    | [百度站点](https://ziyuan.baidu.com/site/index#/)          | 24.02.20 | 提交网站页面供百度收录                                                                                                                         |

## 💬 通知列表

- [PushDeer](https://www.pushdeer.com/)
- [wxPusher](https://wxpusher.zjiecode.com/docs/#/)

> [PushDeer预览](https://pic2.ziyuan.wang/user/fansir/2024/05/1715593565981_39b4eff978354.png)
>
> [wxPusher预览](https://pic2.ziyuan.wang/user/fansir/2024/05/1715593114657_e53ec9acf7e1e.png)
>
> 新增以上渠道配置如下

```json
{
    "PUSHKEY": "", //PushDeer 的 pushkey
    "WXPUSHER_TK": "", //wxpusher_token
    "WXPUSHER_UID": "", //wxpusher_uid
    //以上是新增内容
    "BARK_URL": "",
    ...
}
```


- dingtalk（钉钉）
- 企业微信群机器人（企业微信）
- 企业微信应用消息（企业微信）
- telegram（TG）
- Bark（iOS）
- server 酱（微信）
- server 酱 TURBO（微信）
- pushplus（微信）
- Cool Push（QQ,微信,邮箱）
- qmsg 酱（QQ）
- 飞书（飞书）

## 🤝 参与贡献

我们非常欢迎各种形式的贡献。如果你对贡献代码感兴趣，可以查看我们的 GitHub [Issues][github-issues-link]，大展身手，向我们展示你的奇思妙想。

[![][pr-welcome-shield]][pr-welcome-link]

### 💗 感谢我们的贡献者

[![][github-contrib-shield]][github-contrib-link]

## ✨ Star 数

[![][starchart-shield]][starchart-link]

---

## 📝 License

Copyright © 2021 [Sitoi][profile-link]. <br />
This project is [MIT](https://github.com/Sitoi/dailycheckin/blob/main/LICENSE) licensed.

<!-- LINK GROUP -->

[profile-link]: https://github.com/sitoi
[github-codespace-link]: https://codespaces.new/sitoi/dailycheckin
[github-codespace-shield]: https://github.com/sitoi/dailycheckin/blob/main/images/codespaces.png?raw=true
[github-contributors-link]: https://github.com/sitoi/dailycheckin/graphs/contributors
[github-contributors-shield]: https://img.shields.io/github/contributors/sitoi/dailycheckin?color=c4f042&labelColor=black&style=flat-square
[github-forks-link]: https://github.com/sitoi/dailycheckin/network/members
[github-forks-shield]: https://img.shields.io/github/forks/sitoi/dailycheckin?color=8ae8ff&labelColor=black&style=flat-square
[github-issues-link]: https://github.com/sitoi/dailycheckin/issues
[github-issues-shield]: https://img.shields.io/github/issues/sitoi/dailycheckin?color=ff80eb&labelColor=black&style=flat-square
[github-license-link]: https://github.com/sitoi/dailycheckin/blob/main/LICENSE
[github-license-shield]: https://img.shields.io/github/license/sitoi/dailycheckin?labelColor=black&style=flat-square
[github-stars-link]: https://github.com/sitoi/dailycheckin/stargazers
[github-stars-shield]: https://img.shields.io/github/stars/sitoi/dailycheckin?color=ffcb47&labelColor=black&style=flat-square
[github-releases-link]: https://github.com/sitoi/dailycheckin/releases
[github-releases-shield]: https://img.shields.io/github/v/release/sitoi/dailycheckin?labelColor=black&style=flat-square
[github-release-date-link]: https://github.com/sitoi/dailycheckin/releases
[github-release-date-shield]: https://img.shields.io/github/release-date/sitoi/dailycheckin?labelColor=black&style=flat-square
[pr-welcome-link]: https://github.com/sitoi/dailycheckin/pulls
[pr-welcome-shield]: https://img.shields.io/badge/🤯_pr_welcome-%E2%86%92-ffcb47?labelColor=black&style=for-the-badge
[github-contrib-link]: https://github.com/sitoi/dailycheckin/graphs/contributors
[github-contrib-shield]: https://contrib.rocks/image?repo=sitoi%2Fdailycheckin
[docker-pull-shield]: https://img.shields.io/docker/pulls/sitoi/dailycheckin?labelColor=black&style=flat-square
[docker-pull-link]: https://hub.docker.com/repository/docker/sitoi/dailycheckin
[docker-size-shield]: https://img.shields.io/docker/image-size/sitoi/dailycheckin?labelColor=black&style=flat-square
[docker-size-link]: https://hub.docker.com/repository/docker/sitoi/dailycheckin
[docker-stars-shield]: https://img.shields.io/docker/stars/sitoi/dailycheckin?labelColor=black&style=flat-square
[docker-stars-link]: https://hub.docker.com/repository/docker/sitoi/dailycheckin
[pypi-dm-shield]: https://img.shields.io/pypi/dm/dailycheckin?label=pypi&labelColor=black&style=flat-square
[pypi-dm-link]: https://pypi.org/project/dailycheckin/
[python-version-link]: https://pypi.org/project/dailycheckin/
[python-version-shield]: https://img.shields.io/pypi/pyversions/dailycheckin?labelColor=black&style=flat-square
[pypi-version-shield]: https://img.shields.io/pypi/v/dailycheckin?labelColor=black&style=flat-square
[pypi-version-link]: https://pypi.org/project/dailycheckin/
[starchart-shield]: https://api.star-history.com/svg?repos=sitoi/dailycheckin&type=Date
[starchart-link]: https://star-history.com/#sitoi/dailycheckin&Date
