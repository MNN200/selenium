#!/usr/bin/env python
#vim : set fileencoding=utf-8:

from selenium import webdriver
import time
#��ȡҳ��title

url="https://www.zhihu.com"
browser=webdriver.Chrome()
browser.get(url)
'''
#��ȡ����
#print(browser.title)
#��ȡ�ı�
text=browser.find_element_by_id('setf').text
print text

#��ȡԪ�ر�ǩ
tag=browser.find_element_by_id('kw').tag_name
print tag
#��ȡԪ�ص�����������
name=browser.find_element_by_id('kw').get_attribute('class')
print name
#��ȡ���������
print browser.name
'''


