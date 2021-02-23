#!/bin/bash

curl -O https://raw.githubusercontent.com/Sitoi/dailycheckin/main/docker/docker-compose.yml

curl -O https://raw.githubusercontent.com/Sitoi/dailycheckin/main/docker/Makefile

mkdir -p config

curl https://raw.githubusercontent.com/Sitoi/dailycheckin/main/deploy.sh | bash

docker run -d -v $(pwd)/config:/dailycheckin/config \
  -v $(pwd)/logs:/dailycheckin/logs \
  --name dailycheckin \
  --restart always \
  sitoi/dailycheckin:latest