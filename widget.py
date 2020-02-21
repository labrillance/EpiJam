import pygame

def widget(window, fond, incone_or):
    cont = True;
    pygame.init()
    resources = pygame.display.set_mode((1600, 1000))
    while cont:
        window.blit(fond, [0, 0])
        print_incone(resources, incone_or)
        for event1 in pygame.event.get():
            
            if event1.type == pygame.QUIT:
                cont = False
            if event1.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pos()[0] >= 1500 and pygame.mouse.get_pos()[1] >= 900 \
            and pygame.mouse.get_pos()[0] <= 1600 and pygame.mouse.get_pos()[1] <= 1000:
                    cont = False
        pygame.display.flip()

def print_incone(window, incone_or):
    rect_button = pygame.Rect(1500, 900, 100, 100)
    window.blit(incone_or, [1500, 896])
