import pygame
import test2
pygame.init()
screen = pygame.display.set_mode((1200,750))

launched = True
image = pygame.image.load("tets.jpg")
test2.coucou()
while launched:
    pygame.display.init()
    screen.blit(image, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False
    pygame.display.flip()