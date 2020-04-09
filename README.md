# 自动报健康

### 安装依赖

### 安装 python 模块

```bash
pip install selenium
```

### 安装 Chrome 驱动

[地址](https://sites.google.com/a/chromium.org/chromedriver/downloads)

### 更改配置

* 新建 `user_info.txt`，逐行添加用户名和密码
* 更改 `crontab.txt` 中 `upload.py` 的绝对路径 
* 设置 Energy Saver 中的自动启动时间为00:10之前
* 运行如下命令

```bash
# 自动执行
crontab crontab.txt
```
