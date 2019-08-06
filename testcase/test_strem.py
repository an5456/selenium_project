# import pytest
#
#
# class TestCalc:
#
#     def test_add(self, a, b, c):
#         assert a + b == c
#
#
# c = TestCalc()
# c.test_add(1, 2, 3)
from selenium import webdriver
def test_2():
    browser = webdriver.Firefox()
    re = browser.get("http://www.youdao.com")
    browser.quit()
