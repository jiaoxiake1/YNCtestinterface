#!/usr/bin/env python

import unittest
import json
import requests
from driver import myunit
from driver import base

class sendFeedbacktest(myunit.MyTest):
    """发送用户返回"""

    base_url =myunit.MyTest.base_url+"sendFeedback"

    def test_sendFeedback_success1(self):
        """ firebird 符合规范输入"""
        payload = {"username":"nn.chen@yuneec.com","detail":"ddd",
                   "productName":"firebird","contact":"123455"}
        # self.result = base.Page.baseResquest(self,sendFeedbacktest.base_url,payload)

        self.result = base.Page.baseResquest(self,sendFeedbacktest.base_url, payload)
        self.assertEqual(self.result["status"], "success")
        self.assertEqual(self.result["message"],"10000")

    def test_sendFeedback_success2(self):
        """ breeze 符合规范输入,username 为空"""
        payload = {"username":"nn.chen@yuneec.com","detail":"ddd",
                   "productName":"breeze","contact":"123455"}
        self.result = base.Page.baseResquest(self,sendFeedbacktest.base_url,payload)
        self.assertEqual(self.result["status"], "success")
        self.assertEqual(self.result["message"],"10000")


    def test_sendFeedback_usernameERROR1(self):
        """ username 为空 """
        payload = {"username":"","detail":"ddd",
                   "productName":"breeze","contact":"123455"}
        self.result = base.Page.baseResquest(self,sendFeedbacktest.base_url,payload)
        self.assertEqual(self.result["status"], "error")
        self.assertEqual(self.result["message"],"10105")

    def test_sendFeedback_usernameERROR2(self):
        """ username 格式错误 """
        payload = {"username":"nind@.com","detail":"ddd",
                   "productName":"breeze","contact":"123455"}
        self.result = base.Page.baseResquest(self,sendFeedbacktest.base_url,payload)
        self.assertEqual(self.result["status"], "error")
        self.assertEqual(self.result["message"],"10105")


    def test_sendFeedback_detailERROR(self):
        """ detail 空 """
        payload = {"username":"nn.chen@yuneec.com","detail":"",
                   "productName":"breeze","contact":"123455"}
        self.result = base.Page.baseResquest(self,sendFeedbacktest.base_url,payload)
        self.assertEqual(self.result["status"], "error")
        self.assertEqual(self.result["message"],"14001")


    def test_sendFeedback_productNameERROR1(self):
        """ productName 为空  """
        payload = {"username":"nn.chen@yuneec.com","detail":"1223",
                   "productName":"","contact":"123455"}
        self.result = base.Page.baseResquest(self,sendFeedbacktest.base_url,payload)
        self.assertEqual(self.result["status"], "error")
        self.assertEqual(self.result["message"],"10010")


    def test_sendFeedback_productNameERROR2(self):
        """ productName 输入错误  """
        payload = {"username":"nn.chen@yuneec.com","detail":"1223",
                   "productName":"ddd","contact":"123455"}
        self.result = base.Page.baseResquest(self,sendFeedbacktest.base_url,payload)
        self.assertEqual(self.result["status"], "error")
        self.assertEqual(self.result["message"],"10010")

    def test_sendFeedback_contactERROR(self):
        """ contact  为空  """
        payload = {"username":"nn.chen@yuneec.com","detail":"1223",
                   "productName":"firebird","contact":""}
        self.result = base.Page.baseResquest(self,sendFeedbacktest.base_url,payload)
        self.assertEqual(self.result["status"], "error")
        self.assertEqual(self.result["message"],"11702")



if __name__ == "__main__":
    unittest.main()