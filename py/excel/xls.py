# -*- coding:utf-8 -*-
import xlsxwriter,xlrd

fname = 'test.xlsx'
data = xlrd.open_workbook(fname)
print(data.sheet_names())

table = data.sheet_by_index(0)
nrows = table.nrows
ncols = table.ncols
print(nrows)
print(ncols)
print(table.row_values(0))
print(table.row_values(1))


workbook = xlsxwriter.Workbook('zm6.xlsx')  #创建一个excel文件
worksheet = workbook.add_worksheet('asd')        #创建一个工作表对象
worksheet.set_column(0,ncols,12)            #设定列的宽度为22像素
worksheet.write(1,1,'asdf')
workbook.close()