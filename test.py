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
overlay = [pygame.image.load("textures/overlayplayer1.png"), pygame.image.load("textures/overlayplayer2.png"), pygame.image.load("textures/overlayplayer3.png"), pygame.image.load("textures/overlayplayer4.png")]
overlay = [pygame.transform.scale(overlay[0], (infoObject.current_w, infoObject.current_h)), pygame.transform.scale(overlay[1], (infoObject.current_w, infoObject.current_h)), pygame.transform.scale(overlay[2], (infoObject.current_w, infoObject.current_h)), pygame.transform.scale(overlay[3], (infoObject.current_w, infoObject.current_h))]
font = pygame.font.Font("./fonts/Andromeda-eR2n.ttf", round((infoObject.current_w * infoObject.current_h * 45 / (1920 * 1080))))

list = menu.display_menu(screen, menu_launch)
if (len(list) == 4):
    launched = True

def init_players(list):
    i = 0
    players = []
    while i <= 3:
        players.append(classes.player())
        players[i].name = list[i]
        players[i].name = font.render(players[i].name, True, (0,0,0))
        i += 1
    return players
turn = 0
players = init_players(list)
clock_turn = pygame.time.get_ticks()
seconds = ""

while launched:
    pygame.display.init()
    screen.blit(image, (0,0))
    screen.blit(overlay[turn], (0, 0))
    screen.blit(players[turn].name, (infoObject.current_w * 20 / 1600, infoObject.current_h * 871 / 1000))
    seconds = str(int(((20 - (pygame.time.get_ticks() - clock_turn) / 1000))))
    sec = int(seconds)
    seconds = font.render(seconds, True, (0,0,0))
    screen.blit(seconds, (infoObject.current_w * 1520 / 1600, infoObject.current_h * 8 / 1000))
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            launched = False
        if (event.type == KEYDOWN and event.key == K_RETURN):
            clock_turn = pygame.time.get_ticks()
            if turn != 3:
                turn += 1
            else:
                turn = 0
    if sec <= 0:
        clock_turn = pygame.time.get_ticks()
        if turn != 3:
            turn += 1
        else:
            turn = 0
        
    pygame.display.flip()