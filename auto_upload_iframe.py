#!/home/fang/anaconda3/bin/python
import os
import sys
import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException


def upload_iframe(username, password):
    option = webdriver.ChromeOptions()
    # option.add_argument('headless')

    # login
    # driver = webdriver.Chrome(options=option)
    driver = webdriver.Chrome()
    driver.get(address)
    elem = driver.find_element_by_id('un')
    elem.send_keys(username)
    elem = driver.find_element_by_id('pd')
    elem.send_keys(password)

    # commit
    driver.get(address)
    try:
        time.sleep(10)
        alert_obj = driver.switch_to.alert
        alert_obj.accept()
    except NoAlertPresentException:
        pass
    time.sleep(10)
    driver.switch_to.frame('formIframe')
    try:
        commit = driver.find_element_by_id('commit')
        print(commit)
        # commit.click()
        print("报告成功")
    except NoSuchElementException:
        print("已报告")


if __name__ == '__main__':
    dir_name = os.path.dirname(sys.argv[0])
    address = open(os.path.join(dir_name, 'address.txt')).readline()
    user_info = open(os.path.join(dir_name, 'user_info.txt'))
    for i in user_info:
        p = user_info.readline().strip('\n') + '\n'
        upload_iframe(i, p)
