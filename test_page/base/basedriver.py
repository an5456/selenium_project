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
            "wwrtx.vst": "0I8KvIgHYceYjH-NA82mhi60VKtGb4iw0OU_w_lTW2AQXGMYxJtn6bftZlU-USVmYEG3RmbGJ13-cIIeVvQbBeJe-uIZQzzTSsno4ktmaSO2N0je29uk13ldMJbkOKI67PPf6_Dq8AYHtuhjpwQzdg6Fnpq9zgacxh82XskI2pzXe2lG-VdH3PB2yJ-HFrnZRacyCvnvKq7jYZElX5z7IInhfUtYAqQPBxn1xZ9H4AjO3_b_PgDuQ-b-KVbIaR83Zs0oaCyGFGOPsg50SuUqcA",
            "wwrtx.d2st": "a2909300",
            "wwrtx.sid": "5KLjjmW-aMstJ0AquQESE54nGlRk2p9e3SrKpCjYcwdviLbpBwiqrk6LBOF7LIUw",

            "wwrtx.ltype": "1",
            "wxpay.corpid": "1970324954080438",
            "wxpay.vid": "1688851903656484",
        }
        for k, v in cookies.items():
            self.driver.add_cookie({'name': k, 'value': v})
        self.driver.get(self.url)


if __name__ == '__main__':
    s = BaseDriver("chrome", url="https://work.weixin.qq.com/wework_admin/frame#apps")
