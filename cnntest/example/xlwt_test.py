import xlwt
import xlrd
from xlutils.copy import copy

oldWB = xlrd.open_workbook("test.xls")
rows = oldWB.sheet_by_name("test1").nrows
print(rows)
newWb = copy(oldWB)
# sheet = newWb.get_sheet(0)
sheet = newWb.get_sheet("test1")
sheet.write(rows,0,"sss")
sheet.write(rows,1,"kkk")
sheet.write(rows,2,"lll")
sheet.write(rows,3,"ttt")

# sheet.write(3,3,"ttt")
# sheet.write(3,6,"kkk")
newWb.save("test.xls")

