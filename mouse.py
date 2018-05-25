from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

#鼠标悬停
url="https://www.baidu.com"
browser=webdriver.Chrome()
browser.get(url)
above=browser.find_element_by_link_text('设置')
#perform():执行所有的ActionChains
ActionChains(browser).move_to_element(above).perform()
#context_click()右击
#ActionChains(browser).move_to_element(above).context_click()
#double_click()双击
#ActionChains(browser).move_to_element(above).double_click()
#drag_and_drop():拖动
#ActionChains(browser).move_to_element(above).drag_and_drop()
#move_to_element()鼠标悬停
#ctionChains(browser).move_to_element(above).

#键盘事件

browser.find_element_by_id('kw').send_keys('python!!')
#send_keys(Keys.BACK_SPACE)删除键
browser.find_element_by_id('kw').send_keys(Keys.BACK_SPACE)
#空格键send_keys(Keys.SPACE)
browser.find_element_by_id('kw').send_keys(Keys.SPACE)
browser.find_element_by_id('kw').send_keys("learn")
#ctrl+a send_keys(Keys.CONTROL,'a')
browser.find_element_by_id('kw').send_keys(Keys.CONTROL,'a')
browser.find_element_by_id('kw').send_keys(Keys.CONTROL,'x')
browser.find_element_by_id('kw').send_keys(Keys.CONTROL,'v')
#send_keys('Keys.ENTER')回车成为确认按键
browser.find_element_by_id('su').send_keys(Keys.ENTER)
#send_keys('Keys.F1-F12)
browser.find_element_by_id('su').send_keys(Keys.F1)