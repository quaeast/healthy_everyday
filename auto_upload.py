#!/usr/local/anaconda3/bin/python
from selenium import webdriver
import time
import os
import sys


def upload(username, password):
    # login
    driver = webdriver.Chrome()
    driver.get(address)
    elem = driver.find_element_by_id('un')
    elem.send_keys(username)
    elem = driver.find_element_by_id('pd')
    elem.send_keys(password)

    # commit
    driver.get(address)
    time.sleep(10)
    while True:
        try:
            commit = driver.find_element_by_id('commit')
            commit.click()
            print(commit.text)
            break
        except BaseException as e:
            print(e.args)
            print('error')
            pass


if __name__ == '__main__':
    dir_name = os.path.dirname(sys.argv[0])
    address = open(os.path.join(dir_name, 'address.txt')).readline()
    user_info = open(os.path.join(dir_name, 'user_info.txt'))
    for i in user_info:
        p = user_info.readline().strip('\n') + '\n'
        try:
            upload(i, p)
        except BaseException:
            print(i+'失败')
            pass
