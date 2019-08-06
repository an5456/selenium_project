import time

import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import logging

logging.basicConfig(level=logging.INFO)
"""
最新发布的帖子浏览
社区访问霍格沃兹测试学院，断言未登录是被拒绝的
错误用户名和密码登陆
搜索”测试媛“，找到成立的那个帖子，进去后断言标题与搜索出来的标题是对应的
"""


@allure.feature("课后作业")
class TestHomework:
    # 初始化driver
    def setup_method(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.debugger_address = "127.0.0.1:9999"
        self.driver = webdriver.Chrome(options=chrome_options)

        # self.driver = webdriver.Chrome()
        with allure.step("打开testerhome"):
            self.driver.get("https://testerhome.com")
            # self.driver.maximize_window()
            self.driver.implicitly_wait(10)

    def teardown_method(self):
        self.driver.quit()

    @allure.story("最新发布帖子浏览")
    def test_new_info(self):
        """
        最新发布的帖子浏览
        """
        with allure.step("点击社区"):
            self.driver.find_element(By.CSS_SELECTOR, "#main-nav-menu a[href*='topics']").click()
            # self.driver.find_element(By.XPATH, "//a[contains(text(),'社区'')]").click()

        with allure.step("点击最新发布"):
            self.driver.find_element(By.CSS_SELECTOR, ".nav-pills li:last-child").click()
        time.sleep(3)

        text_element = self.driver.find_element(By.CSS_SELECTOR, "a[href*='20094']")
        print(text_element.get_attribute("title"))
        # page_title = self.driver.title
        # assert page_title in ".最新创建 · 社区 · TesterHome"
        # # 截图
        # allure.attach(self.driver.get_screenshot_as_png(), name="new_info", attachment_type=AttachmentType.PNG)
        # print(self.driver.title)
        # # p: nth - child(2)

    @allure.story("社区访问霍格沃兹测试学院，断言未登录是被拒绝的")
    def test_if_login(self):
        """
        社区访问霍格沃兹测试学院，断言未登录是被拒绝的
        """
        with allure.step("点击社团"):
            self.driver.find_element(By.CSS_SELECTOR, "#main-nav-menu li:nth-child(4)").click()

        with allure.step("点击霍格沃兹测试学院"):
            self.driver.find_element(By.CSS_SELECTOR, "a[data-name='霍格沃兹测试学院']").click()
        with allure.step("a[title='第十期_Selenium 第二周_20190801']"):
            self.driver.find_element(By.CSS_SELECTOR, "a[title='第十期_Selenium 第二周_20190801']").click()

        with allure.step("断言访问被拒绝"):
            error_info = self.driver.find_element(By.CSS_SELECTOR, '.container .alert').text
            assert error_info in '访问被拒绝，你可能没有权限或未登录。'

    @allure.story("错误的用户名密码登录")
    @pytest.mark.parametrize("username,password", [
        ("an5456", 23456),
    ])
    def test_error_username_password(self, username, password):
        """
        错误的用户名密码登录
        """

        with allure.step("点击登录按钮"):
            self.driver.find_element(By.CSS_SELECTOR, "a[href*='sign_in']").click()

        with allure.step("输入用户名、密码"):
            username_element = self.driver.find_element(By.CSS_SELECTOR, "#user_login")
            username_element.clear()
            username_element.send_keys(username)

            password_element = self.driver.find_element(By.CSS_SELECTOR, "#user_password")
            password_element.clear()
            password_element.send_keys(password)

            button_element = self.driver.find_element(By.CSS_SELECTOR, "input[value*='登录']")
            # button_element.click()

        with allure.step("断言用户名密码错误"):
            error_info = self.driver.find_element(By.CSS_SELECTOR, ".alert-warning").text
            print(error_info)
            assert error_info in '帐号或密码错误。'

    @allure.story("搜索”测试媛“，找到成立的那个帖子")
    def test_search(self):
        """
        搜索”测试媛“，找到成立的那个帖子，进去后断言标题与搜索出来的标题是对应的
        """
        print(self.driver.title)
        with allure.step("点击搜索'测试媛'"):
            # js = "var q=document.documentElement.scrollTop=10000"
            # self.driver.execute_script(js)
            self.driver.execute_script("window.scrollTo(0,300);")
            serchh_element = self.driver.find_element(By.CSS_SELECTOR, "input[name*='q']")
            serchh_element.send_keys("测试媛")
            serchh_element.send_keys(Keys.ENTER)
            print(self.driver.title)
            time.sleep(5)
            self.driver.execute_script("window.scrollTo(0,500);")

            time.sleep(5)
        # with allure.step("断言标题与搜索出来的标题是对应的"):
        #     title_element = self.driver.find_element(By.CSS_SELECTOR, ".title a[href*='4577']")
        #     title = title_element.text
        #     title_element.click()
        #
        #     title_1 = self.driver.title
        #     assert title == title_1

    def test_form_login(self):
        self.driver.get("https://testerhome.com/account/sign_in")
        element = self.driver.find_element(By.CSS_SELECTOR, "input[value*='登录']")
        logging.info(element.is_displayed())  # 元素是否可见
        logging.info(element.id)  # 元素ID
        logging.info(element.tag_name)  # 元素的标签
        logging.info(element.text)  # 元素的文本
        logging.info(element.location)  # 元素的位置
        logging.info(element.size)  # 元素的高和宽
        logging.info(element.get_attribute("placeholder"))  # 获取元素的属性值
        logging.info(self.driver.page_source)  # 打印页面元素
        logging.info(self.driver.title)  # 当前页面的title
