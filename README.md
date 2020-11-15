# 自动报健康

## 安装依赖

### 安装 python 模块

```bash
pip install selenium
```

### 安装 Chrome 驱动

[地址](https://sites.google.com/a/chromium.org/chromedriver/downloads)

## 更改配置

* 新建 `user_info.txt`，逐行添加用户名和密码（格式为一行学号一行密码，中间和结尾无空行）
* 更改 `crontab.txt` 中 `upload.py` 的绝对路径
* 修改 `auto_upload.py` 的 `#!` 路径 
* 运行如下命令实现定时启动

```shell script
# 自动执行
crontab crontab.txt
```

## Ubuntu server 配置

### 安装Chrome

```shell script
# 下载
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb

# 安装
sudo dpkg -i google-chrome*.deb

# 如果上一步出现问题，运行
sudo apt update
sudo apt install -fy

# 查看版本
google-chrome --version
```

### 安装驱动

[下载地址](https://sites.google.com/a/chromium.org/chromedriver/downloads)

```shell script
wget https://sites.google.com/a/chromium.org/chromedriver/downloads
unzip chromedriver_linux64.zip
mv chromedriver /usr/bin
```

### docker 配置

```shell script
docker build . -t healthy_every_day
docker run -Pit healthy_every_day

# 在 user_info.txt 中添加学号姓名，可以添加多人，要求中间无空行，结尾无空行。

ctrl + pq
```

## 新增出校申请 out_every_day.py

