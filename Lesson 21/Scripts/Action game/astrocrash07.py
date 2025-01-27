# Astrocrash07
# Добавление взрывов и оптимизация кода

import math, random
from superwires import games

games.init(screen_width=1000, screen_height=600, fps=50)


class Wrapper(games.Sprite):
    """ Огибатель. Спрайт, который двигаясь, огибает графический экран. """
    def update(self):
        """ Переносит спрайт на противоположную сторону окна. """    
        if self.top > games.screen.height:
            self.bottom = 0

        if self.bottom < 0:
            self.top = games.screen.height

        if self.left > games.screen.width:
            self.right = 0

        if self.right < 0:
            self.left = games.screen.width

    def die(self):
        """ Разрушает объект. """
        self.destroy()


class Collider(Wrapper):
    """ Погибатель. Огибатель, который может сталкиваться
        с другими объектами, губить их и гибнуть сам.
        В момент гибели Погибателя появляется анимированный взрыв
    """

    def update(self):

        # вызвать метод update() родительского класса Wrapper,
        # чтобы удержать объект внутри окна
        super().update()
        
        # проверить, нет ли спрайтов, визуально перекрывающихся с данным
        if self.overlapping_sprites:
            # уничтожить все спрайты, которые пересекаются с нашим
            for sprite in self.overlapping_sprites:
                sprite.die()
            # умереть самому
            self.die()               

    def die(self):
        """ Разрушает объект со взрывом. """
        new_explosion = Explosion(pos_x=self.x, pos_y=self.y)
        games.screen.add(new_explosion)
        super().die()


class Asteroid(Wrapper):
    """ Спрайт Астероид, движущийся по экрану. """
    SMALL = 1
    MEDIUM = 2
    LARGE = 3
    images = { SMALL  : games.load_image("asteroid_small.bmp"),
               MEDIUM : games.load_image("asteroid_med.bmp"),
               LARGE  : games.load_image("asteroid_big.bmp") }

    # константа, на основе которой определяется случайная скорость каждого из астероидов
    SPEED = 2

    # количество новых астероидов, на которые распадается один взорванный
    SPAWN = 2  

    def __init__(self, pos_x, pos_y, size):
        """ Инициализирует спрайт с изображением астероида. """
        super().__init__(
            image = Asteroid.images[size],
            x = pos_x, y = pos_y,
            dx = random.choice([1, -1]) * Asteroid.SPEED * random.random() / size,
            dy = random.choice([1, -1]) * Asteroid.SPEED * random.random() / size)
        
        self.size = size

    def die(self):
        """ Разрушает астероид. """

        # если размеры астероида крупные или средние, заменить
        # его двумя более мелкими астероидами 
        if self.size != Asteroid.SMALL:
            for i in range(Asteroid.SPAWN):
                new_asteroid = Asteroid(pos_x=self.x,
                                        pos_y=self.y,
                                        size=self.size - 1)
                games.screen.add(new_asteroid)
                
        super().die()


class Ship(Collider):
    """ Спрайт Космический корабль игрока. """
    image = games.load_image("ship.bmp")
    sound = games.load_sound("thrust.wav")  # звук ускоряющегося рывка
    ROTATION_STEP = 2   # на сколько градусов вращать за один раз
    VELOCITY_STEP = .03 # чем больше, тем быстрее растет скорость корабля
    MISSILE_DELAY = 25  # количество обновлений экрана, в течение которых
                        # игрок не может выпустить очередную ракету

    def __init__(self, pos_x, pos_y):
        """ Инициализировать спрайт Космический корабль. """
        super().__init__(image=Ship.image, x=pos_x, y=pos_y)
        # C помощью атрибута missile_wait будет отсчитываться 
        # задержка, упреждающая запуск очередной ракеты
        self.missile_wait = 0

    def update(self):
        """ Вращает корабль при нажатии клавиш со стрелками
            и делает рывок, в зависимости от нажатых клавиш. """

        # вызвать метод update() родительского класса Collider, чтобы
        # удержать объект внутри окна и обеспечить взрыв при столкновении
        super().update()
        
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

        # если запуск следующей ракеты пока еще не разрешен,
        # вычесть 1 из длины оставшегося интервала ожидания
        if self.missile_wait > 0:
            self.missile_wait -= 1
            
        # если нажат Пробел и интервал ожидания истек, выпустить ракету
        if games.keyboard.is_pressed(games.K_SPACE) and self.missile_wait == 0:
            new_missile = Missile(self.x, self.y, self.angle)
            games.screen.add(new_missile)
            self.missile_wait = Ship.MISSILE_DELAY


class Missile(Collider):
    """ Ракета, которую может выпустить Космический корабль игрока. """
    image = games.load_image("missile.bmp")
    sound = games.load_sound("missile.wav")
    BUFFER = 40  # начальное удаление вновь созданной ракеты от корабля
    VELOCITY_FACTOR = 7  # сказывается на скорости полета ракет
    LIFETIME = 40        # продолжительность существования ракеты до ее самоуничтожения
                         # заданная в количестве циклов обновления mainloop()

    def __init__(self, ship_x, ship_y, ship_angle):
        """ Инициализирует спрайт с изображением ракеты. """
        Missile.sound.play()
        
        # преобразование в радианы
        rad_angle = ship_angle * math.pi / 180  

        # вычисление начальной позиции ракеты
        buffer_x = Missile.BUFFER * math.sin(rad_angle)
        buffer_y = Missile.BUFFER * -math.cos(rad_angle)
        miss_x = ship_x + buffer_x
        miss_y = ship_y + buffer_y

        # вычисление горизонтальной и вертикальной скорости ракеты
        miss_dx = Missile.VELOCITY_FACTOR * math.sin(rad_angle)
        miss_dy = Missile.VELOCITY_FACTOR * -math.cos(rad_angle)

        # создание ракеты
        super().__init__(image=Missile.image,
                         x=miss_x, y=miss_y,
                         dx=miss_dx, dy=miss_dy)
        self.lifetime = Missile.LIFETIME

    def update(self):
        """ Перемещает ракету. """

        # вызвать метод update() родительского класса Collider, чтобы
        # удержать объект внутри окна и обеспечить взрыв при столкновении
        super().update()
        
        # если "срок годности" ракеты истек, она уничтожается
        self.lifetime -= 1
        if self.lifetime == 0:
            self.destroy()


class Explosion(games.Animation):
    """ Анимированный взрыв. """
    sound = games.load_sound("explosion.wav")
    images = ["explosion1.bmp",
              "explosion2.bmp",
              "explosion3.bmp",
              "explosion4.bmp",
              "explosion5.bmp",
              "explosion6.bmp",
              "explosion7.bmp",
              "explosion8.bmp",
              "explosion9.bmp"]

    def __init__(self, pos_x, pos_y):
        super().__init__(images=Explosion.images,
                         x=pos_x, y=pos_y,
                         repeat_interval=4, n_repeats=1,
                         is_collideable=False)
        Explosion.sound.play()


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
    the_ship = Ship(pos_x=games.screen.width/2, pos_y=games.screen.height/2)
    games.screen.add(the_ship)
        
    games.screen.mainloop()

# поехали!
if __name__ == "__main__":
    main()
