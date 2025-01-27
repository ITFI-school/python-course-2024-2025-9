import pygame
import sys
 
W = 400
H = 300
 
sc = pygame.display.set_mode((W, H))
sc.fill((100, 150, 200))
 
image_surf = pygame.image.load('img_1.png')
image_rect = image_surf.get_rect((W, H))
sc.blit(image_surf, image_rect)
 
pygame.display.update()
