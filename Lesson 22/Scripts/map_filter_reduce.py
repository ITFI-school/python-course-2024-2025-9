# Демонстрация общеизвестных техник функционального програмирования:
# 1) отображения, map
# 2) фильтрация, filter
# 3) упрощение, reduce

# 1. отображение - map
list(map(lambda x: x ** 2, [1, 2, 3, 4])) # вернет: [1, 4, 9, 16]
# то же самое с помощью генератора списка
[x ** 2 for x in [1, 2, 3, 4]]   # списочное выражение (list comprehension) 
# то же самое средствами императивного программирования
seq = [1, 2, 3, 4]
for i in range(len(seq)):
    seq[i] = seq[i] ** 2

# 2. фильтрация - filter
list(filter(lambda x: x > 0, [1, -2, 3, -4])) # вернет: [1, 3]
# то же самое с помощью генератора списка с условием
[x for x in [1, -2, 3, -4] if x > 0]
# то же самое средствами императивного программирования
seq_initial = [1, -2, 3, -4]
seq_result = []
for elem in seq_initial:
    if elem > 0:
        seq_result.append(elem)

# 3. упрощение - reduce
import functools
import operator
functools.reduce(lambda x, y: x * y, [1, 2, 3, 4]) # вернет: 24
# то же самое с использованием системной функции для умножения
functools.reduce(operator.mul, [1, 2, 3, 4])
# то же самое средствами императивного программирования
result = 1
seq_data = [1, 2, 3, 4]
for elem in seq_data:
    result *= elem
