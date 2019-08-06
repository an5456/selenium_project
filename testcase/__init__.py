from selenium import webdriver
import time

firefox_capabilities = {
    "browserName": "chrome",
    "version": "",  # 注意版本号一定要写对
    "platform": "ANY",
    "javascriptEnabled": True,
    "marionette": True,
}
browser = webdriver.Remote("http://127.0.0.1:4444/wd/hub",
                           desired_capabilities=firefox_capabilities)  # 注意端口号5555是我们上文中映射的宿主机端口号

browser.get("http://www.baidu.com")

browser.find_element_by_id('kw').send_keys('软件测试')
browser.find_element_by_id('su').click()
time.sleep(1)
browser.get_screenshot_as_file("./baidu.png")
time.sleep(1)
browser.quit()
