FROM python:3.11-slim-bookworm

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    TZ=Asia/Shanghai

WORKDIR /app

RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends cron tzdata \
    && rm -rf /var/lib/apt/lists/*

# 安装当前仓库中的源码，而不是 PyPI 上的发布版本。
COPY pyproject.toml setup.py requirements.txt README.md ./
COPY dailycheckin ./dailycheckin
RUN python -m pip install --no-cache-dir .

COPY docker/source-entrypoint.sh /usr/local/bin/source-entrypoint.sh
RUN chmod +x /usr/local/bin/source-entrypoint.sh

ENTRYPOINT ["source-entrypoint.sh"]
