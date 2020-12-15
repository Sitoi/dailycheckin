## 本地使用教程

### 下载（Clone）本项目到本地

下载地址: [https://github.com/Sitoi/DailyCheckIn/archive/main.zip](https://github.com/Sitoi/DailyCheckIn/archive/main.zip)

Clone 地址: [https://github.com/Sitoi/dailycheckin.git](https://github.com/Sitoi/dailycheckin.git)

> 下载的需要解析压缩包

### 一、拷贝 `config.template.json` 到 `config.json` 并修改

参考[配置说明文档](./settings.md) ，并修改 `config.json`

### 二、安装 Pypi 依赖包

```bash
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

### 三、单次运行

> 运行【日常签到类】（除喜马拉雅极速版&企鹅读书）

```bash
python3 index.py
```

> 运行【喜马拉雅极速版

```bash
python3 index.py xmly
```

> 运行【企鹅读书】

```bash
python3 index.py qqread
```