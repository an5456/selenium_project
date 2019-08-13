from test_page.utils.find_element import FindElement


class PageElement:
    def __init__(self, driver):
        self.fd = FindElement(driver)

    # 获取添加成员元素
    def get_add_contact_element(self):
        return self.fd.get_element("add_contact_element")

    # 获取姓名元素
    def get_username_element(self):
        return self.fd.get_element("username_element")

    # 获取别名元素
    def get_name_element(self):
        return self.fd.get_element("name_element")

    # 账号
    def ger_account_element(self):
        return self.fd.get_element("account_element")

    # 性别元素
    def get_sex_element(self):
        return self.fd.get_element("sex_element")

    # 手机号
    def get_phone_element(self):
        return self.fd.get_element("mobile_element")

    # 取消
    def get_cancel_element(self):
        return self.fd.get_element("cancel_element")

    # 离开此页
    def get_leave_element(self):
        return self.fd.get_element("leave_element")
