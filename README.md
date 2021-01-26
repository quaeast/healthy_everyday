# 自动报健康

## 新增出校申请 out_every_day.py

## 新增零部署功能

fork本项目，携带 github actions 配置文件。之后在 Settings-Secrets-Actions secrets 下点击 New repository secret，添加 secret 变量`USERNAME`和`PASSWORD`为数字北林的账号和密码（应该就是校园网的）。即可在每天1：15自动报健康。

感谢 [Supermesir](https://github.com/Supremesir) 同学的启发。

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


### bash init (recmmend)

```shell script
sudo docker pull quaeast/healthy_everyday:latest

docker run -it --name healthy quaeast/healthy_everyday:latest

cd /root/healthy_everyday;echo -e "{username}\n{password}" >> user_info.txt
```
按 `ctrl p+q` detach

### systemd init

```shell script
sudo docker pull quaeast/healthy

sudo docker run -p 8888:22 -d --name healthy --tmpfs /tmp --tmpfs /run --tmpfs /run/lock -v /sys/fs/cgroup:/sys/fs/cgroup:ro quaeast/healthy

# passwd: fang
ssh -p 8888 fang@localhost 'echo -e "{username}\n{password}" >> /home/fang/healthy_everyday/user_info.txt'

# 更新代码
ssh -p 8888 fang@localhost 'cd ~/healthy_everyday;ls;git fetch;git rebase'
```
