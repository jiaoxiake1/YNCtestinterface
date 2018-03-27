#!/usr/bin/env python

import unittest
from driver import base
from ddt import ddt,data,unpack
import os



base_path = os.path.dirname(os.path.dirname(__file__))
# print(base_path)
base_path = base_path.replace('\\','/')
file_path = base_path+"/test_data/"+"test_data.xls"
AllData = base.get_data(file_path,'test7')

TestData = base.get_data(file_path,'test7')[1:]
# print(TestData)


@ddt
class helpManualtest(unittest.TestCase):
    """用户登录测试"""

    def setUp(self):
        endpoint = "helpManual"
        self.url = base.get_url(endpoint)


    def tearDown(self):
        print(self.result)

    @data(*TestData)
    @unpack
    def test_helpManualtest(self, *TestData):

        """获取产品使用手册"""

        # print(TestData)
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


