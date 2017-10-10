#Script allows you to read data from a spreadsheet
#Gerald McAuley 2017
#!!Important!!
#Spreadsheet must be locatedin the same directory as the python file
import xlrd

xl_workbook = xlrd.open_workbook('sheet.xls')#insert name of your spreadsheet here

#Selects a specific page in spredsheet
xl_sheet = xl_workbook.sheet_by_index(1)

print ('Sheet name: %s' % xl_sheet.name)

#Retrieve data from specific column/row
col= xl_sheet.col(9)
urlFile = open("urlFile.txt", "w")

for x in range(9, 10):
    for i in range(1, 101):
        cell_value = xl_sheet.cell(i, x).value

        print(cell_value)

