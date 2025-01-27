""" 
Есть класс "Воин". От него создаются два экземпляра. Каждому из них устанавливается уровень здоровья в 100 очков. 
В случайном порядке воины бьют друг друга. Тот, кто бьет, здоровья не теряет, а у того, кого бьют, оно уменьшается 
на 20 очков от каждого удара. После удара выводится сообщение, какой воин атаковал, и сколько у противника осталось здоровья.
Как только у кого-то заканчивается ресурс здоровья, программа завершается сообщением о том, кто одержал победу.
"""

import random
 
class Warrior:
    "Класс воина, имеющего здоровье и определёенную силу удара"

    def __init__(self, name, health, strength):
        """ (Warrior, str, int, int) -> NoneType

        Инициализирует воина с именем name, уровнем
        здоровья health и силой удара strength
        """
        self.name = name
        self.health = health
        self.strength = strength

    def attack(self, enemy):
        """ (Warrior, Warrior) -> NoneType

        Моделирует нападение self на enemy
        """
        # послать удар силой self.strength объекту enemy
        enemy.hit(self.strength)
        print("Воин {warrior} атаковал {enemy}. Остаток здоровья у {enemy}: {enemy_health}.".format(
               warrior=self.name, enemy=enemy.name, enemy_health=enemy.health))

    def hit(self, strength):
        """ (Warrior, int) -> NoneType

        Отрабатывает получение self удара силой strength
        """
        # уменьшить здоровье на силу удара
        self.health -= strength

 
def war(warrior_1, warrior_2):
    """ Организует битву между 2-мя воинами """
    while warrior_1.health > 0 and warrior_2.health > 0:
        if random.random() >= 0.5:
            warrior_1.attack(warrior_2)
        else:
            warrior_2.attack(warrior_1)

    winner = warrior_2 if warrior_1.health <= 0 else warrior_1
    print("Воин {name} одержал победу. Уровень его здоровья в конце битвы: {health}".format(
           name=winner.name, health=winner.health))

 
# начало программы
ork = Warrior('Орк', 100, 20)
elf = Warrior('Эльф', 100, 20)

war(ork, elf)

input("\n\nНажмите Enter, чтобы выйти")
