#!/usr/bin/env python

import unittest
import requests
import json
from driver import myunit

"""用户"""

class completeUserInfotest(myunit.MyTest):

    """客户主动修改密码 """

    base_url = myunit.MyTest.base_url + "completeUserInfo"
    token = []


    def test1_login(self):

        "先登录 获取token"

        url = myunit.MyTest.base_url + "login"
        payload = {"username":"nn.chen@yuneec.com","password":"a1234567890"}
        payload = json.dumps(payload)
        r = requests.post(url,data=payload)
        self.result = r.json()
        self.assertEqual(self.result["message"],"10000")
        completeUserInfotest.token= (self.result["data"])["token"]
        print(completeUserInfotest.token)
        return ((self.result["data"])["token"])



    def test_completeUserInfo_SUCCESS1(self):

        """ 更改成功"""

        print(completeUserInfotest.token)
        payload = {"token":completeUserInfotest.token,"country":"","province":"","city":"",
                   "gender":"1","nickname":"tt","lastname":"tt","firstname":"tt"}
        payload = json.dumps(payload)
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result["message"], "10000")
        self.assertEqual(self.result["status"], "success")

    def test_completeUserInfo_tokenNULL(self):

        """token 为空"""

        payload = {"token":"","country":"","province":"","city":"",
                   "gender":"1","nickname":"tt","lastname":"tt","firstname":"tt"}
        payload = json.dumps(payload)
        r = requests.post(self.base_url,data=payload)
        self.result = r.json()
        self.assertEqual(self.result["message"],"10003")
        self.assertEqual(self.result["status"],"error")


    def test_completeUserInfo_takenERROR(self):

        """token 错误"""

        payload = {"token":"rrrr","country":"","province":"","city":"",
                   "gender":"1","nickname":"tt","lastname":"tt","firstname":"tt"}

        payload = json.dumps(payload)
        r = requests.post(self.base_url,data=payload)
        self.result = r.json()
        self.assertEqual(self.result["message"],"10005")
        self.assertEqual(self.result["status"],"error")

    # def test_completeUserInfo_accountNOTEXIST(self):
    #
    #     """用户名不存在   已经有tooken  不可能出现用户名不存在，除非管理员误删了用户的信息
    #
    #     payload = {"token":completeUserInfotest.token,"country":"","province":"","city":"",
    #                "gender":"1","nickname":"KKK","lastname":"tt","firstname":"tt"}
    #
    #     payload = json.dumps(payload)
    #     r = requests.post(self.base_url,data=payload)
    #     self.result = r.json()
    #     self.assertEqual(self.result["message"],"10005")
    #     self.assertEqual(self.result["status"],"error")


    def test_completeUserInfo_nicknameNULL(self):

        """昵称为空"""

        payload = {"token":completeUserInfotest.token,"country":"","province":"","city":"",
                   "gender":"1","nickname":"","lastname":"tt","firstname":"tt"}

        payload = json.dumps(payload)
        r = requests.post(self.base_url,data=payload)
        self.result = r.json()
        self.assertEqual(self.result["message"],"10501")
        self.assertEqual(self.result["status"],"error")

    def test_completeUserInfo_lastnameNULL(self):

        """姓氏为空"""

        payload = {"token":completeUserInfotest.token,"country":"","province":"","city":"",
                   "gender":"1","nickname":"yy","lastname":"","firstname":"tt"}

        payload = json.dumps(payload)
        r = requests.post(self.base_url,data=payload)
        self.result = r.json()
        self.assertEqual(self.result["message"],"10502")
        self.assertEqual(self.result["status"],"error")

    def test_completeUserInfo_firstnameNULL(self):

        """姓氏为空"""

        payload = {"token":completeUserInfotest.token,"country":"","province":"","city":"",
                   "gender":"1","nickname":"yy","lastname":"ii","firstname":""}

        payload = json.dumps(payload)
        r = requests.post(self.base_url,data=payload)
        self.result = r.json()
        self.assertEqual(self.result["message"],"10503")
        self.assertEqual(self.result["status"],"error")





if __name__ == "__main__":
    # unittest.main()
    p1 = completeUserInfotest()

