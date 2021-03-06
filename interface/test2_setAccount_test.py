#!/usr/bin/env python

import unittest
from driver import base,write_execl
from ddt import ddt,data,unpack
import random,string
import os

# 获取路径
base_path = os.path.dirname(os.path.dirname(__file__))
base_path = base_path.replace('\\','/')
file_path = base_path+"/test_data/"+"test_data.xls"

# 写user_Password  和 ExceptResult 格式
username = ''.join(random.sample(string.ascii_letters + string.digits, 8))
username = username+"@yuneec.com"
username_json=str({"json":{"username":username,"password":"a1234567890"}})
exceptResult_json = str({"code":"10000","status":"success"})
discription = "申请用户名成功"
insertArr = [username_json,exceptResult_json,discription]
# datainfo = write_execl.XLDataInsert(file_path,insertArr).insertData_by_sheetname("test2",13)
datainfo = base.insert_data_one_line(file_path,insertArr,"test2",13)
#
# # print(file_path)
AllData = base.get_data(file_path,'test2')
TestData = base.get_data(file_path,'test2')[1:]
print(TestData)

@ddt
class setAccentTest(unittest.TestCase):
    """注册问题"""

    def setUp(self):
        endpoint = "setAccount"
        self.url = base.get_url(endpoint)


    def tearDown(self):
        print(self.result)

    @data(*TestData)
    @unpack
    def test_setAccount(self, *TestData):
        """注册问题"""
        print(TestData)
        DataAll = eval(str(TestData[0]))
        print(DataAll)
        ExceptResult = eval(str(TestData[1]))
        print(ExceptResult)

        methon = "post"
        resp = base.get_response(self.url, methon, **DataAll)
        self.result = resp
        self.assertEqual(self.result['message'], ExceptResult['code'])
        self.assertEqual(self.result['status'], ExceptResult['status'])


if __name__ == "__main__":
    unittest.main()