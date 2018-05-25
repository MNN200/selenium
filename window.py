
import time
from selenium import webdriver
url="*****"

browser=webdriver.Chrome()
browser.get(url)
time.sleep(2)

#获取当前页面的窗口句柄
handle=browser.current_window_handle
print handle
#获取所有窗口句柄
browser.find_element_by_link_text('j1111').click()
handles=browser.window_handles
print handles

#方法一：判断句柄是否首页相等
for i in handles:
    if i!=handle:
        browser.switch_to.window(i)
        print browser.title
        browser.close()
        browser.switch_to.window(handle)
        print browser.title
#方法二：直接在list列表的值
browser.switch_to.window(handles[0])
print browser.tit