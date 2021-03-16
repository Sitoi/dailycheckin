#!/bin/bash

echo "在当前目录下创建 config 文件夹"

mkdir -p config

echo "下载渲染 config 文件的脚本，并执行渲染"

curl https://raw.githubusercontent.com/Sitoi/dailycheckin/main/config/config.template.json -o config.json

docker --version
if [ $? -ne 0 ];then
  echo "未安装 docker ，请先安装 docker 再运行脚本。"
else
  echo "docker 环境存在，检测 docker-compose 环境是否安装..."
  docker-compose --version
  if [ $? -ne 0 ];then
    echo "未安装 docker-compose，将使用 docker 命令启动容器..."
    echo "开始通过 docker 命令创建容器"
    docker run -d -v $(pwd)/config:/dailycheckin/config \
      -v $(pwd)/logs:/dailycheckin/logs \
      --name dailycheckin \
      --restart always \
      sitoi/dailycheckin:latest
  else
    echo "docker-compose 环境存在，将使用 docker-compose 命令启动容器..."
    echo "下载 docker-compose.yml 文件"
    curl -O https://raw.githubusercontent.com/Sitoi/dailycheckin/main/docker/docker-compose.yml
    echo "下载 Makefile 文件（可以无视）"
    curl -O https://raw.githubusercontent.com/Sitoi/dailycheckin/main/docker/Makefile
    echo "开始通过 docker-compose 命令创建容器"
    docker-compose up -d
  fi
fi