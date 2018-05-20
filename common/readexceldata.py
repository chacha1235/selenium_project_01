# coding=utf-8
import xlrd
#打开excel表格
data=xlrd.open_workbook("testddt.xlsx")
table=data.sheet_by_name("Sheet1")

nrows=table.nrows
ncols=table.ncols
print(nrows)     #行数
print(ncols)     #列数
print(table.row_values(0))  #获取第一行的值
print(table.col_values(0))  #获取第一列的值
