import pygame
import menu
from pygame.locals import *
import os
import widget
import planete
import init.init as classes
import math
import fusee

pygame.init()

#---------------------------INITIALISATION WINDOW---------------------------------#

#info fenêtre utilisateur
infoObject = pygame.display.Info()

#création de la fenêtre principale
screen = pygame.display.set_mode((infoObject.current_w, infoObject.current_h), HWSURFACE | DOUBLEBUF | FULLSCREEN)

#---------------------------LOAD SPRITE AND ICONE----------------------------------#

icon = pygame.image.load("textures/icon_game.png")
image = pygame.image.load("textures/tets.jpg")
overlay = [pygame.image.load("textures/overlayplayer1.png"), pygame.image.load("textures/overlayplayer2.png"), pygame.image.load("textures/overlayplayer3.png"), pygame.image.load("textures/overlayplayer4.png")]
popup = pygame.image.load("textures/popup.png")
gold = pygame.image.load("textures/icon_gold.png")
iron = pygame.image.load("textures/icon_iron.png")
oil = pygame.image.load("textures/oil_icon.png")
fusee = pygame.image.load("textures/fusee.png")
btnatk = pygame.image.load("textures/btnatk+.png")
btndef = pygame.image.load("textures/btndef+.png")
btnvit = pygame.image.load("textures/btnvit+.png")
btncolo = pygame.image.load("textures/btncolo.png")

#---------------------------FONT---------------------------------------------------#

font = pygame.font.Font("./fonts/Andromeda-eR2n.ttf", round((infoObject.current_w * infoObject.current_h * 45 / (1920 * 1080))))

#---------------------------init variable and GLOBAL-------------------------------#

global launched
launched = False
global menu_launch
pop_up_id =-1
menu_launch = True
turn = 0
print_inf = 0
color = [(33, 129, 213), (243, 47, 47), (72, 213, 33), (219, 0, 255)]
price_fusee_atk = []
price_fusee_atk.append(500)
price_fusee_atk.append(600)
price_fusee_shild = []
price_fusee_shild.append(10)
price_fusee_shild.append(500)
send_fusee = 1

#---------------------------PYGAME.DISPLAY-----------------------------------------#

pygame.display.set_icon(icon)
pygame.display.set_caption("Planet Star")

#---------------------------SCALE--------------------------------------------------#

image = pygame.transform.scale(image, (infoObject.current_w, infoObject.current_h))
overlay = [pygame.transform.scale(overlay[0], (infoObject.current_w, infoObject.current_h)), pygame.transform.scale(overlay[1], (infoObject.current_w, infoObject.current_h)), pygame.transform.scale(overlay[2], (infoObject.current_w, infoObject.current_h)), pygame.transform.scale(overlay[3], (infoObject.current_w, infoObject.current_h))]
gold = pygame.transform.scale(gold, (round(infoObject.current_w * 70 / 1600), round(infoObject.current_h * 70 / 1000)))
iron = pygame.transform.scale(iron, (round(infoObject.current_w * 70 / 1600), round(infoObject.current_h * 70 / 1000)))
oil = pygame.transform.scale(oil, (round(infoObject.current_w * 70 / 1600), round(infoObject.current_h * 70 / 1000)))
fusee = pygame.transform.scale(fusee, (round(infoObject.current_w * 180 / 1600), round(infoObject.current_h * 90 / 1000)))
btnatk = pygame.transform.scale(btnatk, (round(infoObject.current_w * 200 / 1600), round(infoObject.current_h * 120 / 1000)))
btndef = pygame.transform.scale(btndef, (round(infoObject.current_w * 200 / 1600), round(infoObject.current_h * 120 / 1000)))
btnvit = pygame.transform.scale(btnvit, (round(infoObject.current_w * 200 / 1600), round(infoObject.current_h * 120 / 1000)))
btncolo = pygame.transform.scale(btncolo, (round(infoObject.current_w * 200 / 1600), round(infoObject.current_h * 120 / 1000)))
popup = pygame.transform.scale(popup, (infoObject.current_w, infoObject.current_h))

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

def info_display_on_click(event, disp_base_info, x1, y1, pop_up_id):
    if disp_base_info != True:
        i = 0
        while i < len(all_planete) and disp_base_info != True: 
            x2, y2 = infoObject.current_w * (all_planete[i].x + (all_planete[i].long / 2)) / 1600, infoObject.current_h  * (all_planete[i].y + (all_planete[i].larg / 2)) / 1000
            distance = math.hypot(x1 - x2, y1 - y2)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and distance <= all_planete[i].long / 2:
                    disp_base_info = True
                    pop_up_id = i
            i += 1
    else:
        i = 0
        tmp1, tmp2 = infoObject.current_w * 1380 / 1920, infoObject.current_h * 163 / 1080
        tmpdist = math.hypot(x1- tmp1, y1 - tmp2)
        if event.type == pygame.MOUSEBUTTONDOWN and (event.button == 1 and tmpdist <= infoObject.current_w * 24 / 1920):
            disp_base_info = False
        while i < len(all_planete) and disp_base_info != False:
            x2, y2 = infoObject.current_w * (all_planete[i].x + (all_planete[i].long / 2)) / 1600, infoObject.current_h  * (all_planete[i].y + (all_planete[i].larg / 2)) / 1000
            distance = math.hypot(x1 - x2, y1 - y2)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and distance <= infoObject.current_w * (all_planete[i].long / 2) / 1600:
                    disp_base_info = False
            i += 1
    return disp_base_info, pop_up_id

def create_texture(pl, oil, gold, iron, all_planete):
    nb_gold_text = font.render(str(pl.gold), True, (255, 255, 255))
    nb_oil_text = font.render(str(pl.oil), True, (255, 255, 255))
    nb_iron_text = font.render(str(pl.iron), True, (255, 255, 255))
    screen.blit(gold, (round(infoObject.current_w * 20 / 1600), round(infoObject.current_h * 900 / 1000)))
    screen.blit(nb_gold_text, (round(infoObject.current_w * 100 / 1600), round(infoObject.current_h * 920 / 1000)))
    screen.blit(iron, (round(infoObject.current_w * 190 / 1600), round(infoObject.current_h * 900 / 1000)))
    screen.blit(nb_iron_text, (round(infoObject.current_w * 270 / 1600), round(infoObject.current_h * 920 / 1000)))
    screen.blit(oil, (round(infoObject.current_w * 360 / 1600), round(infoObject.current_h * 900 / 1000)))
    screen.blit(nb_oil_text, (round(infoObject.current_w * 440 / 1600), round(infoObject.current_h * 920 / 1000)))
    screen.blit(pygame.transform.rotate(fusee, 90), (round(infoObject.current_w * 1100 / 1600), round(infoObject.current_h * 840 / 1000)))
    screen.blit(btnatk, (round(infoObject.current_w * 1200 / 1600), round(infoObject.current_h * 880 / 1000)))
    screen.blit(btndef, (round(infoObject.current_w * 1400 / 1600), round(infoObject.current_h * 880 / 1000)))

def print_aire(all, id):
    for i in range(len(all)):
        if all[i].colonise != 0:
            pygame.draw.circle(screen, color[all[i].colonise - 1], [int(infoObject.current_w * (all[i].x + (all[i].long / 2)) / 1600), int(infoObject.current_h * (all[i].y + all[i].larg / 2) / 1000)], int(infoObject.current_w * (all[i].long / 2 + 10) / 1600), 2)

def add_planete_colonise(player, all_planete, turn):
    for i in range (0, 35):
        if all_planete[i].colonise == turn + 1:
            players[turn].gold += all_planete[i].gold
            players[turn].oil += all_planete[i].oil
            players[turn].iron += all_planete[i].iron
    return players[turn]

def bouton_fusee(player, x, y):
    if event.type == pygame.MOUSEBUTTONDOWN:
        if x > infoObject.current_w * 1200 / 1600 and x < infoObject.current_w  * 1400 / 1600 and y > infoObject.current_h * 880 / 1000 and y < infoObject.current_h and player.gold - price_fusee_atk[0] > 0 and player.iron - price_fusee_atk[1] > 0:
            player.gold -= price_fusee_atk[0]
            player.iron -= price_fusee_atk[1]
            player.fusee.atk += 1
            price_fusee_atk[0] *= 5
            price_fusee_atk[1] *= 5
        if x > infoObject.current_w * 1400 / 1600 and x < infoObject.current_w and y > infoObject.current_h * 880 / 1000 and y < infoObject.current_h and player.gold - price_fusee_shild[0] > 0 and player.iron - price_fusee_shild[1] > 0:
            player.gold -= price_fusee_shild[0]
            player.iron -= price_fusee_shild[1]
            player.fusee.shild += 1
            price_fusee_shild[0] *= 5
            price_fusee_shild[1] *= 5

def buy_planete(event, player, planete):
    x, y = pygame.mouse.get_pos()
    if event.type == pygame.MOUSEBUTTONDOWN :
        if event.button == 1:# and x > infoObject.current_w * 1500 / 1600 and x < infoObject.current_w * (1500 + 93) / 1600 and y > infoObject.current_h * 903 / 1000 and y < infoObject.current_h * (903 + 91) / 1000:
            if planete.colonise == 0:
                planete.colonise == player


#---------------------------/function----------------------------------------------#
list = menu.display_menu(screen, menu_launch)
if (len(list) == 4):
    launched = True
all_planete = planete.init_planete()
players = init_players(list)
clock_turn = pygame.time.get_ticks()
seconds = ""
disp_base_info = False
players[0] = add_planete_colonise(players, all_planete, 0)
while launched:    
    pygame.display.init()
    x1, y1 = pygame.mouse.get_pos()
    screen.blit(image, (0,0))
    screen.blit(overlay[turn], (0, 0))

    print_aire(all_planete, turn)
    screen.blit(players[turn].name, (infoObject.current_w * 20 / 1600, infoObject.current_h * 871 / 1000))
    create_texture(players[turn], oil, gold, iron, all_planete)
    seconds = str(int(((20 - (pygame.time.get_ticks() - clock_turn) / 1000))))
    sec = int(seconds)
    seconds = font.render(seconds, True, (0,0,0))
    screen.blit(players[turn].name, (infoObject.current_w * 20 / 1600, infoObject.current_h * 871 / 1000))
    screen.blit(seconds, (infoObject.current_w * 1520 / 1600, infoObject.current_h * 8 / 1000))
    if disp_base_info:
        screen.blit(popup, (0, 0))
    for event in pygame.event.get():
        disp_base_info, pop_up_id = info_display_on_click(event, disp_base_info, x1, y1, pop_up_id )
        if event.type == pygame.QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            launched = False
        if (event.type == KEYDOWN and event.key == K_RETURN):
            clock_turn = pygame.time.get_ticks()
            if turn != 3:
                turn += 1
            else:
                turn = 0
            players[turn] = add_planete_colonise(players, all_planete, turn)
        bouton_fusee(players[turn], x1, y1)  
    if sec <= 0:
        clock_turn = pygame.time.get_ticks()
        if turn != 3:
            turn += 1
        else:
            turn = 0
        players[turn] = add_planete_colonise(players, all_planete, turn)
    pygame.display.flip()