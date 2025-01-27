import pygame
import sys

class Sprite(pygame.sprite.Sprite):
    def __init__(self, x, y, image_path):
        super().__init__()
        self.image = pygame.image.load(image_path)
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

# Создание экземпляра Sprite
sprite = Sprite(width // 2, height // 2, "img_1.png")

#Тригер направления
flag = True
# Основной цикл программы
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if flag == True:
        # Движение спрайта
        sprite.move(5, 0)
        if sprite.rect.topright[0] >= width:
            flag = False
            sprite.image = pygame.image.load("img_2.png").convert_alpha();
    else:
        sprite.move(-5, 0)
        if sprite.rect.x <= 0:
            flag = True
            sprite.image = pygame.image.load("img_1.png")
        # Очистка экрана
    screen.fill(BLACK)

    # Отрисовка спрайта
    screen.blit(sprite.image, sprite.rect)

    # Обновление экрана
    pygame.display.flip()

    # Задержка для контроля частоты кадров
    pygame.time.Clock().tick(30)
