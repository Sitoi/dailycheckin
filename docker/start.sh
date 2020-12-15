#!/bin/sh
set -e

export LANG="zh_CN.UTF-8"

echo "Git 拉取最新代码，并安装更新依赖..."
git -C /dailycheckin pull
pip install -r /dailycheckin/requirements.txt

echo "Load the latest crontab task file..."
echo "加载最新的定时任务文件..."

CRONTAB_LIST_FILE="/dailycheckin/docker/default_list.sh"

sed -i 's/>>/|ts >>/g' $CRONTAB_LIST_FILE
crontab $CRONTAB_LIST_FILE

echo "Start crontab task main process..."
echo "启动 crondtab 定时任务主进程..."
crond -f