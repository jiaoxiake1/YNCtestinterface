#!/usr/bin/env python

import unittest
import requests
import json
from driver import myunit

"""分页问题  ； vedio没有传分页数，Status = success,返回页码错误"""

class helpManualtest(myunit.MyTest):

    """获取产品使用手册"""

    base_url = myunit.MyTest.base_url + "helpManual"

    def test_helpManual_Video_Success1(self):

        """ VIDEO  中文 获取成功"""

        payload = {"productName":"Firebird","fileType":"video",
                   "language":"zh-cn","pageNo":"1"}
        payload = json.dumps(payload)

        r = requests.post(self.base_url,data=payload)
        self.result = r.json()
        self.assertEqual(self.result["status"],"success")
        self.assertEqual(self.result["message"], "10000")

    def test_helpManual_Video_Success2(self):

        """ pdf  英文 获取成功"""

        payload = {"productName":"Firebird","fileType":"pdf",
                   "language":"en-us","pageNo":"1"}
        payload = json.dumps(payload)

        r = requests.post(self.base_url,data=payload)
        self.result = r.json()
        self.assertEqual(self.result["status"],"success")
        self.assertEqual(self.result["message"], "10000")


    def test_helpManual_Video_Success3(self):

        """ productName language 为空  获取成功 """

        payload = {"productName":"","fileType":"video",
                   "language":"","pageNo":"1"}
        payload = json.dumps(payload)

        r = requests.post(self.base_url,data=payload)
        self.result = r.json()
        self.assertEqual(self.result["status"],"success")
        self.assertEqual(self.result["message"], "10000")


    def test_helpManual_Video_filetypeERROR1(self):

        """  filetype 为空  """

        payload = {"productName":"Firebird","fileType":"",
                   "language":"zh-cn","pageNo":"1"}
        payload = json.dumps(payload)

        r = requests.post(self.base_url,data=payload)
        self.result = r.json()
        self.assertEqual(self.result["status"],"error")
        self.assertEqual(self.result["message"], "10702")


    def test_helpManual_Video_filetypeERROR2(self):

        """  有问题 filetype 格式错误 ，返回找不到文件 """

        payload = {"productName":"Firebird","fileType":"xxxx",
                   "language":"zh-cn","pageNo":"1"}
        payload = json.dumps(payload)

        r = requests.post(self.base_url,data=payload)
        self.result = r.json()
        self.assertEqual(self.result["status"],"success")
        self.assertEqual(self.result["message"], "10009")


    def test_helpManual_Video_NOfile1(self):

        """  页数太大导致 ， 没有此文档 """

        payload = {"productName":"Firebird","fileType":"video",
                   "language":"zh-cn","pageNo":"100"}
        payload = json.dumps(payload)

        r = requests.post(self.base_url,data=payload)
        self.result = r.json()
        self.assertEqual(self.result["status"],"success")
        self.assertEqual(self.result["message"], "10706")

    def test_helpManual_Video_NOfile2(self):

        """  没有 productName 导致 ， 没有此文档 """

        payload = {"productName":"xxx ","fileType":"video",
                   "language":"zh-cn","pageNo":"1"}
        payload = json.dumps(payload)

        r = requests.post(self.base_url,data=payload)
        self.result = r.json()
        self.assertEqual(self.result["status"],"success")
        self.assertEqual(self.result["message"], "10009")

    def test_helpManual_Video_NOfile3(self):

        """  没有 language 导致 ， 没有此文档 """

        payload = {"productName":"Firebird ","fileType":"video",
                   "language":"xxxx","pageNo":"1"}
        payload = json.dumps(payload)

        r = requests.post(self.base_url,data=payload)
        self.result = r.json()
        self.assertEqual(self.result["status"],"success")
        self.assertEqual(self.result["message"], "10009")


    def test_helpManual_Video_pageERROR1(self):

        """  pageNo < 0  """

        payload = {"productName":"Firebird ","fileType":"video",
                   "language":"","pageNo":"-1"}
        payload = json.dumps(payload)

        r = requests.post(self.base_url,data=payload)
        self.result = r.json()
        self.assertEqual(self.result["status"],"error")
        self.assertEqual(self.result["message"], "10707")

    def test_helpManual_Video_pageERROR2(self):

        """  pageNo = 0  """

        payload = {"productName":"Firebird ","fileType":"video",
                   "language":"","pageNo":"0"}
        payload = json.dumps(payload)

        r = requests.post(self.base_url,data=payload)
        self.result = r.json()
        self.assertEqual(self.result["status"],"error")
        self.assertEqual(self.result["message"], "10707")


    def test_helpManual_Video_pageERROR3(self):

        """  pageNo 为不规则字符"""

        payload = {"productName":"Firebird ","fileType":"video",
                   "language":"","pageNo":"xxxxx"}
        payload = json.dumps(payload)

        r = requests.post(self.base_url,data=payload)
        self.result = r.json()
        self.assertEqual(self.result["status"],"error")
        self.assertEqual(self.result["message"], "10707")






if __name__ == "__main__":
    unittest.main()


