# Стеснительная зверушка, которая "прячет" свое настроение.
# Демонстрирует закрытые переменные экземпляра и методы класса

class Critter(object):
    """Виртуальный питомец"""
    def __init__(self, name, mood):
        print("Появилась на свет новая зверушка!")
        self.name = name            # открытый атрибут
        self.__mood = mood          # закрытый атрибут

    def talk(self):
        print("\nМеня зовут", self.name)
        print("Сейчас я чувствую себя", self.__mood, "\n")

    def __private_method(self):
        print("Это закрытый метод.")

    def public_method(self):
        print("Это открытый метод.")
        self.__private_method()


# Основная часть программы

crit = Critter(name = "Бобик", mood = "прекрасно")
crit.talk()
crit.public_method()

input("\n\nНажмите Enter, чтобы выйти")
