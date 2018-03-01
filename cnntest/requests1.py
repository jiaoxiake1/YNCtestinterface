#!/usr/bin/env python

import requests
import pprint

host = "http://139.196.43.67:8080/"
endpoint = "login"


url = "".join([host,endpoint])
url1 = "http://www.baidu.com"

r = requests.get(url1)

print(r.cookies)
print("------------------")
pprint.pprint(r.text)
print("------------------")
d = requests.utils.dict_from_cookiejar(r.cookies) #jar包转换为字典

print(d)

print({a.name:a.value for a in r.cookies})