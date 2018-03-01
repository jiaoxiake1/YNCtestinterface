#!/usr/bin/env python

import unittest
import requests
import json
from driver import myunit

class findPasswordtest(myunit.MyTest):
    """用户忘记密码时，重新申请密码"""
    base_url = myunit.MyTest.base_url + "findPassword"

    def test_findPassword_sendmailSuccessful(self):

        """发用验证码邮件成功"""
        payload = {"username":"nn.chen@yuneec.com"}
        payload=json.dumps(payload)
        r = requests.post(self.base_url,data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'],"success")
        self.assertEqual(self.result['message'],'10000')

    def test_findPassword_AccountNULL(self):
        """用户名为空"""
        payload = {"username": ""}
        payload = json.dumps(payload)
        r = requests.post(self.base_url,data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'],'error')
        self.assertEqual(self.result['message'],'10002')

    def test_findPassword_AccountNotExist(self):
        """用户名不存在"""
        payload = {"username": "11111111@yuneec.com"}
        payload = json.dumps(payload)
        r = requests.post(self.base_url,data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'],'error')
        self.assertEqual(self.result['message'],'10007')

    # def test_findPassword_sendEmailFail(self):
    #     """邮件发送失败   ? 无法判断邮件发送失败"""
    #     payload = {"username": "vv@yuneec.com"}
    #     payload = json.dumps(payload)
    #     r = requests.post(self.base_url, data=payload)
    #     self.result = r.json()
    #     self.assertEqual(self.result['status'], 'error')
    #     self.assertEqual(self.result['message'], '10301')



if __name__ == "__main__":
    unittest.main()