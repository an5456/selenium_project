from datetime import time
import time
from selenium import webdriver

from test_po.basepage import BasePage
from test_po.wework_page import Wework
from .contact_page import ContactPage


class TestContact:

    def setup(self):
        self.work = Wework()
        self.contact = ContactPage(self.work)

    def teardown(self):
        time.sleep(4)
        self.work.quit()

    # def test_add_member_002(self):
    #     self.contact.add_member("wanglili", "zhangxiao", "s34567", "17779867654")
    #     assert self.contact.get_tips() == "ok"
    #
    def test_add_member_001(self):
        self.contact.add_member("张三", "网速", "s34567", "17779867654")
        assert self.contact.get_tips() == "ok"

    # def test_update_profile(self):
    #     self.contact.search("zhang").update()
    # def test_delete(self):
    #     uuid = str(time())
    #     self.contact\
    #         .add_member("王柳"+uuid,"网速"+uuid, "dt"+uuid, "17768958765")\
    #         .delete_member()
