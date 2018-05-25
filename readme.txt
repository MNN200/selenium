#selenium+python的操作练习

浏览器：chrome
1.确定chrome的版本，chrome://version 
2.查找chrome对应的chromedriver,下载，放到python路径和浏览器的路径下

安装python

安装selenium
1.下载selenium（放到python路径下）
2.安装：pip install selenium


alert/confirm/prompt弹出框操作主要方法有：
text：获取文本值
accept() ：点击"确认"
dismiss() ：点击"取消"或者叉掉对话框
send_keys() ：输入文本值 --仅限于prompt,在alert和confirm上没有输入框

1.先用switch_to_alert()方法切换到alert弹出框上
2.可以用text方法获取弹出的文本 信息
3.accept()点击确认按钮
4.dismiss()相当于点右上角x，取消弹出框
5.send_keys()这里多个输入框，可以用send_keys()方法输入文本内容

browser.find_element_by_id('alert').click()
a=browser.switch_to.alert()
a.accept()


 # 勾选前判断是否勾选
 t = browser.find_element_by_id('c1').is_selected()
