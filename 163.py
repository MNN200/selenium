#163µÄÓÊÏäµÇÂ½£¬iframeµÄÇÐ»»
from selenium import webdriver
import time

browser=webdriver.Chrome()
browser.maximize_window()
#browser.set_window_size(480,800)
browser.get("https://mail.163.com/")

#find iframe
iframe1 = browser.find_element_by_tag_name('iframe')
#change to iframe
browser.switch_to.frame(iframe1)

browser.find_element_by_name("email").send_keys("***")
browser.find_element_by_name("password").send_keys("****")
browser.find_element_by_id("dologin").click()
time.sleep(2)
browser.switch_to_default.content()