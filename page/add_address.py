from selenium.webdriver.common.by import By

from page.address_book import AddressBook
from page.base import Base


class AddAddress(Base):
    def add_new(self):
        self.find(By.ID, "username").send_keys("1234567")
        self.find(By.ID, "memberAdd_acctid").send_keys("1234567")
        self.find(By.ID, "memberAdd_phone").send_keys("15712341248")
        self.find_list(By.CSS_SELECTOR, ".js_btn_save")[1].click()
        return AddressBook(self._driver)
