import pygame
import menu
from pygame.locals import *
import os
import widget
import init.init as classes

pygame.init()

infoObject = pygame.display.Info()

screen = pygame.display.set_mode((infoObject.current_w, infoObject.current_h), HWSURFACE | DOUBLEBUF | FULLSCREEN)

icon = pygame.image.load("textures/icon_game.png")

global launched
launched = False
global menu_launch
menu_launch = True

pygame.display.set_icon(icon)
pygame.display.set_caption("Planet Star")



image = pygame.image.load("textures/tets.jpg")
image = pygame.transform.scale(image, (infoObject.current_w, infoObject.current_h))
earth = pygame.image.load("textures/earth.png")
jupiter = pygame.image.load("textures/jupiter.png")
mars = pygame.image.load("textures/mars.png")
sprite = pygame.image.load("textures/spriteplanete.png")
incone_or = pygame.image.load("textures/incone_or.jpg")
incone_or.convert()

list = menu.display_menu(screen, menu_launch)
if (len(list) == 4):
    launched = True

def init_players(list):
    i = 0
    players = []
    while i <= 3:
        players.append(classes.player())
        players[i].name = list[i]
        i += 1
    return players

turn = 0
players = init_players(list)

while launched:
    pygame.display.init()
    screen.blit(image, (0,0))
    screen.blit(earth, (20,50))
    screen.blit(jupiter, (120,30))
    screen.blit(mars, (250,65))
    screen.blit(sprite, (400,10))
    widget.print_incone(screen, incone_or)
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            launched = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pos()[0] >= 1500 and pygame.mouse.get_pos()[1] >= 900 \
            and pygame.mouse.get_pos()[0] <= 1600 and pygame.mouse.get_pos()[1] <= 1000:
                widget.widget(screen, image, incone_or)
    pygame.display.flip()