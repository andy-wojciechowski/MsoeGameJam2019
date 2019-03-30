import pygame
from abc import ABC


class Level(ABC):
    def __init__(self, player, ground):
        self.rift_list = pygame.sprite.Group()
        self.player = player
        self.ground = ground

    def update(self):
        self.rift_list.update()
        self._stop_player_on_collision(self.rift_list)
        if self.player.is_jumping and self.player.rect.colliderect(self.ground.get_rect()):
            self.player.stop()

    def draw(self, screen):
        self.rift_list.draw(screen)

    def handle_rift_close(self):
        for rift in self.rift_list:
            if pygame.sprite.collide_rect(rift, self.player):
                rift.close()

    def _stop_player_on_collision(self, sprites_to_check):
        for sprite in sprites_to_check:
            if pygame.sprite.collide_rect(self.player, sprite):
                self.player.stop()
