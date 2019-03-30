import pygame
import sys
from pygame.locals import QUIT
from game.player import Player
from game.Level1 import Level1


def main():
    pygame.init()

    player = Player(pygame.image.load("anim1.png"))
    current_level = Level1(player)

    sprite_list = pygame.sprite.Group()
    sprite_list.add(player)

    screen = pygame.display.set_mode((1000, 700), 0, 32)
    # TODO: Update this Title
    pygame.display.set_caption('Hello World')

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        sprite_list.update()
        current_level.update()

        current_level.draw(screen)
        sprite_list.draw(screen)
        
        pygame.display.update()


if __name__ == "__main__":
    main()
