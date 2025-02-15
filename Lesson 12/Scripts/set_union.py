﻿# Первое множество set_1
set_1 = {1, 2, 3, 4}
# Отображаем содержимое множества
print("Множество #1:", set_1)
# Второе множество set_2
set_2 = {3, 4, 5, 6}
# Отображаем содержимое множества
print("Множество #2:", set_2)

# Объединение множеств через |
union_set = set_1 | set_2
# Проверяем результат
print("Результат объединения union_set = set_1 | set_2:", union_set)

# Объединение множеств через union()
print("Множество set_1.union(set_2):", set_1.union(set_2))
print("Множество set_2.union(set_1):", set_2.union(set_1))

# Обновляем множество set_1 множеством set_2 с их объединением
set_1.update(set_2)
# Проверяем результат
print("Множество set_1.update(set_2):", set_1)

# Изменяем множество 
set_2 = set_2 | { -1, -2, -3 }
# Проверяем результат
print("Множество set_2 после объединения с {-1, -2, -3}:", set_2)

# Изменяем множество union_set
union_set |= {7, 8, 9}
# Проверяем результат
print("Множество union_set |= {7, 8, 9}:", union_set)

input("\n\nДля выхода нажмите Enter.")
