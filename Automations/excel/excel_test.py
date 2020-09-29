import openpyxl

wb = openpyxl.load_workbook("data.xlsx")
sheet = wb.get_sheet_by_name("Sheet1")
print(sheet)