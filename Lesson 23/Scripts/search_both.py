def linear_search(items, value):
    """ (list, object) -> int
    Возвращает индекс первого вхождения value в список items или -1, если значение value в этом списке не найдено.
    Предусловие: все элементы списка должны иметь такой тип, который может сравниваться с value
    """
    i = 0
    LEN = len(items)
    while i != LEN and value != items[i]:
        i = i + 1

    if i == LEN:
        return -1
    else:
        return i


def binary_search(items, value):
    """ (list, object) -> int

    Возвращает индекс первого вхождения value в список items или -1, если значение value в этом списке не найдено.
    Предусловия:
    1) все элементы списка должны иметь такой тип, который может сравниваться с value
    2) список items должен быть отсортирован по возрастанию
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
