#!/home/fang/anaconda3/bin/python
import datetime
import os
import sys
import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def click_select_list(my_driver, data_id, answer_position):
    wait = WebDriverWait(my_driver, 60)
    main_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-id='%s'][1]" % (data_id,))))
    my_driver.execute_script("arguments[0].click();", main_button)
    list_item = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-id='%s']/..//li[@rel='%d']/a" % (data_id, answer_position))))
    my_driver.execute_script("arguments[0].click();", list_item)


def out_upload(username, password, web_address, **kwargs):
    option = webdriver.ChromeOptions()
    option.add_argument('headless')
    option.add_argument('--no-sandbox')
    option.add_argument('--disable-dev-shm-usage')

    # login
    driver = webdriver.Chrome(options=option)
    driver.get(web_address)
    wait = WebDriverWait(driver, 60)
    driver.implicitly_wait(60)
    elem = driver.find_element_by_id('un')
    elem.send_keys(username)
    elem = driver.find_element_by_id('pd')
    elem.send_keys(password)

    apply_button = driver.find_element_by_name('学生出校申请')
    apply_button.click()

    confirm_button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '#layui-layer1 .layui-layer-btn0:first-of-type')))
    confirm_button.click()
    wait.until(EC.frame_to_be_available_and_switch_to_it('formIframe'))

    # 出校类别
    click_select_list(driver, "CXLB", 1)

    # 出校事由
    click_select_list(driver, "CXSY", 3)

    # 地区
    click_select_list(driver, "SZSF", 1)
    click_select_list(driver, "SZSQ", 1)
    click_select_list(driver, "SZX", 6)

    # 具体事由
    other_reasons = driver.find_element_by_id('QTSY')
    other_reasons.send_keys(kwargs['specific_reason'])

    # 时间
    today = datetime.date.today() + datetime.timedelta(days=1)
    out_time_string = str(today) + ' 00:01'
    back_time_string = str(today) + ' 23:59'
    driver.execute_script("document.getElementById('JHCXSJ').value = \"%s\"" % (out_time_string,))
    driver.execute_script("document.getElementById('JHFXSJ').value = \"%s\"" % (back_time_string,))

    # 同意协议
    checkbox = driver.find_elements_by_xpath("//div[@id=\"CXCN_vant\"]//i")[0]
    checkbox.click()

    # 提交
    driver.switch_to.default_content()
    commit_button = driver.find_elements_by_xpath("//button[@id=\"commit\"]")[0]
    print(commit_button.text)
    # commit_button.click()
    time.sleep(1000)


if __name__ == '__main__':
    address = 'https://s.bjfu.edu.cn/tp_fp/view?m=fp#from=hall&serveID=280612cb-5fcf-47f2-850a-d2084ca7e3c6&act=fp/serveapply'
    dir_name = os.path.dirname(sys.argv[0])
    user_info = open(os.path.join(dir_name, 'out_user_info.txt'))
    for i in user_info:
        p = user_info.readline().strip('\n') + '\n'
        specific_reason = user_info.readline().strip('\n')
        out_upload(i, p, address, specific_reason=specific_reason)
