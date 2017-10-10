import xlrd

xl_workbook = xlrd.open_workbook('sheet.xls')

xl_sheet = xl_workbook.sheet_by_index(1)

print ('Sheet name: %s' % xl_sheet.name)

col= xl_sheet.col(9)
urlFile = open("urlFile.txt", "w")

for x in range(9, 10):
    for i in range(1, 101):
        cell_value = xl_sheet.cell(i, x).value

        print(cell_value)

