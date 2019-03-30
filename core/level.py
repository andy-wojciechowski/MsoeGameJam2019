import pygame
from abc import ABC


class Level(ABC):
    def __init__(self, player):
        self.platform_list = pygame.sprite.Group()
        self.rift_list = pygame.sprite.Group()
        self.player = player

    def update(self):
        self.platform_list.update()
        self.rift_list.update()
        self._handle_player_collision(self.platform_list)
        self._handle_player_collision(self.rift_list)

    def draw(self, screen):
        self.platform_list.draw(screen)
        self.rift_list.draw(screen)

    def _handle_player_collision(self, sprites_to_check):
        for sprite in sprites_to_check:
            if sprite != self.player.sprite_grounded_on:
                if pygame.sprite.collide_rect(sprite, self.player):
                    self.player.stop(sprite_collided_with=sprite)
