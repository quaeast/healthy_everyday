from selenium import webdriver
import time

address = open('address.txt')
address = address.readline()

# login
driver = webdriver.Chrome()
driver.get(address)
elem = driver.find_element_by_id('un')
elem.send_keys('??')
elem = driver.find_element_by_id('pd')
elem.send_keys('??')
elem = driver.find_element_by_id('index_login_btn')
elem.click()

# commit
driver.get(address)
elem = driver.find_element_by_id('commit')
elem.click()
time.sleep(100)
driver.close()
