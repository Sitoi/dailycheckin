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
  \"DINGTALK_SECRET\": \"${DINGTALK_SECRET}\",
  \"DINGTALK_ACCESS_TOKEN\": \"${DINGTALK_ACCESS_TOKEN}\",
  \"SCKEY\": \"${SCKEY}\",
  \"QMSG_KEY\": \"${QMSG_KEY}\",
  \"TG_BOT_TOKEN\": \"${TG_BOT_TOKEN}\",
  \"TG_USER_ID\": \"${TG_USER_ID}\",
  \"CITY_NAME_LIST\": ${CITY_NAME_LIST},
  \"MOTTO\": ${MOTTO},
  \"IQIYI_COOKIE_LIST\": ${IQIYI_COOKIE_LIST},
  \"VQQ_COOKIE_LIST\": ${VQQ_COOKIE_LIST},
  \"POJIE_COOKIE_LIST\": ${POJIE_COOKIE_LIST},
  \"YOUDAO_COOKIE_LIST\": ${YOUDAO_COOKIE_LIST},
  \"KGQQ_COOKIE_LIST\": ${KGQQ_COOKIE_LIST},
  \"MUSIC163_ACCOUNT_LIST\": ${MUSIC163_ACCOUNT_LIST},
  \"XMLY_COOKIE_LIST\": ${XMLY_COOKIE_LIST},
  \"ONEPLUSBBS_COOKIE_LIST\": ${ONEPLUSBBS_COOKIE_LIST},
  \"QQREAD_ACCOUNT_LIST\": ${QQREAD_ACCOUNT_LIST},
  \"BAIDU_URL_SUBMIT_LIST\": ${BAIDU_URL_SUBMIT_LIST}
}"
echo $JSONSTR > config.json

cat config.json