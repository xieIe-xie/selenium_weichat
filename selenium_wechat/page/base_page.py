"""
======================
@author:小谢学测试
@time:2021/9/12:21:03
@email:xie7791@qq.com
======================
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver

class BasePage:
    driver = None   #类变量
    base_url=""     #类变量
    def __init__(self,driver:WebDriver = None):
        if driver is None:
            options=Options()
            options.debugger_address='127.0.0.1:9333'
            self.driver=webdriver.Chrome(options=options)
        else:
            self.driver=driver
        if  self.base_url != "":
            self.driver.get(self.base_url)

    def find(self,by ,locator):
        return  self.driver.find_element(by, locator)

    def finds(self,by ,locator):
        return  self.driver.find_elements(by, locator)