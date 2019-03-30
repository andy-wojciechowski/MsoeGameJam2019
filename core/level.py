import pygame
from abc import ABC


class Level(ABC):
    def __init__(self, player):
        self.rift_list = pygame.sprite.Group()
        self.player = player

    def update(self):
        self.rift_list.update()
        self._stop_player_on_collision(self.rift_list)

    def draw(self, screen):
        self.rift_list.draw(screen)

    def handle_rift_close(self):
        for rift in self.rift_list:
            if pygame.sprite.collide_rect(rift, self.player):
                rift.close()

    def _stop_player_on_collision(self, sprites_to_check):
        for sprite in sprites_to_check:
            if sprite != self.player.sprite_grounded_on:
                if pygame.sprite.collide_rect(sprite, self.player):
                    self.player.stop(sprite_collided_with=sprite)
