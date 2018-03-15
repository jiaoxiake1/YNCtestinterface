import xlwt
import xlrd
from xlutils.copy import copy

oldWB = xlrd.open_workbook("test.xls")

newWb = copy(oldWB)
sheet = newWb.get_sheet(0)
sheet.write(3,3,"sss")
newWb.save("new.xls")