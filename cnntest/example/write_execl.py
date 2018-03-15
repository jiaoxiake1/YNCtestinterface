#!/usr/bin/env python

import xlsxwriter

# 创建excel 和sheet
workbook = xlsxwriter.Workbook(r"E:\python_lianxi\webinterface\YNCtestinterface\test_data\test_data.xlsx")
worksheet = workbook.add_worksheet('test6')
# 特定单元格写入
#
worksheet.write('A1','乔巴软件测')
worksheet.write(1,0,'乔巴软件A2')
workbook.close()

# if __name__ == "__main__":
#     filepath = r'E:\python_lianxi\webinterface\YNCtestinterface\test_data\test1_login_test_data.xlsx'