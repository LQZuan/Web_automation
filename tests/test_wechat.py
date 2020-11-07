from page.main import Main


class TestWechat:
    def setup(self):
        self.main = Main()

    def teardown(self):
        pass

    def test_wechat(self):
        assert self.main.add_newMember().add_new().addressBook()

