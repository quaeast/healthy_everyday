# 自动报健康

## 安装依赖

### 安装 python 模块

```bash
pip install selenium
```

### 安装 Chrome 驱动

[地址](https://sites.google.com/a/chromium.org/chromedriver/downloads)

## 更改配置

* 新建 `user_info.txt`，逐行添加用户名和密码
* 更改 `crontab.txt` 中 `upload.py` 的绝对路径
* 修改 `auto_upload.py` 的 `#!` 路径 
* 设置 Energy Saver 中的自动启动时间为00:10之前
* 运行如下命令实现定时启动

```bash
# 自动执行
crontab crontab.txt
```

## 注意

* 需要给 cron 和 crontab 两个软件 full disk access

## 笔记

```python
# 不显示浏览器（存疑）
option = webdriver.ChromeOptions()
option.add_argument('headless')
driver = webdriver.Chrome(options=option)
```
