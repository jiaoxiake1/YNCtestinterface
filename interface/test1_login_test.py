#!/usr/bin/env python
import unittest
from driver import base
from ddt import ddt,data,unpack
import os


base_path = os.path.dirname(os.path.dirname(__file__))
# print(base_path)
base_path = base_path.replace('\\','/')
file_path = base_path+"/test_data/"+"test_data.xls"
AllData = base.get_data(file_path,'test1')

TestData = base.get_data(file_path,'test1')[1:]
print(TestData[0])



@ddt
class loginTest(unittest.TestCase):
    """用户登录测试"""

    def setUp(self):
        endpoint = "login"
        # self.base_url = "http://139.196.43.67:8080/login"
        self.url = base.get_url(endpoint)


    def tearDown(self):
        print(self.result)

    @data(*TestData)
    @unpack
    def test_login_Accout(self, *TestData):
        u'''用户登录测试'''
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