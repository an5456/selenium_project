from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, dirver: WebDriver):
        self.driver = dirver

    # 单个元素，如果传入的是一个元祖，则会被打散即拆开
    def find_element(self, locator, value=None):
        if value == None:
            return self.driver.find_element(*locator)
        else:
            return self.driver.find_element(locator, value)

    # 多个元素，如果传入的是一个元祖，则会被打散即拆开
    def find_elements(self, locator, value=None):
        if value == None:
            return self.driver.find_elements(*locator)
        else:
            return self.driver.find_elements(locator, value)

    # 使用js点击
    def click_by_js(self, by, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((by, locator)))
        self.driver.execute_script("arguments[0].click();", self.driver.find_element(by, locator))

    # 页面点击
    def click_element(self, locator):
        self.driver.find_element(*locator).click()

    # 页面输入
    def send_key(self, locator, value):
        self.driver.find_element(*locator).send_keys(value)

    # 退出浏览器进程
    def quit(self):
        self.driver.quit()

