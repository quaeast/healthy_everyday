FROM quaeast/ubuntu-chrome-driver:0.0.2
COPY . /root/healthy_everyday
RUN crontab /root/healthy_everyday/crontab.txt
RUN echo 'service cron start' >> /root/.bashrc
CMD ["/bin/bash"]
