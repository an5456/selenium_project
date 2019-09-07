from page_object.page.basepage import BasePage


class SearchPage(BasePage):
    # 输入关键字
    def search(self, keyword):
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys(keyword)
        return self

    # 选择点击第几个
    def select(self, index):
        self.driver.find_elements_by_id("name")[index].click()
        return self

    # 获取股票价格
    def get_price(self, stock_type):
        price = float(self.driver.find_element_by_xpath("//*[contains(@resource-id, 'stockCode') and "
                                                        "@text='" + stock_type + "']/../../..//*[contains("
                                                                                 "@resource-id, "                                                                         "'current_price')]").text)
        return price


