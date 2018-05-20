# coding=utf-8
from page.loginpage import LoginPage
from selenium import webdriver
import unittest
import ddt
#参数和代码进行分离
# testdata=[
#     {"username":"admin","password":"123456","result":"admin"},
#     {"username":"admin","password":"111111","result":""},
#     {"username":"admin","password":"123456","result":"admin"}
# ]

@ddt.ddt
class LoginCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("开始测试")

    @ddt.data(*testdata)
    def test_login_01(self,canshu):
        print(canshu)
        print("账户：%s" %canshu["username"])
        print("密码：%s" %canshu["password"])
        print("结果：%s" %canshu["result"])

    def tearDown(self):
        pass
    @classmethod
    def tearDownClass(cls):
        pass
if __name__ == '__main__':
    unittest.main()
