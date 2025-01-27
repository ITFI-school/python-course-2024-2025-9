# Astrocrash03
# Движущийся Космический корабль

import math, random
from superwires import games

games.init(screen_width=1000, screen_height=600, fps=50)


class Asteroid(games.Sprite):
    """ Спрайт Астероид, движущийся по экрану. """
    SMALL = 1
    MEDIUM = 2
    LARGE = 3
    images = { SMALL  : games.load_image("asteroid_small.bmp"),
               MEDIUM : games.load_image("asteroid_med.bmp"),
               LARGE  : games.load_image("asteroid_big.bmp") }

    # константа, на основе которой определяется случайная скорость каждого из астероидов
    SPEED = 2
      
    def __init__(self, pos_x, pos_y, size):
        """ Инициализирует спрайт с изображением астероида. """
        super().__init__(
            image=Asteroid.images[size],
            x=pos_x, y=pos_y,
            dx=random.choice([1, -1]) * Asteroid.SPEED * random.random() / size, 
            dy=random.choice([1, -1]) * Asteroid.SPEED * random.random() / size)
        
        self.size = size

    def update(self):
        """ Заставляет астероид обогнуть экран. """
        if self.top > games.screen.height:
            self.bottom = 0
 
        if self.bottom < 0:
            self.top = games.screen.height

        if self.left > games.screen.width:
            self.right = 0

        if self.right < 0:
            self.left = games.screen.width


class Ship(games.Sprite):
    """ Спрайт Космический корабль игрока. """
    image = games.load_image("ship.bmp")
    sound = games.load_sound("thrust.wav")  # звук ускоряющегося рывка
    ROTATION_STEP = 2   # на сколько градусов вращать за один раз
    VELOCITY_STEP = .03 # чем больше, тем быстрее растет скорость корабля

    def update(self):
        """ Вращает корабль при нажатии клавиш со стрелками
            и делает рывок, в зависимости от нажатых клавиш. """
        # вращать по левой и правой стрелке
        if games.keyboard.is_pressed(games.K_LEFT):
            self.angle -= Ship.ROTATION_STEP        
        if games.keyboard.is_pressed(games.K_RIGHT):
            self.angle += Ship.ROTATION_STEP

        # корабль совершает рывок по нажатию стрелки вверх
        if games.keyboard.is_pressed(games.K_UP):
            Ship.sound.play()
          
            # изменение горизонтальной и вертикальной скорости корабля
            # с учетом его угла поворота
            radian_angle = self.angle * math.pi / 180  # преобразование в радианы
            self.dx += Ship.VELOCITY_STEP * math.sin(radian_angle)
            self.dy += Ship.VELOCITY_STEP * -math.cos(radian_angle)

        # Заставляем Космический корабль обогнуть экран при достижении границ
        if self.top > games.screen.height:
            self.bottom = 0
 
        if self.bottom < 0:
            self.top = games.screen.height

        if self.left > games.screen.width:
            self.right = 0

        if self.right < 0:
            self.left = games.screen.width


def main():
    # назначаем фоновую картинку
    space_image = games.load_image("space.jpg")
    games.screen.background = space_image

    # создаем 8 астероидов
    for i in range(8):
        rand_x = random.randrange(games.screen.width)
        rand_y = random.randrange(games.screen.height)
        rand_size = random.choice([Asteroid.SMALL, Asteroid.MEDIUM, Asteroid.LARGE])
        new_asteroid = Asteroid(pos_x=rand_x, pos_y=rand_y, size=rand_size)
        games.screen.add(new_asteroid)

    # создаем космический корабль
    the_ship = Ship(image=Ship.image,
                    x=games.screen.width/2,
                    y=games.screen.height/2)
    games.screen.add(the_ship)
        
    games.screen.mainloop()

# поехали!
if __name__ == "__main__":
    main()
