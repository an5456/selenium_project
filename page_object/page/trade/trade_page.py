import time

from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from page_object.page.basepage import BasePage


class TradePage(BasePage):
    _danjuan_open = (By.XPATH, '//*[@text="已有蛋卷基金账户登录"]')
    #"//*[@text='交易']"
    _danjuan_menu = (By.ID, "page_type_fund")

    def goto_danjuan(self):
        self.driver.find_element(*self._danjuan_menu).click()

    # def click_a_open(self):
    #     WebDriverWait(self.driver, 20).until(expected_conditions.visibility_of_element_located(self._a_open))
    #     self.driver.find_element(*self._danjuan_open).click()

    def danjuan_open(self):
        self.goto_danjuan()
        WebDriverWait(self.driver, 20, 2).until(
            expected_conditions.visibility_of_element_located(self._danjuan_open))
        # self.driver.switch_to.context('WEBVIEW_com.xueqiu.android')
        print(self.driver.page_source)
        self.driver.find_element(*self._danjuan_open).click()
        # self.driver.find_element(*self._danjuan_open).click()
