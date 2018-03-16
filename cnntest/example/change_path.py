#!/usr/bin/env python

# #导入包
import os

#
#查看默认工作目录
print(os.getcwd())

#改变工作目录
# os.chdir('E:\\python_lianxi\\webinterface\\YNCtestinterface\\test_data')
# print(os.getcwd())


base_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
file_path = base_path+"/test_data/"
os.chdir(file_path)
print(os.getcwd())
# print(base_path)
# base_path = base_path.replace('\\','/')
# file_path = base_path+"/test_data/"+"test_data.xlsx"
# print (file_path)







