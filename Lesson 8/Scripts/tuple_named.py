# Демонстрация работы с кортежами: использование namedtuple

from collections import namedtuple

# Sale - имя типа создаваемого кортежа
# Второй аргумент – это строка имен, разделенных пробелами,
# для каждого элемента, который будет присутствовать в кортеже
Sale = namedtuple("Sale", "productid customerid date quantity price")

# создадим список из двух элементов типа Sale, то есть из двух именованных кортежей
sales = []
sales.append(Sale(432, 921, "2017-09-14", 3, 7.99))
sales.append(Sale(419, 874, "2017-09-15", 1, 18.49))

total = 0
for sale in sales:
    print(sale)
    total += sale.quantity * sale.price
print("Total ${0:.2f}".format(total)) # выведет: Total $42.46

# версия из tuple_indexing.py, реализованная через именованные кортежи
Aircraft = namedtuple("Aircraft", "manufacturer model seating")
Seating = namedtuple("Seating", "minimum maximum")

# объявление структуры для хранения данных по самолету
aircraft = Aircraft("Airbus", "A320-200", Seating(100, 220)) 

# использование читаемых индексов для адресации в кортеже,
# сравните с aircraft[SEATING][MAXIMUM] или с aircraft[2][1]
print("Tuple indexing with names:", aircraft.seating.maximum)

input("\nPress enter to exit")

