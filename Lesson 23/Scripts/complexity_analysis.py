# Примеры функций для анализа вычислительной сложности приведенных в них алгоритмов

def print_all(n):
    """ (int) -> NoneType
    Печатает целые числа от 1 до n включительно
    """
    for i in range(1, n + 1):
        print(i)

def print_odd(n):
    """ (int) -> NoneType
    Печатает нечетные значения от 1 to n, включительно
    """
    for i in range(1, n + 1, 2):
        print(i)

def print_pairs(n):
    """ (int) -> NoneType
    Печатает все комбинации пар чисел от 1 до n включительно
    """
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(i, j)

def print_dbl_step(n):
    """ (int) -> NoneType
    Печатает числа от 1 до N включительно с начальным шагом 1, увеличивая шаг в 2 раза с каждой итерацией
    """
    i = 1
    while i < n + 1:
        print(i)
        i = i * 2
