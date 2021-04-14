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

- value: config.json 配置文件全部

## 三、Star 一下，立即执行，观察运行情况

点一下自己 fork 项目的 star 立即执行

## 四、开启定时运行

必须修改一次文件（比如自己库中的 `README.md` 文件）才能定时运行