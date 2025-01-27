# Программа демонстрирует чтение данных из JSON-файла в словарь

import json

file_handler = open("dict.json", encoding="UTF8")
data = json.load(file_handler)
file_handler.close()

print("Удивительно, но тип данных переменной data:", type(data))

print("\nДавайте переведём несколько слов:")
print("Перевод на русский слова 'OK' - ", data["OK"])
print("Перевод на русский слова 'Monday' - ", data["Monday"])
print("Перевод на русский слова 'plenty' - ", data["plenty"])

print("\nКоличество терминов в словаре:", len(data))
input("Если готовы увидеть их все, нажмите Enter.")
print(data)

input("\n\nДля выхода нажмите Enter.")
