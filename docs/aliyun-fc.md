# 阿里云函数计算教程

### 一、创建服务和函数

> 地域选哪里都可以

![创建服务](img/fc_create_service.jpg)

![创建函数](img/fc_create_function.jpg)

### 二、修改超时时间并配置定时触发器

在“触发器管理”页签中添加定时触发器

![添加触发器](img/fc_add_trigger.jpg)

在“函数配置”页签中修改超时时间

![修改超时时间](img/fc_edit_timeout.jpg)

### 三、修改代码并安装依赖

![修改代码](img/fc_edit_code.jpg)

```python
# -*- coding: utf-8 -*-
from dailycheckin.main import checkin


def handler(event, context):
  checkin()
```

![安装依赖包](img/fc_module_install.jpg)

```bash
pip3 install dailycheckin --upgrade -t .
```

### 四、添加配置文件

> ⚠️ 请务必到 [http://www.json.cn](http://www.json.cn) 网站检查 `config.json` 文件格式是否正确！

![添加配置文件](img/fc_config.jpg)

### 四、部署并测试

![部署](img/fc_deploy.jpg)

![测试](img/fc_test.jpg)
