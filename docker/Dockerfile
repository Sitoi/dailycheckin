FROM python:3.9-alpine

WORKDIR /dailycheckin
COPY ./start.sh /usr/local/bin

RUN set -ex \
    && apk update && apk upgrade\
    && apk add --no-cache gcc g++ make libffi-dev openssl-dev\
    && ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
    && echo "Asia/Shanghai" > /etc/timezone \
    && chmod +x /usr/local/bin/start.sh \
    && pip install dailycheckin --upgrade \
    && ln -s /root/.local/bin/dailycheckin /usr/bin/dailycheckin

ADD . /dailycheckin

ENTRYPOINT ["start.sh"]