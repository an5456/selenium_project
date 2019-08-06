from selenium import webdriver
import time
browser = webdriver.Firefox()
browser.get("http://www.baidu.com")
browser.find_element_by_id("kw").send_keys("pytest")
browser.find_element_by_id("su").click()
time.sleep(5)
browser.quit()

