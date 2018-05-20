# coding=utf-8
from common.base import Base

# 用到其它模块。先导入

# 继承过来的类，里面的方法可以直接self.调用，不需要实例化
loginurl="http://127.0.0.1/zentao/user-login-L3plbnRhby8=.html"
class LoginPage(Base):
    '''登录页面'''
    user_loc = ("id", "account")  # 输入账号
    psw_loc = ("name", "password")  # 输入密码
    sub_loc = ("id", "submit")    # 点登录
    zhanghao_loc = ("css selector", "#userMenu>a")

    def open_login_page(self):
        self.driver.get(loginurl)

    def logout(self):
        '''登出'''
        # driver = webdriver.Firefox()
        self.driver.delete_all_cookies() # 删除所有的cookies
        self.driver.refresh()

    def input_username(self,usrname):
        '''输入账号'''
        self.sendKeys(self.user_loc, usrname)

    def input_psw(self, psw):
        '''输入密码'''
        self.sendKeys(self.psw_loc, psw)

    def click_login_button(self):
        '''点击登录按钮'''
        self.click(self.sub_loc)

    def login(self, username="admin", psw="123456"):
        '''登录流程:'''
        self.open_login_page()
        self.input_username(username)
        self.input_psw(psw)
        self.click_login_button()

    def get_login_result(self):
        '''获取登录的结果'''
        try:
            t = self.findElement(self.zhanghao_loc).text
            return t
        except:
            print("登录失败！！！，返回空字符")
            return ""

    def is_alert_exist(self):
        '''判断有弹框点确定，没有弹框的话直接退出'''
        try:
            alert=self.driver.switch_to_alert()   #切换到弹框
            print(alert.text)                     #输出弹框上的内容
            alert.accept()
        except:
            pass