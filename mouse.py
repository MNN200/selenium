from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

#�����ͣ
url="https://www.baidu.com"
browser=webdriver.Chrome()
browser.get(url)
above=browser.find_element_by_link_text('����')
#perform():ִ�����е�ActionChains
ActionChains(browser).move_to_element(above).perform()
#context_click()�һ�
#ActionChains(browser).move_to_element(above).context_click()
#double_click()˫��
#ActionChains(browser).move_to_element(above).double_click()
#drag_and_drop():�϶�
#ActionChains(browser).move_to_element(above).drag_and_drop()
#move_to_element()�����ͣ
#ctionChains(browser).move_to_element(above).

#�����¼�

browser.find_element_by_id('kw').send_keys('python!!')
#send_keys(Keys.BACK_SPACE)ɾ����
browser.find_element_by_id('kw').send_keys(Keys.BACK_SPACE)
#�ո��send_keys(Keys.SPACE)
browser.find_element_by_id('kw').send_keys(Keys.SPACE)
browser.find_element_by_id('kw').send_keys("learn")
#ctrl+a send_keys(Keys.CONTROL,'a')
browser.find_element_by_id('kw').send_keys(Keys.CONTROL,'a')
browser.find_element_by_id('kw').send_keys(Keys.CONTROL,'x')
browser.find_element_by_id('kw').send_keys(Keys.CONTROL,'v')
#send_keys('Keys.ENTER')�س���Ϊȷ�ϰ���
browser.find_element_by_id('su').send_keys(Keys.ENTER)
#send_keys('Keys.F1-F12)
browser.find_element_by_id('su').send_keys(Keys.F1)