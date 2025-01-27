def binary_search(items, value):
    """ (list, object) -> int

    Возвращает индекс первого вхождения value в список items или -1,
    если значение value в этом списке не найдено.

    Предусловия:
    1) все элементы списка items должны иметь такой тип, который
       может сравниваться с value
    2) список items должен быть отсортирован по возрастанию

    >>> binary_search([2, 3, 5, 7], 2)
    0
    >>> binary_search([2, 3, 5, 5], 5)
    2
    >>> binary_search([2, 3, 5, 7], 8)
    -1
    """

    beg = 0
    end = len(items) - 1

    while beg <= end:
        mid = (beg + end) // 2
        if items[mid] < value:
            beg = mid + 1
        else:
            end = mid - 1

    if beg == len(items) or items[beg] != value:
        return -1
    else:
        return beg

if __name__ == '__main__':
    import doctest
    doctest.testmod()
