import shelve

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class TestWechat:
    """
    本模块主要是用来获取cookies，并生成cookie文件，以便测试代码调用。
    """
    def setup(self):
        # 配置debug接口
        option = Options()
        option.debugger_address = "localhost:9222"
        self.driver = webdriver.Chrome(options=option)
        # 隐式等待
        self.driver.implicitly_wait(5)
        # 登录到企业微信
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")

    def teardown(self):
        self.driver.quit()

    """ 获取cookie，并将cookie保存到文件"""
    def test_getAndSaveCookie(self):
        cookies = self.driver.get_cookies()
        db = shelve.open('db_cookies')
        # shelve模块是以key和value进行存储的，所以下面给了一个key
        db['cookie'] = cookies
        db.close()