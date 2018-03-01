#!/usr/bin/env python


#!/usr/bin/env python

import unittest
import requests
import json
from driver import myunit

"""用户"""

class getUserInfo_test(myunit.MyTest):

    """客户主动修改密码 """

    base_url = myunit.MyTest.base_url + "getUserInfo"
    token = []


    def test1_login(self):

        "先登录 获取token"

        url = myunit.MyTest.base_url + "login"
        payload = {"username":"nn.chen@yuneec.com","password":"a1234567890"}
        payload = json.dumps(payload)
        r = requests.post(url,data=payload)
        self.result = r.json()
        self.assertEqual(self.result["message"],"10000")
        getUserInfo_test.token= (self.result["data"])["token"]
        print(getUserInfo_test.token)
        return ((self.result["data"])["token"])



    def test_completeUserInfo_SUCCESS(self):

        """ 成功"""

        print(getUserInfo_test.token)
        payload = {"token":getUserInfo_test.token}
        payload = json.dumps(payload)
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result["message"], "10000")
        self.assertEqual(self.result["status"], "success")

    def test_completeUserInfo_tokenERROR1(self):

        """ token 为空"""

        print(getUserInfo_test.token)
        payload = {"token":" "}
        payload = json.dumps(payload)
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result["message"], "10003")
        self.assertEqual(self.result["status"], "error")

    def test_completeUserInfo_tokenERROR2(self):

        """ token 错误 """

        print(getUserInfo_test.token)
        payload = {"token":getUserInfo_test.token+"q"}
        payload = json.dumps(payload)
        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result["message"], "10005")
        self.assertEqual(self.result["status"], "error")







if __name__ == "__main__":
    unittest.main()


