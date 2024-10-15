val_1 = input("Введите первое значение: ")
val_2 = input("Введите второе значение: ")

try:
    result = float(val_1) + float(val_2)
except ValueError:
    result = val_1 + val_2

print("Полученный результат: ", result)

input("\n\nНажмите Enter для выхода")
