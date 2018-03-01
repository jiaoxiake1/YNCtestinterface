#!/usr/bin/env python

import unittest
import requests
import json
from driver import myunit
import random,string

class setAccentTest(myunit.MyTest):
    """用户注册"""
    base_url = myunit.MyTest.base_url + "setAccount"

    # def setUp(self):
    #     self.base_url = "http://139.196.43.67:8080/setAccount"

    # def tearDown(self):
    #     print(self.result)

    def test_setAccount_AccountNULL(self):
        """ 账号为空"""
        payload={"username":"","password":"ABC2345"}
        payload = json.dumps(payload)
        r = requests.post(self.base_url,data=payload)
        self.result = r.json()
        self.assertEqual(self.result["status"],"error")
        self.assertEqual(self.result['message'],'10002')

    def test_setAccount_AccountFormatError1(self):
        """ 用户名格式不正确 不含@"""
        payload = {"username": "10000helang.com", "password": "abc123456"}
        payload = json.dumps(payload)
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result["status"], "error")
        self.assertEqual(self.result['message'], '10105')

    def test_setAccount_AccountFormatError2(self):
        """ 用户名格式不正确  用户名结尾处加@"""
        payload = {"username": "10000helang@.com", "password": "abc123456"}
        payload = json.dumps(payload)
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result["status"], "error")
        self.assertEqual(self.result['message'], '10105')


    def test_setAccount_PasswordFormatError1(self):
        """ 密码不正确 纯数字 小于6位"""
        payload = {"username": "10000@helang.com", "password": "12345"}
        payload = json.dumps(payload)
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result["status"], "error")
        self.assertEqual(self.result['message'], '10106')

    def test_setAccount_PasswordFormatError2(self):
        """ 密码不正确 纯数字 大于18位"""
        payload = {"username": "10000@helang.com", "password": "1234567890123456789"}
        payload = json.dumps(payload)
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result["status"], "error")
        self.assertEqual(self.result['message'], '10106')

    def test_setAccount_PasswordFormatError3(self):
        """ 密码不正确 纯字母 小于6"""
        payload = {"username": "91111@helang.com", "password": "emoji"}
        payload = json.dumps(payload)
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result["status"], "error")
        self.assertEqual(self.result['message'], '10106')

    def test_setAccount_PasswordFormatError4(self):
        """ 密码不正确 纯字母 大于18位"""
        salt = ''.join(random.sample(string.ascii_letters + string.digits, 8))
        payload = {"username": "10000@helang.com", "password": "aaaaabbbbbcccccdddd"}
        payload = json.dumps(payload)
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result["status"], "error")
        self.assertEqual(self.result['message'], '10106')

    def test_setAccount_PasswordFormatError5(self):
        """ 密码不正确 纯字母 大于18位"""
        payload = {"username": "10000@helang.com", "password": "aaaaabbbbbcccccdddd"}
        payload = json.dumps(payload)
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result["status"], "error")
        self.assertEqual(self.result['message'], '10106')

    def test_setAccount_PasswordFormatError6(self):
        """ 密码不正确 特殊字符 小于6位"""
        payload = {"username": "10000@helang.com", "password": "!@#$%"}
        payload = json.dumps(payload)
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result["status"], "error")
        self.assertEqual(self.result['message'], '10106')

    def test_setAccount_PasswordFormatError7(self):
        """ 密码不正确 特殊字符 大于16"""
        payload = {"username": "10000@helang.com", "password": "!@#$%^&*()_- +?/,.<>"}
        payload = json.dumps(payload)
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result["status"], "error")
        self.assertEqual(self.result['message'], '10106')

    def test_setAccount_PasswordFormatError8(self):
        """ 密码不正确 特殊字符 大于18"""
        payload = {"username": "10000@helang.com", "password": "!@#$%^&*()_- +?/,.<>"}
        payload = json.dumps(payload)
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result["status"], "error")
        self.assertEqual(self.result['message'], '10106')
    def test_setAccount_PasswordFormatError9(self):
        """ 密码不正确 特殊字符 大于6小于大于18"""
        payload = {"username": "10000@helang.com", "password": "!@#$%^&*()_"}
        payload = json.dumps(payload)
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result["status"], "error")
        self.assertEqual(self.result['message'], '10106')

    def test_setAccount_PasswordNULL(self):
        """ 密码为空"""
        payload={"username":"mmm@yuneec.com","password":""}
        payload = json.dumps(payload)
        r = requests.post(self.base_url,data=payload)
        self.result = r.json()
        self.assertEqual(self.result["status"],"error")
        self.assertEqual(self.result['message'],'10103')

    def test_setAccount_AccountExist(self):
        """ 该账号已被注册"""
        payload={"username":"1111@helang.com","password":"abc123456"}
        # print(type(payload))
        payload = json.dumps(payload)
        # print(type(payload))
        r = requests.post(self.base_url,data=payload)
        # print("text : "+ r.text)
        # print("url : "+r.url)
        # print("r.encoding : "+r.encoding)
        self.result = r.json()
        # print("333")
        # print("self.result : "+ str(self.result))
        # print("self.base_url : " + self.base_url)
        self.assertEqual(self.result["status"],"error")
        self.assertEqual(self.result['message'],'10104')


    # def test_setAccount_RegestSuccessful(self):
    #     """账号注册成功"""
    #     username = ''.join(random.sample(string.ascii_letters + string.digits, 8))
    #     username=username+"@yuneec.com"
    #     print(username)
    #     payload={"username":username,"password":"abcde1"}
    #     payload = json.dumps(payload)
    #     r = requests.post(self.base_url,data=payload)
    #     self.result = r.json()
    #     self.assertEqual(self.result["status"],"success")
    #     self.assertEqual(self.result['message'],'10000')


if __name__ == "__main__":
    unittest.main()