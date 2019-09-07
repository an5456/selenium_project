from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


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
            self.driver.find_element(*locator)
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
            self.find(locator)
