import pygame
from abc import ABC


class Level(ABC):
    def __init__(self, player, ground_factor):
        self.rift_list = pygame.sprite.Group()
        self.platform_list = []
        self.player = player
        self.ground_factor = ground_factor

    def update(self):
        self.rift_list.update()
        for platform_group in self.platform_list:
            platform_group.update()
        self._handle_rift_player_collisions()
        self._handle_platform_collisions()
        if self.player.rect.y >= self.ground_factor:
            self.player.rect.y = self.ground_factor
            self.player.stop()
            self.player.is_grounded = True
            self.player.sprite_grounded_on = None
            self.player.sprite_grounded_on_multiplier = 1

    def draw(self, screen):
        self.rift_list.draw(screen)
        for platform_group in self.platform_list:
            platform_group.draw(screen)

    def handle_rift_close(self):
        for rift in self.rift_list:
            if pygame.sprite.collide_rect(rift, self.player):
                rift.close()

    def _handle_rift_player_collisions(self):
        for rift in self.rift_list:
            if pygame.sprite.collide_rect(self.player, rift):
                rift.handle_player_collision(self.player)

    def _handle_platform_collisions(self):
        for platform_group in self.platform_list:
            for platform in platform_group:
                if pygame.sprite.collide_rect(self.player, platform):
                    if self.player.is_jumping and self.player.rect.y >= (platform.rect.y - platform.rect.height):
                        self.player.rect.y = platform.rect.y - platform.rect.height + 20
                        self.player.stop()
                        self.player.is_grounded = True
                        self.player.sprite_grounded_on = platform
                        self.player.sprite_grounded_on_multiplier = len(platform_group.sprites())
