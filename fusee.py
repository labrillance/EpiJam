import pygame
from pygame import *
import init.init as classes
from random import randrange
import math
#---------------------------------------------------------

def init_fusée():
    fusee = []

    fusee[0] 
    fusee[1]
    fusee[2]
    fusee[3]

def getdistance(xplanete1, yplanete1, xplanete2, yplanete2):
    xdist = xplanete1 - xplanete2
    ydist = yplanete1 - yplanete2
    xdist = math.sqrt(math.pow(xdist, 2))
    ydist = math.sqrt(math.pow(ydist, 2))
    return math.sqrt(math.pow(xdist, 2) + math.pow(ydist, 2))

def endfusee():
    #if coordonnées == planete2 -> return 0
    sale = 0

def getangle(xplanete1, yplanete1, xplanete2, yplanete2):
    return math.atan((yplanete1 - yplanete2) / (xplanete1 - xplanete2))

def send_fusée(fusee, xplanete1, yplanete1, xplanete2, yplanete2):
    #int fusée pour que l'animation se fasse
    if fusee == 1:
        if endfusee() == 0:
            fusee = 0
        else:
            mdr = 0
            angle = getangle(xplanete1, yplanete1, xplanete2, yplanete2)
            #recup la rotation en fonction de la diff entre les 2 planetes
            #rotate le sprite
            distancepixel = getdistance(xplanete1, yplanete1, xplanete2, yplanete2)
            #convertir la distance en coordonnées
            #drwlafusée
            
#---------------------------------------------------------