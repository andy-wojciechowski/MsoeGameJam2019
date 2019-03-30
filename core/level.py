import pygame
from abc import ABC


class Level(ABC):
    def __init__(self, player):
        self.platform_list = pygame.sprite.Group()
        self.player = player

    def update(self):
        self.platform_list.update()

    def draw(self, screen):
        self.platform_list.draw(screen)
