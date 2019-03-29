import pygame, sys
from pygame.locals import QUIT

pygame.init()

window_surface = pygame.display.set_mode((800, 800), 0, 32)
#TODO: Update this Title
pygame.display.set_caption('Hello World')

pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
