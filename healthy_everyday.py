#!/home/fang/anaconda3/bin/python
import os
import random
import sys
from datetime import datetime

from selenium import webdriver
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from out_every_day import click_select_list


def upload(username, password):
    option = webdriver.ChromeOptions()
    option.add_argument('headless')

    # login
    driver = webdriver.Chrome(options=option)
    driver.get(address)
    wait = WebDriverWait(driver, 60)
    elem = driver.find_element_by_id('un')
    elem.send_keys(username)
    elem = driver.find_element_by_id('pd')
    elem.send_keys(password)

    # commit
    driver.get(address)

    wait.until(EC.frame_to_be_available_and_switch_to_it('formIframe'))

    click_select_list(driver, "TW1", random.randint(1, 6))
    click_select_list(driver, "TW2", random.randint(1, 6))
    click_select_list(driver, "TW3", random.randint(1, 6))

    driver.switch_to.default_content()

    commit = wait.until(EC.element_to_be_clickable((By.ID, 'commit')))
    commit.click()
    # time.sleep(1000)
    driver.close()


if __name__ == '__main__':
    dir_name = os.path.dirname(sys.argv[0])
    address = open(os.path.join(dir_name, 'address.txt')).readline()
    user_info = open(os.path.join(dir_name, 'user_info.txt'))
    print(datetime.today())
    for i in user_info:
        p = user_info.readline().strip('\n') + '\n'
        try:
            upload(i, p)
            print(i + " 填报完成")
        except UnexpectedAlertPresentException:
            print(i + " 已经填报")
