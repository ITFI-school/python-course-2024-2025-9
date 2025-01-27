import pygame
import sys

# Инициализация Pygame
pygame.init()

# Определение размеров окна
width, height = 400, 300

# Создание окна
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Key Events')

# Цвета
black = (0, 0, 0)
white = (255, 255, 255)

# Позиция и размеры прямоугольника
rect_x, rect_y = 50, 50
rect_width, rect_height = 50, 50

# Управление движением прямоугольника
move_speed = 5

#Флаги управления движением
move_up = False
move_down = False
move_right = False
move_left  = False
# Главный цикл программы
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


        # Обработка событий клавиш
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                rect_x -= move_speed
            elif event.key == pygame.K_RIGHT:
                rect_x += move_speed
            elif event.key == pygame.K_UP:
                rect_y -= move_speed
            elif event.key == pygame.K_DOWN:
                rect_y += move_speed

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                rect_x -= move_speed
            elif event.key == pygame.K_RIGHT:
                rect_x += move_speed
            elif event.key == pygame.K_UP:
                rect_y -= move_speed
            elif event.key == pygame.K_DOWN:
                rect_y += move_speed



    # Заполнение экрана белым цветом
    screen.fill(white)

    # Рисование прямоугольника
    pygame.draw.rect(screen, black, (rect_x, rect_y, rect_width, rect_height))

    # Обновление дисплея
    pygame.display.flip()
