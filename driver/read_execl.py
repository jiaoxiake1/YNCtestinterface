#!/usr/bin/env python

import xlrd
import pprint

class XLDatainfo(object):
    def __init__(self,path=""):
        self.xl = xlrd.open_workbook(path)


    #获取整个sheet 的信息
    def get_sheetinfo_by_name(self,sheetname):
        self.sheet = self.xl.sheet_by_name(sheetname)
        # return self.get_sheet_info()
        return self.get_sheet_info()

    def get_sheet_info(self):
        infolist = []
        for row in range(0,self.sheet.nrows):
            info = self.sheet.row_values(row)
            # print(info)
            # print("-"*100)
            infolist.append(info)
        return infolist

    # #获取sheet 某一列的信息
    # def get_sheetinfo_by_name_columns(self,sheetname,column):
    #     self.sheet = self.xl.sheet_by_name(sheetname)
    #     # return self.get_sheet_info()
    #     return self.get_sheet_by_columns(column)
    #
    # def get_sheet_by_columns(self,column):
    #     infolist = []
    #     # for row in range(1,self.sheet.nrows):
    #     #     info = self.sheet.cell_value(row,column)
    #     #     # print(info)
    #     #     # print("-"*100)
    #     #     infolist.append(info)
    #     rows = self.sheet.nrows
    #     # print(rows)
    #     info = self.sheet.col_values(colx=column,start_rowx=1,end_rowx=rows)
    #     # print(info)
    #     # print("-"*1000)
    #     infolist.append(info)
    #     return infolist
    #
    # #获取一列信息，并转换成二位数组
    # def get_sheetinfo_by_name_by_column(self,sheetname,column):
    #     self.sheet = self.xl.sheet_by_name(sheetname)
    #     # return self.get_sheet_info()
    #     return self.get_sheet_by_column(column)
    #
    # def get_sheet_by_column(self,column):
    #     # print(self.sheet.nrows)
    #     infolist = [[] for i in range(self.sheet.nrows-1)]
    #     # print(infolist)
    #     rows = self.sheet.nrows
    #     # print(rows)
    #     infor = self.sheet.col_values(colx=column,start_rowx=1,end_rowx=rows)
    #     for t in range(0,(self.sheet.nrows-1)):
    #         # print(tt)
    #         infolist[t].append(infor[t])
    #         # print(infolist[tt])
    #     return infolist





if __name__ == "__main__":
    filepath = r'E:\python_lianxi\webinterface\YNCtestinterface\test_data\test1_login_test_data.xlsx'
    datainfo = XLDatainfo(filepath)
    # alldata = datainfo.get_sheetinfo_by_name('test1')
    # alldata_column = datainfo.get_sheetinfo_by_name_columns('test1',0)
    # alldata2 = datainfo.get_sheetinfo_by_name_by_column('test1',0)
    # print(alldata)
    # print(alldata_column)
