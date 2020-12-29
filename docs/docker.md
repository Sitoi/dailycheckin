# Docker 使用教程

## 一、新建目录结构

```text
dailycheckin
├── logs
│   └── xxxxxx.log
├── config.json
└── docker-compose.yml
```

- dailycheckin/logs: 建一个空文件夹就行
- dailycheckin/config.json: 配置文件
- dailycheckin/docker-compose.yml: docker启动文件

## 二、修改配置文件等

### dailycheckin/logs

建一个空文件夹就行

### dailycheckin/config.json

参考[配置说明文档](https://github.com/Sitoi/dailycheckin/blob/main/docs/settings.md) ，并修改 `config.json`

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
      - ./config.json:/dailycheckin/config.json
      - ./logs:/dailycheckin/logs
```

## 三、启动 docker

目录文件配置好之后在 `dailycheckin` 目录执行。

```bash
docker-compose up -d
```

> 修改 `docker-compose.yml` 后需要使用上述命令使更改生效

## 附录

- `docker-compose logs` 打印日志
- `docker-compose pull` 更新镜像
- `docker-compose stop` 停止容器
- `docker-compose restart` 重启容器
- `docker-compose down` 停止并删除容器
- `docker exec -it dailycheckin sh` 进入 docker