import pytest
from selenium import webdriver
import time
# import os ,sys
# base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.append(base_dir)
import logging

from selenium.webdriver import ActionChains

logging.basicConfig(level=logging.INFO)
from selenium.webdriver.common.by import By


class TestCase:
    def setup(self):
        self.dirver = webdriver.Chrome()
        self.dirver.implicitly_wait(3)

    def teardown(self):
        self.dirver.quit()

    # @pytest.mark.repeat(2)
    def test_1(self):
        self.dirver.get("https://testerhome.com/")

        self.dirver.find_element(By.CSS_SELECTOR, '.infos a[href*="19682"]').click()

        self.dirver.find_element(By.XPATH, '//p[contains(text(),"问卷")]/a').click()
        logging.info(self.dirver.title)
        win = self.dirver.window_handles
        # print(win)
        # win1 = self.dirver.current_window_handle
        self.dirver.switch_to.window(win[-1])
        logging.info(self.dirver.title)

        for w in self.dirver.window_handles:
            logging.info(w)

        for w in self.dirver.window_handles:
            logging.info(w)
        # 拖住滚动
        # time.sleep(3)
        # ActionChains(self.dirver).click_and_hold(self.dirver.find_element(By.CSS_SELECTOR, '.reply-buttons .total')) \
        #     .move_by_offset(0,200).release().perform()
        # time.sleep(3)
        time.sleep(3)
        # 利用js进行滚动
        self.dirver.execute_script('window.scrollTo(0,800)')
        time.sleep(3)

        # 切换到ifame中
        # self.dirver.switch_to.frame(self.dirver.find_element(By.TAG_NAME, "iframe"))
        # self.dirver.find_element(By.XPATH, "//span[contains(text(),'[张文] 网易云音乐质量可视化实践')]").click()
        # time.sleep(2)
        # logging.info(self.dirver.page_source)page_source
