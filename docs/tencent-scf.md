# 腾讯云函数教程

## 方式一、下载到本地修改后上传

> （腾讯云函数相关教程请自行百度）

### 一、下载（Clone）本项目到本地

> ⚠️ 下载的需要解压压缩包

- 下载地址: [https://github.com/Sitoi/DailyCheckIn/archive/main.zip](https://github.com/Sitoi/DailyCheckIn/archive/main.zip)

- Clone 地址: [https://github.com/Sitoi/dailycheckin.git](https://github.com/Sitoi/dailycheckin.git)

### 二、创建并修改 config.json 配置文件

拷贝 `config/config.template.json` 到 `config/config.json` 并修改

参考[配置说明文档](https://sitoi.github.io/dailycheckin/settings/) ，并修改 `config/config.json`

### 三、上传至【腾讯云函数】

云函数 → 函数服务 → 新建 → 自定义创建 → 本地上传文件夹 → 选择带有自定义配置文件的文件夹上传

### 四、配置定时触发器

进入函数 → 触发管理 → 新建触发器 → 安装下图进行配置

![触发器配置](https://cdn.jsdelivr.net/gh/Sitoi/dailycheckin/docs/img/scf_timer.png)

## 方式二、配置 Secrets 参数 基于 GitHub Action 上传致腾讯云函数

### 一、将需要签到的 cookie 账号信息填入 GitHub Actions Secrets 变量里

参考: [GitHub Actions 使用教程](https://sitoi.github.io/dailycheckin/github-actions/)

### 二、多配置腾讯云函数相关的两个参数

- TENCENT_SECRET_ID
- TENCENT_SECRET_KEY

### 三、运行相关的 GitHub Actions 进行部署

- 根据 Secrets 配置的账号等信息自动渲染 config.json 文件
- 自动将项目部署到腾讯云函数
- 自动创建触发器