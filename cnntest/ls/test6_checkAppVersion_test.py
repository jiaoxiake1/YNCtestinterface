#!/usr/bin/env python

import unittest
import requests
import json
from driver import myunit

"""platfrom 码错误  和  version 码格式错误 """

class checkAppVersiontest(myunit.MyTest):

    """检测App版本是否需要更新"""

    base_url = myunit.MyTest.base_url + "checkAppVersion"

    def test_checkAppVersion_SUCCESS(self):

        """ 检测成功  有可用版本" 只是检测是否有版本并
        返回最新版本信息，并不对比是否可以需要更新"""

        payload = {"platform":"1","version":"13"}
        payload = json.dumps(payload)

        r = requests.post(self.base_url,data=payload)
        self.result = r.json()
        self.assertEqual(self.result["message"],"10000")
        self.assertEqual(self.result["status"],"success")

    def test_checkAppVersion_platformNULL(self):
        """ platform 为空"""

        payload = {"platform": " ", "version": "13"}
        payload = json.dumps(payload)

        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result["message"], "10602")
        self.assertEqual(self.result["status"], "error")


    def test_checkAppVersion_appversionNULL(self):
        """ 版本 为空"""

        payload = {"platform": "1", "version": " "}
        payload = json.dumps(payload)

        r = requests.post(self.base_url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result["message"], "10603")
        self.assertEqual(self.result["status"], "error")

    # def test_checkAppVersion_appversionLastest(self):
    #     """ 版本已经是最新的   。现在接口只是返回服务器最新的版本号，
        # 并没有和我请求的版本号做对比"""
    #
    #     payload = {"platform":"1","version":"23"}
    #     payload = json.dumps(payload)
    #
    #     r = requests.post(self.base_url, data=payload)
    #     self.result = r.json()
    #     self.assertEqual(self.result["message"], "10606")
    #     self.assertEqual(self.result["status"], "error")




if __name__ == "__main__":
    unittest.main()


