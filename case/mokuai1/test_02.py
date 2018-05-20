# coding=utf-8
from selenium import webdriver
import time
import unittest
class TestErich(unittest.TestCase):
    u'''测试网站登录'''
    @classmethod                      #装饰器别忘了
    def setUpClass(cls):
        cls.driver=webdriver.Firefox()
    def setUp(self):
        self.driver.get("https://trade.erichfund.com/center/login")
        time.sleep(3)
    def test_01(self):
        u'''用户名密码正确'''
        self.driver.find_element_by_id("username").send_keys("13661403216")
        self.driver.find_element_by_id("password").send_keys("920423pmdf")
        self.driver.find_element_by_link_text("登录").click()
        time.sleep(3)
        a=self.driver.find_element_by_id("userName_head").text
        print(a)
        self.assertTrue(a=="高晓欢")
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()