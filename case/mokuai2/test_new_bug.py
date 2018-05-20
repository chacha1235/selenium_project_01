# coding=utf-8
import unittest
from page.loginpage import LoginPage
from page.editbug import NewBug
from selenium import webdriver
import time
class TestNewBug(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Firefox()
        cls.loginpage=LoginPage(cls.driver)    #继承自base，因此需要传入driver参数
        cls.newbug=NewBug(cls.driver)
    def add_bug(self,bugtitle,bugdetails):
        '''新建bug的流程'''
        #1.登录
        self.loginpage.login("admin","123456")
        #2.点测试，bug,提bug
        self.newbug.click_test_tab()
        self.newbug.click_bug()
        self.newbug.click_add_bug()
        #3.编辑bug
        self.newbug.input_title(bugtitle)
        self.newbug.input_bug_detail(bugdetails)
        self.newbug.add_truk()
        self.newbug.click_save()
        #4.获取保存后显示的实际内容
        result=self.newbug.get_bug_title()
        print("获取结果：%s"%result)
        return result
    def test_add_bug(self):
        nowtime=time.strftime("%Y_%m_%d_%H_%M_%S")
        bugtitle="新建一个bug"+nowtime
        bugdetails="bug详情"
        re=self.add_bug(bugtitle,bugdetails)
        #5.期望结果
        ex=bugtitle
        #6.断言:实际结果和期望结果对比
        self.assertEqual(re,ex,msg="断言失败了就输出")


