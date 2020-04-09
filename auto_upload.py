from selenium import webdriver
import time


# option = webdriver.ChromeOptions()
# option.add_argument('headless')
# driver = webdriver.Chrome(options=option)


def upload(username, password):
    # login
    driver = webdriver.Chrome()
    driver.get(address)
    elem = driver.find_element_by_id('un')
    elem.send_keys(username)
    elem = driver.find_element_by_id('pd')
    elem.send_keys(password)
    elem = driver.find_element_by_id('index_login_btn')
    elem.click()

    # commit
    driver.get(address)
    elem = driver.find_element_by_id('commit')
    elem.click()
    time.sleep(10)
    driver.close()


if __name__ == '__main__':
    address = open('address.txt').readline()
    user_info = open('user_info.txt')
    for i in user_info:
        p = user_info.readline()
        try:
            upload(i, p)
        except BaseException:
            print(i)
            pass

