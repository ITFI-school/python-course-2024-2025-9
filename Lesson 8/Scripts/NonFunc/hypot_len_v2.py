import math

# Программа вычисляет длину гипотенузы прямоугольного треугольника,
# запрашивая длины его катетов у пользователя

try:
    leg1_len = float(input("Введите длину 1-го катета: "))
    leg2_len = float(input("Введите длину 2-го катета: "))

    hypot_len = math.sqrt(leg1_len**2 + leg2_len**2)
    print("Длина гипотенузы равна", hypot_len)
except ValueError as err:
    print("Ошибка ввода данных:", err, "\nНужно вводить действительные числа")
