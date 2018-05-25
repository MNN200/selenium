from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

url="****"
driver=webdriver.Chrome()
driver.get(url)

#打开文件，按行读取用户名密码
file=open("D:\****\username.txt")
lines=file.readlines()
file1=open("D:\****\password.txt")
lines1=file1.readlines()

for i in lines:
	for j in lines1:
		driver.find_element_by_id("loginuserName1").send_keys(i)
		driver.find_element_by_id("loginpassword1").send_keys(j)
		#通过键盘事件进行确定
		driver.find_element_by_id("btn").send_keys(Keys.ENTER)
		time.sleep(3)
		#清空输入框
		driver.find_element_by_id("loginuserName1").clear()
		driver.find_element_by_id("loginpassword1").clear()
		#driver.back()
		
file.close()
file1.close()
driver.close()
