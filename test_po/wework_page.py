from selenium import webdriver


class Wework:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        # self.driver.maximize_window()
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
        cookies = {
            "wwrtx.vst": "iYU0NMdemQDne6O7W6MCyY2xIJ3TPeJ9q1HH64OBUFiW2tEW2RJxS9ZxMfqUzVkU_l8QVIbHM89NNuKu8pc7K10I0eYkR7PcAXmId_m8YdleHXMqkeous3mAfly8rE7WncY9LINHEMHdjPA4PDjDhO5WMEoqyIXA0zDsXUQB0hX_62Zg7v5l7SYGmlnuRuBaJMzbkadlu0Pp4PNtMBZTOAWpWHq6QN8yT01I742E0_8VxrJM-MW9u_UOWdE6Ky5krPIZsCgr0-30TwLSLfeJEg",
            "wwrtx.d2st": "a7436873",
            "wwrtx.sid": "5KLjjmW-aMstJ0AquQESE-rB5qRvaiQ947Eq06SECTPm-T-BRQye8mnN4VArHPKf",
            "wwrtx.ltype": "1",
            "wxpay.corpid": "1970324954080438",
            "wxpay.vid": "1688851903656484",
        }
        for k, v in cookies.items():
            self.driver.add_cookie({"name": k, "value": v})

        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")

    def quit(self):
        self.driver.quit()
