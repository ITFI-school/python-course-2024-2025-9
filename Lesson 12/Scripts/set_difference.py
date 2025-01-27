# Первое множество set_1
set_1 = {1, 2, 3, 4}
# Отображаем содержимое множества
print("Множество #1:", set_1)
# Второе множество set_2
set_2 = {3, 4, 5, 6}
# Отображаем содержимое множества
print("Множество #2:", set_2)

# Разность множеств через "-"
diff_set = set_1 - set_2
# Проверяем результат
print("Результат разности diff_set = set_1 - set_2:", diff_set)

# Разность множеств через difference()
print("Множество set_1.difference(set_2):", set_1.difference(set_2))
print("Множество set_2.difference(set_1):", set_2.difference(set_1))

# Обновляем множество set_1 множеством set_2 c их разностью
set_1.difference_update(set_2)
# Проверяем результат
print("Множество set_1.difference_update(set_2):", set_1)

# Изменяем множество 2
set_2 = set_2 - { 4, 6, 8, 10 }
# Проверяем результат
print("Множество set_2 после вычитания {4, 6, 8, 10}:", set_2)

# Изменяем множество intersect_set
diff_set -= {1, 3, 5}
# Проверяем результат
print("Множество diff_set -= {1, 3, 5}:", diff_set)

# Проверим, что множества set_2 и diff_set несвязные, то же, то и метод isdisjoint()
print("Множество set_2 != diff_set:", set_2 != diff_set)

input("\n\nДля выхода нажмите Enter.")
