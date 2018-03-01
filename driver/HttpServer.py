#!/usr/bin/env python

import requests
from driver import config
import json
# import pprint
#
class MyHTTP(object):

    def __init__(self):
        self.url =config.url()


    def get(self,url,**DataALL):
        params = DataALL.get("params")
        headers = DataALL.get("headers")
        r = requests.get(url,params=params,headers=headers)
        text = r.json()
        return text

    # def post(self,**DataALL):
    def post(self,url,**DataALL):
        params = DataALL.get("params")
        headers = DataALL.get("headers")
        data = DataALL.get("data")
        json = DataALL.get("json")
        files = DataALL.get("files")
        print(self.url)
        try:

        # resp = requests.post(self.url,params=params,headers=headers,data=data,json=json,files=files)
            resp = requests.post(url,params=params,headers=headers,data=data,json=json,files=files)
            text = resp.json()
            return text
        except Exception as e:
            print("post 错误:s%"%e)
