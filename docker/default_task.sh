#!/bin/sh
set -e

echo "定时任务更新代码，git 拉取最新代码，并安装更新依赖..."
git -C /dailycheckin pull
pip install -r /dailycheckin/requirements.txt