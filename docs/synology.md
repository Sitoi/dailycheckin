# 群晖 Docker 使用教程

## 一、注册表搜索 sitoi 或者 dailycheckin ， 双击下载

![获取 cookie 教程](https://cdn.jsdelivr.net/gh/Sitoi/dailycheckin/docs/img/synology1.jpg)

如果注册表储存库没找到，请添加 Docker Hub 库地址：https://registry.hub.docker.com

![获取 cookie 教程](https://cdn.jsdelivr.net/gh/Sitoi/dailycheckin/docs/img/synology2.jpg)

## 二、映像 下载完成 双击或者点击启动开始创建

![获取 cookie 教程](https://cdn.jsdelivr.net/gh/Sitoi/dailycheckin/docs/img/synology3.jpg)

点击高级设置，设置卷，按照下图添加文件夹和装载路径

![获取 cookie 教程](https://cdn.jsdelivr.net/gh/Sitoi/dailycheckin/docs/img/synology4.jpg)

![获取 cookie 教程](https://cdn.jsdelivr.net/gh/Sitoi/dailycheckin/docs/img/synology5.jpg)

群晖内本地文件夹请自行创建

![获取 cookie 教程](https://cdn.jsdelivr.net/gh/Sitoi/dailycheckin/docs/img/synology6.jpg)

```text
.
|-- config
|   `-- config.json
|-- docker-compose.yml
|-- logs
|   `-- default_task.log
`-- Makefile
```

如图，设置好直接点应用，其他默认，可按需点击高级设置里的启用自动重新启动，以防机器意外重启出现脚本停止现象。
![获取 cookie 教程](https://cdn.jsdelivr.net/gh/Sitoi/dailycheckin/docs/img/synology7.jpg)

## 三、回到容器，如图即是运行成功
![获取 cookie 教程](https://cdn.jsdelivr.net/gh/Sitoi/dailycheckin/docs/img/synology8.jpg)

## 四：配置测试

1、双击容器查看进程，如下图说明正在运行

![获取 cookie 教程](https://cdn.jsdelivr.net/gh/Sitoi/dailycheckin/docs/img/synology9.jpg)

2、日志查看运行状态

![获取 cookie 教程](https://cdn.jsdelivr.net/gh/Sitoi/dailycheckin/docs/img/synology10.jpg)

3、执行脚本之后自动生成的脚本

![获取 cookie 教程](https://cdn.jsdelivr.net/gh/Sitoi/dailycheckin/docs/img/synology11.jpg)
