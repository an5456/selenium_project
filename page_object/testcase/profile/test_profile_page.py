from page_object.page.main.xueqiu_page import XueQiuPage


class TestProfile:
    def setup(self):
        self.xueqiu = XueQiuPage()
        self.profile = self.xueqiu.goto_profile()

    def test_login_by_phone(self):
        # print(self.profile.login_by_phone("17729598765", "2345").get_msg())
        assert "验证码已过期" in self.profile.login_by_phone("17729598765", "2345").get_msg()
        # print(self.profile.login_by_phone("17729598765", "2345").get_msg())

    def test_login_by_wechat(self):
        self.profile.login_by_wechat()
        print(self.profile.get_toast())
        assert "请先安装微信" in self.profile.get_toast()

    def test_login_by_weibo(self):
        self.fail()

    def test_login_by_qq(self):
        self.fail()
