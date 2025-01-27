# План по созданию собственного типа данных для учета денежных средств в банкомате

class ATMRegister:
    """Класс для учета денежных средств в банкомате.
    Банкомат имеет 4 кассеты, в которые могут заправляться
    только российские рубли достоинством 100, 500, 1000 и 5000 рублей
    """
    def __init__(self, note100, note500, note1000, note5000):
        """ (ATMRegister, int, int, int, int) -> NoneType

        Метод инициализации объектов класса ATMRegister

        >>> atm = ATMRegister(5, 5, 5, 5)
        >>> atm.notes
        {100: 5, 500: 5, 1000: 5, 5000: 5}
        """
        self.notes = {100: note100, 500: note500, 1000: note1000, 5000: note5000}
        
    def get_total(self):
        """ (ATMRegister) -> int

        Возвращает общую сумму средств в банкомате

        >>> atm = ATMRegister(5, 5, 5, 5)
        >>> atm.get_total()
        33000
        """
        return self.notes[100] * 100 + self.notes[500] * 500 + \
               self.notes[1000] * 1000 + self.notes[5000] * 5000
    
    def increase(self, count, denomination):
        """ (ATMRegister, int, int) -> int

        Добавляет count купюр номинала denomination в банкомат.
        denomination может иметь одно из следующих значений: 100, 500, 1000, 5000

        >>> atm = ATMRegister(5, 5, 5, 5)
        >>> atm.increase(2, 500)
        >>> atm.notes[500]
        7
        >>> atm.increase(1, 1000)
        >>> atm.notes[1000]
        6
        """
        self.notes[denomination] += count

    def decrease(self, count, denomination):
        """ (ATMRegister, int, int) -> int

        Удаляет count купюр номинала denomination из банкомата.
        denomination может иметь одно из следующих значений: 100, 500, 1000, 5000

        >>> atm = ATMRegister(5, 5, 5, 5)
        >>> atm.decrease(2, 500)
        >>> atm.notes[500]
        3
        >>> atm.decrease(1, 1000)
        >>> atm.notes[1000]
        4
        """
        self.notes[denomination] -= count

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    # Создадим объект банкомат, заправленный купюрами
    # 20x100руб, 40x500руб, 30x1000руб и 10x5000руб
    atm = ATMRegister(20, 40, 30, 10)
    print("Рублей в банкомате после создания объекта:", atm.get_total())

    # добавим 3 сотни и удалим 2 пятисотки
    atm.increase(3, 100)
    atm.decrease(2, 500)
    print("Рублей в банкомате после 2-ух операций:", atm.get_total())
