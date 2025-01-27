# Скрипт демонстрирует разработку ФУНКЦИИ ВЫСШЕГО ПОРЯДКА apply(), 
# которая может принимать другую функцию как аргумент

def apply(func, number1, number2):
    """(func, number1, number2)
    Возвращает результат вызова func для чисел number1 и number2
    """
    return func(number1, number2)

print("apply() for max():", apply(max, 1, 2))

def num_action(x, y):
    return x - 2 * y

print("apply() for num_action():", apply(num_action, 100, 10))

input("\n\nДля выхода нажмите Enter.")
