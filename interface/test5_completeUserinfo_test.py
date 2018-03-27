#!/usr/bin/env python

import unittest
from driver import base
from ddt import ddt,data,unpack
import os



# 获取路径
base_path = os.path.dirname(os.path.dirname(__file__))
base_path = base_path.replace('\\','/')
file_path = base_path+"/test_data/"+"test_data.xls"
# print(file_path)


# 写 inserArr
token =base.login_token()
# print("token : "+ token)
# print(token)

# 1、token错误  2、token 为空  3、nicknames 为空
# 4、lastname 为空  5、firstname 为空 6、success

inputPara1 = str({"json":{"token":"xxxxx","nickname":"kk","lastname":"kk","firstname":"kk"}})
exceptResul1 =str({"code":"10005","status":"error"})
discription1 = "token错误"

inputPara2 = str({"json":{"token":"","nickname":"kk","lastname":"kk","firstname":"kk"}})
exceptResul2 =str({"code":"10003","status":"error"})
discription2 = "token为空"

inputPara3 = str({"json":{"token":token,"nickname":"","lastname":"kk","firstname":"kk"}})
exceptResul3 =str({"code":"10501","status":"error"})
discription3 = "昵称为空"

inputPara4 = str({"json":{"token":token,"nickname":"kk","lastname":"","firstname":"kk"}})
exceptResul4 =str({"code":"10502","status":"error"})
discription4 = "姓氏为空"

inputPara5 = str({"json":{"token":token,"nickname":"kk","lastname":"kk","firstname":""}})
exceptResul5 =str({"code":"10503","status":"error"})
discription5 = "名称为空"

inputPara6 = str({"json":{"token":token,"nickname":"kk","lastname":"kk","firstname":"kk"}})
exceptResul6 =str({"code":"10000","status":"success"})
discription6 = "success"

insertArr = [
            [inputPara1,exceptResul1,discription1],[inputPara2,exceptResul2,discription2],
             [inputPara3, exceptResul3, discription3],[inputPara4,exceptResul4,discription4],
             [inputPara5, exceptResul5, discription5],[inputPara6,exceptResul6,discription6]
]

datainfo = base.insert_data_several_lines(file_path,insertArr,"test5")


# # AllData = base.get_data(file_path,'test5')
TestData = base.get_data(file_path,'test5')[1:]
# print(TestData)
#
#
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
    def test_completeUserInfo(self, *TestData):
        u'''用户登录测试'''
        # print(TestData)
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

