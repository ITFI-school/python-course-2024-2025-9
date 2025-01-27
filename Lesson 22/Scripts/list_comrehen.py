# Можно создать список целых чисел от 1 до 5, добавляя их туда по одному за раз:
number_list = []
number_list.append(1)
number_list.append(2)
number_list.append(3)
number_list.append(4)
number_list.append(5)
print(number_list)

# Или же вы можно использовать итератор с функцией range():
number_list = []
for number in range(1, 6):
    number_list.append(number)
print(number_list)

# Можно даже преобразовать в список сам результат работы функции range():
number_list = list(range(1, 6))
print(number_list)

# Более характерным для Python является создание списка с помощью включения списка
# т.е. list comprehension:
number_list = [number for number in range(1,6)]
print(number_list)

# Включение списка может содержать условное выражение
odd_list = [number for number in range(1,6) if number % 2 != 0]
print(odd_list)

# Такое включение выглядит более компактно, чем его алгоритмический аналог:
odd_list = []
for number in range(1,6):
    if number % 2 != 0:
        odd_list.append(number)
print(odd_list)

input("\n\nДля выхода нажмите Enter.")
