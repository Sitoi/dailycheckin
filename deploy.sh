#!/bin/bash
if [[ $DINGTALK_SECRET ]]; then echo "DINGTALK_SECRET 变量存在，并成功赋值" ;else DINGTALK_SECRET="";fi;
if [[ $DINGTALK_ACCESS_TOKEN ]]; then echo "DINGTALK_ACCESS_TOKEN 变量存在，并成功赋值" ;else DINGTALK_ACCESS_TOKEN=""; fi;
if [[ $SCKEY ]]; then echo "SCKEY 变量存在，并成功赋值" ;else SCKEY=""; fi;
if [[ $SENDKEY ]]; then echo "SENDKEY 变量存在，并成功赋值" ;else SENDKEY=""; fi;
if [[ $BARK_URL ]]; then echo "BARK_URL 变量存在，并成功赋值" ;else BARK_URL=""; fi;
if [[ $QMSG_KEY ]]; then echo "QMSG_KEY 变量存在，并成功赋值" ;else QMSG_KEY=""; fi;
if [[ $TG_BOT_TOKEN ]]; then echo "TG_BOT_TOKEN 变量存在，并成功赋值" ;else TG_BOT_TOKEN=""; fi;
if [[ $TG_USER_ID ]]; then echo "TG_USER_ID 变量存在，并成功赋值" ;else TG_USER_ID=""; fi;
if [[ $COOLPUSHSKEY ]]; then echo "COOLPUSHSKEY 变量存在，并成功赋值" ;else COOLPUSHSKEY=""; fi;
if [[ $COOLPUSHQQ ]]; then echo "COOLPUSHQQ 变量存在，并成功赋值" ;else COOLPUSHQQ=true; fi;
if [[ $COOLPUSHWX ]]; then echo "COOLPUSHWX 变量存在，并成功赋值" ;else COOLPUSHWX=false; fi;
if [[ $COOLPUSHEMAIL ]]; then echo "COOLPUSHEMAIL 变量存在，并成功赋值" ;else COOLPUSHEMAIL=false; fi;
if [[ $QYWX_KEY ]]; then echo "QYWX_KEY 变量存在，并成功赋值" ;else QYWX_KEY=""; fi;
if [[ $QYWX_CORPID ]]; then echo "QYWX_CORPID 变量存在，并成功赋值" ;else QYWX_CORPID=""; fi;
if [[ $QYWX_AGENTID ]]; then echo "QYWX_AGENTID 变量存在，并成功赋值" ;else QYWX_AGENTID=""; fi;
if [[ $QYWX_CORPSECRET ]]; then echo "QYWX_CORPSECRET 变量存在，并成功赋值" ;else QYWX_CORPSECRET=""; fi;
if [[ $QYWX_TOUSER ]]; then echo "QYWX_TOUSER 变量存在，并成功赋值" ;else QYWX_TOUSER=""; fi;
if [[ $PUSHPLUS_TOKEN ]]; then echo "PUSHPLUS_TOKEN 变量存在，并成功赋值" ;else PUSHPLUS_TOKEN=""; fi;
if [[ $PUSHPLUS_TOPIC ]]; then echo "PUSHPLUS_TOPIC 变量存在，并成功赋值" ;else PUSHPLUS_TOPIC=""; fi;
if [[ $IQIYI_COOKIE_LIST ]]; then echo "IQIYI_COOKIE_LIST 变量存在，并成功赋值" ;else IQIYI_COOKIE_LIST=[]; fi;
if [[ $VQQ_COOKIE_LIST ]]; then echo "VQQ_COOKIE_LIST 变量存在，并成功赋值" ;else VQQ_COOKIE_LIST=[]; fi;
if [[ $YOUDAO_COOKIE_LIST ]]; then echo "YOUDAO_COOKIE_LIST 变量存在，并成功赋值" ;else YOUDAO_COOKIE_LIST=[]; fi;
if [[ $KGQQ_COOKIE_LIST ]]; then echo "KGQQ_COOKIE_LIST 变量存在，并成功赋值" ;else KGQQ_COOKIE_LIST=[]; fi;
if [[ $MUSIC163_ACCOUNT_LIST ]]; then echo "MUSIC163_ACCOUNT_LIST 变量存在，并成功赋值" ;else MUSIC163_ACCOUNT_LIST=[]; fi;
if [[ $BAIDU_URL_SUBMIT_LIST ]]; then echo "BAIDU_URL_SUBMIT_LIST 变量存在，并成功赋值" ;else BAIDU_URL_SUBMIT_LIST=[]; fi;
if [[ $CITY_NAME_LIST ]]; then echo "CITY_NAME_LIST 变量存在，并成功赋值" ;else CITY_NAME_LIST=[]; fi;
if [[ $MOTTO ]]; then echo "MOTTO 变量存在，并成功赋值" ;else MOTTO=false; fi;
if [[ $XMLY_COOKIE_LIST ]]; then echo "XMLY_COOKIE_LIST 变量存在，并成功赋值" ;else XMLY_COOKIE_LIST=[]; fi;
if [[ $ONEPLUSBBS_COOKIE_LIST ]]; then echo "ONEPLUSBBS_COOKIE_LIST 变量存在，并成功赋值" ;else ONEPLUSBBS_COOKIE_LIST=[]; fi;
if [[ $FMAPP_ACCOUNT_LIST ]]; then echo "FMAPP_ACCOUNT_LIST 变量存在，并成功赋值" ;else FMAPP_ACCOUNT_LIST=[]; fi;
if [[ $TIEBA_COOKIE_LIST ]]; then echo "TIEBA_COOKIE_LIST 变量存在，并成功赋值" ;else TIEBA_COOKIE_LIST=[]; fi;
if [[ $BILIBILI_COOKIE_LIST ]]; then echo "BILIBILI_COOKIE_LIST 变量存在，并成功赋值" ;else BILIBILI_COOKIE_LIST=[]; fi;
if [[ $LIANTONG_ACCOUNT_LIST ]]; then echo "LIANTONG_ACCOUNT_LIST 变量存在，并成功赋值" ;else LIANTONG_ACCOUNT_LIST=[]; fi;
if [[ $V2EX_COOKIE_LIST ]]; then echo "V2EX_COOKIE_LIST 变量存在，并成功赋值" ;else V2EX_COOKIE_LIST=[]; fi;
if [[ $WWW2NZZ_COOKIE_LIST ]]; then echo "WWW2NZZ_COOKIE_LIST 变量存在，并成功赋值" ;else WWW2NZZ_COOKIE_LIST=[]; fi;
if [[ $SMZDM_COOKIE_LIST ]]; then echo "SMZDM_COOKIE_LIST 变量存在，并成功赋值" ;else SMZDM_COOKIE_LIST=[]; fi;
if [[ $MIMOTION_ACCOUNT_LIST ]]; then echo "MIMOTION_ACCOUNT_LIST 变量存在，并成功赋值" ;else MIMOTION_ACCOUNT_LIST=[]; fi;
if [[ $ACFUN_ACCOUNT_LIST ]]; then echo "ACFUN_ACCOUNT_LIST 变量存在，并成功赋值" ;else ACFUN_ACCOUNT_LIST=[]; fi;
if [[ $WPS_COOKIE_LIST ]]; then echo "WPS_COOKIE_LIST 变量存在，并成功赋值" ;else WPS_COOKIE_LIST=[]; fi;
if [[ $POJIE_COOKIE_LIST ]]; then echo "POJIE_COOKIE_LIST 变量存在，并成功赋值" ;else POJIE_COOKIE_LIST=[]; fi;
if [[ $MGTV_PARAMS_LIST ]]; then echo "MGTV_PARAMS_LIST 变量存在，并成功赋值" ;else MGTV_PARAMS_LIST=[]; fi;
if [[ $PICACOMIC_ACCOUNT_LIST ]]; then echo "PICACOMIC_ACCOUNT_LIST 变量存在，并成功赋值" ;else PICACOMIC_ACCOUNT_LIST=[]; fi;
if [[ $MEIZU_COOKIE_LIST ]]; then echo "MEIZU_COOKIE_LIST 变量存在，并成功赋值" ;else MEIZU_COOKIE_LIST=[]; fi;
if [[ $CLOUD189_ACCOUNT_LIST ]]; then echo "CLOUD189_ACCOUNT_LIST 变量存在，并成功赋值" ;else CLOUD189_ACCOUNT_LIST=[]; fi;
if [[ $CAIYUN_COOKIE_LIST ]]; then echo "CAIYUN_COOKIE_LIST 变量存在，并成功赋值" ;else CAIYUN_COOKIE_LIST=[]; fi;


JSONSTR="{
  \"DINGTALK_SECRET\": \"${DINGTALK_SECRET}\",
  \"DINGTALK_ACCESS_TOKEN\": \"${DINGTALK_ACCESS_TOKEN}\",
  \"SCKEY\": \"${SCKEY}\",
  \"SENDKEY\": \"${SENDKEY}\",
  \"BARK_URL\": \"${BARK_URL}\",
  \"QMSG_KEY\": \"${QMSG_KEY}\",
  \"TG_BOT_TOKEN\": \"${TG_BOT_TOKEN}\",
  \"TG_USER_ID\": \"${TG_USER_ID}\",
  \"COOLPUSHSKEY\": \"${COOLPUSHSKEY}\",
  \"COOLPUSHQQ\": ${COOLPUSHQQ},
  \"COOLPUSHWX\": ${COOLPUSHWX},
  \"COOLPUSHEMAIL\": ${COOLPUSHEMAIL},
  \"QYWX_KEY\": \"${QYWX_KEY}\",
  \"QYWX_CORPID\": \"${QYWX_CORPID}\",
  \"QYWX_AGENTID\": \"${QYWX_AGENTID}\",
  \"QYWX_CORPSECRET\": \"${QYWX_CORPSECRET}\",
  \"QYWX_TOUSER\": \"${QYWX_TOUSER}\",
  \"PUSHPLUS_TOKEN\": \"${PUSHPLUS_TOKEN}\",
  \"PUSHPLUS_TOPIC\": \"${PUSHPLUS_TOPIC}\",
  \"CITY_NAME_LIST\": ${CITY_NAME_LIST},
  \"MOTTO\": ${MOTTO},
  \"IQIYI_COOKIE_LIST\": ${IQIYI_COOKIE_LIST},
  \"VQQ_COOKIE_LIST\": ${VQQ_COOKIE_LIST},
  \"YOUDAO_COOKIE_LIST\": ${YOUDAO_COOKIE_LIST},
  \"KGQQ_COOKIE_LIST\": ${KGQQ_COOKIE_LIST},
  \"MUSIC163_ACCOUNT_LIST\": ${MUSIC163_ACCOUNT_LIST},
  \"XMLY_COOKIE_LIST\": ${XMLY_COOKIE_LIST},
  \"ONEPLUSBBS_COOKIE_LIST\": ${ONEPLUSBBS_COOKIE_LIST},
  \"FMAPP_ACCOUNT_LIST\": ${FMAPP_ACCOUNT_LIST},
  \"BAIDU_URL_SUBMIT_LIST\": ${BAIDU_URL_SUBMIT_LIST},
  \"BILIBILI_COOKIE_LIST\": ${BILIBILI_COOKIE_LIST},
  \"LIANTONG_ACCOUNT_LIST\": ${LIANTONG_ACCOUNT_LIST},
  \"V2EX_COOKIE_LIST\": ${V2EX_COOKIE_LIST},
  \"WWW2NZZ_COOKIE_LIST\": ${WWW2NZZ_COOKIE_LIST},
  \"SMZDM_COOKIE_LIST\": ${SMZDM_COOKIE_LIST},
  \"MIMOTION_ACCOUNT_LIST\": ${MIMOTION_ACCOUNT_LIST},
  \"ACFUN_ACCOUNT_LIST\": ${ACFUN_ACCOUNT_LIST},
  \"CLOUD189_ACCOUNT_LIST\": ${CLOUD189_ACCOUNT_LIST},
  \"WPS_COOKIE_LIST\": ${WPS_COOKIE_LIST},
  \"POJIE_COOKIE_LIST\": ${POJIE_COOKIE_LIST},
  \"MGTV_PARAMS_LIST\": ${MGTV_PARAMS_LIST},
  \"PICACOMIC_ACCOUNT_LIST\": ${PICACOMIC_ACCOUNT_LIST},
  \"MEIZU_COOKIE_LIST\": ${MEIZU_COOKIE_LIST},
  \"CAIYUN_COOKIE_LIST\": ${CAIYUN_COOKIE_LIST},
  \"TIEBA_COOKIE_LIST\": ${TIEBA_COOKIE_LIST}
}"
echo $JSONSTR > config/config.json

cat config/config.json
