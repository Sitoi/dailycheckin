# 青龙使用教程

## 一、进入青龙容器内部

```bash
docker exec -it qinglong bash
```

## 二、安装依赖

```bash
apk add --no-cache gcc g++ python python-dev py-pip mysql-dev linux-headers libffi-dev openssl-dev
```

```bash
pip3 install dailycheckin --upgrade
```

> 如果上述命令仍然安装失败运行下面的命令

```bash
apk add --no-cache --virtual .build-deps gcc musl-dev python2-dev python3-dev
pip3 install pip setuptools --upgrade
pip3 install cryptography~=3.2.1
```

## 三、新建并编写 `/ql/scripts/config.json` 配置文件

> ⚠️ 请务必到 [http://www.json.cn](http://www.json.cn) 网站检查 `config.json` 文件格式是否正确！

参考[配置说明文档](https://sitoi.gitee.io/dailycheckin/settings/) ，并修改 `config.json`

## 四、配置定时任务

1. 运行全部脚本
   ![定时任务](img/ql-base.png)
2. 运行指定脚本（包含），可以同时选择多个，用「空格」分开
   ![定时任务](img/ql-include.png)
3. 运行指定脚本（排除），可以同时选择多个，用「空格」分开
   ![定时任务](img/ql-exclude.png)
4. 配置定时更新
   ![定时更新](img/ql-update.png)