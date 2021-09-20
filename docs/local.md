# 本地使用教程

## 一、安装

```bash
pip install dailycheckin --user
```

## 二、编写 `config.json` 配置文件

> ⚠️ 请务必到 [http://www.json.cn](http://www.json.cn) 网站检查 `config.json` 文件格式是否正确！

参考[配置说明文档](https://sitoi.gitee.io/dailycheckin/settings/) ，并修改 `config.json`

## 三、单次运行

1. 运行全部脚本

    ```bash
    dailycheckin
    ```

2. 运行指定脚本（包含），可以同时选择多个，用「空格」分开

    ```bash
    dailycheckin --include MUSIC163 BAIDU 
    ```

3. 运行指定脚本（排除），可以同时选择多个，用「空格」分开

    ```bash
    dailycheckin --exclude MUSIC163 BAIDU 
    ```

## 四、更新

```bash
pip install dailycheckin --user --upgrade
```
