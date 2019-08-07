from selenium import webdriver


class Wework:
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
        cookies = {
            "wwrtx.vst": "Ly8_fvFcOApbvwrjYiTh2fQ0OBrr2zzKvQHp1aRUHZCtVy7L_M_ei11GTKdEMyQyEc9Q-Q3-l3CnyZbikBvF2KBY_AIg5G0E7fjjO7UMFEvzjto4nbNOtWZE-EI8FlkRiifSGa7WCeZXceeUHEn2ZZO3IF_y9Yih9V1PY3fKxQQgGzBidZZdMjZ26n2GTfv3YUKjm-QQM5x-5xNUhWDsYWGS6-uGmo7tTNrXkcZCQis9yuO4nnezC6pd4MEQW-hPXSOjDQv7NIjD3BYdUjuOMA",
            "wwrtx.d2st": "a5255438",
            "wwrtx.sid": "5KLjjmW-aMstJ0AquQESE7RC3tEejOln6lERyso5XMebdIOCPWDu7HikID84CX5U",
            "wwrtx.ltype": "1",
            "wxpay.corpid": "1970324954080438",
            "wxpay.vid": "1688851903656484",
        }
        for k, v in cookies.items():
            self.driver.add_cookie({"name": k, "value": v})

        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")

    def quit(self):
        self.driver.quit()
