class WordplayStr(str):
    """Тип строка, которая может сообщать обладает ли она одним интересным свойством"""

    
    def first_eq_last(self):
        """ (WordplayStr) -> bool

        Предусловие: len(self) != 0

        Возвращает признак "строка self начинается и заканчивается одной и той же буквой"

        >>> s = WordplayStr('абракадабра')
        >>> s.first_eq_last()
        True
        >>> s = WordplayStr('пример')
        >>> s.first_eq_last()
        False
        """
        if not self:
            return False

        return self[0] == self[-1]

if __name__ == '__main__':
    import doctest
    doctest.testmod()
