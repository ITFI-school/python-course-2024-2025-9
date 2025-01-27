import pygame
import sys
pygame.init()
sc = pygame.display.set_mode((400, 300))
sc.fill((200, 255, 200))
font = pygame.font.Font(None, 72) # arg1 -> шрифт, arg2-> Размер шрифта
text = font.render("Hello Wold", True, (0, 100, 0)) # arg1-> текст, arg2 -> сглаживание, arg3 -> цвет текста
place = text.get_rect(center=(200, 150)) #получаем координаты надписи
sc.blit(text, place) # отображаем надпись
sc.fill((200, 255, 200))
sc.blit(text, place)
pygame.display.update()
    
