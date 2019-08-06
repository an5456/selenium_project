import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestCookies:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
        cookies = {
            "wwrtx.vst": "19NQ2XtpdMSwwUH6pWX7FsQzCBGQ_ykd68GEdTXYEInKF0mAkFlqMjtJJBakRbMlU5-domydDDsxm9kZtTuBysVewHAXBOF02zONgDyGs9Qxt0NWzvpODJ8Jh_9sFWKXv08JKGe0LEeg-U3DjZcYjmtuXpnMC3sSeFzqM6XMzK7A91NwrcQyghDmlIPNJwNA2I_zfxvIWhi-EVAQzFJwMs2cxfNh5tqeE6SuCYp2N58NjF93c9b1xSkH4BVuwTsjNDzxWD2lh01VfQsWEgerBg",
            "wwrtx.d2st": "a3327543",
            "wwrtx.sid": "5KLjjmW-aMstJ0AquQESE7Zesy2gaWElilhy_KxvWmOlq7vkFbDlwaBDVCwcvyzE",
            "wwrtx.ltype": "1",
            "wxpay.corpid": "1970324954080438",
            "wxpay.vid": "1688851903656484",
        }
        for k, v in cookies.items():
            self.driver.add_cookie({"name": k, "value": v})

        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")

    def teardown(self):
        time.sleep(3)
        self.driver.quit()

    def test_01(self):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".ww_operationBar:first-child "
                                                                                ".js_add_member")))

        element = self.driver.find_element(By.CSS_SELECTOR, ".ww_operationBar:first-child .js_add_member")

        for index in range(10):
            element = self.driver.find_element_by_css_selector(".ww_operationBar:first-child .js_add_member")
            print(element.rect)
            print(element.text)
            print(element.tag_name)
            time.sleep(0.5)