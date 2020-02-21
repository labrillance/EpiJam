import pygame
from pygame import *

validChars = "`1234567890°+azertyuiop^$qsdfghjklmùwxcvbn,;:!"
shiftChars = '~!@#$%^&*()_+QWERTYUIOP{}|ASDFGHJKL:"ZXCVBNM<>?'

pygame.font.init()
class TextBox(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.text = ""
    self.font = pygame.font.Font("./fonts/Andromeda-eR2n.ttf", 72)
    self.image = self.font.render("Enter your name", True, [255, 255, 255])
    self.rect = self.image.get_rect()

  def add_chr(self, char):
    global shiftDown
    if char in validChars and not shiftDown:
        self.text += char
    elif char in validChars and shiftDown:
        self.text += shiftChars[validChars.index(char)]
    self.update()

  def update(self):
    old_rect_pos = self.rect.center
    if (len(self.text) > 0):
        self.image = self.font.render(self.text, True, [255, 255, 255])
    else:
        self.image = self.font.render("Enter your name", True, [255, 255, 255])
    self.rect = self.image.get_rect()
    self.rect.center = old_rect_pos

textBox = TextBox()
shiftDown = False
textBox.rect.center = [300, 700]
play_button = pygame.image.load("button_play.png")
font = pygame.font.Font("./fonts/Andromeda-eR2n.ttf", 30)
p1, p2, p3, p4 = "Player 1", "Player 2", "Player 3", "Player 4"
p1, p2, p3, p4 = font.render(p1, True, (255,255,255)), font.render(p2, True, (255,255,255)), font.render(p3, True, (255,255,255)), font.render(p4, True, (255,255,255))

def display_menu(screen, menu_launch):
    scrrec = screen.get_rect()
    menu_background_or = pygame.image.load("menu.png").convert()
    menu_background = menu_background_or
    menu_background = pygame.transform.scale(menu_background, (scrrec.right, scrrec.bottom))
    nb_players = 0
    list_players = ["", "", "", ""]
    while menu_launch:
        pygame.display.init()
        screen.blit(menu_background, (0,0))
        screen.blit(textBox.image, textBox.rect)
        pl1, pl2, pl3, pl4 = font.render(list_players[0], True, (255,255,255)), font.render(list_players[1], True, (255,255,255)), font.render(list_players[2], True, (255,255,255)), font.render(list_players[3], True, (255,255,255))
        screen.blit(p1, (1200, 200))
        screen.blit(p2, (1200, 270))
        screen.blit(p3, (1200, 340))
        screen.blit(p4, (1200, 410))
        screen.blit(pl1, (1350, 200))
        screen.blit(pl2, (1350, 270))
        screen.blit(pl3, (1350, 340))
        screen.blit(pl4, (1350, 410))
        if (nb_players >= 4):
            screen.blit(play_button, (1175, 792))
        x, y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                menu_launch = False
            if event.type == VIDEORESIZE:
                menu_background = menu_background_or
                menu_background = pygame.transform.scale(menu_background, (event.w, event.h))

            if event.type == pygame.KEYUP:
                if event.key in [pygame.K_RSHIFT, pygame.K_LSHIFT]:
                    shiftDown = False
            if event.type == pygame.KEYDOWN:
                textBox.add_chr(event.dict['unicode'])
                if event.key == pygame.K_SPACE:
                    textBox.text += " "
                    textBox.update()
                if event.key in [pygame.K_RSHIFT, pygame.K_LSHIFT]:
                    shiftDown = True
                if event.key == pygame.K_BACKSPACE:
                    textBox.text = textBox.text[:-1]
                    textBox.update()
                if event.key == pygame.K_RETURN:
                    if len(textBox.text) > 0 and nb_players < 4:
                        list_players[nb_players] = textBox.text
                        textBox.text = ""
                        textBox.update()
                        nb_players += 1
            if event.type == pygame.MOUSEBUTTONDOWN :
                if event.button == 1 and x > 1175 and x < 1775 + 225 and y > 792 and y < 792 + 75 and nb_players >= 4:
                    launched = True
                    menu_launch = False
                    return list_players
        pygame.display.flip()
