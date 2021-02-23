#!/bin/sh
set -e

export LANG="zh_CN.UTF-8"

echo "Git 拉取最新代码，并安装更新依赖..."
git -C /dailycheckin pull
pip install -r /dailycheckin/requirements.txt

defaultListFile="/dailycheckin/docker/default_list.sh"

customListFile="/dailycheckin/docker/$CUSTOM_LIST_FILE"
mergedListFile="/dailycheckin/docker/merged_list_file.sh"

if type ts >/dev/null 2>&1; then
    echo 'moreutils tools installed, default task append |ts output'
    echo '系统已安装 moreutils 工具包，默认定时任务增加｜ts 输出'
    ##复制一个新文件来追加|ts，防止git pull的时候冲突
    cp $defaultListFile /dailycheckin/docker/crontab_list.sh
    defaultListFile="/dailycheckin/docker/crontab_list.sh"

    sed -i 's/>>/|ts >>/g' $defaultListFile
fi

if [ $CUSTOM_LIST_FILE ]; then
    echo "You have configured a custom list file: $CUSTOM_LIST_FILE, custom list merge type: $CUSTOM_LIST_MERGE_TYPE..."
    echo "您配置了自定义任务文件：$CUSTOM_LIST_FILE，自定义任务类型为：$CUSTOM_LIST_MERGE_TYPE..."
    if [ -f "$customListFile" ]; then
        if [ $CUSTOM_LIST_MERGE_TYPE == "append" ]; then
            echo "merge default list file: $DEFAULT_LIST_FILE and custom list file: $CUSTOM_LIST_FILE"
            echo "合并默认定时任务文件：$DEFAULT_LIST_FILE 和 自定义定时任务文件：$CUSTOM_LIST_FILE"
            cat $defaultListFile >$mergedListFile
            echo -e "" >>$mergedListFile
            cat $customListFile >>$mergedListFile
        elif [ $CUSTOM_LIST_MERGE_TYPE == "overwrite" ]; then
            cat $customListFile >$mergedListFile
            echo "merge custom list file: $CUSTOM_LIST_FILE..."
            echo "合并自定义任务文件：$CUSTOM_LIST_FILE"
            touch "$customListFile"
        else
            echo "配置配置了错误的自定义定时任务类型：$CUSTOM_LIST_MERGE_TYPE，自定义任务类型为只能为append或者overwrite..."
            cat $defaultListFile >$mergedListFile
        fi
    else
        echo "Not found custom list file: $CUSTOM_LIST_FILE ,use default list file: $DEFAULT_LIST_FILE"
        echo "自定义任务文件：$CUSTOM_LIST_FILE 未找到，使用默认配置$DEFAULT_LIST_FILE..."
        cat $defaultListFile >$mergedListFile
    fi
else
    echo "The currently used is the default crontab task file: $DEFAULT_LIST_FILE ..."
    echo "当前使用的为默认定时任务文件 $DEFAULT_LIST_FILE ..."
    cat $defaultListFile >$mergedListFile
fi

# 判断最后要加载的定时任务是否包含默认定时任务，不包含的话就加进去
if [ $(grep -c "default_task.sh" $mergedListFile) -eq '0' ]; then
    echo "Merged crontab task file，the required default task is not included, append default task..."
    echo "合并后的定时任务文件，未包含必须的默认定时任务，增加默认定时任务..."
    echo -e >>$mergedListFile
    echo "52 */1 * * * sh /dailycheckin/docker/default_task.sh >> /dailycheckin/logs/default_task.log 2>&1" >>$mergedListFile
fi

echo "Load the latest crontab task file..."
echo "加载最新的定时任务文件..."
crontab $mergedListFile

echo "Start crontab task main process..."
echo "启动 crondtab 定时任务主进程..."

if [ $CUSTOM_LIST_FILE ]; then
  chmod -R 777 $customListFile
fi

crond -f