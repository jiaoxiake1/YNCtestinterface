#!/usr/bin/env python
import unittest
from driver import base

from ddt import ddt,data,unpack


# import pprint

filepath = r'E:\python_lianxi\webinterface\YNCtestinterface\test_data\test1_login_test_data.xlsx'
AllData = base.get_data(filepath,'test1')
TestData = base.get_data(filepath,'test1')[1:]
# DataALL = eval(AllData[1:] )
# ExceptResult = eval(AllData[1][1])
print(TestData)

# 可以增加 测试函数数：endpoint ；测试方法：get post;










@ddt
class loginTest(unittest.TestCase):
    """用户登录测试"""

    # base_url = myunit.MyTest.base_url + "login"

    def setUp(self):
        endpoint = "login"
        # self.endpoint =
        self.url = base.get_url(endpoint)
        # self.ResquestMethod = get  # post 或get 方法
        # self.RequestData = AllData[1:]



    def tearDown(self):
        print(self.result)

    #
    @data(*TestData)
    @unpack
    def test_login_AccoutSuccessful(self,*TestData):

        DataAll = eval(TestData[0])
        # DataAll = eval(str(TestData))
        # print(DataAll)
        ExceptResult = eval(TestData[1])
        # print(ExceptResult)

        methon = "post"
        resp = base.get_response(self.url,methon,**DataAll)
        self.result = resp
        self.assertEqual(self.result['message'],ExceptResult['code'])
        self.assertEqual(self.result['status'],ExceptResult['status'])


#
#     def test_login_AccountNULL(self):
#         """用户名为空"""
#         json = {"username": "", "password": "a1234567890"}
#         DataALL = {"json": json}
#         methon = "post"
#         resp = base.get_response(self.url,methon,**DataALL)
#         # resp = HttpServer.MyHTTP.post(self,**DataALL)
#         self.result = resp
#         self.assertEqual(self.result['message'],'10002')
#         self.assertEqual(self.result['status'],'error')
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
# #
# #     def test_login_PasswordError(self):
# #         """密码错误"""
# #         json = {"username": "nn.chen@yuneec.com", "password": "a123456789"}
# #         DataALL = {"json": json}
# #         methon = "post"
# #         resp = base.get_response(self.url,methon,**DataALL)
# #         # resp = HttpServer.MyHTTP.post(self, **DataALL)
# #         self.result = resp
# #         self.assertEqual(self.result['message'],'10203')
# #         self.assertEqual(self.result['status'],'error')
# #
# #     # def test_login_Password(self):
# #     #     """数据库错误"""
# #     #     pass
# #
if __name__ == "__main__":
    unittest.main()