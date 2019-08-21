from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from test_page.utils.read_ini import ReadIni
from selenium import webdriver


class FindElement:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def get_element(self, key):
        read_ini = ReadIni()
        data = read_ini.get_value(key)
        by = data.split(">")[0]
        value = data.split(">")[1]
        try:
            if by == 'id':
                return (By.ID, value)
            elif by == 'name':
                return (By.NAME, value)
            elif by == 'css':
                return (By.CSS_SELECTOR, value)
            elif by == 'classname':
                return (By.CLASS_NAME, value)
            elif by == 'tag_name':
                return (By.TAG_NAME, value)
            elif by == 'xpath':
                return (By.XPATH, value)
            else:
                return (By.LINK_TEXT, value)
        except:
            return None


if __name__ == '__main__':
    driver = webdriver.Chrome()
    f = FindElement(driver)
    print(f.get_element('add_contact'))
