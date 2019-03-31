import pygame
import sys
from game.player import Player
from game.level1 import Level1

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700


def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
    pygame.display.set_caption('Cross Dimensional Platformer')

    player_image = pygame.image.load("img/anim1.png").convert_alpha()
    player_image = pygame.transform.scale(player_image, (60, 60))

    background_image1 = pygame.image.load("img/Hills Layer 01.png").convert_alpha()
    background_image1 = pygame.transform.scale(background_image1, (SCREEN_WIDTH, SCREEN_HEIGHT))

    background_image2 = pygame.image.load("img/Hills Layer 02.png").convert_alpha()
    background_image2 = pygame.transform.scale(background_image2, (SCREEN_WIDTH, SCREEN_HEIGHT))

    background_image3 = pygame.image.load("img/Hills Layer 03.png").convert_alpha()
    background_image3 = pygame.transform.scale(background_image3, (SCREEN_WIDTH, SCREEN_HEIGHT))

    background_image4 = pygame.image.load("img/Hills Layer 04.png").convert_alpha()
    background_image4 = pygame.transform.scale(background_image4, (SCREEN_WIDTH, SCREEN_HEIGHT))

    background_image5 = pygame.image.load("img/Hills Layer 05.png").convert_alpha()
    background_image5 = pygame.transform.scale(background_image5, (SCREEN_WIDTH, SCREEN_HEIGHT))

    player = Player(player_image, SCREEN_WIDTH)
    current_level = Level1(player)

    sprite_list = pygame.sprite.Group()
    sprite_list.add(player)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    player.move_right = True
                elif event.key == pygame.K_LEFT:
                    player.move_left = True
                elif event.key == pygame.K_UP:
                    player.jump()
                elif event.key == pygame.K_f:
                    current_level.handle_rift_close()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    player.move_right = False
                elif event.key == pygame.K_LEFT:
                    player.move_left = False

        screen.fill((0, 0, 0))
        sprite_list.update()
        current_level.update()

        screen.blit(background_image1, (0, 0))
        screen.blit(background_image2, (0, 0))
        screen.blit(background_image3, (0, 0))
        screen.blit(background_image4, (0, 0))
        screen.blit(background_image5, (0, 0))

        current_level.draw(screen)
        sprite_list.draw(screen)

        pygame.display.flip()


if __name__ == "__main__":
    main()
