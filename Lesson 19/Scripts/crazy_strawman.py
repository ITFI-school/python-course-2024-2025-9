# Сумасшедшая масленица
# Игрок должен ловить падающие блины, пока они не достигли земли

from superwires import games, color
import random

games.init(screen_width=1000, screen_height=600, fps=50)

games.pygame.display.set_caption("Crazy Carnival")
icon = games.pygame.image.load("pancake.bmp")
games.pygame.display.set_icon(icon)

class Pan(games.Sprite):
    """
    Сковорода, в которую игрок может ловить падающие блины
    """
    image = games.load_image("pan.bmp")

    def __init__(self):
        """ Инициализирует объект Pan и создает объект Text для отображения счета """
        super().__init__(image=Pan.image,
                         x=games.mouse.x,
                         bottom=games.screen.height)
        
        self.score = games.Text(value=0, size=25, color=color.black,
                                top=5, right=games.screen.width-10)
        games.screen.add(self.score)

    def update(self):
        """ Передвигает объект по горизонтали вслед за указателем мыши """
        self.x = games.mouse.x
        
        if self.left < 0:
            self.left = 0
            
        if self.right > games.screen.width:
            self.right = games.screen.width
            
        self.check_catch()

    def check_catch(self):
        """ Проверяет поймал ли игрок падающий блин """
        for pancake in self.overlapping_sprites:
            self.score.value += 10
            self.score.right = games.screen.width - 10 
            pancake.handle_caught()


class Pancake(games.Sprite):
    """
    Класс блинов, падающих на землю
    """ 
    image = games.load_image("pancake.bmp")
    speed = 1   

    def __init__(self, x, y=90):
        """ Инициализирует объект Pancake """
        super().__init__(image=Pancake.image,
                         x=x, y=y,
                         dy=Pancake.speed)

    def update(self):
        """ Проверяет не коснулась ли нижняя кромка спрайта нижней границы экрана """
        if self.bottom > games.screen.height:
            self.end_game()
            self.destroy()

    def handle_caught(self):
        """ Уничтожает блин, пойманный игроком """
        self.destroy()

    def end_game(self):
        """ Завершает игру. """
        end_message = games.Message(value="Конец игры",
                                    size=90,
                                    color=color.red,
                                    x=games.screen.width/2,
                                    y=games.screen.height/2,
                                    lifetime=5*games.screen.fps,
                                    after_death=games.screen.quit)
        games.screen.add(end_message)


class Strawman(games.Sprite):
    """
    Чучело, которое, двигаясь влево-вправо, разбрасывает блины
    """
    image = games.load_image("strawman.bmp")

    def __init__(self, y=110, speed=2, dir_change_chance=200):
        """ Инициализирует объект Strawman """
        super().__init__(image=Strawman.image,
                         x=games.screen.width/2,
                         y=y,
                         dx=speed)
        # Вероятностное значение для задания нового направления движения чучелу
        # Если, например, параметр dir_change_chance равен 200, то существует
        # один шанс из 200 на каждой итерации mainloop, что буквально в данный
        # момент вектор горизонтальной скорости поменяет знак и чучело
        # побежит в другом направлении
        self.dir_change_chance = dir_change_chance
        # интервал ожидания появления нового блина, выброшенного чучелом
        self.time_til_drop = 0

    def update(self):
        """ Определяет надо ли сменить направление """
        if self.left < 0 or self.right > games.screen.width:
            self.dx = -self.dx
        elif random.randrange(self.dir_change_chance) == 0:
           self.dx = -self.dx
                
        self.check_drop()

    def check_drop(self):
        """ Уменьшает интервал ожидания на единицу или сбрасывает
            очередной блин и восстанавливает исходный интервал """
        if self.time_til_drop > 0:
            self.time_til_drop -= 1
        else:
            new_pancake = Pancake(x=self.x)
            games.screen.add(new_pancake)

            # вне зависимости от скорости падения блина "зазор" между падающими
            # кругами принимается равным 30% каждого из них по высоте
            self.time_til_drop = int(new_pancake.height * 1.3 / Pancake.speed) + 1      


def main():
    """ Главная функция. Организует игровой процесс. """
    wall_image = games.load_image("wall.jpg", transparent=False)
    games.screen.background = wall_image

    the_strawman = Strawman()
    games.screen.add(the_strawman)

    the_pan = Pan()
    games.screen.add(the_pan)

    games.mouse.is_visible = False

    games.screen.event_grab = True
    games.screen.mainloop()

# Начинаем игру!
if __name__ == "__main__":
    main()
