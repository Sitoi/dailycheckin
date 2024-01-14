#!/bin/sh
set -e

export LANG="zh_CN.UTF-8"

CRONTAB_FILE="/dailycheckin/cron/crontab_list.sh"

echo "安装最新依赖..."
pip install dailycheckin --upgrade --user

echo "加载最新的定时任务文件..."
crontab $CRONTAB_FILE

if [ $CRONTAB_FILE ]; then
  chmod -R 777 $CRONTAB_FILE
fi

echo "启动 crondtab 定时任务主进程..."
crond -f