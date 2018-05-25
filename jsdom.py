from selenium import webdriver
import time

driver=webdriver.Chrome()
driver.get("ssss")
time.sleep(2)
js='document.getElementById("").style.display="none"'
driver.execute_script(js)
driver.quit()