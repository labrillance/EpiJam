import pygame
import menu
from pygame.locals import *
import os

pygame.init()
screen = pygame.display.set_mode((1600,1000), HWSURFACE | DOUBLEBUF | FULLSCREEN)

icon = pygame.image.load("icon_game.png")
global launched
launched = False
global menu_launch
menu_launch = True

pygame.display.set_icon(icon)
pygame.display.set_caption("Planet Star")



image = pygame.image.load("tets.jpg")
earth = pygame.image.load("earth.png")
jupiter = pygame.image.load("jupiter.png")
mars = pygame.image.load("mars.png")
sprite = pygame.image.load("spriteplanete.png")


list = menu.display_menu(screen, menu_launch)
if (len(list) == 4):
    launched = True

while launched:
    pygame.display.init()
    screen.blit(image, (0,0))
    screen.blit(earth, (20,50))
    screen.blit(jupiter, (120,30))
    screen.blit(mars, (250,65))
    screen.blit(sprite, (400,10))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False
    pygame.display.flip()