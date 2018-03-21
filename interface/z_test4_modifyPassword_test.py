#!/usr/bin/env python

import unittest
import requests
import json
from driver import myunit



class modifyPasswordtest(myunit.MyTest):

    """客户主动修改密码 """

    base_url = myunit.MyTest.base_url + "modifyPassword"
    token = []


    def test_login(self):

        "先登录 获取token"

        url = myunit.MyTest.base_url + "login"
        payload = {"username":"nn.chen@yuneec.com","password":"a1234567890"}
        payload = json.dumps(payload)
        r = requests.post(url,data=payload)
        self.result = r.json()
        self.assertEqual(self.result["message"],"10000")
        print((self.result["data"]))
        modifyPasswordtest.token= (self.result["data"])["token"]
        print(modifyPasswordtest.token)
        return ((self.result["data"])["token"])

    def _login(self):

        "先登录 获取token"

        url = myunit.MyTest.base_url + "login"
        payload = {"username":"nn.chen@yuneec.com","password":"1234567890a"}
        payload = json.dumps(payload)
        r = requests.post(url,data=payload)
        self.result = r.json()
        self.assertEqual(self.result["message"],"10000")
        print((self.result["data"]))
        modifyPasswordtest.token= (self.result["data"])["token"]
        print(modifyPasswordtest.token)
        return ((self.result["data"])["token"])





    def test_modifyPassword_TokenNULL(self):

        """token 为空"""


        payload = {"token":"", "username":"nn.chen@yuneec.com",
                   "password":"a1234567890","newPassword":"1234567890a"}
        payload = json.dumps(payload)
        r = requests.post(self.base_url,data=payload)
        self.result = r.json()
        self.assertEqual(self.result["message"],"10003")
        self.assertEqual(self.result["status"],"error")

    def test_modifyPassword_TokenError(self):

        """token 错误 """


        payload = {"token": "ttt", "username": "nn.chen@yuneec.com",
                   "password": "1234567890a", "newPassword": "1234567890a"}
        payload = json.dumps(payload)
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result["message"], "10005")
        self.assertEqual(self.result["status"], "error")

    def test_modifyPassword_PassworkEqual(self):

        """ 新密码和旧密码相同 """


        payload = {"token": modifyPasswordtest.token, "username": "nn.chen@yuneec.com",
                   "password": "1234567890a", "newPassword": "1234567890a"}
        payload = json.dumps(payload)
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result["message"], "10202")
        self.assertEqual(self.result["status"], "error")

    def test_modifyPassword_AccountORPasswordError1(self):

        """ 用户名或密码错误  用户名错"""

        payload = {"token":modifyPasswordtest.token, "username": "yuneec.com",
                   "password": "1234567890a", "newPassword": "a1234567890"}
        payload = json.dumps(payload)
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result["message"], "10406")
        self.assertEqual(self.result["status"], "error")

    def test_modifyPassword_AccountORPasswordError2(self):

        """ 用户名或密码错误 密码错 """

        payload = {"token":modifyPasswordtest.token, "username": "nn.chen@yuneec.com",
                   "password": "4567890a", "newPassword": "a1234567890"}
        payload = json.dumps(payload)
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result["message"], "10406")
        self.assertEqual(self.result["status"], "error")

    def test_modifyPassword_AccountORPasswordError3(self):

        """ 用户名或密码错误  用户名密码都错 """

        payload = {"token":modifyPasswordtest.token, "username": "n@yuneec.com",
                   "password": "4567890a", "newPassword": "a1234567890"}
        payload = json.dumps(payload)
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result["message"], "10406")
        self.assertEqual(self.result["status"], "error")

    def test_modifyPassword_AccountORPasswordError4(self):

        """ 用户名或密码错误  用户名为空"""

        payload = {"token":modifyPasswordtest.token, "username": "",
                   "password": "a1234567890", "newPassword": ""}
        payload = json.dumps(payload)
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result["message"], "10006")
        self.assertEqual(self.result["status"], "error")

    def test_modifyPassword_AccountORPasswordError5(self):

        """ 用户名或密码错误  密码为空"""

        payload = {"token":modifyPasswordtest.token, "username": "nn.chen@yuneec.com",
                   "password": "", "newPassword": ""}
        payload = json.dumps(payload)
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result["message"], "10006")
        self.assertEqual(self.result["status"], "error")


    def test_modifyPassword_PasswordNULL(self):

        """ 新密码为空"""

        payload = {"token":modifyPasswordtest.token, "username": "nn.chen@yuneec.com",
                   "password": "a1234567890", "newPassword": ""}
        payload = json.dumps(payload)
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result["message"], "10006")
        self.assertEqual(self.result["status"], "error")

    def test_modifyPassword_PasswordFormatError1(self):

        """ 新密码格式不正确 小于6位 全数字"""

        payload = {"token":modifyPasswordtest.token, "username": "nn.chen@yuneec.com",
                   "password": "a1234567890", "newPassword": "12335"}
        payload = json.dumps(payload)
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result["message"], "10405")
        self.assertEqual(self.result["status"], "error")

    def test_modifyPassword_PasswordFormatError2(self):

        """ 新密码格式不正确 大于18位 全数字"""

        payload = {"token":modifyPasswordtest.token, "username": "nn.chen@yuneec.com",
                   "password": "a1234567890", "newPassword": "1234567890123456789"}
        payload = json.dumps(payload)
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result["message"], "10405")
        self.assertEqual(self.result["status"], "error")

    def test_modifyPassword_PasswordFormatError3(self):

        """ 新密码格式不正确  6-18 全数字"""

        payload = {"token":modifyPasswordtest.token, "username": "nn.chen@yuneec.com",
                   "password": "1234567890a", "newPassword": "123456789012345678"}
        payload = json.dumps(payload)
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result["message"], "10405")
        self.assertEqual(self.result["status"], "error")

    def test_modifyPassword_PasswordFormatError4(self):

        """ 新密码格式不正确  6-18 全字母"""

        payload = {"token":modifyPasswordtest.token, "username": "nn.chen@yuneec.com",
                   "password": "1234567890a", "newPassword": "aaaaaaaaaaaaaaaaa"}
        payload = json.dumps(payload)
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result["message"], "10405")
        self.assertEqual(self.result["status"], "error")

    def test_modifyPassword_PasswordFormatError5(self):

        """ 新密码格式不正确  6-18 特殊符号"""

        payload = {"token":modifyPasswordtest.token, "username": "nn.chen@yuneec.com",
                   "password": "1234567890a", "newPassword": "aaaaaaaaaaaaaaaa!"}
        payload = json.dumps(payload)
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result["message"], "10405")
        self.assertEqual(self.result["status"], "error")


    def test_modifyPassword_PasswordFormatError6(self):

        """ 新密码格式不正确  6-18 含中文"""

        payload = {"token": modifyPasswordtest.token, "username": "nn.chen@yuneec.com",
                   "password": "1234567890a", "newPassword": "aaaaaaaaaaaaaa啦!"}
        payload = json.dumps(payload)
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result["message"], "10405")
        self.assertEqual(self.result["status"], "error")

    def test_modifyPassword_SUCCESS1(self):

        """ 更改成功"""

        payload = {"token":modifyPasswordtest.token, "username": "nn.chen@yuneec.com",
                   "password": "a1234567890", "newPassword": "1234567890a"}
        print(modifyPasswordtest.token)
        payload = json.dumps(payload)
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result["message"], "10000")
        self.assertEqual(self.result["status"], "success")





    def test_modifyPassword_SUCCESS2(self):

        """ 更改成功"""

        payload = {"token": self._login(), "username": "nn.chen@yuneec.com",
                   "password": "1234567890a", "newPassword": "a1234567890"}
        payload = json.dumps(payload)
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result["message"], "10000")
        self.assertEqual(self.result["status"], "success")





if __name__ == "__main__":
    unittest.main()
