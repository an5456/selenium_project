import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import logging
logging.basicConfig(level=logging.INFO)


class TestSelenium:
    def setup(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.debugger_address = "127.0.0.1:9999"
        self.driver = webdriver.Chrome(options=chrome_options)
        # self.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
        self.driver.implicitly_wait(10)

    def test_add(self):
        # add_element = self.driver.find_element(By.XPATH,"//div[@class='ww_operationBar']/a[1]")
        # self.driver.find_element(By.LINK_TEXT, "添加成员").click()
        # add_element = self.driver.find_element(By.CSS_SELECTOR, ".ww_operationBar:first-child .js_add_member")
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".ww_operationBar:first-child "
                                                                                ".js_add_member")))

        self.click_js(By.CSS_SELECTOR, ".ww_operationBar:first-child .js_add_member")
        # print(add_element.text)
        # add_element.click()
        logging.info(self.driver.page_source)
        logging.info(self.driver.title)

    def test_upload_file(self):
        click_add = self.driver.find_element(By.CSS_SELECTOR, ".js_upload_file_selector")

        print(click_add.text)
        print(click_add.rect)
        # print(self.driver.execute_script("console.log('hello from selenium')"))
        # # print(self.driver.execute_script("return document.title;"))
        # click_add.click()

        self.driver.execute_script("arguments[0].click();", click_add)

        upload_image = self.driver.find_element(By.CSS_SELECTOR, "#js_upload_input")
        upload_image.send_keys("/Users/anxiaodong/Downloads/timg.jpeg")
        print(self.driver.page_source)
        WebDriverWait(self.driver, 3).until_not(
            expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".js_uploadProgress_cancel")))
        # time.sleep(5)
        self.click_js(By.CSS_SELECTOR, ".js_next")
        # self.driver.execute_script("arguments[0].click();", self.driver.find_element(By.CSS_SELECTOR, ".js_next"))
        # self.driver.find_element(By.CSS_SELECTOR, "a[d_ck*='submit']").click()

    # 使用js点击元素
    def click_js(self, by, element):
        self.driver.execute_script("arguments[0].click();", self.driver.find_element(by, element))
        # /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9999
