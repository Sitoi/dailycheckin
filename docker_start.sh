#!/bin/bash

echo "在当前目录下创建 config 和 cron 文件夹"
mkdir -p config
mkdir -p cron

CONFIG_FILE="config/config.json"
CRONTAB_FILE="cron/crontab_list.sh"

if [ ! -f "$CONFIG_FILE" ]; then
    echo "config.json 不存在. 开始下载默认文件..."
    curl https://fastly.jsdelivr.net/gh/sitoi/dailycheckin@main/docker/config.template.json -o $CONFIG_FILE
else
    echo "config.json 已存在. 跳过下载。"
fi

if [ ! -f "$CRONTAB_FILE" ]; then
    echo "crontab_list.sh 不存在. 开始下载默认文件..."
    curl https://fastly.jsdelivr.net/gh/sitoi/dailycheckin@main/docker/crontab_list.sh -o $CRONTAB_FILE
else
    echo "crontab_list.sh 已存在. 跳过下载。"
fi


docker --version
if [ $? -ne 0 ];then
  echo "未安装 docker ，请先安装 docker 再运行脚本。"
else
  echo "docker 环境存在，检测 docker-compose 环境是否安装..."
  docker-compose --version || docker compose version && alias docker-compose="docker compose"
  if [ $? -ne 0 ];then
    echo "未安装 docker-compose，将使用 docker 命令启动容器..."
    echo "开始通过 docker 命令创建容器"
    docker pull sitoi/dailycheckin:latest
    docker run -d -v $(pwd)/config:/dailycheckin/config \
      -v $(pwd)/logs:/dailycheckin/logs \
      -v $(pwd)/cron:/dailycheckin/cron \
      --name dailycheckin \
      --restart always \
      sitoi/dailycheckin:latest
  else
    echo "docker-compose 环境存在，将使用 docker-compose 命令启动容器..."
    echo "下载 docker-compose.yml 文件"
    curl -O https://fastly.jsdelivr.net/gh/sitoi/dailycheckin@main/docker/docker-compose.yml
    echo "开始通过 docker-compose 命令创建容器"
    docker-compose pull
    docker-compose up -d
  fi
fi
