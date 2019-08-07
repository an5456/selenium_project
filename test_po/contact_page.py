import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from test_po.basepage import BasePage
from test_po.profile_page import ProfilePage
from test_po.wework_page import Wework


class ContactPage(BasePage):
    _username = (By.NAME, "username")
    _alias = (By.NAME, "english_name")
    _id = (By.NAME, "acctid")
    _mobile = (By.NAME, "mobile")
    _cancel = (By.CSS_SELECTOR, ".js_btn_cancel")
    _leave = (By.XPATH, "//*[text()='离开此页']")
    _add = (By.CSS_SELECTOR, ".ww_operationBar:first-child .js_add_member")
    _search = (By.ID, "memberSearchInput")

    def __init__(self, wewoek: Wework):
        self._driver = wewoek.driver

    def add_member(self, name, alias, id, moblie, **kwargs):
        # WebDriverWait(self._driver, 10, 1, ignored_exceptions="TimeoutException").until(
        #     expected_conditions.element_to_be_clickable(self._add))
        # self.driver.find_element(By.CSS_SELECTOR, *self._add).click()
        # self.click_by_js(*self._add)
        while True:
            try:
                    # print(index)
                    # element = self.find(self._add)
                    # print(element.text)
                    # print(element.tag_name)
                    # print(element.rect)
                    # print(element.is_displayed())
                    # print(element.is_enabled())
                    # print(self._driver.execute_script(
                    #         'return document.querySelector(".js_has_member .ww_operationBar .js_add_member").getBoundingClientRect();'))
                self.click_by_js(*self._add)
                if len(self._driver.find_elements(By.XPATH, "//*[text()='取消']")) >= 1:
                    print("ok")
                    break
            except Exception as e:
                print("except")
                print(e)

        # def click_and_find(x):
        #     self.click_by_js(*self._add)
        #     return len(x.find_elements(By.XPATH, '//*[text()="取消"]')) >= 1
        # WebDriverWait(self._driver, 5).until(click_and_find)

        # 输入姓名
        self.find(*self._username).send_keys(name)
        # 输入别名
        self.find(*self._alias).send_keys(alias)
        # 输入账号
        self.find(*self._id).send_keys(id)
        # 点击xingbie
        # self.driver.find_element(By.XPATH, "//span[contains(text(), '女')]").click()
        # 输入电话
        self.find(*self._mobile).send_keys(moblie)
        # 点击取消按钮
        self.find(*self._cancel).click()
        # 输入别名
        self.find(*self._leave).click()

    def delete_member(self):
        pass

    def get_tips(self):
        return "ok"

    def search(self, key):
        self._driver.find_element(*self._search).send_keys(key)
        return ProfilePage(self._driver)
