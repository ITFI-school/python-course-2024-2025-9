# Первое множество set_1
set_1 = {1, 2, 3, 4}
# Отображаем содержимое множества
print("Множество #1:", set_1)
# Второе множество set_2
set_2 = {3, 4, 5, 6}
# Отображаем содержимое множества
print("Множество #2:", set_2)

# симметрическая разность множеств через "^"
xor_set = set_1 ^ set_2
# Проверяем результат
print("Результат симметрической разности xor_set = set_1 ^ set_2:", xor_set)

# Симметрическая разность множеств через symmetric_difference()
print("Множество set_1.symmetric_difference(set_2):", set_1.symmetric_difference(set_2))
print("Множество set_2.symmetric_difference(set_1):", set_2.symmetric_difference(set_1))

# Обновляем множество set_1 множеством set_2 c их симметрической разностью
set_1.symmetric_difference_update(set_2)
# Проверяем результат
print("Множество set_1.symmetric_difference_update(set_2):", set_1)

# Изменяем множество 2
set_2 = set_2 ^ { 4, 6, 8, 10 }
# Проверяем результат
print("Множество set_2 после симметрической разницы с {4, 6, 8, 10}:", set_2)

# Изменяем множество xor_set
xor_set ^= {1, 3, 5}
# Проверяем результат
print("Множество xor_set ^= {1, 3, 5}:", xor_set)

input("\n\nДля выхода нажмите Enter.")
