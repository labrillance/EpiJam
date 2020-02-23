import pygame
from pygame import *
import init.init as classes
from random import randrange

def init_planete():
    planete = []

    planete.append(random_planete(4, 179, 67, 32, 32, "Lune 1"))
    planete.append(random_planete(4, 215, 184, 32, 32, "Lune 2"))
    planete.append(random_planete(4, 321, 201, 32, 32, "Lune 3"))
    planete.append(random_planete(4, 246, 617, 32, 32, "Lune 4"))
    planete.append(random_planete(4, 158, 675, 32, 32, "Lune 5"))
    planete.append(random_planete(4, 161, 789, 32, 32, "Lune 6"))
    planete.append(random_planete(4, 739, 222, 32, 32, "Lune 7"))
    planete.append(random_planete(4, 574, 342, 32, 32, "Lune 8"))
    planete.append(random_planete(4, 646, 576, 32, 32, "Lune 9"))
    planete.append(random_planete(4, 1020, 346, 32, 32, "Lune 10"))
    planete.append(random_planete(4, 990, 600, 32, 32, "Lune 11"))
    planete.append(random_planete(4, 1337, 28, 32, 32, "Lune 12"))
    planete.append(random_planete(4, 1330, 146, 32, 32, "Lune 13"))
    planete.append(random_planete(4, 1232, 197, 32, 32, "Lune 14"))
    planete.append(random_planete(4, 1248, 596, 32, 32, "Lune 15"))
    planete.append(random_planete(4, 1333, 647, 32, 32, "Lune 16"))
    planete.append(random_planete(4, 1340, 773, 32, 32, "Lune 17"))
    planete.append(random_planete(1, 579, 732, 63, 65, "BB8"))
    planete.append(random_planete(1, 647, 83, 63, 65, "Lodoth"))
    planete.append(random_planete(3, 701, 393, 180, 180, "Mudrehiri"))
    planete.append(random_planete(0, 271, 33, 96, 92, "TERRA1"))
    planete.append(random_planete(-1, 257, 730, 92, 93, "TERR2"))
    planete.append(random_planete(-2, 1186, 27, 96, 94, "TERRA3"))
    planete.append(random_planete(-3, 1187, 718, 90, 94, "TERRA4"))
    planete.append(random_planete(1, 413, 201, 68, 65, "Gisiuhiri"))
    planete.append(random_planete(2, 66, 368, 141, 143, "Agora"))
    planete.append(random_planete(1, 334, 390, 66, 67, "Nion"))
    planete.append(random_planete(1, 445, 579, 64, 64, "Bromia"))
    planete.append(random_planete(1, 857, 178, 65, 64, "Namides"))
    planete.append(random_planete(1, 999, 108, 61, 61, "Cetania"))
    planete.append(random_planete(2, 1395, 361, 148, 146, "Team JUL"))
    planete.append(random_planete(1, 1115, 497, 64, 63, "Treaclite"))
    planete.append(random_planete(1, 1263, 339, 65, 63, "Cezuno"))
    planete.append(random_planete(1, 950, 771, 62, 62, "Sailia"))
    planete.append(random_planete(1, 773, 658, 64, 62, "R2D2"))

    return (planete)

def random_planete(taille, posx, posy, long, larg, name):
    result = classes.planete()
    result.name = name
    result.x = posx
    result.y = posy
    result.long = long
    result.larg = larg
    if taille < 0:
        result.gold = 35
        result.oil = 130
        result.iron = 580
        result.colonise = taille * -1
    if taille == 1:
        result.gold = randrange(7, 20)
        result.oil = randrange(20, 60)
        result.iron = randrange(100, 300)
    if taille == 2:
        result.gold = randrange(15, 50)
        result.oil = randrange(60, 180)
        result.iron = randrange(350, 800)
    if taille == 3:
        result.gold = randrange(35, 100)
        result.oil = randrange(150, 340)
        result.iron = randrange(650, 1200)
    if taille == 4:
        i = randrange(0, 3)
        if (i == 0):
            result.gold = randrange(15, 50)
        if (i == 1):
            result.oil = randrange(60, 180)
        if (i == 2):
            result.iron = randrange(350, 800)
    return result