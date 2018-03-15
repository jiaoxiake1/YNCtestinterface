#!/usr/bin/env python

import unittest
import requests
import json
from driver import base
from ddt import ddt,data,unpack
import random,string
import os


base_path = os.path.dirname(os.path.dirname(__file__))
# print(base_path)
# base_path = base_path.replace('\\','/')
file_path = base_path+"/test_data/"+"test_data.xlsx"
# print(file_path)
AllData = base.get_data(file_path,'test2')
TestData = base.get_data(file_path,'test2')[1:]

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


    def test_setAccount_RegestSuccessful(self):
        """账号注册成功"""
        username = ''.join(random.sample(string.ascii_letters + string.digits, 8))
        username=username+"@yuneec.com"
        print(username)
        payload={"username":username,"password":"abcde1"}
        payload = json.dumps(payload)
        r = requests.post(self.url,data=payload)
        self.result = r.json()
        self.assertEqual(self.result["status"],"success")
        self.assertEqual(self.result['message'],'10000')
#
#
if __name__ == "__main__":
    unittest.main()