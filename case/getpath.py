# coding=utf-8
import os
print(__file__)      #当前脚本的地址
re=os.path.realpath(__file__)
print(re)  #真实路径
dir=os.path.dirname(re)
print(dir)       #当前脚本的文件夹路径
gc=os.path.dirname(dir)        #继续进入到工程下面
print(gc)
com=os.path.join(gc,"common")      #进入到common文件夹下
print(com)
exl=os.path.join(com,"testddt.xlsx")   #进入到文件路径
print(exl)
