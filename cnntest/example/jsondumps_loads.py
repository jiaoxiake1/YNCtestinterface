#!/usr/bin/env python


# json.dumps : dict转成str
# json.loads:str转成dict

import json

dict_ = {1:2, 3:4, "55":"66"}

# test json.dumps

print(type(dict_), dict_)
json_str = json.dumps(dict_)
print("json.dumps(dict) return:")
print(type(json_str), json_str)

# test json.loads
print("\njson.loads(str) return")
dict_2 = json.loads(json_str)
print (type(dict_2), dict_2)


