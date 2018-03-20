#!/usr/bin/env python
import xlrd,xlwt
from xlutils.copy import copy
import os
import random,string

class XLDataInsert(object):

    def __init__(self,path,insert_text):
        self.path = path
        self.insert_text = insert_text
        self.x1 = xlrd.open_workbook(path,formatting_info=True,)# formatting_info copy 后保存原来的execl 格式


    def insertData_by_sheetname(self,sheetname,row):
        self.sheet_old = self.x1.sheet_by_name(sheetname)
        # self.rows = self.sheet_old.nrows
        # print(self.rows)
        self.cols = self.sheet_old.ncols
        # print(self.cols)
        self.new_xl = copy(self.x1)
        self.sheet = self.new_xl.get_sheet(sheetname)
        # self.cols = self.sheet.ncols
        # self.rows = self.sheet_old.nrows
        self.insertData(row)

        self.new_xl.save(self.path)

    # #写入连续的几行
    # def insertDataLines(self,rows):
    #
    #     for row in range(1,rows):
    #         col = 0
    #         while(col<3):
    #             if col == 0:
    #                 self.sheet.write(row, col, self.insert_text[col])
    #             elif col == 1:
    #                 self.sheet.write(row, col, self.insert_text[col])
    #             elif col == 2:
    #                 self.sheet.write(row, col, self.insert_text[col])
    #             else:
    #                 break





    #写入固定一行
    def insertData(self,row):

        for i in range(0,self.cols):

            if i == 0:
                self.sheet.write(row,i,self.insert_text[i])
            elif i == 1:
                self.sheet.write(row, i, self.insert_text[i])
            elif i == 2:
                self.sheet.write(row, i, self.insert_text[i])




# old_xl = xlrd.open_workbook(r'E:\python_lianxi\webinterface\YNCtestinterface\test_data\test_data1.xls')
#
# sheet = old_xl.sheet_by_name("test2")
# rows = sheet.nrows
# cols = sheet.ncols
# print(rows)
# print(cols)
#
# new_xl = copy(old_xl)
#
# sheet = new_xl.get_sheet("test2")
# sheet.write(rows,0,"sss")
# sheet.write(rows,1,"ttt")
# new_xl.save(r'E:\python_lianxi\webinterface\YNCtestinterface\test_data\test_data2.xls')





if __name__ == "__main__":
    base_path = os.path.dirname(os.path.dirname(__file__))
    base_path = base_path.replace('\\', '/')
    file_path = base_path + "/test_data/"
    print(file_path)
    os.chdir(file_path)
    #
    print(os.getcwd())
    filepath = os.getcwd()+"\\test_data1.xls"
    print(filepath)
    # filepath = r'E:\python_lianxi\webinterface\YNCtestinterface\test_data\test_data1.xls'
    # description = "hello description!!"
    username = ''.join(random.sample(string.ascii_letters + string.digits, 8))
    username = username + "@yuneec.com"
    username_json = str({"json": {"username": username, "password": "a1234567890"}})

    exceptResult_json = str({"code": "10000", "status": "success"})
    discription = "申请用户名成功"
    # insertArr = {"username_json":username_json,"exceptResult_json":exceptResult_json,"discription":discription}
    insertArr = [username_json, exceptResult_json, discription]
    print(insertArr)
    print(type(insertArr))
    print(type(insertArr[0]))
    print(insertArr[0])
    datainfo = XLDataInsert(filepath,insertArr).insertData_by_sheetname("test1",13)
