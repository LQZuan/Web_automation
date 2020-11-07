from selenium.webdriver.common.by import By

from page.add_address import AddAddress
from page.base import Base

"""本模块为企业微信登录后首页"""


class Main(Base):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame"

    """点击添加成员"""
    def add_newMember(self):
        self.find(By.CSS_SELECTOR, ".index_service_cnt_item_title").click()
        return AddAddress(self._driver)
