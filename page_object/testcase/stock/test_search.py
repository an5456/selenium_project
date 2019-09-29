import allure
import pytest
from hamcrest import assert_that, close_to

from page_object.page.main.xueqiu_page import XueQiuPage


@allure.feature("首页测试")
class TestSearch:
    def setup(self):
        self.xueqiu = XueQiuPage()

    @pytest.mark.parametrize("index, te, price", [
        (0, "BABA", 170),
        (1, "01060", 1.3)
    ])
    @allure.story("搜索股票")
    def test_search_us(self, index, te, price):
        price = self.xueqiu.goto_search().search("ali").select(index).get_price(te)
        # assert self.xueqiu.goto_search().search("alibaba").select(0).get_price("BABA") > 170
        assert_that(float(price), close_to(price, price * 0.1))
