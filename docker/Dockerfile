FROM python:3.8-alpine
MAINTAINER Sitoi <Sitoi0418@gmail.com>

ENV CRONTAB_LIST_FILE crontab_list.sh

WORKDIR /dailycheckin

#GitHub Actions 构建
COPY ./docker /dailycheckin
COPY ./docker/start.sh /usr/local/bin

#本地构建
#COPY . /dailycheckin
#COPY ./start.sh /usr/local/bin

RUN set -ex \
    && apk update && apk upgrade\
    && apk add --no-cache tzdata moreutils git gcc g++ py-pip mysql-dev linux-headers libffi-dev openssl-dev\
    && ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
    && echo "Asia/Shanghai" > /etc/timezone \
    && chmod +x /usr/local/bin/start.sh

ENTRYPOINT ["start.sh"]