from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
import logging


class BasePage:
    black_list = [
        (By.ID, "image_cancel"),
    ]
    max = 0

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def find(self, locator) -> WebElement:
        # todo: 处理弹框
        try:
            logging.info('定位元素：' + str(locator))
            return self.driver.find_element(*locator)
        except Exception as e:
            if self.max > 4:
                raise e
            self.max += 1
            for blak in self.black_list:
                elements = self.driver.find_elements(*blak)
                if len(elements) >= 1:
                    # WebDriverWait(self.driver, 40).until(
                    #     expected_conditions.visibility_of_element_located(*blak))
                    elements[0].click()
            return self.find(locator)

    # 返回元素的大小
    def size(self, locator):
        return len(self.driver.find_elements(*locator))

    @classmethod
    def profile_id(cls, value):
        return (By.ID, value)

    # 通过xpath定位
    @classmethod
    def text(cls, value):

        return (By.XPATH, "//*[@text='%s']" % value)

    # 获取弹框提示信息
    @classmethod
    def toast_locator(cls):

        return (By.XPATH, "//*[@class='android.widget.Toast']")
