from selenium import webdriver
import time

driver=webdriver.Firefox()
driver.get("https://www.cnblogs.com/yoyoketang/")
# driver.get("https://sh.ganji.com")
time.sleep(1)
#滚动到底部
js="window.scrollTo(0,document.body.scrollHeight)"
driver.execute_script(js)

time.sleep(1)
#顶部
js="window.scrollTo(0,0)"
driver.execute_script(js)

# ele=driver.find_element_by_link_text("新车")
# driver.execute_script("arguments[0].scrollIntoView();", ele)