# План по созданию собственного типа данных для учета денежных средств в банкомате

class ATMRegister:
    """Класс для учета денежных средств в банкомате.
    Банкомат имеет 4 кассеты, в которые могут заправляться
    только российские рубли достоинством 100, 500, 1000 и 5000 рублей
    """
    def __init__(self, note100, note500, note1000, note5000):
        """ (ATMRegister, int, int, int, int) -> NoneType

        Метод инициализации объектов класса ATMRegister

        >>> atm = ATMRegister(5, 5, 5, 6)
        >>> atm.note100
        5
        >>> atm.note500
        5
        >>> atm.note1000
        5
        >>> atm.note5000
        5
        """
        self.note100 = note100
        self.note500 = note500
        self.note1000 = note1000
        self.note5000 = note5000
        
    def get_total(self):
        """ (ATMRegister) -> int

        Возвращает общую сумму средств в банкомате

        >>> atm = ATMRegister(5, 5, 5, 5)
        >>> atm.get_total()
        33000
        """
        return self.note100 * 100 + self.note500 * 500 + \
               self.note1000 * 1000 + self.note5000 * 5000
    
    def increase(self, count, denomination):
        """ (ATMRegister, int, int) -> int

        Добавляет count купюр номинала denomination в банкомат.
        denomination может иметь одно из следующих значений: 100, 500, 1000, 5000

        >>> atm = ATMRegister(5, 5, 5, 5)
        >>> atm.increase(2, 500)
        >>> atm.note500
        7
        >>> atm.increase(1, 1000)
        >>> atm.note1000
        6
        """
        if denomination == 100:
            self.note100 += count
        elif denomination == 500:
            self.note500 += count
        elif denomination == 1000:
            self.note1000 += count
        elif denomination == 5000:
            self.note5000 += count

    def decrease(self, count, denomination):
        """ (ATMRegister, int, int) -> int

        Удаляет count купюр номинала denomination из банкомата.
        denomination может иметь одно из следующих значений: 100, 500, 1000, 5000

        >>> atm = ATMRegister(5, 5, 5, 5)
        >>> atm.decrease(2, 500)
        >>> atm.note500
        3
        >>> atm.decrease(1, 1000)
        >>> atm.note1000
        4
        """
        if denomination == 100:
            self.note100 -= count
        elif denomination == 500:
            self.note500 -= count
        elif denomination == 1000:
            self.note1000 -= count
        elif denomination == 5000:
            self.note5000 -= count

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
