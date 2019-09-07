from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from page_object.page.basepage import BasePage
from page_object.page.stock.search_page import SearchPage
from page_object.page.trade.trade_page import TradePage


class XueQiuPage(BasePage):
    driver = None
    app = "com.xueqiu.android"
    acticity = ".view.WelcomeActivityAlias"

    def first_start(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "hogwarts"
        caps["appPackage"] = self.app
        caps["appActivity"] = self.acticity
        caps['autoGrantPermissions'] = True
        caps['chromedriverExecutable'] = '/workspace/chrmedriver69/'
        # caps['unicodeKeyboard']= True
        # caps['resetKeyboard']= True
        caps['automationName'] = 'uiautomator2'

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)
        XueQiuPage.driver = self.driver
        # 等待元素出现
        # WebDriverWait(self.driver, 40).until(expected_conditions.visibility_of_element_located((By.ID, "image_cancel")))
        # self.driver.find_element_by_id("image_cancel").click()
        # self.driver.find_element_by_id("user_profile_icon")

    # 第一次启动初始化程序，第二次会直接从首页开始
    def __init__(self):
        if XueQiuPage.driver is None:
            print("diyici chushihua")
            self.first_start()
        else:
            print("lanch")
            self.driver.start_activity(self.app, self.acticity)
        self.find((By.ID, "user_profile_icon"))
        # WebDriverWait(self.driver, 60).until(
        #     expected_conditions.visibility_of_element_located((By.ID, "user_profile_icon")))

    def goto_search(self):
        self.driver.find_element_by_id("home_search").click()
        return SearchPage(self.driver)

    # 交易
    def goto_trade(self):
        self.driver.find_element(By.XPATH, "//*[@text='交易']").click()
        return TradePage(self.driver)


if __name__ == '__main__':
    s = XueQiuPage()
