import pygame
from pygame import *

WIDTH = 800 # Ширина окна
HEIGHT = 640 # Высота окна
#BACKGROUND_COLOR = (0, 0, 0) # Цвет заднего фона

pygame.init() 

screen = display.set_mode((WIDTH, HEIGHT)) 

game_over = False #Переменная которая отвечает за игровой цикл

while game_over != True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      game_over = True
  pygame.display.update() 

