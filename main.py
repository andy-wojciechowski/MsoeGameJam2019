import pygame, sys
from pygame.locals import QUIT


def main():
    pygame.init()

    pygame.display.set_mode((1000, 700), 0, 32)
    # TODO: Update this Title
    pygame.display.set_caption('Hello World')

    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()


if __name__ == "__main__":
    main()
