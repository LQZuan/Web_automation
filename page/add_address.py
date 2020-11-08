from selenium.webdriver.common.by import By

from page.address_book import AddressBook
from page.base import Base

"""本模块为添加通讯录页"""


class AddAddress(Base):
    """
    1.填表
    2.点击保存
    3.页面跳转
    """
    def add_new(self, username, uid, phonenum):
        # 填表
        self.find(By.ID, "username").send_keys(username)
        self.find(By.ID, "memberAdd_acctid").send_keys(uid)
        self.find(By.ID, "memberAdd_phone").send_keys(phonenum)
        # 保存
        self.find_list(By.CSS_SELECTOR, ".js_btn_save")[1].click()
        # 返回通讯录页面
        return AddressBook(self._driver)
