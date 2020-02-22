import pygame
from pygame import *
import init.init as classes
from random import randrange

def random_planete(taille, posx, posy, long, larg, name):
    classes.planete.name = name
    classes.planete.x = posx
    classes.planete.y = posy
    classes.planete.long = long
    classes.planete.larg = larg
    if taille == 1:
        classes.planete.gold = randrange(7, 20)
        classes.planete.oil = randrange(20, 60)
        classes.planete.iron = randrange(100, 300)
    if taille == 2:
        classes.planete.gold = randrange(15, 50)
        classes.planete.oil = randrange(60, 180)
        classes.planete.iron = randrange(350, 800)
    if taille == 3:
        classes.planete.gold = randrange(25, 100)
        classes.planete.oil = randrange(120, 340)
        classes.planete.iron = randrange(600, 1200)