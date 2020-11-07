import shelve

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver

"""本模块主要封装了通用方法"""


class Base:
    _base_url = ""

    def __init__(self, driver: WebDriver = None):
        """如果driver为空，那么创建一个driver，否则复用之前的driver"""
        if driver is None:
            self._driver = webdriver.Chrome()
        else:
            self._driver = driver

        """如果_base_url不为空，那么根据url登录"""
        if self._base_url != "":
            # shelve 模块，打开cookie文件，并付给变量
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
            """刷新页面"""
            self._driver.refresh()
            """最大化session"""
            self._driver.maximize_window()
            """隐式等待"""
            self._driver.implicitly_wait(10)

    """封装两个查找元素的方法"""
    def find(self, by, locator):
        return self._driver.find_element(by, locator)

    def find_list(self, by, locator):
        return self._driver.find_elements(by, locator)
