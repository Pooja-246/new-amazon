from xlrd import open_workbook
def read_locators(sheetname):
    wb=open_workbook(r"C:\Users\Archan\Documents\OBJECT.xls")
    ws=wb.sheet_by_name(sheetname)
    used_rows=ws.nrows
    data={}
    for index in range(1,used_rows):
        row=ws.row_values(index)
        data[row[0]]=(row[1],row[2])
    return data
print(read_locators("Sheet1"))