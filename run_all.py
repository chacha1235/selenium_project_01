# coding=utf-8
import unittest
import time
from common.HTMLTestRunner_jpg import HTMLTestRunner
discover=unittest.defaultTestLoader.discover("F:\\pythonTest\\case","test*.py")  #discover(路径，匹配规则)
print(discover)
# discover2=unittest.defaultTestLoader.discover("F:\\pythonTest\\case","test*.py")  #discover(路径，匹配规则)
# all=unittest.TestSuite()      #定义一个测试套件
# for i in discover1:
#     all.addTests(i)
# for j in discover2:
#     all.addTests(j)
# print(all)

nowtime=time.strftime("%Y_%m_%d_%H_%M_%S")
reportpath ="F:\\pythonTest\\report"+"\\resut%s.html" %nowtime
fp = open(reportpath,"wb")
runner =HTMLTestRunner(fp,title="这是我的报告",description="报告内容如下")
# runner.run(all)
runner.run(discover)
fp.close()
