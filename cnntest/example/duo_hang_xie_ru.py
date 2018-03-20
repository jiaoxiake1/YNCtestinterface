#!/usr/bin/env python

import xlrd
from xlutils.copy import copy

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









