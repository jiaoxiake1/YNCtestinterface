#!/usr/bin/env python

import xlrd
from xlutils.copy import copy
from driver.base import login_token
import random,string

xl = xlrd.open_workbook("test.xls")
new_xl = copy(xl)
new_sheet = new_xl.get_sheet("test1")
l = [1,2,3,4,5,6,7]
s = [["nihao0","00","tt"],["haha1","11","12"],["dddd2","22","13"]]
# print(len(l))
# print(len(s))
print(s)




for row in range(len(s)):
    cols = 0
    while(cols<3):
        new_sheet.write(row+1,cols,s[row][cols])
        print("*"*100)
        print(row,cols)
        print(s[row][cols])
        print("_" * 100)
        cols = cols+1

new_xl.save("testnew.xls")



# token = login_token()
# t = ''.join(random.sample(string.ascii_letters + string.digits, 8))
# print(t)
# print(token)




# print(random.random()) # 返回0<=n<1 之间的随机数

# print(random.choice([1,2,3,4,5])) # 从序列中返回随机元素（序列有两种：tuple，list）
# print(random.choice((1,2,3,4,5,6)))

# print(random.sample([1,2,3,4,5],4)) # 从序列中随机取n个元素（序列有两种：tuple，list）
# print(random.sample((1,2,3,4,5),4)) #返回的是list ，不是元组

# print(random.getrandbits(k)) #返回不大于k 位的长整型数(10进制)

# print(random.shuffle([])) #将序列的所有元素随机排序 （序列有两种：tuple，list）








