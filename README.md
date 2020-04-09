# 自动报健康

### 安装依赖

### 安装 python 模块

```bash
pip install selenium
```

### 安装 Chrome 驱动

[地址](https://sites.google.com/a/chromium.org/chromedriver/downloads)

### 更改配置


* 更改 `upload.py` 中的用户名和密码
* 更改 `crontab.txt` 中 `upload.py` 的绝对路径 

```bash
# 自动执行
crontab crontab.txt
```
