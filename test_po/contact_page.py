from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from test_po.basepage import BasePage
from test_po.profile_page import ProfilePage


class ContactPage(BasePage):
    def __init__(self, wewoek):
        self.driver = wewoek.driver

    def add_member(self, name, alias, id, moblie, **kwargs):
        locator = ".ww_operationBar:first-child .js_add_member"
        WebDriverWait(self.driver, 10, 1, ignored_exceptions="TimeoutException").until(
            expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, locator)))
        # self.driver.find_element(By.CSS_SELECTOR, locator).click()

        # for index in range(10):
        #     print(self.driver.find_element(By.CSS_SELECTOR, locator).rect)
        #     print(self.driver.find_element(By.CSS_SELECTOR, locator).text)
        #     print(self.driver.find_element(By.CSS_SELECTOR, locator).size)
        #     print(self.driver.find_element(By.CSS_SELECTOR, locator).tag_name)
        #     time.sleep(0.5)
        # self.driver.find_element(By.CSS_SELECTOR, locator).click()
        self.click_js(By.CSS_SELECTOR, locator)
        # 输入姓名
        self.driver.find_element(By.CSS_SELECTOR, "input[name*='username']").send_keys(name)
        # 输入别名
        self.driver.find_element(By.CSS_SELECTOR, "#memberAdd_english_name").send_keys(alias)
        # 输入账号
        self.driver.find_element(By.NAME, "acctid").send_keys(id)
        # 点击xingbie
        self.driver.find_element(By.XPATH, "//span[contains(text(), '女')]").click()
        # 输入电话
        self.driver.find_element(By.NAME, "mobile").send_keys(moblie)
        # 点击取消按钮
        self.driver.find_element(By.CSS_SELECTOR, "form>div:last-child .js_btn_cancel").click()
        # 输入别名
        self.driver.find_element(By.XPATH, "//a[contains(text(),'离开此页')]").click()

    def delete_member(self):
        pass

    def get_tips(self):
        return "ok"

    def search(self, key):
        self.driver.find_element(By.CSS_SELECTOR, "#memberSearchInput").send_keys(key)
        return ProfilePage(self.driver)

