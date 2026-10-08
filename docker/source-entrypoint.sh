#!/bin/sh
set -eu

config_file=/app/config/config.json
crontab_file=/app/cron/crontab_list.sh
logs_dir=/app/logs

if [ ! -f "$config_file" ]; then
    echo "错误：未找到 $config_file。请先创建 config/config.json。" >&2
    exit 1
fi

if ! python -m json.tool "$config_file" >/dev/null 2>&1; then
    echo "错误：$config_file 不是合法的 JSON 文件。" >&2
    exit 1
fi

# docker compose run 传入命令时，直接执行该命令，便于一次性测试。
if [ "$#" -gt 0 ]; then
    exec "$@"
fi

if [ ! -f "$crontab_file" ]; then
    echo "错误：未找到 $crontab_file。" >&2
    exit 1
fi

mkdir -p "$logs_dir"
crontab "$crontab_file"

echo "已加载定时任务："
crontab -l
echo "启动 cron，容器时区：$(date '+%Z %z')"

exec cron -f
