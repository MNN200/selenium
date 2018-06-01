#!/usr/bin/env python
#vim : set fileencoding=utf-8:

from selenium import webdriver
import time
#获取页面title

url="https://www.zhihu.com"
browser=webdriver.Chrome()
browser.get(url)
'''
#获取标题
#print(browser.title)
#获取文本
text=browser.find_element_by_id('setf').text
print text

#获取元素标签
tag=browser.find_element_by_id('kw').tag_name
print tag
#获取元素的其他的属性
name=browser.find_element_by_id('kw').get_attribute('class')
print name
#获取浏览器名称
print browser.name
'''


