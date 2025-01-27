# Astrocrash08
# Добавлен объект Game для завершения программы

import math, random
from superwires import games, color

games.init(screen_width=1000, screen_height=600, fps=50)

games.pygame.display.set_caption("Astro crash")
icon = games.pygame.image.load("asteroid_small.bmp")
games.pygame.display.set_icon(icon)


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
        с другими объектами и гибнуть. """

    def update(self):
        """ Проверяет, нет ли спрайтов, визуально перекрывающихся с данным. """
        super().update()
        
        if self.overlapping_sprites:
            for sprite in self.overlapping_sprites:
                sprite.die()
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

    # исходная величина, на основе которой будет рассчитываться количество очков 
    # за уничтожение отдельного астероида - оно будет тем больше, чем меньше астероид
    POINTS = 30
    
    total =  0   # текущая численность астероидов
      
    def __init__(self, game, pos_x, pos_y, size):
        """ Инициализирует спрайт с изображением астероида. """
        Asteroid.total += 1
        
        super().__init__(
            image=Asteroid.images[size],
            x=pos_x, y=pos_y,
            dx=random.choice([1, -1]) * Asteroid.SPEED * random.random() / size, 
            dy=random.choice([1, -1]) * Asteroid.SPEED * random.random() / size)

        self.game = game
        self.size = size

    def die(self):
        """ Разрушает астероид. """
        Asteroid.total -= 1

        self.game.score.value += int(Asteroid.POINTS / self.size)
        self.game.score.right = games.screen.width - 10   
        
        # если размеры астероида крупные или средние, заменить
        # его двумя более мелкими астероидами 
        if self.size != Asteroid.SMALL:
            for i in range(Asteroid.SPAWN):
                new_asteroid = Asteroid(game=self.game,
                                        pos_x=self.x,
                                        pos_y=self.y,
                                        size=self.size - 1)
                games.screen.add(new_asteroid)

        # если астероидов не осталось, переходим на следующий уровень
        if Asteroid.total == 0:
            self.game.advance()

        super().die()


class Ship(Collider):
    """ Спрайт Космический корабль игрока. """
    image = games.load_image("ship.bmp")
    sound = games.load_sound("thrust.wav")  # звук ускоряющегося рывка
    ROTATION_STEP = 2   # на сколько градусов вращать за один раз
    VELOCITY_STEP = .03 # чем больше, тем быстрее растет скорость корабля
    MISSILE_DELAY = 25  # количество обновлений экрана, в течение которых
                        # игрок не может выпустить очередную ракету
    VELOCITY_MAX = 3    # ограничение максимальной скорости корабля

    def __init__(self, game, pos_x, pos_y):
        """ Инициализировать спрайт Космический корабль. """
        super().__init__(image=Ship.image, x=pos_x, y=pos_y)
        self.game = game
        # C помощью атрибута missile_wait будет отсчитываться 
        # задержка, упреждающая запуск очередной ракеты
        self.missile_wait = 0

    def update(self):
        """ Вращает корабль при нажатии клавиш со стрелками
            и делает рывок, в зависимости от нажатых клавиш. """
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

            # ограничение горизонтальной и вертикальной скоростей
            self.dx = min(max(self.dx, -Ship.VELOCITY_MAX), Ship.VELOCITY_MAX)
            self.dy = min(max(self.dy, -Ship.VELOCITY_MAX), Ship.VELOCITY_MAX)
            
        # если запуск следующей ракеты пока еще не разрешен,
        # вычесть 1 из длины оставшегося интервала ожидания
        if self.missile_wait > 0:
            self.missile_wait -= 1
            
        # если нажат Пробел и интервал ожидания истек, выпустить ракету
        if games.keyboard.is_pressed(games.K_SPACE) and self.missile_wait == 0:
            new_missile = Missile(self.x, self.y, self.angle)
            games.screen.add(new_missile)        
            self.missile_wait = Ship.MISSILE_DELAY

    def die(self):
        """ Разрушает корабль и завершает игру. """
        self.game.end()
        super().die()


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
        angle = ship_angle * math.pi / 180  

        # вычисление начальной позиции ракеты
        buffer_x = Missile.BUFFER * math.sin(angle)
        buffer_y = Missile.BUFFER * -math.cos(angle)
        miss_x = ship_x + buffer_x
        miss_y = ship_y + buffer_y

        # вычисление горизонтальной и вертикальной скорости ракеты
        miss_dx = Missile.VELOCITY_FACTOR * math.sin(angle)
        miss_dy = Missile.VELOCITY_FACTOR * -math.cos(angle)

        # создание ракеты
        super().__init__(image=Missile.image,
                         x=miss_x, y=miss_y,
                         dx=miss_dx, dy=miss_dy)
        self.lifetime = Missile.LIFETIME

    def update(self):
        """ Перемещает ракету. """
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


class Game:
    """ Собственно игра. """
    def __init__(self):
        """ Инициализирует объект Game. """

        # выбор начального уровня игры = 0, пока не начали играть
        self.level = 0

        # загрузка звука, сопровождающего переход на следующий уровень
        self.sound = games.load_sound("level.wav")

        # создание объекта, в котором будет храниться текущий счет
        self.score = games.Text(value=0,
                                size=30,
                                color=color.white,
                                top=5,
                                right=games.screen.width-10,
                                is_collideable=False)
        games.screen.add(self.score)

        # создание корабля, которым будет управлять игрок
        self.ship = Ship(game=self, 
                         pos_x=games.screen.width/2,
                         pos_y=games.screen.height/2)
        games.screen.add(self.ship)

    def play(self):
        """ Начинает игру. """

        # запуск музыкальной темы с бесконечным проигрыванием
        games.music.load("theme.mid")
        games.music.play(-1)

        # загрузка и назначение фоновой картинки
        space_image = games.load_image("space.jpg")
        games.screen.background = space_image

        # переход к уровню 1
        self.advance()

        # начало игры
        games.screen.mainloop()

    def advance(self):
        """ Переводит игру на очередной уровень. """
        self.level += 1
        
        # зарезервированное пространство вокруг корабля, чтобы
        # сохранить его от астероидов сразу же после создания
        BUFFER = 150
     
        # создание новых астероидов
        for i in range(self.level):
            # вычислим х и у, чтобы от корабля они отстояли минимум на BUFFER пикселов

            # сначала выберем минимальные отступы по горизонтали и вертикали
            x_min = random.randrange(BUFFER)
            y_min = BUFFER - x_min

            # исходя из этих минимумов, сгенерируем расстояния от корабля по горизонтали и вертикали 
            x_distance = random.randrange(x_min, games.screen.width - x_min)
            y_distance = random.randrange(y_min, games.screen.height - y_min)

            # исходя из этих расстояний, вычислим экранные координаты астероида
            aster_x = self.ship.x + x_distance
            aster_y = self.ship.y + y_distance

            # если необходимо, вернем объект внутрь окна
            aster_x %= games.screen.width
            aster_y %= games.screen.height
       
            # создадим астероид
            new_asteroid = Asteroid(game=self,
                                    pos_x=aster_x, pos_y=aster_y,
                                    size=Asteroid.LARGE)
            games.screen.add(new_asteroid)

        # отображение номера текущего уровня
        level_message = games.Message(value="Уровень "+str(self.level),
                                      size=40,
                                      color=color.yellow,
                                      x=games.screen.width/2,
                                      y=games.screen.width/10,
                                      lifetime=3*games.screen.fps,
                                      is_collideable=False)
        games.screen.add(level_message)

        # звуковой эффект переход (кроме 1-го уровня)
        if self.level > 1:
            self.sound.play()
            
    def end(self):
        """ Завершает игру. """
        # 5-ти секундное отображение 'Конец игры'
        end_message = games.Message(value="Конец игры",
                                    size=90,
                                    color=color.red,
                                    x=games.screen.width/2,
                                    y=games.screen.height/2,
                                    lifetime=5*games.screen.fps,
                                    after_death=games.screen.quit,
                                    is_collideable=False)
        games.screen.add(end_message)


def main():
    astrocrash = Game()
    astrocrash.play()

# поехали!
if __name__ == "__main__":
    main()
