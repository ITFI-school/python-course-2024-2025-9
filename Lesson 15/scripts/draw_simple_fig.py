import pygame
import sys

pygame.init()

# Размеры экрана
screen_width = 800
screen_height = 600

# Цвета
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# Создание окна
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pygame Filled Shapes Example")

clock = pygame.time.Clock()

# Основной цикл программы
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Очистка экрана
    screen.fill(white)

    # Рисование и заполнение прямоугольника
    pygame.draw.rect(screen, red, pygame.Rect(50, 50, 100, 100))

    # Рисование и заполнение многоугольника
    pygame.draw.polygon(screen, green, [(200, 50), (250, 150), (300, 50)])

    # Рисование и заполнение круга
    pygame.draw.circle(screen, blue, (450, 200), 50)

    # Рисование и заполнение линии
    pygame.draw.line(screen, red, (550, 50), (650, 150), 2)

    # Рисование и заполнение линий
    pygame.draw.lines(screen, blue, True, [(700, 50), (750, 150), (800, 50)], 2)

    # Рисование и заполнение антиалиасинг линии
    pygame.draw.aaline(screen, green, (50, 200), (200, 300), 2)

    # Обновление экрана
    pygame.display.flip()

    # Задержка для управления частотой кадров
    clock.tick(30)
