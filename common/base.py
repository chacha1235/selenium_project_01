# coding=utf-8
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

# driver = webdriver.Firefox()
# mos = driver.find_element()  # element
# ActionChains(driver).move_to_element(mos).perform()

class Base():

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 30
        self.poll = 0.5

    def findElement(self, loctor):
        '''
        args:
        loctor 传元祖，如（"id","xx"）
        '''
        element = WebDriverWait(self.driver, self.timeout, self.poll).until(lambda x: x.find_element(*loctor))
        return element

    def findElementNew(self, loctor):
        # 找到了返回element，没找到抛异常
        element = WebDriverWait(self.driver, self.timeout, self.poll).until(EC.presence_of_element_located(loctor))
        return element

    def findElementsNew(self, loctor):
        # 找到了返回list, 没找到抛异常
        elements = WebDriverWait(self.driver, self.timeout, self.poll).until(EC.presence_of_all_elements_located(loctor))
        return elements

    def findElements(self, loctor):
        '''
        args:
        loctor 传元祖，如（"id","xx"）
        '''
        elements = WebDriverWait(self.driver, self.timeout, self.poll).until(lambda x: x.find_elements(*loctor))
        return elements

    def clickElements(self, loctor, n=0):
        elems = self.findElements(loctor)  # list
        if len(elems) < 1:
            print("没找到元素！！！")
        elif n > len(elems):
            print("越界了！！！！！，最大值是：%s" % len(elems))
        else:
            elems[n].click()

    def sendKeys(self, loctor, text):
        ele = self.findElement(loctor)
        ele.send_keys(text)

    def click(self, loctor):
        ele = self.findElement(loctor)
        ele.click()

    def clear(self, loctor):
        ele = self.findElement(loctor)
        ele.clear()

    def moveToElement(self, loctor):
        '''鼠标悬停'''
        ele = self.findElement(loctor)
        ActionChains(driver).move_to_element(ele).perform()

    def is_text_in_element(self,locator,text):
        '''判断text包含在元素里面的时候统一返回bool'''
        try:
             result = WebDriverWait(self.driver, self.timeout, self.poll).until(EC.text_to_be_present_in_element(locator,text))
             return result
        except:
            return False

    def is_value_in_element(self,locator,text):
        '''判断value值，统一返回bool
        1.找不到元素返回False
        2.value为空返回False
        3.text不在元素的value值里返回False
        '''
        try:
             result = WebDriverWait(self.driver, self.timeout, self.poll).until(EC.text_to_be_present_in_element_value(locator,text))
             return result
        except:
            return False

    def is_element_exsists(self, locator):
        try:
            self.findElementNew(locator)
            return True
        except:
            return False

    def  is_title(self,text):
        try:
            result= WebDriverWait(self.driver, self.timeout, self.poll).until(EC.title_is(text))
            return True
        except:
            return False


if __name__ == "__main__":
    driver = webdriver.Firefox()
    base = Base(driver)
    driver.get("https://www.baidu.com")
    # loc1 = ("id", "kw")  # 定位百度输入框
    # base.sendKeys(loc1, "发送的内容")  # 关键字
    # loc2 = ("css selector", "#su")   # 定位搜索按钮
    # base.click(loc2)
    news_loc = ("xpath", ".//*[@id='u1']/a[1]")
    res = base.is_text_in_element(news_loc, "新")
    print(res)
    but_loc = ("id", "su")
    res1 = base.is_value_in_element(but_loc, "百度一下")
    print(res1)





