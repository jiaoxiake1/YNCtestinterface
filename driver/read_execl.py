#!/usr/bin/env python

import xlrd

class XLDatainfo(object):
    def __init__(self,path=""):
        self.xl = xlrd.open_workbook(path)

    def get_sheetinfo_by_name(self,sheetname):
        self.sheet = self.xl.sheet_by_name(sheetname)
        return self.get_sheet_info()

    def get_sheet_info(self):
        infolist = []
        for row in range(0,self.sheet.nrows):
            info = self.sheet.row_values(row)
            # print(info)
            # print("-"*100)
            infolist.append(info)
        return infolist

if __name__ == "__main__":
    filepath = r'E:\python_lianxi\webinterface\YNCtestinterface\test_data\test1_login_test_data.xlsx'
    datainfo = XLDatainfo(filepath)
    alldata = datainfo.get_sheetinfo_by_name('test1')
    print(alldata)