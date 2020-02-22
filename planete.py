import pygame
from pygame import *
import init.init as classes
from random import randrange

def random_planete(taille, posx, posy, long, larg):
    names_planetes = ["Gisiuhiri", "Mudrehiri", "Lodoth", "Namides", "Cetania", "Cezuno", "Treaclite", "Sailia", "Bromia ALO", "Nion 7FJ", "Team JUL", "R2D2", "Tibz", "Smash", "Coca", "Iris"]
    nombreAleatoire = randrange(0,16)
    print("nombre %d" % nombreAleatoire)
    name = names_planetes[nombreAleatoire]

    classes.planete.name = name
    print(classes.planete.name)
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
