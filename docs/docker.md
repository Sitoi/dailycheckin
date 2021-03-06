# Docker 使用教程

## 一、运行如下命令一键启动并创建服务

```bash
curl https://raw.githubusercontent.com/Sitoi/dailycheckin/main/docker_start.sh | bash
```

国内源:

```bash
curl https://gitee.com/sitoi/dailycheckin/raw/main/docker_start.sh | bash
```

> 运行成功会自动创建如下目录结构, 并成功启动 docker 服务。

```text
.
|-- config
|   `-- config.json
|-- docker-compose.yml
|-- logs
|   `-- default_task.log
`-- Makefile
```

- `./config/config.json`: 配置文件
- `./docker-compose.yml`: docker 启动文件（只在有 docker-compose 的情况下创建）
- `./logs`: 日志文件
- `./Makefile`: make 脚本命令（只在有 docker-compose 的情况下创建）

## 二、修改配置文件

文件路径: `./config/config.json`

> ⚠️ ️请务必到 [http://www.json.cn](http://www.json.cn) 网站检查 `config.json` 文件格式是否正确！

参考 [配置说明文档](https://sitoi.github.io/dailycheckin/settings/) ，并修改 `config.json`

## 三、立即执行单次签到(确保容器已启动)，检查 config.json 是否配置正确

##### 运行【日常签到类】（除喜马拉雅极速版）

```bash
docker exec dailycheckin python3 index.py
```

##### 运行【喜马拉雅极速版】

```bash
docker exec dailycheckin python3 index.py xmly
```


##### 更新最新脚本

```bash
docker exec dailycheckin sh /dailycheckin/docker/default_task.sh
```

## 附录

### docker-compose 安装

##### 方式一（Python 环境）

```bash
pip3 install docker-compose
```

##### 方式二

```
sudo curl -L "https://github.com/docker/compose/releases/download/1.24.1/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```

通过 `docker-compose version` 查看 `docker-compose` 版本，确认是否安装成功。

### docker-compose 常用命令

- `docker-compose logs` 打印日志
- `docker-compose pull` 更新镜像
- `docker-compose stop` 停止容器
- `docker-compose restart` 重启容器
- `docker-compose down` 停止并删除容器
- `docker exec -it dailycheckin sh` 进入 docker
