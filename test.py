import pygame
import menu
from pygame.locals import *
import os
import widget


pygame.init()
screen = pygame.display.set_mode((1600,1000), HWSURFACE | DOUBLEBUF | FULLSCREEN)

icon = pygame.image.load("textures/icon_game.png")
global launched
launched = False
global menu_launch
menu_launch = True

pygame.display.set_icon(icon)
pygame.display.set_caption("Planet Star")



image = pygame.image.load("textures/tets.jpg")
earth = pygame.image.load("textures/earth.png")
jupiter = pygame.image.load("textures/jupiter.png")
mars = pygame.image.load("textures/mars.png")
sprite = pygame.image.load("textures/spriteplanete.png")
incone_or = pygame.image.load("textures/incone_or.jpg")
incone_or.convert()
launched = menu.display_menu(screen, menu_launch)

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
    widget.print_incone(screen, incone_or)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pos()[0] >= 1500 and pygame.mouse.get_pos()[1] >= 900 \
            and pygame.mouse.get_pos()[0] <= 1600 and pygame.mouse.get_pos()[1] <= 1000:
                widget.widget(screen, image, incone_or)
    pygame.display.flip()