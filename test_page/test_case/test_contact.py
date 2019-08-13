from test_page.base.basedriver import BaseDriver
from test_page.page.contact_page import ContactPage
import pytest
import time


class TestContact:
    def setup(self):
        self.driver = BaseDriver("chrome")
        self.el = ContactPage(self.driver)

    def teardown(self):
        time.sleep(5)
        self.el.quit()

    @pytest.mark.parametrize("username,name,account,phone", [("zhangxiao", "liming", "12434", "17729597869"), ])
    def test_add_contact(self, username, name, account, phone):
        #     self.el.click_contact()
        self.el.add_contact(username=username, name=name, account=account, phone=phone)
