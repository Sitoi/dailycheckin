#!/bin/sh
set -e

export LANG="zh_CN.UTF-8"

echo "定时任务更新依赖..."
pip install dailycheckin --upgrade --user

echo "Load the latest crontab task file..."
echo "加载最新的定时任务文件..."
crontab /dailycheckin/cron/crontab_list.sh
