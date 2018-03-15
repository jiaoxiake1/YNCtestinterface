#!/usr/bin/env python

import os,sys

import xlrd
import datetime

newpath ="E:/python_lianxi/webinterface/YNCtestinterface/test_data/"

filename = "test1_login_test_data.xlsx"

os.chdir(newpath)
retval= os.getcwd()
print(retval)

file = os.path.join(retval,filename)

print(file)

#一 打开文件
xl = xlrd.open_workbook(file)


# 二 获取sheet
# print(xl.sheet_names())
# print(xl.sheets())
# print(xl.sheet_by_name("test1"))
# print(xl.sheet_by_index(1))

#三 获取sheet内的汇总数据
table1 = xl.sheet_by_name("test2")

# print(table1.name)
print(table1.nrows)
# print(table1.ncols)

# 四 单元格批量读取

# print(table1.col_values(0))
# print(table1.col_values(2))
print(table1.col_values(2,0,6))

# print(table1.row_values(0))
# print(table1.row(0))
# print(table1.row_types(0))
# print(table1.row_values(0,1,3))
# print(table1.row_values(2,1,3))

# print(table1.row_slice(0))
# print(table1.row_slice(0,1,3))


#特定单元格读取

# 取值
# print(table1.cell(1,2).value)
print(table1.cell_value(1,3))
# print(table1.row(1)[2].value)
#
# #获取类型
#
# print(table1.cell(1,2).ctype)
# print(table1.cell_type(1,2))
# print(table1.row(1)[2].ctype)
#
# #常用技巧（0，0）转成A1
#
# print(xlrd.cellname(0,0))
# print(xlrd.cellnameabs(0,0))
# print(xlrd.colname(0))



# def read_excel(table,row,col):
#     name = table1.cell_value(row,col)
#     type = table1.cell_type(row,col)
#
#     if type == 0:
#         name = "' '"
#     elif type == 1:
#         name = name
#     elif type == 2 and name % 1 == 0:
#         name = int(name)
#     elif type == 3:
#         # 方法1 转换为日期时间
#         # date_value = xlrd.xldate_as_datetime(name,0)
#         # name = date_value
#         #方法二 转换为元组
#         date_value = xlrd.xldate_as_tuple(name,0)
#         name =datetime(*date_value).strftime('%Y/%m/%d %H:%M:%S')
#
#     elif type == 4:
#         name = True if name == 1 else False
#     return name
#
# # 七 获取表格内不同的类型的name
#
# print(table1.cell_value(1,2))
# print(table1.cell_type(1,2))



# retval = os.getcwd()
# print("当前: %s" %retval)
#
# os.chdir(path)
#
# retval= os.getcwd()
#
# print("genggaihou : %s" % retval)