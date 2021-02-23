# Docker 使用教程

## 环境

- docker
- docker-compose

### Docker 安装

安装教程请自行百度

### docker-compose 安装

> 方式一（Python 环境）

```bash
pip3 install docker-compose
```

> 方式二

```
sudo curl -L "https://github.com/docker/compose/releases/download/1.24.1/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```

通过 `docker-compose version` 查看 `docker-compose` 版本，确认是否安装成功。

## 一、新建目录结构

```text
dailycheckin
|-- config
|   `-- config.json
`-- docker-compose.yml
```

- dailycheckin/config/config.json: 配置文件
- dailycheckin/docker-compose.yml: docker启动文件

## 二、修改配置文件等

### dailycheckin/config/config.json

> 请务必到 [http://www.json.cn](http://www.json.cn) 网站检查 `config.json` 文件格式是否正确！

> 请务必到 [http://www.json.cn](http://www.json.cn) 网站检查 `config.json` 文件格式是否正确！

> 请务必到 [http://www.json.cn](http://www.json.cn) 网站检查 `config.json` 文件格式是否正确！

参考[配置说明文档](https://sitoi.github.io/dailycheckin/settings/) ，并修改 `config.json`

### dailycheckin/docker-compose.yml

```yaml
version: '3'
services:
  dailycheckin:
    image: sitoi/dailycheckin:latest
    container_name: dailycheckin
    restart: always
    tty: true
    volumes:
      - ./config:/dailycheckin/config
      - ./logs:/dailycheckin/logs
```

## 三、启动 docker

目录文件配置好之后在 `dailycheckin` 目录执行。

```bash
docker-compose up -d
```

> 修改 `docker-compose.yml` 后需要使用上述命令使更改生效

## 立即执行单次签到(确保容器已启动)

> 运行【日常签到类】（除喜马拉雅极速版）

```bash
docker exec dailycheckin python3 index.py
```

> 运行【喜马拉雅极速版】

```bash
docker exec dailycheckin python3 index.py xmly
```

## 常见问题

1. 对于修改 `config.json` 文件发现为更改的情况

   先执行 `docker-compose down` 停止并删除容器，再执行 `docker-compose up -d` 启动容器

## 附录

- `docker-compose logs` 打印日志
- `docker-compose pull` 更新镜像
- `docker-compose stop` 停止容器
- `docker-compose restart` 重启容器
- `docker-compose down` 停止并删除容器
- `docker exec -it dailycheckin sh` 进入 docker
