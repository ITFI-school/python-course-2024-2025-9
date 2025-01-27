import openpyxl

# создаем новую рабочую книгу Excel и выбираем активный лист
wb = openpyxl.Workbook()
sheet =	wb.active

sheet['A1'] = 'Высокая строка'
sheet['B2'] = 'Широкий столбец'

# задаем высоту строки в пунктах
sheet.row_dimensions[1].height = 70

# задаем ширину колонки в шагах шрифта
sheet.column_dimensions['B'].width = 20

# сохраняем рабочую книгу Excel
wb.save('dimensions.xlsx')

print("Записан файл:", 'dimensions.xlsx')
input("\nДля выхода нажмите Enter.")
