from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from test_po.basepage import BasePage


class ProfilePage(BasePage):

    def update(self):
        WebDriverWait(self.driver, 10, 1, ignored_exceptions="TimeoutException").until(
            expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".member_colRight_operationBar>a:first-child")))
        self.click_js(By.CSS_SELECTOR, ".member_colRight_operationBar>a:first-child")
        # self.driver.find_element(By.CSS_SELECTOR, ".member_colRight_operationBar>a:first-child")

    def disable(self):
        pass

    def delete(self):
        pass

    def invite(self):

        pass

