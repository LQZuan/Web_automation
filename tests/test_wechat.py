import pytest

from page.main import Main

"""本模块为测试代码"""


class TestWechat:
    def setup(self):
        self.main = Main()

    def teardown(self):
        self.main.quit()

    @pytest.mark.parametrize("username, uid, phonenum", [("hogwarts007", "19799", "15879654998")])
    def test_wechat(self, username, uid, phonenum):
        assert self.main.add_newMember().add_new(username, uid, phonenum).addressBook(username)
