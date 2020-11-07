from selenium.webdriver.common.by import By

from page.base import Base

"""本模块为通讯录页"""


class AddressBook(Base):
    """
    1.获取通讯录列表，并将内容放入一个列表中
    2.判断目标值并放回bool
    """
    def addressBook(self):
        arr_ele = self.find_list(By.CSS_SELECTOR, "#member_list > tr > td:nth-child(2) > span")
        address_list = []
        for ele in arr_ele:
            address_list.append(ele.text)
        print(address_list)

        if "hello" in address_list:
            return True
        else:
            return False
