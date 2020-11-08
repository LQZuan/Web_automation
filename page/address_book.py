from selenium.webdriver.common.by import By

from page.base import Base

"""本模块为通讯录页"""


class AddressBook(Base):
    """
    1.获取通讯录列表，并将内容放入一个列表中
    2.判断目标值并放回bool
    """
    def addressBook(self, username):
        # arr_ele = self.find_list(By.CSS_SELECTOR, "#member_list > tr > td:nth-child(2) > span")
        # address_list = []
        # for ele in arr_ele:
        #     address_list.append(ele.text)
        # print(address_list)
        # 列表推导式：
        # address_list = [ele.text for ele in arr_ele]
        # print(address_list)

        """优化后的代码："""
        """定义一个列表来拼凑每个页面的通讯录列表"""
        all_address = []
        # while True:
        #     arr_ele = self.find_list(By.CSS_SELECTOR, "#member_list > tr > td:nth-child(2) > span")
        #     address_list = [ele.text for ele in arr_ele]
        #     print(address_list)
        #     """拼凑列表"""
        #     all_address.extend(address_list)
        #
        #     pageNav: str = self.find_list(By.CSS_SELECTOR, ".ww_pageNav_info_text")[0].text
        #     curr_page, total_page = pageNav.split("/", 1)
        #
        #     """判断翻页是否是最后一页，如果是，跳出循环，否则点击下一页"""
        #     if curr_page == total_page:
        #         break
        #     else:
        #         self.find_list(By.CSS_SELECTOR, ".ww_commonImg_PageNavArrowRightNormal")[0].click()
        #
        # if username in all_address:
        #     return True
        # else:
        #     return False
        """继续优化"""
        # while True:
        #     arr_ele = self.find_list(By.CSS_SELECTOR, "#member_list > tr > td:nth-child(2) > span")
        #     address_list = [ele.text for ele in arr_ele]
        #     print(address_list)
        #
        #     """如果当前页面能够查找到插入元素，直接返回"""
        #     if username in all_address:
        #         return True
        #
        #     """拼凑列表"""
        #     all_address.extend(address_list)
        #
        #     pageNav: str = self.find_list(By.CSS_SELECTOR, ".ww_pageNav_info_text")[0].text
        #     curr_page, total_page = pageNav.split("/", 1)
        #
        #     """判断翻页是否是最后一页，如果是，跳出循环，否则点击下一页"""
        #     if curr_page == total_page:
        #         break
        #     else:
        #         self.find_list(By.CSS_SELECTOR, ".ww_commonImg_PageNavArrowRightNormal")[0].click()
        #
        # if username in all_address:
        #     return True
        # else:
        #     return False

        """继续优化，兼容单页和多页"""
        while self.isElementExist(".ww_pageNav_info_text"):
            arr_ele = self.find_list(By.CSS_SELECTOR, "#member_list > tr > td:nth-child(2) > span")
            address_list = [ele.text for ele in arr_ele]
            print(address_list)

            """如果当前页面能够查找到插入元素，直接返回"""
            if username in address_list:
                return True

            """拼凑列表"""
            all_address.extend(address_list)

            pageNav: str = self.find_list(By.CSS_SELECTOR, ".ww_pageNav_info_text")[0].text
            curr_page, total_page = pageNav.split("/", 1)

            """判断翻页是否是最后一页，如果是，跳出循环，否则点击下一页"""
            if curr_page == total_page:
                break
            else:
                self.find_list(By.CSS_SELECTOR, ".ww_commonImg_PageNavArrowRightNormal")[0].click()
            """如果通讯录只有一页："""
        else:
            arr_ele = self.find_list(By.CSS_SELECTOR, "#member_list > tr > td:nth-child(2) > span")
            all_address = [ele.text for ele in arr_ele]

        """判断目标是否在列表中"""
        if username in all_address:
            return True
        else:
            return False
