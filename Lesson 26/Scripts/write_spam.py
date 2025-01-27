import openpyxl

wb = openpyxl.load_workbook('example.xlsx')
sheet = wb.active

sheet.title = 'Spam Spam Spam'
wb.save('example_copy.xlsx')

input("\nДля выхода нажмите Enter.")
