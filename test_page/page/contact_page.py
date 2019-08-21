import time

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

from test_page.base.basepage import BasePage
from selenium import webdriver

from test_page.element.page_element import PageElement
from test_page.utils.find_element import FindElement


@allure.feature("测试添加成员页面")
class ContactPage(BasePage):

    def __init__(self, casedriver):
        self.driver = casedriver.driver
        self.ele = PageElement(self.driver)

    # 添加成员
    @allure.story("添加成员")
    def add_contact(self, username, name, account, phone, telephone, email, address, **kwargs):
        while True:
            try:
                self.click_by_js(*self.ele.get_add_contact_element())
                if len(self.driver.find_elements(By.XPATH, "//*[text()='取消']")):
                    print("ok")
                    break
            except Exception as e:
                print("except")
                print(e)

        # 输入姓名
        with allure.step("输入姓名"):
            self.send_key(self.ele.get_username_element(), username)

        # 输入别名
        with allure.step("输入别名"):
            self.send_key(self.ele.get_name_element(), name)

        # 输入账号
        with allure.step("输入账号"):
            self.send_key(self.ele.ger_account_element(), account)

        # 性别选择
        with allure.step("性别选择"):
            self.click_element(self.ele.get_sex_element())

        # 输入手机号
        with allure.step("输入手机号"):
            self.send_key(self.ele.get_phone_element(), phone)

        # 座机
        with allure.step("输入座机"):
            self.send_key(self.ele.get_telephone_element(), telephone)

        # 邮箱
        with allure.step("输入邮箱"):
            self.send_key(self.ele.get_email_element(), email)

        # 地址
        with allure.step("输入地址"):
            self.send_key(self.ele.get_address_element(), address)

        # 保存
        with allure.step("点击保存"):
            self.click_element(self.ele.get_save_element())

        assert "zhangxiao" > self.driver.page_source

        # 点击取消
        # self.click_element(self.ele.get_cancel_element())

        # 点击离开此页
        # self.click_by_js(*self.ele.get_leave_element())


if __name__ == '__main__':
    s = webdriver.Chrome()
