#!/usr/bin/env python

import xlsxwriter

# 创建excel 和sheet
workbook = xlsxwriter.Workbook("test.xlsx")
worksheet = workbook.add_worksheet('test')
# 特定单元格写入

worksheet.write('A1','乔巴软件测试')
worksheet.write(1,0,'乔巴软件A2')