# Моя зверюшка, полная версия.
# Виртуальный питомец, о котором пользователь может заботиться

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
        """Узнает значение свойства mood объекта класса Critter
        и сообщает о самочувствии зверюшки
        """
        print("Меня зовут", self.name, "и сейчас я чувствую себя", self.mood, "\n")
        self.__pass_time()
    
    def eat(self, food = 4):
        """Уменьшает уровень голода зверюшки на величину, переданную в параметре food.
        Следит за уровнем голода, не позволяя ему оказаться отри­цательным числом
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
            crit.eat()
         
        # игра со зверюшкой
        elif choice == PLAY:
            crit.play()

        # непонятный пользовательский ввод
        else:
            print("\nИзвините, в меню нет пункта", choice)

main()
input("\n\nНажмите Enter, чтобы выйти")
