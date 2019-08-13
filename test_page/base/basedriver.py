from selenium import webdriver


class BaseDriver:

    def __init__(self, browser, url=None):
        if browser == 'chrome':
            self.driver = webdriver.Chrome()
        elif browser == 'firefox':
            self.driver = webdriver.Firefox()
        else:
            self.driver = webdriver.Edge()
        self.driver.implicitly_wait(5)

        if url == None:
            self.url = "https://work.weixin.qq.com/wework_admin/frame#contacts"
        else:
            self.url = url
        self.driver.get(self.url)
        cookies = {
            "wwrtx.vst": "hzYgg2X3hEDNOkPvEqTgXRd6bAz1kGCAqGxDOxKE4luzj7UzTmVmNJWS01Dh3tfNgljfPLqJrvEDrFKozZy6PtJguGXnV6QmbRVUfO6-d2CpBJDePFOeyfMGpi2sSQeyHHPYRBCEEDBa3outSFKYj98Q1VQCeNzqwRTcekD8kau78Gt6MeyK1dT0m3LR-y49rnnH_Unt-nQKnapQg_fHkMtjOBnbZIN7Sq4gRAUojAeN6AB_0b4NLPuAejAIGoBeEGFr3dIQ0L6GHN-DamhKXw",
            "wwrtx.d2st": "a8797088",
            "wwrtx.sid": "5KLjjmW-aMstJ0AquQESE9gAivE3x7ofcNRwgXg15XS0WVCsWPEXjFptD-9mL7M3",

            "wwrtx.ltype": "1",
            "wxpay.corpid": "1970324954080438",
            "wxpay.vid": "1688851903656484",
        }
        for k, v in cookies.items():
            self.driver.add_cookie({'name': k, 'value': v})
        self.driver.get(self.url)


if __name__ == '__main__':
    s = BaseDriver("chrome",url="https://work.weixin.qq.com/wework_admin/frame#apps")
