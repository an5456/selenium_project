# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
import time

import pytest
from appium import webdriver
from selenium.webdriver.common.by import By
from hamcrest import *
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestXueqiu:

    # def setup_class(self):
    #     self.caps = {}
    #     self.caps["platformName"] = "android"
    #     self.caps["deviceName"] = "hogwarts"
    #     self.caps["appPackage"] = "com.xueqiu.android"
    #     self.caps["appActivity"] = ".view.WelcomeActivityAlias"
    #     self.caps["autoGrantPermissions"] = True
    #     self.driver = webdriver.Remote("http://localhost:4723/wd/hub", self.caps)
    #     self.driver.implicitly_wait(15)

    # def setup(self):
    #     pass
    #
    # def teardown(self):
    #     self.driver.find_element_by_id("action_close").click()
    #     time.sleep(3)
    def wait(self, by, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((by, locator)))
    @pytest.fixture()
    def test_reach(self):
        yield
        self.driver.find_element_by_id("action_close").click()

    def teardown_class(self):
        time.sleep(10)
        self.driver.quit()

    def test_wrong_phone(self):
        # el1 = self.driver.find_element_by_id("com.xueqiu.android:id/tv_open")
        # el1.click()
        # el2 = self.driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button")
        # el2.click()
        # el3 = self.driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button")
        # el3.click()
        # //*[contains(@resource-id,'id/user_profile_icon' ) and contains(@class,'mageView')]
        self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.ImageView").click()
        self.driver.find_element(By.ID, "iv_login_phone").click()
        self.driver.find_element(By.ID, "tv_login_with_account").click()
        self.driver.find_element(By.ID, "login_account").send_keys('12345678912')
        print(self.driver.find_element(By.ID, "login_password").send_keys('12345678912'))
        print(self.driver.find_element(By.ID, "button_next").get_attribute("class"))
        print(self.driver.page_source)

    def test_search(self):
        self.driver.find_element(By.ID, "tv_search").click()
        self.driver.find_element(By.ID, "search_input_text").send_keys("alibaba")
        ele = self.driver.find_element(By.ID, "com.xueqiu.android:id/listview")
        ele.find_elements(By.CLASS_NAME, "android.widget.RelativeLayout")[2].click()

    def test_click(self):
        self.driver.tap()

    def test_sendkeys(self):
        self.driver.keyevent()

    def test_get_attribute(self):
        self.driver.find_element_by_id("")

    def test_swipe(self):
        self.driver.swipe(500, 900, 100, 200, 1000)
        # self.driver.find_element_by_accessibility_id("Views").click()
        for i in range(5):
            self.driver.swipe(500, 900, 100, 200, 1000)

    def test_swipe_percent(self):
        self.wait(By.ID, "com.xueqiu.android:id/user_profile_icon")
        size = self.driver.get_window_size()
        print(size)
        width = size["width"]
        height = size["height"]
        self.driver.swipe(width * 0.8, height * 0.8, width * 0.2, height * 0.2, 1000)
        # self.driver.find_element_by_accessibility_id("Views").click()
        for i in range(5):
            self.driver.swipe(width * 0.8, height * 0.8, width * 0.2, height * 0.2, 1000)

    def test_uiautomator(self):
        self.wait(By.ID, "com.xueqiu.android:id/user_profile_icon")
        self.driver.find_element_by_android_uiautomator('new UiScrollable('
                                                        'new UiSelector().scrollable(true).instance(0))'
                                                        '.scrollIntoView('
                                                        'new UiSelector().text("龙哥AI炒股  58评  15赞").instance(0));').click()
        # self.driver.find_element_by_android_uiautomator('new UiScrollable('
        #                                                 'new UiSelector().scrollable(true).instance(0))'
        #                                                 '.scrollIntoView('
        #                                                 'new UiSelector().text("Tabs").instance(0));').click()

    @pytest.mark.parametrize("keyword,stock_type,expect_price", [
        ("alibaba", "BABA", 170),
        ("xiaomi", "01810", 8.8)
    ])
    def test_search1(self, base_driver,test_reach, keyword, stock_type, expect_price):
        self.driver = base_driver
        self.driver.implicitly_wait(15)
        self.driver.find_element_by_id("home_search").click()
        self.driver.find_element_by_id("search_input_text").send_keys(keyword)
        self.driver.find_element_by_id("name").click()
        price = self.driver.find_element_by_xpath("//*[contains(@resource-id,'stockCode') and "
                                                  "@text='" + stock_type + "']/../../..//*[ "
                                                                           "contains(@resource-id, 'current_price')]").text
        print(price)
        assert float(price) > expect_price
        assert_that(float(price), close_to(expect_price, expect_price*0.1))
