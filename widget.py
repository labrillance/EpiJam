import pygame

def widget():
    cont = True;
    pygame.init()
    resources = pygame.display.set_mode((1600, 1000))
    while cont:
        for event1 in pygame.event.get():
            
            if event1.type == pygame.QUIT:
                cont = False
            pygame.display.flip()

def print_incone(window, incone_or):
    rect_button = pygame.Rect(1500, 900, 100, 100)
    window.blit(incone_or, [1500, 896])
