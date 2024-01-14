##############默认任务##############
# 每 12 小时更新 Pipy 包，如果不需要更新 pypi 包请注释掉下面这行
0 */12 * * * echo "定时任务更新依赖..." && pip install dailycheckin --upgrade --user >> /dailycheckin/logs/update-pypi.log 2>&1
# 每天的 23:50 分清理一次日志
50 23 */2 * * rm -rf /dailycheckin/logs/*.log

##############每日签到一次任务##############
# 每日签到(9:00 执行全部签到)
0 9 * * * cd /dailycheckin && dailycheckin >> /dailycheckin/logs/dailycheckin.log 2>&1
