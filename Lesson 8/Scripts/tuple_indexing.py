# Демонстрация работы с кортежами через индексацию с помощью констант

MANUFACTURER, MODEL, SEATING = (0, 1, 2)       # множественное присваивание констант
MINIMUM, MAXIMUM = (0, 1)

# объявление структуры для хранения данных по самолету
aircraft = ("Airbus", "A320-200", (100, 220))

# использование читаемых индексов для адресации в кортеже - сравните с aircraft[2][1]
print("Tuple indexing with constants:", aircraft[SEATING][MAXIMUM])

input("\nPress enter to exit")
