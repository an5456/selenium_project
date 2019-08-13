import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

from test_page.base.basepage import BasePage
from selenium import webdriver

from test_page.element.page_element import PageElement
from test_page.utils.find_element import FindElement


class ContactPage(BasePage):

    def __init__(self, casedriver):
        self.driver = casedriver.driver
        self.ele = PageElement(self.driver)

    # 添加成员
    def add_contact(self, username, name, account, phone, **kwargs):
        for index in range(20):
            try:
                element = self.ele.get_add_contact_element()
                # print(element.text)
                # print(element.tag_name)
                # print(element.rect)
                # print(element.is_displayed())
                # print(element.is_enabled())

                self.click_by_js(*self.ele.get_add_contact_element())
                if self.ele.get_cancel_element():
                    print("ok")
                    break
            except Exception as e:
                print("except")
                print(e)


        # def click_and_find(x):
        #     self.click_by_js(*self.ele.get_add_contact_element())
        #     return len(self.ele.get_cancel_element()) >= 1
        # WebDriverWait(self.driver, 10).until(click_and_find)
        # 点击添加成员
        # self.click_by_js(*self.ele.get_add_contact_element())
        # 输入姓名
        self.send_key(self.ele.get_username_element(), username)
        # 输入别名
        self.send_key(self.ele.get_name_element(), name)
        # 输入账号
        self.send_key(self.ele.ger_account_element(), account)
        # 性别选择
        self.click_element(self.ele.get_sex_element())
        # 输入手机号
        self.send_key(self.ele.get_phone_element(),phone)
        # 点击取消
        self.click_element(self.ele.get_cancel_element())
        # 点击离开此页
        self.click_by_js(*self.ele.get_leave_element())


if __name__ == '__main__':
    s = webdriver.Chrome()

