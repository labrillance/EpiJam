import pygame
import menu
from pygame.locals import *
import os
import widget
import planete
import init.init as classes
import math

pygame.init()

#---------------------------INITIALISATION WINDOW---------------------------------#

#info fenêtre utilisateur
infoObject = pygame.display.Info()

#création de la fenêtre principale
screen = pygame.display.set_mode((infoObject.current_w, infoObject.current_h), 0)

#---------------------------LOAD SPRITE AND ICONE----------------------------------#

icon = pygame.image.load("textures/icon_game.png")
image = pygame.image.load("textures/tets.jpg")
overlay = [pygame.image.load("textures/overlayplayer1.png"), pygame.image.load("textures/overlayplayer2.png"), pygame.image.load("textures/overlayplayer3.png"), pygame.image.load("textures/overlayplayer4.png")]
popup = pygame.image.load("textures/popup.png")
little1 = pygame.image.load("textures/little1.png")
middle1 = pygame.image.load("textures/middle1.png")
big = pygame.image.load("textures/big.png")
gold = pygame.image.load("textures/icon_gold.png")
iron = pygame.image.load("textures/icon_iron.png")
oil = pygame.image.load("textures/oil_icon.png")
#---------------------------FONT---------------------------------------------------

#---------------------------FONT---------------------------------------------------#

font = pygame.font.Font("./fonts/Andromeda-eR2n.ttf", round((infoObject.current_w * infoObject.current_h * 45 / (1920 * 1080))))

#---------------------------init variable and GLOBAL-------------------------------#

global launched
launched = False
global menu_launch
menu_launch = True
turn = 0
print_inf = 0
#---------------------------PYGAME.DISPLAY-----------------------------------------

#---------------------------PYGAME.DISPLAY-----------------------------------------#

pygame.display.set_icon(icon)
pygame.display.set_caption("Planet Star")

#---------------------------SCALE--------------------------------------------------#

image = pygame.transform.scale(image, (infoObject.current_w, infoObject.current_h))
overlay = [pygame.transform.scale(overlay[0], (infoObject.current_w, infoObject.current_h)), pygame.transform.scale(overlay[1], (infoObject.current_w, infoObject.current_h)), pygame.transform.scale(overlay[2], (infoObject.current_w, infoObject.current_h)), pygame.transform.scale(overlay[3], (infoObject.current_w, infoObject.current_h))]
little1 = pygame.transform.scale(little1, (round(infoObject.current_w * 60 / 1920), round(infoObject.current_h * 60 / 1080)))
middle1 = pygame.transform.scale(middle1, (round(infoObject.current_w * 190 / 1920), round(infoObject.current_h * 173 / 1080)))
big = pygame.transform.scale(big, (round(infoObject.current_w * 180 / 1980), round(infoObject.current_h * 180 / 1020)))
gold = pygame.transform.scale(gold, (round(infoObject.current_w * 70 / 1600), round(infoObject.current_h * 70 / 1000)))
iron = pygame.transform.scale(iron, (round(infoObject.current_w * 70 / 1600), round(infoObject.current_h * 70 / 1000)))
oil = pygame.transform.scale(oil, (round(infoObject.current_w * 70 / 1600), round(infoObject.current_h * 70 / 1000)))
#---------------------------Function-----------------------------------------------

#---------------------------Function-----------------------------------------------#
def init_players(list):
    i = 0
    players = []
    x = [50, 160, 1350, 1450]
    y = [735, 35, 35, 735]
    while i <= 3:
        
        players.append(classes.player())
        players[i].name = list[i]
        players[i].name = font.render(players[i].name, True, (0,0,0))
        players[i].gold = 0
        players[i].oil = 0
        players[i].iron = 0
        players[i].bases.prop = list[i]
        players[i].bases.posx = infoObject.current_w * x[i] / 1600
        players[i].bases.posy = infoObject.current_h * y[i] / 1000
        i += 1
    return players

def create_texture(pl, oil, gold, iron):
    nb_gold_text = font.render(str(pl.gold), True, (0, 128, 0))
    nb_oil_text = font.render(str(pl.oil), True, (0, 128, 0))
    nb_iron_text = font.render(str(pl.iron), True, (0, 128, 0))
    screen.blit(gold, (infoObject.current_w * 20 / 1600, infoObject.current_h * 900 / 1000))
    screen.blit(nb_gold_text, (infoObject.current_w * 90 / 1600, infoObject.current_h * 910 / 1000))
    screen.blit(iron, (infoObject.current_w * 190 / 1600, infoObject.current_h * 900 / 1000))
    screen.blit(nb_iron_text, (infoObject.current_w * 260 / 1600, infoObject.current_h * 910 / 1000))
    screen.blit(oil, (infoObject.current_w * 360 / 1600, infoObject.current_h * 900 / 1000))
    screen.blit(nb_oil_text, (infoObject.current_w * 430 / 1600, infoObject.current_h * 910 / 1000))
#---------------------------/function---------------------------------------------
#---------------------------/function----------------------------------------------#

planete.random_planete(1, 1, 1, 1, 1)
list = menu.display_menu(screen, menu_launch)
if (len(list) == 4):
    launched = True

players = init_players(list)
clock_turn = pygame.time.get_ticks()
seconds = ""
disp_base_info = False

while launched:    
    pygame.display.init()
    screen.blit(image, (0,0))
    screen.blit(overlay[turn], (0, 0))

    screen.blit(players[turn].name, (infoObject.current_w * 20 / 1600, infoObject.current_h * 871 / 1000))
    create_texture(players[turn], oil, gold, iron)
    seconds = str(int(((20 - (pygame.time.get_ticks() - clock_turn) / 1000))))
    sec = int(seconds)
    seconds = font.render(seconds, True, (0,0,0))
    screen.blit(seconds, (infoObject.current_w * 1520 / 1600, infoObject.current_h * 8 / 1000))
    if disp_base_info:
        screen.blit(popup, (95, 680))
    for event in pygame.event.get():
        if disp_base_info != True:
            x1, y1 = pygame.mouse.get_pos()
            x2, y2 = 95, 835
            distance = math.hypot(x1 - x2, y1 - y2)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and distance <= 45:
                    disp_base_info = True
        if event.type == pygame.QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            launched = False
        if (event.type == KEYDOWN and event.key == K_RETURN):
            clock_turn = pygame.time.get_ticks()
            if turn != 3:
                turn += 1
            else:
                turn = 0
        if event.type == pygame.MOUSEBUTTONDOWN:
            if (print_inf % 2 == 0 and infoObject.current_w * 1400 / 1600, infoObject.current_h  * 600 / 1000, infoObject.current_w * 200 / 1600, infoObject.current_h  * 400 / 1000):
                print_inf += 1
                rect = (infoObject.current_w * 1400 / 1600, infoObject.current_h  * 800 / 1000, infoObject.current_w * 200 / 1600, infoObject.current_h  * 200 / 1000)
            elif (print_inf % 2 != 0 and infoObject.current_w * 1400 / 1600, infoObject.current_h  * 600 / 1000, infoObject.current_w * 200 / 1600, infoObject.current_h  * 400 / 1000):
                print_inf = 0
    if sec <= 0:
        clock_turn = pygame.time.get_ticks()
        if turn != 3:
            turn += 1
        else:
            turn = 0
    pygame.display.flip()