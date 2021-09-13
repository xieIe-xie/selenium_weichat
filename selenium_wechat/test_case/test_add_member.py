"""
======================
@author:小谢学测试
@time:2021/9/11:20:39
@email:xie7791@qq.com
======================
"""
from time import sleep
from selenium_wechat.page.main import Main
class TestAddMember:
    def setup(self):
        self.main = Main()
    def test_add_menber(self):
        add_member = self.main.goto_add_member()
        add_member.add_member()
        sleep(2)
        assert "def789" in add_member.get_member()