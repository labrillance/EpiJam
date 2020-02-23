import pygame
from pygame import *
import init.init as classes
from random import randrange

def init_planete():
    planete = []

    planete.append(random_planete(4, 179, 67, 32, 32, "Lune 1", 10))
    planete.append(random_planete(4, 215, 184, 32, 32, "Lune 2", 10))
    planete.append(random_planete(4, 321, 201, 32, 32, "Lune 3", 10))
    planete.append(random_planete(4, 246, 617, 32, 32, "Lune 4", 10))
    planete.append(random_planete(4, 158, 675, 32, 32, "Lune 5", 10))
    planete.append(random_planete(4, 161, 789, 32, 32, "Lune 6", 10))
    planete.append(random_planete(4, 739, 222, 32, 32, "Lune 7", 10))
    planete.append(random_planete(4, 574, 342, 32, 32, "Lune 8", 10))
    planete.append(random_planete(4, 646, 576, 32, 32, "Lune 9", 10))
    planete.append(random_planete(4, 1020, 346, 32, 32, "Lune 10", 10))
    planete.append(random_planete(4, 990, 600, 32, 32, "Lune 11", 10))
    planete.append(random_planete(4, 1337, 28, 32, 32, "Lune 12", 10))
    planete.append(random_planete(4, 1330, 146, 32, 32, "Lune 13", 10))
    planete.append(random_planete(4, 1232, 197, 32, 32, "Lune 14", 10))
    planete.append(random_planete(4, 1248, 596, 32, 32, "Lune 15", 10))
    planete.append(random_planete(4, 1333, 647, 32, 32, "Lune 16", 10))
    planete.append(random_planete(4, 1340, 773, 32, 32, "Lune 17", 10))
    planete.append(random_planete(1, 579, 732, 63, 65, "BB8", 100))
    planete.append(random_planete(1, 647, 83, 63, 65, "Lodoth", 100))
    planete.append(random_planete(3, 701, 393, 180, 180, "Mudrehiri", 5000))
    planete.append(random_planete(-1, 271, 33, 96, 92, "TERRA1", 0))
    planete.append(random_planete(-2, 257, 730, 92, 93, "TERR2", 0))
    planete.append(random_planete(-3, 1186, 27, 96, 94, "TERRA3", 0))
    planete.append(random_planete(-4, 1187, 718, 90, 94, "TERRA4", 0))
    planete.append(random_planete(1, 413, 201, 68, 65, "Gisiuhiri", 100))
    planete.append(random_planete(2, 66, 368, 141, 143, "Agora", 500))
    planete.append(random_planete(1, 334, 390, 66, 67, "Nion", 100))
    planete.append(random_planete(1, 445, 579, 64, 64, "Bromia", 100))
    planete.append(random_planete(1, 857, 178, 65, 64, "Namides", 100))
    planete.append(random_planete(1, 999, 108, 61, 61, "Cetania", 100))
    planete.append(random_planete(2, 1395, 361, 148, 146, "Team JUL", 500))
    planete.append(random_planete(1, 1115, 497, 64, 63, "Treaclite", 100))
    planete.append(random_planete(1, 1263, 339, 65, 63, "Cezuno", 100))
    planete.append(random_planete(1, 950, 710, 62, 62, "Sailia", 100))
    planete.append(random_planete(1, 773, 658, 64, 62, "R2D2", 100))

    return (planete)

def random_planete(taille, posx, posy, long, larg, name, valeur):
    result = classes.planete()
    result.name = name
    result.x = posx
    result.y = posy
    result.long = long
    result.larg = larg
    result.colonise = 0
    result.valeur = valeur
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