import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestDemo:
    def setup(self):
        # 使用Chrome-debug绕过登录
        # chrome_options = webdriver.ChromeOptions()
        # chrome_options.debugger_address = "127.0.0.1:9999"
        # self.driver = webdriver.Chrome(options=chrome_options)
        # self.driver.implicitly_wait(10)  # 隐士等待

        # 通过cookies绕过登录
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
        cookies = {
            "wwrtx.vst": "F7_e3AWbJRf5nI8axNKtZodcW5TAPHd39_wEeY8GFhPDHwDOwjpqFyrWzbeEz5JtXGMD8kzkDhwS-4_aU9IX8U5GIUTlhAgbUbY2-Iy_Z593rWSNApTXKD4UdtYLa13ApNZ2Eev1fnRJ-zhuKqHURiQK1ByEADOpkTzM7UvkCHzvVCdCkc1IfgX2SQflV6ZiWS9yL7ZdSUVnIg63EydzAIf3WOlmlMVWTTJGEydgJ0hXpUKj_y1FYnD0-ZBdyNRAmiaFU08M0rxABFHF2wVMcw",
            "wwrtx.d2st": "a1687837",
            "wwrtx.sid": "5KLjjmW-aMstJ0AquQESE9H_RbxQ9Kk7Fw2Ce6nF8ox7Zna_sTYKRG2z99XiHR4P",
            "wwrtx.ltype": "1",
            # "wxpay.corpid": "1970324954080438",
            # "wxpay.vid": "1688851903656484",
        }
        for k, v in cookies.items():
            self.driver.add_cookie({"name": k, "value": v})

        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")

    def teardown(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")

    def test_add(self):
        locator = ".ww_operationBar:first-child .js_add_member"
        WebDriverWait(self.driver, 5, 1, ignored_exceptions="TimeoutException").until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, locator)))
        # self.driver.find_element(By.CSS_SELECTOR, locator).click()

        # for index in range(10):
        #     print(self.driver.find_element(By.CSS_SELECTOR, locator).rect)
        #     print(self.driver.find_element(By.CSS_SELECTOR, locator).text)
        #     print(self.driver.find_element(By.CSS_SELECTOR, locator).size)
        #     print(self.driver.find_element(By.CSS_SELECTOR, locator).tag_name)
        #     time.sleep(0.5)
        self.driver.find_element(By.CSS_SELECTOR,locator).click()

        # 输入姓名
        self.driver.find_element(By.CSS_SELECTOR, "#username").send_keys("zhangxiao")
        # 输入别名
        self.driver.find_element(By.CSS_SELECTOR, "#memberAdd_english_name").send_keys("bangzhu")
        #输入账号
        self.driver.find_element(By.NAME, "acctid").send_keys("xt123456")
        # 点击xingbie
        self.driver.find_element(By.XPATH, "//span[contains(text(), '女')]").click()
        # 输入电话
        self.driver.find_element(By.NAME, "mobile").send_keys("17729597956")
