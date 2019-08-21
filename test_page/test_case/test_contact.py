from test_page.base.basedriver import BaseDriver
from test_page.page.contact_page import ContactPage
import pytest
import time

from test_page.page.prfile_page import ProfilePage


class TestContact:
    def setup(self):
        self.driver = BaseDriver("chrome")
        self.el = ContactPage(self.driver)
        self.pro = ProfilePage(self.driver)

    def teardown(self):
        time.sleep(5)
        self.el.quit()

    @pytest.mark.parametrize("username, name, account, phone, telephone, email, address",
                             [("zhangxiao", "liming", "12434", "17729597869", "0917-5456837", "123456@qq.com",
                               "前进路18号"), ])
    def test_add_contact(self, username, name, account, phone, telephone, email, address):

        self.el.add_contact(username, name, account, phone, telephone, email, address)

    def test_search_page(self):
       self.pro.edit("zhangxiao")
