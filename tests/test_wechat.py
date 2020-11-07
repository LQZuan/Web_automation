from page.main import Main

"""本模块为测试代码"""


class TestWechat:
    def setup(self):
        self.main = Main()

    def teardown(self):
        self.main.quit()

    def test_wechat(self):
        assert self.main.add_newMember().add_new().addressBook()
