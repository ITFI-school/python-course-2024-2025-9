﻿# Демонстрация функций reversed(), sorted() для работы с итерабельными объектами.
# Для примера взят список

lst5 = list(range(6))
print("Список:", lst5)

# reversed() возвращает итератор, который позволяет выполнить обход элементов
# заданного итератора в обратном порядке
lst5_rev = list(reversed(lst5))
print("Перевернутый список:", lst5_rev)

x_list = [-10, 0, 1, -9, 2, 3, -8, 4, 5, -7, 6, 7, -6, 8, 9]
print("\nСписок: ", x_list)

print("sorted():", sorted(x_list))
print("sorted( ,reverse=True ):", sorted(x_list, reverse=True))
print("sorted( ,key=abs ):", sorted(x_list, key=abs))

# Сортировка может применяться только к коллекциям, все элементы которых могут сравниваться друг с другом:
print("Правильная сортировка:", sorted([3, 8, -7.5, 0, 1.3])) # вернет: [-7.5, 0, 1.3, 3, 8]
try:
    sorted([3, "spinner", -7.5, 0, 1.3])
except TypeError as err:
    print("Словили TypeError: ", err)    

# Если необходимо отсортировать список, содержащий целые числа, числа с плавающей точкой и строки, 
# представляющие числа, можно передать в аргументе key вызова sorted() функцию float
print("Сортировка разнотипных данных с числовой информацией:",
	  sorted(["1.3", -7.5, "5", 4, "-2.4", 1], key=float))

input("\n\nДля выхода нажмите Enter.")
