import pygame
import sys
from game.player import Player
from game.level1 import Level1


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
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    player.move_right()
                elif event.key == pygame.K_LEFT:
                    player.move_left()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    player.stop()

        screen.fill((0, 0, 0))
        sprite_list.update()
        current_level.update()

        current_level.draw(screen)
        sprite_list.draw(screen)

        pygame.display.update()


if __name__ == "__main__":
    main()
