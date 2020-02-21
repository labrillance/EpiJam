import pygame


validChars = "`1234567890°+azertyuiop^$qsdfghjklmùwxcvbn,;:!"
shiftChars = '~!@#$%^&*()_+QWERTYUIOP{}|ASDFGHJKL:"ZXCVBNM<>?'

pygame.font.init()
class TextBox(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.text = ""
    self.font = pygame.font.SysFont("andromeda Moyen", 72)
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
menu_background = pygame.image.load("menu.png")

def display_menu(screen, menu_launch):
    nb_players = 0
    list_players = ["", "", "", ""]
    while menu_launch:
        pygame.display.init()
        screen.blit(menu_background, (0,0))
        screen.blit(textBox.image, textBox.rect)
        x, y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu_launch = False
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
                        print(list_players)
                        textBox.text = ""
                        textBox.update()
                        nb_players += 1
            if event.type == pygame.MOUSEBUTTONDOWN :
                if event.button == 1 and x > 1175 and x < 1775 + 225 and y > 792 and y < 792 + 75 :
                    launched = True
                    menu_launch = False
                    return launched
        pygame.display.flip()
