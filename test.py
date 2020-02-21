import pygame
import menu
import widget


pygame.init()
screen = pygame.display.set_mode((1600,1000))

icon = pygame.image.load("icon_game.png")
global launched
launched = False
global menu_launch
menu_launch = True

pygame.display.set_icon(icon)
pygame.display.set_caption("Planet Star")

menu_background = pygame.image.load("menu.png")
image = pygame.image.load("tets.jpg")
earth = pygame.image.load("earth.png")
jupiter = pygame.image.load("jupiter.png")
mars = pygame.image.load("mars.png")
sprite = pygame.image.load("spriteplanete.png")
incone_or = pygame.image.load("incone_or.jpg")
incone_or.convert()
launched = menu.display_menu(screen, menu_launch)

while launched:
    pygame.display.init()
    screen.blit(image, (0,0))
    screen.blit(earth, (20,50))
    screen.blit(jupiter, (120,30))
    screen.blit(mars, (250,65))
    screen.blit(sprite, (400,10))
    widget.print_incone(screen, incone_or)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pos()[0] >= 1500 and pygame.mouse.get_pos()[1] >= 900 \
            and pygame.mouse.get_pos()[0] <= 1600 and pygame.mouse.get_pos()[1] <= 1000:
                widget.widget();
    pygame.display.flip()