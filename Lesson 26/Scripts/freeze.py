import openpyxl

# открываем рабочую книгу Excel из файла и выбираем активный лист
wb = openpyxl.load_workbook('produceSales.xlsx')
sheet = wb.active

# замораживаем 1-ую строку
sheet.freeze_panes = 'A2'

# сохраняем рабочую книгу Excel
wb.save('freezeExample.xlsx')

print("Записан файл:", 'freezeExample.xlsx')
input("\nДля выхода нажмите Enter.")
