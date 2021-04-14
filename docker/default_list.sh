#必须要的默认定时任务请勿删除
0 */12 * * * sh /dailycheckin/docker/default_task.sh >> /dailycheckin/logs/default_task.log 2>&1
# 每天的 23:50 分清理一次日志
50 23 */2 * * rm -rf /dailycheckin/logs/*.log


##############每日签到一次任务##############
# 每日签到(8：45 执行一次)
45 8 * * * python /dailycheckin/index.py >> /dailycheckin/logs/dailycheckin.log 2>&1
