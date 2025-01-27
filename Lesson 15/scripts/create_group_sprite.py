import pygame
import sys

class Sprite(pygame.sprite.Sprite):
    def __init__(self, x, y, image_path):
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.speed = 5

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy



# Инициализация Pygame
pygame.init()

# Определение цветов
BLACK = (0, 0, 0)

# Создание окна
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Спрайт с движением")

# Создание спрайт-группы
all_sprites = pygame.sprite.Group()

# Тригеры
flag = True

# Создание экземпляра Sprite и добавление в группу
sprites = []
for i in range(5):
    sprite = Sprite(0 + i * 80, 0, "img_3.png")
    all_sprites.add(sprite)
    sprites.append(sprite)

# Основной цикл программы
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    for sprite in all_sprites:
        if flag == True:
            sprite.move(5, 0)
        else:
            sprite.move(-5, 0)

        if sprite.rect.topright[0] > width:
            flag = False
        if sprite.rect.x < 0:
            flag = True

        all_sprites.update()



        # Обновление координат спрайтов
    all_sprites.update()

    # Очистка экрана
    screen.fill(BLACK)

    # Отрисовка спрайтов из группы
    all_sprites.draw(screen)

    # Обновление экрана
    pygame.display.flip()

    # Задержка для контроля частоты кадров
    pygame.time.Clock().tick(40)
