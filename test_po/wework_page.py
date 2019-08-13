from selenium import webdriver


class Wework:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        # self.driver.maximize_window()
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
        cookies = {
            "wwrtx.vst": "hzYgg2X3hEDNOkPvEqTgXRd6bAz1kGCAqGxDOxKE4luzj7UzTmVmNJWS01Dh3tfNgljfPLqJrvEDrFKozZy6PtJguGXnV6QmbRVUfO6-d2CpBJDePFOeyfMGpi2sSQeyHHPYRBCEEDBa3outSFKYj98Q1VQCeNzqwRTcekD8kau78Gt6MeyK1dT0m3LR-y49rnnH_Unt-nQKnapQg_fHkMtjOBnbZIN7Sq4gRAUojAeN6AB_0b4NLPuAejAIGoBeEGFr3dIQ0L6GHN-DamhKXw",
            "wwrtx.d2st": "a8797088",
            "wwrtx.sid": "5KLjjmW-aMstJ0AquQESE9gAivE3x7ofcNRwgXg15XS0WVCsWPEXjFptD-9mL7M3",

            "wwrtx.ltype": "1",
            "wxpay.corpid": "1970324954080438",
            "wxpay.vid": "1688851903656484",
        }
        for k, v in cookies.items():
            self.driver.add_cookie({"name": k, "value": v})

        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")

    def quit(self):
        self.driver.quit()
