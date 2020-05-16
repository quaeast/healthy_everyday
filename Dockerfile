FROM continuumio/anaconda3:2020.02
RUN mkdir -p /home/healthy_everyday
WORKDIR /home/healthy_everyday
COPY . /home/healthy_everyday
RUN pip install selenium
RUN apt update
RUN apt install -y cron
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN dpkg -i google-chrome*.deb
RUN apt update
sudo apt install -fy
RUN wget https://chromedriver.storage.googleapis.com/81.0.4044.138/chromedriver_linux64.zip
RUN apt install unzip
RUN unzip chromedriver_linux64.zip
RUN mv chromedriver /usr/bin
RUN touch user_info.txt
RUN crontab crontab.txt
