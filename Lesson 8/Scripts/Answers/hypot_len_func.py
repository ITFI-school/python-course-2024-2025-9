import math

# Программа вычисляет длину гипотенузы прямоугольного треугольника,
# запрашивая длины его катетов у пользователя

def calc_hypot(side_1, side_2):
    ''' (number, number) -> number

    Calculate a triangle hypotenuse taking the lengths of 2 sides

    Precondition: side_1 and side_2 must be positive, otherwise -> 0
    
    '''
    if side_1 <= 0 or side_2 <= 0:
        return 0

    hyp_len = math.sqrt(side_1**2 + side_2**2)
    return hyp_len


try:
    leg1_len = float(input("Введите длину 1-го катета: "))
    leg2_len = float(input("Введите длину 2-го катета: "))

    hypot_len = calc_hypot(leg1_len, leg2_len)
    print("Длина гипотенузы равна", hypot_len)
except ValueError as err:
    print("Ошибка ввода данных:", err, "\nНужно вводить действительные числа")
