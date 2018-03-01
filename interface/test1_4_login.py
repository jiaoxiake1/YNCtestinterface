#!/usr/bin/env python

"""
mock 实例使用
"""
import unittest
from driver import base
from unittest import mock
from test_data.mock_data.get_params_test_mock import *
from ddt import ddt,data,unpack


# import pprint
#
# filepath = r'E:\python_lianxi\webinterface\YNCtestinterface\test_data\test1_login_test.xlsx'
# # datainfo = read_execl.XLDatainfo(filepath)
# # alldata = datainfo.get_sheetinfo_by_name('test1')
# AllData = base.get_data(filepath,'test1')
# TestData = base.get_data(filepath,'test1')[1:]
# # AllData2 = base.get_data(filepath,'test2')
# # UserPasswd =AllData[1][1] #输入数据
# # ExceptResult =AllData[1][2]#返回结果

# 可以增加 测试函数数：endpoint ；测试方法：get post;

# print(AllData)
# UserPasswd = eval(UserPasswd)
# print(UserPasswd)
# print(type(ExceptRsult))

# print(type(ExceptRsult))
# print(ExceptRsult['code'])








# print(AllData)

# # @ddt
class loginTest(unittest.TestCase):
    """用户登录测试"""

    # base_url = myunit.MyTest.base_url + "login"

    def setUp(self):
        endpoint = "login"
        # self.base_url = "http://139.196.43.67:8080/login"
        self.url = base.get_url(endpoint)
        # self.UserPasswd = eval(AllData[1][0])  # 输入数据
        # self.ExceptResult = eval(AllData[1][1])  # 返回结果


    def tearDown(self):
        print(self.result)


    # @data([UserPasswd])
    # @unpack
    # def test_login_AccoutSuccessful(self):
    #
    #     """登录成功"""
    #     # json = {"username":"nn.chen@yuneec.com","password":"a1234567890"}
    #     # DataALL = {"json":json}
    #     # DataALL = eval(self.UserPasswd)
    #     # ExceptResult1 = eval(self.ExceptResult)
    #
    #     methon = "post"
    #     resp = base.get_response(self.url,methon,**self.UserPasswd)
    #     self.result = resp
    #     self.assertEqual(self.result['message'],self.ExceptResult['code'])
    #     self.assertEqual(self.result['status'],self.ExceptResult['status'])
    #

#
    def test_login_AccountNULL(self):
        """用户名为空"""
        json = {"username": "nn.chen@yuneec.com", "password": "a1234567890"}
        DataALL = {"json": json}
        methon = "post"
        resp = base.get_response(self.url,methon,**DataALL)
        if base.get_mock_status() =='ON':
            mockresp = mock.Mock(side_effect = mockFoo)
            resp = mockFoo()
            print(mockresp)
        # resp = HttpServer.MyHTTP.post(self,**DataALL)
        self.result = resp
        self.assertEqual(self.result['message'],'10000')
        self.assertEqual(self.result['status'],'success')
#
#
#     def test_login_AccountError(self):
#         """用户名错误"""
#         json = {"username": "wnien", "password": "a1234567890"}
#         DataALL = {"json": json}
#         methon = "post"
#         resp = base.get_response(self.url,methon,**DataALL)
#         # resp = HttpServer.MyHTTP.post(self, **DataALL)
#         self.result = resp
#         self.assertEqual(self.result['message'],'10203')
#         self.assertEqual(self.result['status'],'error')
#
#
#     def test_login_PasswordError(self):
#         """密码错误"""
#         json = {"username": "nn.chen@yuneec.com", "password": "a123456789"}
#         DataALL = {"json": json}
#         methon = "post"
#         resp = base.get_response(self.url,methon,**DataALL)
#         # resp = HttpServer.MyHTTP.post(self, **DataALL)
#         self.result = resp
#         self.assertEqual(self.result['message'],'10203')
#         self.assertEqual(self.result['status'],'error')
#
#     # def test_login_Password(self):
#     #     """数据库错误"""
#     #     pass
#
if __name__ == "__main__":
    unittest.main()