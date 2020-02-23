import pygame
from pygame import *
import init.init as classes
from random import randrange
import math
#---------------------------------------------------------

def init_fusée():


def getdistance(xplanete1, yplanete1, xplanete2, yplanete2):
    xdist = xplanete1 - xplanete2
    ydist = yplanete1 - yplanete2
    xdist = math.sqrt(math.pow(xdist, 2))
    ydist = math.sqrt(math.pow(ydist, 2))
    return math.sqrt(math.pow(xdist, 2) + math.pow(ydist, 2))

def endfusee(xfusee, yfusee, xplanete2, yplanete2):
    #if coordonnées == planete2 -> return 0
    if (xfusee == xplanete2 and yfusee == yplanete2):
        return 0
    else:
        return 1

def getangle(xplanete1, yplanete1, xplanete2, yplanete2):
    return math.atan((yplanete1 - yplanete2) / (xplanete1 - xplanete2))

def sendfusee(fusee, xplanete1, yplanete1, xplanete2, yplanete2, send_fusee):
    xfusee = 0  #inserer classe fusee posx 
    yfusee = 0  #inserer classe fusee posy
    
    #int fusée pour que l'animation se fasse
    if fusee == 1:
        if endfusee(xfusee, yfusee, xplanete2, yplanete2) == 0:
            fusee = 0
        else:
            angle = getangle(xplanete1, yplanete1, xplanete2, yplanete2)
            #recup la rotation en fonction de la diff entre les 2 planetes

            pygame.transform.rotate(fusee.sprite, angle) #rotate sprite en fonction de l'angle

            distancepixel = getdistance(xplanete1, yplanete1, xplanete2, yplanete2)
            #convertir la distance en coordonnées
            #drwlafusée
    return 0
            
#---------------------------------------------------------