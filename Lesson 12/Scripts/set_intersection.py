# Первое множество set_1
set_1 = {1, 2, 3, 4}
# Отображаем содержимое множества
print("Множество #1:", set_1)
# Второе множество set_2
set_2 = {3, 4, 5, 6}
# Отображаем содержимое множества
print("Множество #2:", set_2)

# пересечение множеств через &
intersect_set = set_1 & set_2
# Проверяем результат
print("Результат объединения intersect_set = set_1 & set_2:", intersect_set)

# Пересечение множеств через intersection()
print("Множество set_1.intersection(set_2):", set_1.intersection(set_2))
print("Множество set_2.intersection(set_1):", set_2.intersection(set_1))

# Обновляем множество set_1 множеством set_2 с их пересечением
set_1.intersection_update(set_2)
# Проверяем результат
print("Множество set_1.intersection_update(set_2):", set_1)

# Изменяем множество 2
set_2 = set_2 & { 4, 6, 8, 10 }
# Проверяем результат
print("Множество set_2 после пересечения с {4, 6, 8, 10}:", set_2)

# Изменяем множество intersect_set
intersect_set &= {1, 2, 3}
# Проверяем результат
print("Множество intersect_set &= {1, 2, 3}:", intersect_set)

input("\n\nДля выхода нажмите Enter.")
