from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def click_js(self, by, element):
        self.driver.execute_script("arguments[0].click();", self.driver.find_element(by, element))


