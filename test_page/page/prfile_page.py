from test_page.base.basepage import BasePage
from test_page.element.page_element import PageElement


class ProfilePage(BasePage):
    def __init__(self, casedriver):
        self.driver = casedriver.driver
        self.ele = PageElement(self.driver)

    # 编辑
    def edit(self, value):
        self.send_key(self.ele.get_search_element(), value)

