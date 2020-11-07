from selenium.webdriver.common.by import By

from page.add_address import AddAddress
from page.base import Base


class Main(Base):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame"

    def add_newMember(self):
        self.find(By.CSS_SELECTOR, ".index_service_cnt_item_title").click()
        return AddAddress(self._driver)
