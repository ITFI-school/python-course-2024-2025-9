def linear_search(items, value):
    """ (list, object) -> int

    Возвращает индекс первого вхождения value в список items или -1,
    если значение value в этом списке не найдено.

    Предусловие: все элементы списка должны иметь такой тип,
                 который может сравниваться с value

    >>> linear_search([2, 3, 5, 3], 2)
    0
    >>> linear_search([2, 3, 5, 3], 5)
    2
    >>> linear_search([2, 3, 5, 3], 8)
    -1
    """

    i = 0

    while i != len(items) and value != items[i]:
        i = i + 1

    if i == len(items):
        return -1
    else:
        return i
