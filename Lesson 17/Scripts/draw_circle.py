import pygame
import sys
import random

# Инициализация Pygame
pygame.init()

# Размеры экрана
screen_width = 800
screen_height = 600

# Цвета
white = (255, 255, 255)

# Создание окна
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Создание круга по щелчку")

clock = pygame.time.Clock()

# Основной цикл программы
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Получение координат щелчка
            x, y = pygame.mouse.get_pos()

            # Создание случайного размера круга
            radius = random.randint(10, 50)

            # Рисование круга на экране
            pygame.draw.circle(screen, white, (x, y), radius)

    # Обновление экрана
    pygame.display.flip()

    # Задержка для управления частотой кадров
    clock.tick(30)
