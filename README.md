# 自动报健康

## 新增出校申请 out_every_day.py

## 通用配置

### 安装 python 模块

```bash
pip install selenium
```

## 更改配置

* 新建 `user_info.txt`，逐行添加用户名和密码（格式为一行学号一行密码，中间和结尾无空行）
* 更改 `crontab.txt` 中 `upload.py` 的绝对路径
* 修改 `auto_upload.py` 的 `#!` 路径 
* 运行如下命令实现定时启动

```shell script
# 自动执行
crontab crontab.txt
```

**注意：不要用 root 运行**

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

## docker 一键部署

```shell script
sudo docker pull quaeast/healthy

sudo docker run -p 8888:22 -d --name systemd-ubuntu --tmpfs /tmp --tmpfs /run --tmpfs /run/lock -v /sys/fs/cgroup:/sys/fs/cgroup:ro quaeast/healthy

# passwd: fang
ssh -p 8888 fang@localhost 'echo -e "{username}\n{password}" >> /home/fang/healthy_everyday/user_info.txt'
```

