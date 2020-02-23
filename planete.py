import pygame
from pygame import *
import init.init as classes
from random import randrange

def init_planete():
    planete = []

    planete[0] = random_planete(4, 179, 67, 32, 32, "Lune 1")
    planete[1] = random_planete(4, 215, 184, 32, 32, "Lune 2")
    planete[2] = random_planete(4, 321, 201, 32, 32, "Lune 3")
    planete[3] = random_planete(4, 246, 617, 32, 32, "Lune 4")
    planete[4] = random_planete(4, 158, 675, 32, 32, "Lune 5")
    planete[5] = random_planete(4, 161, 789, 32, 32, "Lune 6")
    planete[6] = random_planete(4, 739, 222, 32, 32, "Lune 7")
    planete[7] = random_planete(4, 574, 342, 32, 32, "Lune 8")
    planete[8] = random_planete(4, 646, 576, 32, 32, "Lune 9")
    planete[9] = random_planete(4, 1020, 346, 32, 32, "Lune 10")
    planete[10] = random_planete(4, 990, 600, 32, 32, "Lune 11")
    planete[11] = random_planete(4, 1337, 28, 32, 32, "Lune 12")
    planete[12] = random_planete(4, 1330, 146, 32, 32, "Lune 13")
    planete[13] = random_planete(4, 1232, 197, 32, 32, "Lune 14")
    planete[14] = random_planete(4, 1248, 596, 32, 32, "Lune 15")
    planete[15] = random_planete(4, 1333, 647, 32, 32, "Lune 16")
    planete[16] = random_planete(4, 1340, 773, 32, 32, "Lune 17")
    planete[32] = random_planete(1, 579, 732, 63, 65, "BB8")
    planete[33] = random_planete(1, 647, 83, 63, 65, "Lodoth")
    planete[34] = random_planete(3, 701, 393, 180, 180, "Mudrehiri")

def random_planete(taille, posx, posy, long, larg, name):
    result = classes.planete()
    result.name = name
    result.x = posx
    result.y = posy
    result.long = long
    result.larg = larg
    if taille == 0:
        result.gold = 35
        result.oil = 130
        result.iron = 580
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