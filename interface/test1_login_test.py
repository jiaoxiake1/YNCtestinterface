#!/usr/bin/env python
import unittest
from driver import base
from driver import HttpServer,read_execl

from ddt import ddt,data,unpack


# import pprint

filepath = r'E:\python_lianxi\webinterface\YNCtestinterface\test_data\test1_login_test_data.xlsx'
AllData = base.get_data(filepath,'test1')
TestData = base.get_data(filepath,'test1')[1:]


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
    def test_login_AccoutSuccessful(self, *TestData):
        u'''用户登录测试'''
        DataAll = eval(TestData[0])
        # DataAll = eval(str(TestData))
        # print(DataAll)
        ExceptResult = eval(TestData[1])
        # print(ExceptResult)

        methon = "post"
        resp = base.get_response(self.url, methon, **DataAll)
        self.result = resp
        self.assertEqual(self.result['message'], ExceptResult['code'])
        self.assertEqual(self.result['status'], ExceptResult['status'])




    # # def test_login_Password(self):
    # #     """数据库错误"""
    # #     pass

if __name__ == "__main__":
    unittest.main()