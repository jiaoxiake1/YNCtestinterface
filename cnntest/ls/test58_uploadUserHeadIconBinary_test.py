#!/usr/bin/env python

import unittest
import json
import requests
from driver import base,myunit


class uploadUserHeadIconBinarytest(myunit.MyTest):

    """上传用户头像"""

    base_url = myunit.MyTest.base_url+"uploadUserHeadIconBinary"
    token = []

    def test1_login(self):

        "先登录 获取token"

        url = myunit.MyTest.base_url + "login"
        payload = {"username":"nn.chen@yuneec.com","password":"1234567890a"}
        payload = json.dumps(payload)
        r = requests.post(url,data=payload)
        self.result = r.json()
        self.assertEqual(self.result["message"],"10000")
        uploadUserHeadIconBinarytest.token= (self.result["data"])["token"]
        print(uploadUserHeadIconBinarytest.token)
        return ((self.result["data"])["token"])

    def test_uploadUserHeadIconBinary_SUCCESS1(self):

        """png  成功"""
        token = uploadUserHeadIconBinarytest.token
        params = {"token": token, "fileType": "png"}
        url = uploadUserHeadIconBinarytest.base_url
        with open(r"E:\python_lianxi\webinterface\YNCtestinterface\report\image\12.png","rb") as f:
            p=requests.post(url,params=params,data=f)
            self.result = p.json()
        self.assertEqual(self.result["message"],"10000")
        self.assertEqual(self.result["status"],"success")

    def test_uploadUserHeadIconBinary_SUCCESS3(self):

        """png  成功"""
        token = uploadUserHeadIconBinarytest.token
        params = {"token":token,"fileType":"png"}
        # url = uploadUserHeadIconBinarytest.base_url+tokens+fileTypes
        url = uploadUserHeadIconBinarytest.base_url
        with open(r"E:\python_lianxi\webinterface\YNCtestinterface\report\image\12.png","rb") as f:
            p=requests.post(url,params = params,data=f)
            self.result = p.json()
        self.assertEqual(self.result["message"],"10000")
        self.assertEqual(self.result["status"],"success")

    def test_uploadUserHeadIconBinary_SUCCESS2(self):

        """jpg 成功(这个有问题，返回还是png 格式的)"""

        token = uploadUserHeadIconBinarytest.token
        params = {"token": token, "fileType": "png"}
        url = uploadUserHeadIconBinarytest.base_url
        with open(r"E:\python_lianxi\webinterface\YNCtestinterface\report\image\8.bmp","rb") as f:
            p=requests.post(url,params=params,data=f)
            self.result = p.json()
        self.assertEqual(self.result["message"],"10001")
        self.assertEqual(self.result["status"],"success")

    def test_uploadUserHeadIconBinary_tokenERROR1(self):

        """token 错误"""

        token = uploadUserHeadIconBinarytest.token+"w"
        params = {"token": token, "fileType": "png"}
        url = uploadUserHeadIconBinarytest.base_url
        with open(r"E:\python_lianxi\webinterface\YNCtestinterface\report\image\8.bmp","rb") as f:
            p=requests.post(url,params=params,data=f)
            self.result = p.json()
        self.assertEqual(self.result["message"],"10005")
        self.assertEqual(self.result["status"],"error")

    def test_uploadUserHeadIconBinary_tokenERROR2(self):

        """token 为空"""

        token = ""
        params = {"token": token, "fileType": "png"}
        url = uploadUserHeadIconBinarytest.base_url
        with open(r"E:\python_lianxi\webinterface\YNCtestinterface\report\image\8.bmp","rb") as f:
            p=requests.post(url,params=params,data=f)
            self.result = p.json()
        self.assertEqual(self.result["message"],"10003")
        self.assertEqual(self.result["status"],"error")


if __name__ == "__main__":
    unittest.main()





