# Моя зверюшка
# Виртуальный питомец, о котором пользователь может заботиться

class MyRangeError(Exception): pass

def get_integer(message, name="целое число", minimum=None, maximum=None):
    """ (str, str, int, int) -> int
    Запрашивает у пользователя целочисленное значение name с приглашением message и возвращает это значение.
    Контролирует, чтобы введенное значение было строго больше minimum и строго меньше maximum, если эти параметры заданы
    """
    message += ": "
    while True:
        try:
            line = input(message)
            int_val = int(line)
            if (minimum is not None and minimum > int_val) or (maximum is not None and maximum < int_val):
                raise MyRangeError("Ожидается значение {0} между {1} и {2} ".format(name.upper(), minimum, maximum))
            return int_val
        except MyRangeError as err:
            print("ОШИБКА.", err)
        except ValueError as err:
            print("ОШИБКА. Значение {0} должно быть целочисленным".format(name.upper()))

class Critter(object):
    """Виртуальный питомец"""
    def __init__(self, name, hunger = 0, boredom = 0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom

    def __pass_time(self):
        """Закрытый метод, который увеличивает уровень голода (hunger)
        и уныния (boredom) зверюшки
        """
        self.hunger += 1
        self.boredom += 1

    def __str__(self):
        return "Critter {0}, hunger {1}, boredom {2}".format(
                         self.name, self.hunger, self.boredom)
        
    @property
    def mood(self):
        """Свойство mood отражает самочувствие зверюшки. Значение свойства
        вычисляется "на лету", исходя из значений атрибутов hunger и boredom
        экземпляра self класса Critter
        """
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            calc_mood = "прекрасно"
        elif 5 <= unhappiness <= 10:
            calc_mood = "неплохо"
        elif 11 <= unhappiness <= 15:
            calc_mood = "не сказать чтобы хорошо"
        else:
            calc_mood = "ужасно"
        return calc_mood

    def talk(self):
        """Узнает  значение свойства mood объекта класса Critter
        и сообщает о самочувствии зверюшки
        """
        print("Меня зовут", self.name, "и сейчас я чувствую себя", self.mood, "\n")
        self.__pass_time()
    
    def eat(self, food = 4):
        """Уменьшает уровень голода зверюшки на величину, переданную в параметре food.
        Следит за уровнем голода, не позволяя ему оказаться отрицательным числом
        """
        print("Мррр... Спасибо!")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def play(self, fun = 4):
        """Снижает уровень уныния зверюшки на величину, переданную в параметре fun.
        Следит за уровнем уныния зверюшки, не позволяя ему оказаться отрицательным
        """
        print("Уиии!")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()


def main():
    # инициализация констант для пунктов меню
    EXIT, LISTEN, FEED, PLAY = map(str, range(4))
    BACKDOOR = "9"

    crit_name = input("Kaк вы назовете свою зверюшку?: ")
    crit = Critter(crit_name)

    choice = None  
    while choice != EXIT:
        print \
        ("""
        Моя зверюшка
    
        0 - Выйти
        1 - Узнать о самочувствии зверюшки
        2 - Покормить зверюшку
        3 - Поиграть со зверюшкой
        """)

        if crit.hunger > 10:
            print("Ваша зверюшка проголодалась и умерла!")
            del crit
            choice = EXIT
        else:
            choice = input("Ваш выбор: ")
            print()

        # выход
        if choice == EXIT:
            print("До свидания.")

        # беседа со зверюшкой
        elif choice == LISTEN:
            crit.talk()
        
        # кормление зверюшки
        elif choice == FEED:
            food = get_integer("Сколько кормить?")
            crit.eat(food)
         
        # игра со зверюшкой
        elif choice == PLAY:
            fun_level = get_integer("Сколько играть?")
            crit.play(fun_level)

        # печать атрибутов зверюшки
        elif choice == BACKDOOR:
            print(crit)

        # непонятный пользовательский ввод
        else:
            print("\nИзвините, в меню нет пункта", choice)

main()
input("\n\nНажмите Enter, чтобы выйти")
