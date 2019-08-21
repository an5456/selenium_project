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

    # 座机
    def get_telephone_element(self):
        return self.fd.get_element("telephone_element")

    # 邮箱
    def get_email_element(self):
        return self.fd.get_element("email_element")

    # 地址
    def get_address_element(self):
        return self.fd.get_element("address_element")

    # 保存
    def get_save_element(self):
        return self.fd.get_element("save_element")

    # 添加成员tr标签
    def get_tr_element(self):
        return self.fd.get_element("tr_element")

    # 搜索
    def get_search_element(self):
        return self.fd.get_element("search_element")
