#!/home/fang/anaconda3/bin/python

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
import time
import os
import sys


def upload(username, password):
    option = webdriver.ChromeOptions()
    option.add_argument('headless')

    # login
    driver = webdriver.Chrome(options=option)
    driver.get(address)
    elem = driver.find_element_by_id('un')
    elem.send_keys(username)
    elem = driver.find_element_by_id('pd')
    elem.send_keys(password)

    # commit
    driver.get(address)
    flag = True
    while flag:
        try:
            time.sleep(60)
            commit = driver.find_element_by_id('commit')
            commit.click()
            print(str(username) + commit.text)
            flag = False
        except NoSuchElementException as e:
            print('获取中...')
        except ElementClickInterceptedException as e:
            print('已平安')
            flag = False
    driver.close()


if __name__ == '__main__':
    dir_name = os.path.dirname(sys.argv[0])
    address = open(os.path.join(dir_name, 'address.txt')).readline()
    user_info = open(os.path.join(dir_name, 'user_info.txt'))
    for i in user_info:
        p = user_info.readline().strip('\n') + '\n'
        upload(i, p)

