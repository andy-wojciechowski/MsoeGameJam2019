import pygame
import sys
from pygame.locals import QUIT
from core.platform import Platform


def main():
    pygame.init()

    pygame.display.set_mode((1000, 700), 0, 32)
    # TODO: Update this Title
    pygame.display.set_caption('Hello World')

    temp = Platform(300, 300)
    temp.update()
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()


if __name__ == "__main__":
    main()
