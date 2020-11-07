import shelve

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver


class Base:
    _base_url = ""

    def __init__(self, driver: WebDriver = None):
        if driver is None:
            self._driver = webdriver.Chrome()
        else:
            self._driver = driver
        if self._base_url != "":
            # shelve 模块， python 自带的对象持久化存储
            db = shelve.open('../tests/db_cookies')
            cookies = db['cookie']
            db.close()
            # 打开无痕新页面
            self._driver.get(self._base_url)
            # 加入cookie
            for cookie in cookies:
                if 'expiry' in cookie.keys():
                    cookie.pop('expiry')
                self._driver.add_cookie(cookie)
            self._driver.refresh()
            self._driver.maximize_window()
            self._driver.implicitly_wait(10)

    def find(self, by, locator):
        return self._driver.find_element(by, locator)

    def find_list(self, by, locator):
        return self._driver.find_elements(by, locator)
