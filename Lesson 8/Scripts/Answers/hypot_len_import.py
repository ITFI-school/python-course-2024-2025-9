import math
import triangle

# Программа вычисляет длину гипотенузы прямоугольного треугольника,
# запрашивая длины его катетов у пользователя

try:
    leg1_len = float(input("Введите длину 1-го катета: "))
    leg2_len = float(input("Введите длину 2-го катета: "))

    hypot_len = triangle.calc_hypot(leg1_len, leg2_len)
    print("Длина гипотенузы равна", hypot_len)
except ValueError as err:
    print("Ошибка ввода данных:", err, "\nНужно вводить действительные числа")
