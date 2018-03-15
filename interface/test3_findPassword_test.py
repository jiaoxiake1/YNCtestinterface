#!/usr/bin/env python

import unittest
import requests
import json
from driver import base
from ddt import ddt,data,unpack
import os



base_path = os.path.dirname(os.path.dirname(__file__))
file_path = base_path+"/test_data/"+"test_data.xlsx"
AllData = base.get_data(file_path,'test3')
TestData = base.get_data(file_path,'test3')[1:]
# print(TestData)


@ddt
class findPasswordtest(unittest.TestCase):

    """用户忘记密码时，重新申请密码"""

    def setUp(self):
        endpoint = "findPassword"
        # self.base_url = "http://139.196.43.67:8080/login"
        self.url = base.get_url(endpoint)


    def tearDown(self):
        print(self.result)

    @data(*TestData)
    @unpack
    def test_findPassword_sendmailSuccessful(self,*TestData):
        """找回密码"""

        print(TestData)
        DataAll = eval(str(TestData[0]))
        # print(DataAll)
        ExceptResult = eval(str(TestData[1]))
        # print(ExceptResult)

        methon = "post"
        resp = base.get_response(self.url, methon, **DataAll)
        self.result = resp
        self.assertEqual(self.result['message'], ExceptResult['code'])
        self.assertEqual(self.result['status'], ExceptResult['status'])

if __name__ == "__main__":
    unittest.main()