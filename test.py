from selenium import webdriver
import time

browser=webdriver.Chrome()
browser.maximize_window()
browser.get("rrrr")
print 1111
browser.find_element_by_id("loginuserName").send_keys('111')
print 333333
browser.find_element_by_id("loginpassword").send_keys('111')
print 22222222222
browser.find_element_by_id("btn").click()