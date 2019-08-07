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
            "wwrtx.vst": "Ly8_fvFcOApbvwrjYiTh2fQ0OBrr2zzKvQHp1aRUHZCtVy7L_M_ei11GTKdEMyQyEc9Q-Q3-l3CnyZbikBvF2KBY_AIg5G0E7fjjO7UMFEvzjto4nbNOtWZE-EI8FlkRiifSGa7WCeZXceeUHEn2ZZO3IF_y9Yih9V1PY3fKxQQgGzBidZZdMjZ26n2GTfv3YUKjm-QQM5x-5xNUhWDsYWGS6-uGmo7tTNrXkcZCQis9yuO4nnezC6pd4MEQW-hPXSOjDQv7NIjD3BYdUjuOMA",
            "wwrtx.d2st": "a5255438",
            "wwrtx.sid": "5KLjjmW-aMstJ0AquQESE7RC3tEejOln6lERyso5XMebdIOCPWDu7HikID84CX5U",
            "wwrtx.ltype": "1",
            "wxpay.corpid": "1970324954080438",
            "wxpay.vid": "1688851903656484",
        }
        for k, v in cookies.items():
            self.driver.add_cookie({"name": k, "value": v})

        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")

    def teardown(self):
        pass
        # self.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
    def test_add(self):
        locator = ".ww_operationBar:first-child .js_add_member"
        WebDriverWait(self.driver, 5, 1, ignored_exceptions="TimeoutException").until(
            expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, locator)))
        self.driver.find_element(By.CSS_SELECTOR, locator).click()

        # for index in range(10):
        #     print(self.driver.find_element(By.CSS_SELECTOR, locator).rect)
        #     print(self.driver.find_element(By.CSS_SELECTOR, locator).text)
        #     print(self.driver.find_element(By.CSS_SELECTOR, locator).size)
        #     print(self.driver.find_element(By.CSS_SELECTOR, locator).tag_name)
        #     time.sleep(0.5)
        # self.click_js(By.CSS_SELECTOR, locator)
        # self.driver.find_element(By.CSS_SELECTOR, locator).click()
        # 输入姓名
        # WebDriverWait(self.driver, 5, 1, ignored_exceptions="TimeoutException").until(
        #     expected_conditions.element_to_be_clickable((By.NAME, "#username")))
        self.driver.find_element(By.CSS_SELECTOR, "input[name*='username']").send_keys("zhangxiao")

        # 输入别名
        self.driver.find_element(By.CSS_SELECTOR, "#memberAdd_english_name").send_keys("bangzhu")
        # 输入账号
        self.driver.find_element(By.NAME, "acctid").send_keys("xt123456")
        # 点击xingbie
        self.driver.find_element(By.XPATH, "//span[contains(text(), '女')]").click()
        # 输入电话
        self.driver.find_element(By.NAME, "mobile").send_keys("17729597956")

    def click_js(self, by, element):
        self.driver.execute_script("arguments[0].click();", self.driver.find_element(by, element))
