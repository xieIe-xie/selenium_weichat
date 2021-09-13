"""
======================
@author:小谢学测试
@time:2021/9/11:20:25
@email:xie7791@qq.com
======================
"""
from time import sleep
from selenium.webdriver.common.by import By
from selenium_wechat.page.base_page import BasePage
class AddMember(BasePage):
    def add_member(self):
        #成员信息
        sleep(2)
        self.find(By.ID,'username').send_keys('def789')
        self.find(By.ID,'memberAdd_acctid').send_keys('def789')
        self.find(By.ID,'memberAdd_phone').send_keys('12345678911')
        self.find(By.CSS_SELECTOR,'.qui_btn.ww_btn.js_btn_save').click()
        # self.driver.find_element_by_id('username').send_keys('def789')
        # self.driver.find_element(By.ID,'memberAdd_acctid').send_keys('def789')
        # self.driver.find_element(By.ID,'memberAdd_phone').send_keys('13565894788')
        # self.driver.find_element(By.CSS_SELECTOR,('.qui_btn.ww_btn.js_btn_save')).click()
        sleep(5)
        return True
    def get_member(self):
        elements = self.finds(By.CSS_SELECTOR,'.member_colRight_memberTable_td:nth-child(2)')
        list = []
        for element in elements:
            list.append(element.get_attribute("title"))
        return list
