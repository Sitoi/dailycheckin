#!/bin/bash
if [[ $DINGTALK_SECRET ]]; then echo "DINGTALK_SECRET 变量存在，并成功赋值" ;else DINGTALK_SECRET="";fi;
if [[ $DINGTALK_ACCESS_TOKEN ]]; then echo "DINGTALK_ACCESS_TOKEN 变量存在，并成功赋值" ;else DINGTALK_ACCESS_TOKEN=""; fi;
if [[ $SCKEY ]]; then echo "SCKEY 变量存在，并成功赋值" ;else SCKEY=""; fi;
if [[ $QMSG_KEY ]]; then echo "QMSG_KEY 变量存在，并成功赋值" ;else QMSG_KEY=""; fi;
if [[ $TG_BOT_TOKEN ]]; then echo "TG_BOT_TOKEN 变量存在，并成功赋值" ;else TG_BOT_TOKEN=""; fi;
if [[ $TG_USER_ID ]]; then echo "TG_USER_ID 变量存在，并成功赋值" ;else TG_USER_ID=""; fi;
if [[ $IQIYI_COOKIE_LIST ]]; then echo "IQIYI_COOKIE_LIST 变量存在，并成功赋值" ;else IQIYI_COOKIE_LIST=[]; fi;
if [[ $VQQ_COOKIE_LIST ]]; then echo "VQQ_COOKIE_LIST 变量存在，并成功赋值" ;else VQQ_COOKIE_LIST=[]; fi;
if [[ $POJIE_COOKIE_LIST ]]; then echo "POJIE_COOKIE_LIST 变量存在，并成功赋值" ;else POJIE_COOKIE_LIST=[]; fi;
if [[ $YOUDAO_COOKIE_LIST ]]; then echo "YOUDAO_COOKIE_LIST 变量存在，并成功赋值" ;else YOUDAO_COOKIE_LIST=[]; fi;
if [[ $KGQQ_COOKIE_LIST ]]; then echo "KGQQ_COOKIE_LIST 变量存在，并成功赋值" ;else KGQQ_COOKIE_LIST=[]; fi;
if [[ $MUSIC163_ACCOUNT_LIST ]]; then echo "MUSIC163_ACCOUNT_LIST 变量存在，并成功赋值" ;else MUSIC163_ACCOUNT_LIST=[]; fi;
if [[ $BAIDU_URL_SUBMIT_LIST ]]; then echo "BAIDU_URL_SUBMIT_LIST 变量存在，并成功赋值" ;else BAIDU_URL_SUBMIT_LIST=[]; fi;
if [[ $CITY_NAME_LIST ]]; then echo "CITY_NAME_LIST 变量存在，并成功赋值" ;else CITY_NAME_LIST=[]; fi;
if [[ $MOTTO ]]; then echo "MOTTO 变量存在，并成功赋值" ;else MOTTO=false; fi;
if [[ $XMLY_COOKIE_LIST ]]; then echo "XMLY_COOKIE_LIST 变量存在，并成功赋值" ;else XMLY_COOKIE_LIST=[]; fi;
if [[ $ONEPLUSBBS_COOKIE_LIST ]]; then echo "ONEPLUSBBS_COOKIE_LIST 变量存在，并成功赋值" ;else ONEPLUSBBS_COOKIE_LIST=[]; fi;
if [[ $QQREAD_ACCOUNT_LIST ]]; then echo "QQREAD_ACCOUNT_LIST 变量存在，并成功赋值" ;else QQREAD_ACCOUNT_LIST=[]; fi;


JSONSTR="{
  \"dingtalk\": {
    \"dingtalk_secret\": \"${DINGTALK_SECRET}\",
    \"dingtalk_access_token\": \"${DINGTALK_ACCESS_TOKEN}\"
  },
  \"server\": {
    \"sckey\": \"${SCKEY}\"
  },
  \"qmsg\": {
    \"qmsg_key\": \"${QMSG_KEY}\"
  },
  \"telegram\": {
    \"tg_bot_token\": \"${TG_BOT_TOKEN}\",
    \"tg_user_id\": \"${TG_USER_ID}\"
  },
  \"weather\": ${CITY_NAME_LIST},
  \"motto\": ${MOTTO},
  \"iqiyi\": ${IQIYI_COOKIE_LIST},
  \"vqq\": ${VQQ_COOKIE_LIST},
  \"52pojie\": ${POJIE_COOKIE_LIST},
  \"youdao\": ${YOUDAO_COOKIE_LIST},
  \"kgqq\": ${KGQQ_COOKIE_LIST},
  \"music163\": ${MUSIC163_ACCOUNT_LIST},
  \"xmly\": ${XMLY_COOKIE_LIST},
  \"oneplusbbs\": ${ONEPLUSBBS_COOKIE_LIST},
  \"qqread\": ${QQREAD_ACCOUNT_LIST},
  \"baidu_url_submit\": ${BAIDU_URL_SUBMIT_LIST}
}"
echo $JSONSTR > config.json

cat config.json