SHELL=/bin/sh
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

# 每天北京时间 01:10 和 07:10 执行全部已配置任务。
10 1,7 * * * cd /app && dailycheckin >> /app/logs/dailycheckin.log 2>&1
