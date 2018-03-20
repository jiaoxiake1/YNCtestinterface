#!/usr/bin/env python

import requests
import json
from driver import myunit
import unittest
from driver import base,write_execl
from ddt import ddt,data,unpack
import random,string
import os



# 获取路径
base_path = os.path.dirname(os.path.dirname(__file__))
base_path = base_path.replace('\\','/')
file_path = base_path+"/test_data/"+"test_data1.xls"
print(file_path)

# 写user_Password  和 ExceptResult 格式

# username_json=str({"json":{"username":"cc@yuneec.com","password":"a1234567890"}})
# exceptResult_json = str({"code":"10000","status":"success"})
# discription = "申请用户名成功"
# insertArr = [username_json,exceptResult_json,discription]
# datainfo = write_execl.XLDataInsert(file_path,insertArr).insertData_by_sheetname("test5",5)

# AllData = base.get_data(file_path,'test5')
TestData = base.get_data(file_path,'test5')[1:]
# print(TestData)


@ddt
class completeUserInfotest(unittest.TestCase):
    """用户登录测试"""

    def setUp(self):
        endpoint = "completeUserInfo"
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




# @ddt
# # class completeUserInfotest(myunit.MyTest):
# class completeUserInfotest(unittest.TestCase):
#
#
#     """客户主动修改密码 """
#
#     # base_url = myunit.MyTest.base_url + "completeUserInfo"
#     # token = []
#
#     def setUp(self):
#         endpoint = "completeUserInfo"
#         self.url = base.get_url(endpoint)
#         print(self.url)
#
#
#     def tearDown(self):
#         print("*****tear down zhong ******")
#         print(self.result)


    # def test1_login(self):
    #
    #     "先登录 获取token"
    #
    #     url = myunit.MyTest.base_url + "login"
    #     payload = {"username":"nn.chen@yuneec.com","password":"a1234567890"}
    #     payload = json.dumps(payload)
    #     r = requests.post(url,data=payload)
    #     self.result = r.json()
    #     self.assertEqual(self.result["message"],"10000")
    #     completeUserInfotest.token= (self.result["data"])["token"]
    #     print(completeUserInfotest.token)
    #     return ((self.result["data"])["token"])




#     @data(*TestData)
#     @unpack
#     def test_completeUserInfo(self,*TestData):
#         """ 更改成功"""
#
#         print(TestData)
#         DataAll = eval(str(TestData[0]))
#         print(DataAll)
#         ExceptResult = eval(str(TestData[1]))
#         print(ExceptResult)
#         methon = "post"
#         resp = base.get_response(self.url, methon, **DataAll)
#         self.result = resp
#         print(resp['message'])
#         self.assertEqual(self.result['message'], ExceptResult['code'])
#         self.assertEqual(self.result['status'], ExceptResult['status'])
# #
#     def test_completeUserInfo_tokenNULL(self):
#
#         """token 为空"""
#
#         payload = {"token":"","country":"","province":"","city":"","gender":"1","nickname":"tt","lastname":"tt","firstname":"tt"}
#         payload = json.dumps(payload)
#         r = requests.post(self.base_url,data=payload)
#         self.result = r.json()
#         self.assertEqual(self.result["message"],"10003")
#         self.assertEqual(self.result["status"],"error")
#
#
    # def test_completeUserInfo_takenERROR(self):
    #
    #     """token 错误"""
    #
    #     payload = {"token":"rrrr","country":"","province":"","city":"",
    #                "gender":"1","nickname":"tt","lastname":"tt","firstname":"tt"}
    #
    #     payload = json.dumps(payload)
    #     r = requests.post(self.base_url,data=payload)
    #     self.result = r.json()
    #     self.assertEqual(self.result["message"],"10005")
    #     self.assertEqual(self.result["status"],"error")
#
#     # def test_completeUserInfo_accountNOTEXIST(self):
#     #
#     #     """用户名不存在   已经有tooken  不可能出现用户名不存在，除非管理员误删了用户的信息
#     #
#     #     payload = {"token":completeUserInfotest.token,"country":"","province":"","city":"",
#     #                "gender":"1","nickname":"KKK","lastname":"tt","firstname":"tt"}
#     #
#     #     payload = json.dumps(payload)
#     #     r = requests.post(self.base_url,data=payload)
#     #     self.result = r.json()
#     #     self.assertEqual(self.result["message"],"10005")
#     #     self.assertEqual(self.result["status"],"error")
#
#
#     def test_completeUserInfo_nicknameNULL(self):
#
#         """昵称为空"""
#
#         payload = {"token":completeUserInfotest.token,"country":"","province":"","city":"",
#                    "gender":"1","nickname":"","lastname":"tt","firstname":"tt"}
#
#         payload = json.dumps(payload)
#         r = requests.post(self.base_url,data=payload)
#         self.result = r.json()
#         self.assertEqual(self.result["message"],"10501")
#         self.assertEqual(self.result["status"],"error")
#
#     def test_completeUserInfo_lastnameNULL(self):
#
#         """姓氏为空"""
#
#         payload = {"token":completeUserInfotest.token,"country":"","province":"","city":"",
#                    "gender":"1","nickname":"yy","lastname":"","firstname":"tt"}
#
#         payload = json.dumps(payload)
#         r = requests.post(self.base_url,data=payload)
#         self.result = r.json()
#         self.assertEqual(self.result["message"],"10502")
#         self.assertEqual(self.result["status"],"error")
#
#     def test_completeUserInfo_firstnameNULL(self):
#
#         """姓氏为空"""
#
#         payload = {"token":completeUserInfotest.token,"country":"","province":"","city":"",
#                    "gender":"1","nickname":"yy","lastname":"ii","firstname":""}
#
#         payload = json.dumps(payload)
#         r = requests.post(self.base_url,data=payload)
#         self.result = r.json()
#         self.assertEqual(self.result["message"],"10503")
#         self.assertEqual(self.result["status"],"error")





if __name__ == "__main__":
    unittest.main()

