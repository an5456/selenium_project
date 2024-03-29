from appium import webdriver
from selenium.webdriver.common.by import By
import logging

from page_object.logs.getlog import GetLog
from page_object.page.basepage import BasePage
from page_object.page.profile.profile_page import ProfilePage
from page_object.page.stock.search_page import SearchPage
from page_object.page.trade.trade_page import TradePage


class XueQiuPage(BasePage):
    driver = None
    _app = "com.xueqiu.android"
    _acticity = ".view.WelcomeActivityAlias"
    _profile_icon = (By.ID, "user_profile_icon")
    logger = GetLog().set_log_config_1()

    def first_start(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "hogwarts"
        caps["appPackage"] = self._app
        caps["appActivity"] = self._acticity
        caps['autoGrantPermissions'] = True
        caps['chromedriverExecutable'] = '/workspace/chrmedriver69/'
        caps['noReset'] = True
        # caps['unicodeKeyboard']= True
        # caps['resetKeyboard']= True
        caps['automationName'] = 'uiautomator2'
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        logging.info("")
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
            logging.info("第一启动")
            self.first_start()
        else:
            print("lanch")
            self.driver.start_activity(self._app, self._acticity)
        self.find(self._profile_icon)
        # WebDriverWait(self.driver, 60).until(
        #     expected_conditions.visibility_of_element_located((By.ID, "user_profile_icon")))

    def goto_search(self):
        self.driver.find_element_by_id("home_search").click()
        return SearchPage(self.driver)

    # 交易
    def goto_trade(self):
        self.driver.find_element(By.XPATH, "//*[@text='交易']").click()
        return TradePage(self.driver)

    def goto_profile(self):
        self.find(self._profile_icon).click()
        return ProfilePage(self.driver)



