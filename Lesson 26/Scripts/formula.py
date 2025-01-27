import openpyxl

# создаем новую рабочую книгу Excel
wb = openpyxl.Workbook()

# выбираем 1-ый активный лист
sheet =	wb.active

# вносим в 2 ячейки обычные данные
sheet['A1'] = 200
sheet['A2'] = 300

# вносим в 3-ю ячейку формулу
sheet['A3'] = '=SUM(A1:A2)'

# сохраняем рабочую книгу Excel
wb.save('writeFormula.xlsx')

print("Записан файл:", 'writeFormula.xlsx')
input("\nДля выхода нажмите Enter.")
