"""
======================
@author:小谢学测试
@time:2021/9/11:20:20
@email:xie7791@qq.com
======================
"""
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium_wechat.page.add_member import AddMember
from selenium_wechat.page.base_page import BasePage

class Main(BasePage):
    base_url = 'https://work.weixin.qq.com/wework_admin/frame'
    def goto_add_member(self):
        #点击添加成员
        self.find(By.ID,'menu_contacts').click()
        sleep(2)
        self.find(By.LINK_TEXT,("添加成员")).click()

        return AddMember(self.driver)