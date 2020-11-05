import shelve
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestWechat:

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        # 隐式等待
        self.driver.implicitly_wait(5)

        # 读取cookies
        db = shelve.open('cookies')
        cookies = db['cookie']
        db.close()

        # 登录到企业微信
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        # 添加cookie
        for cookie in cookies:
            if 'expiry' in cookie.keys():
                cookie.pop('expiry')
            self.driver.add_cookie(cookie)
        # 刷新页面
        self.driver.refresh()

    def teardown(self):
        self.driver.quit()

    def test_wechat(self):
        # # 找到添加成员元素
        # AddMember = self.driver.find_element_by_xpath('//*[@class="ww_indexImg ww_indexImg_AddMember"]')
        # # 添加成员
        # AddMember.click()
        #
        # UserName = self.driver.find_element_by_id('username')
        # UserName.send_keys('1234')
        #
        # memberAdd_acctid = self.driver.find_element_by_id('memberAdd_acctid')
        # memberAdd_acctid.send_keys('1234')
        #
        # memberAdd_phone = self.driver.find_element_by_id('memberAdd_phone')
        # memberAdd_phone.send_keys('15812312312')
        #
        # # 保存
        # save = self.driver.find_element_by_css_selector('.member_colRight > div > div:nth-child(4) > div > form > '
        #                                                 'div:nth-child(1) > '
        #                                                 'a.qui_btn.ww_btn.ww_btn_Blue.js_btn_continue')
        # save.click()

        self.driver.find_element_by_css_selector('#menu_contacts > span').click()

        # 断言
        mlist = self.driver.find_elements(By.XPATH, '//*[@id="member_list"]/tr//span')  # 获取成员列表
        print(mlist)
        memberlist = []
        for m in mlist:
            member = m.text
            memberlist.append(member)
        return memberlist
        print(memberlist)

        test = self.driver.find_elements(By.XPATH, '//*[@id="js_tips"]').text
        print(test)
        # assert "123" in mlist
