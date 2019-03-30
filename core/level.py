import pygame
from abc import ABC


class Level(ABC):
    def __init__(self, player, ground_factor):
        self.rift_list = pygame.sprite.Group()
        self.platform_list = pygame.sprite.Group()
        self.player = player
        self.ground_factor = ground_factor

    def update(self):
        self.rift_list.update()
        self.platform_list.update()
        self._handle_rift_player_collisions()
        if self.player.is_jumping and self.player.rect.y >= self.ground_factor:
            self.player.rect.y = self.ground_factor
            self.player.stop()
            self.player.is_grounded = True

    def draw(self, screen):
        self.rift_list.draw(screen)
        self.platform_list.draw(screen)

    def handle_rift_close(self):
        for rift in self.rift_list:
            if pygame.sprite.collide_rect(rift, self.player):
                rift.close()

    def _handle_rift_player_collisions(self):
        for rift in self.rift_list:
            if pygame.sprite.collide_rect(self.player, rift):
                rift.handle_player_collision(self.player)
