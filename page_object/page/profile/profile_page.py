from page_object.page.basepage import BasePage


class ProfilePage(BasePage):
    _phone = BasePage.profile_id('rl_login_phone')
    _wechat = BasePage.profile_id('rl_login_wx')
    _weibo = BasePage.profile_id('rl_login_weibo')
    _qq = BasePage.profile_id('rl_login_qq')
    _phone_input = BasePage.profile_id('register_phone_number')
    _phone_captch = BasePage.profile_id('register_code')
    _phone_next = BasePage.profile_id('button_next')

    def login_by_phone(self, phone, captch):
        self.find(self._phone).click()
        self.find(self._phone_input).send_keys(phone)
        self.find(self._phone_captch).send_keys(captch)
        self.find(self._phone_next).click()
        self.find(self.profile_id('md_content'))
        return self

    def get_msg(self):
        return self.driver.page_source

    def login_by_wechat(self):
        self.find(self._wechat).click()

    def get_toast(self):
        return self.find(self.toast_locator()).text

    def login_by_weibo(self):
        pass

    def login_by_qq(self):
        pass
