import openpyxl
"""
# открываем рабочую книгу Excel из файла и выбираем активный лист
wb_formulas = openpyxl.load_workbook('writeFormula.xlsx')
sheet = wb_formulas.active

# печатаем формулу из ячейки A3
print(sheet['A3'].value)
# '=SUM(A1:A2)'
"""
# печатаем данные из ячейки A3
wb_data = openpyxl.load_workbook('writeFormula.xlsx', data_only=True)
sheet = wb_data.active
print(sheet['A3'].value)
# 500

input("\nДля выхода нажмите Enter.")
