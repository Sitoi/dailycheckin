# 从源码使用 Docker Compose 部署

本项目已经提供默认的 `Dockerfile` 和 `compose.yaml`。在仓库根目录直接执行标准 `docker compose` 命令，即可从当前源码构建并运行，无需通过 `-f` 指定 Compose 文件。

本方案使用 `pip install .` 安装当前仓库源码，容器启动时不会从 PyPI 更新 `dailycheckin`。因此，运行的代码与当前 Git 工作区构建时的代码一致。

## 一、部署文件

仓库中的相关文件：

```text
dailycheckin/
├── dailycheckin/                    # Python 源码
├── cron/
│   └── crontab_list.sh              # 容器定时任务
├── docker/
│   └── source-entrypoint.sh         # 容器启动检查及 cron 入口
├── config/
│   └── config.json                  # 账号配置，不提交 Git
├── .dockerignore                    # 防止凭据、日志进入构建上下文
├── Dockerfile                       # 源码镜像
├── compose.yaml                     # Docker Compose 默认配置
└── SOURCE_DOCKER_DEPLOY.md
```

`config/config.json` 包含 Cookie、Token 等敏感信息，已被 `.gitignore` 和 `.dockerignore` 排除。它只会在容器启动时挂载，不会被复制进镜像。

## 二、准备环境

需要安装 Git、Docker Engine 和 Docker Compose v2：

```bash
git --version
docker --version
docker compose version
```

拉取源码（已有仓库可跳过）：

```bash
git clone https://github.com/Sitoi/dailycheckin.git
cd dailycheckin
```

后续命令均在仓库根目录执行。

## 三、准备配置

如果还没有 `config/config.json`，先创建配置目录并从模板复制：

```bash
mkdir -p config
cp docker/config.template.json config/config.json
```

编辑 `config/config.json`，删除不需要的示例账号并填写真实信息，然后检查 JSON 格式：

```bash
python -m json.tool config/config.json >/dev/null && echo "config.json 格式正确"
```

准备日志目录：

```bash
mkdir -p logs
```

默认定时任务位于 `cron/crontab_list.sh`：

```cron
SHELL=/bin/sh
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

# 每天北京时间 01:10 和 07:10 执行全部已配置任务
10 1,7 * * * cd /app && dailycheckin >> /app/logs/dailycheckin.log 2>&1
```

容器固定使用 `Asia/Shanghai` 时区，因此 cron 中直接填写北京时间。需要调整时间时，编辑该文件后重启容器。

## 四、构建并启动

验证配置：

```bash
docker compose config
```

从当前源码构建镜像：

```bash
docker compose build --pull
```

后台启动：

```bash
docker compose up -d
```

也可以用一条命令完成构建和启动：

```bash
docker compose up -d --build
```

检查运行状态和启动日志：

```bash
docker compose ps
docker compose logs --tail=100
```

启动脚本会自动检查：

- `/app/config/config.json` 是否存在；
- 配置文件是否为合法 JSON；
- cron 文件是否存在；
- 定时任务是否成功加载。

## 五、验证部署

确认容器时区和定时任务：

```bash
docker compose exec dailycheckin date
docker compose exec dailycheckin crontab -l
```

确认安装的是镜像中的源码包：

```bash
docker compose exec dailycheckin python -c \
  'import dailycheckin; from dailycheckin.__version__ import __version__; print(__version__); print(dailycheckin.__file__)'
```

手动运行全部已配置任务：

```bash
docker compose exec dailycheckin dailycheckin
```

只运行或排除指定任务：

```bash
docker compose exec dailycheckin dailycheckin --include BAIDUWP
docker compose exec dailycheckin dailycheckin --exclude IMAOTAI MIMOTION
```

容器尚未启动时，也可以使用一次性容器测试：

```bash
docker compose run --rm dailycheckin dailycheckin --include BAIDUWP
```

查看签到日志：

```bash
tail -f logs/dailycheckin.log
```

建议首次部署先手动执行一次，确认账号配置、网络和通知均正常。

## 六、从现有旧容器迁移

> **注意：** 新旧部署不能同时运行，否则会重复执行签到任务。迁移前先备份旧目录；停止旧容器不会删除其配置和日志。

当前旧部署目录为 `/root/DailyCheckin` 时，可以先备份并复制配置：

```bash
sudo cp -a /root/DailyCheckin /root/DailyCheckin.backup
mkdir -p config
sudo cp /root/DailyCheckin/config/config.json ./config/config.json
sudo chown "$(id -u):$(id -g)" config/config.json
```

本源码部署已经提供适配 `/app` 路径的 `cron/crontab_list.sh`。如需沿用旧执行时间，请编辑新文件中的时间，不要直接复制包含 `/dailycheckin` 路径的旧 cron 文件。

检查新配置后，停止旧容器并启动源码版本：

```bash
python -m json.tool config/config.json >/dev/null
docker stop dailycheckin
docker compose up -d --build
```

检查新容器：

```bash
docker compose ps
docker compose logs --tail=100
docker compose exec dailycheckin dailycheckin --include BAIDUWP
```

如果新版本有问题，可以先停止它，再启动旧容器回退：

```bash
docker compose down
docker start dailycheckin
```

这里的回退命令要求旧容器仍然保留。确认源码版本长期稳定后，再决定是否删除旧容器。

## 七、更新源码

拉取代码并重建：

```bash
git pull --ff-only
docker compose up -d --build
```

Docker 会根据源码和依赖变化重建必要层。如果需要完全忽略缓存：

```bash
docker compose build --pull --no-cache
docker compose up -d
```

修改 `config/config.json` 后无需重建或重启。修改 `cron/crontab_list.sh` 后需要重启以重新加载：

```bash
docker compose restart dailycheckin
```

## 八、常用命令

```bash
# 查看状态
docker compose ps

# 查看容器启动日志
docker compose logs -f

# 查看签到日志
tail -f logs/dailycheckin.log

# 重启
docker compose restart

# 停止服务
docker compose stop

# 停止并删除容器，保留宿主机配置和日志
docker compose down
```

## 九、常见问题

### 修改源码后没有生效

源码在构建阶段安装，修改后需要重新构建镜像：

```bash
docker compose up -d --build
```

### 容器提示找不到 config.json

确认 `config/config.json` 是文件而不是目录：

```bash
ls -l config/config.json
python -m json.tool config/config.json >/dev/null
```

如果误生成了同名目录，需要先处理该目录，再从模板复制配置文件。

### 定时任务没有执行

检查容器时间、crontab、容器日志和签到日志：

```bash
docker compose exec dailycheckin date
docker compose exec dailycheckin crontab -l
docker compose logs --tail=100
tail -n 100 logs/dailycheckin.log
```

同时确保 `cron/crontab_list.sh` 最后一行以换行符结束。

### 构建后如何确认没有使用 PyPI 发布版

Dockerfile 中安装命令应为：

```dockerfile
RUN python -m pip install --no-cache-dir .
```

本方案没有 `pip install dailycheckin --upgrade`。查看构建日志时，应能看到从本地 `/app` 构建 `dailycheckin`。
