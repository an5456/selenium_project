from logs.log_one.use_log import GetLog
from page_object.page.main.xueqiu_page import XueQiuPage


class TestTrade:
    def setup(self):
        self.xueqiu = XueQiuPage()
        self.trade = self.xueqiu.goto_trade()

    # a股
    # def test_a_open(self):
    #     self.trade.goto_danjuan()

    def test_danjuan_open(self):
        self.trade.danjuan_open()

