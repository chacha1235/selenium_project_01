# coding=utf-8
from page.loginpage import LoginPage
from selenium import webdriver
import unittest
from common.readexcel import ExcelUtil
#参数和代码进行分离
import ddt
# case1={"username":"admin","password":"123456","result":"admin"}
# case2={"username":"admin","password":"111111","result":""}
# case3={"username":"admin","password":"123456","result":"admin"}
# testdata=[
#     {"username":"admin","password":"123456","result":"admin"},
#     {"username":"admin","password":"111111","result":""},
#     {"username":"admin","password":"123456","result":"admin"}
# ]
filepath = "testddt.xlsx"
data = ExcelUtil(filepath)
testdata=data.dict_data()       #读取数据为list
print(testdata)
@ddt.ddt
class LoginCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Firefox()
        cls.loginpage=LoginPage(cls.driver)
    def login(self,username,password):
        #登录
        self.loginpage.login(username,password)
        #判断是否有弹框
        self.loginpage.is_alert_exist()
        #获取登录结果
        result=self.loginpage.get_login_result()
        return result
    @ddt.data(*testdata)
    def test_01(self,canshu):
        re=self.login(canshu["username"],canshu["password"])
        #断言
        self.assertEqual(canshu["result"],re)
    # def test_login_fail(self,canshu):
    #     re=self.login(canshu["username"],canshu["password"])
    #     #断言
    #     self.assertEqual(canshu["result"],"")
    # def test_login_03(self):
    #     re=self.login(case3["username"],case3["password"])
    #     self.assertEqual(case3["result"],"admin2")
    # def test_login_again(self,canshu):
    #     re=self.login(canshu["username"],canshu["password"])
    #     #断言
    #     self.assertEqual(canshu["result"],"admin")
    def tearDown(self):
        self.driver.delete_all_cookies()   #清空
        self.driver.refresh()              #刷新页面
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
if __name__ == '__main__':
    unittest.main()
