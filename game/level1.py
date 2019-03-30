import pygame
from core.level import Level
from game.interdimensionalrift import InterDimensionalRift


class Level1(Level):
    def __init__(self, player):
        super().__init__(player, 600)

        self.player.rect.x = 10
        self.player.rect.y = 600

        self._setup_rifts()

    def _setup_rifts(self):
        crate_image = pygame.image.load("img/RTS_Crate.png").convert()
        crate_image = pygame.transform.scale(crate_image, (50, 50))
        all_rift_images = [pygame.image.load("img/barrel.png").convert(), crate_image]
        level_rifts = [(all_rift_images, 150, 600)]
        for rift in level_rifts:
            created_rift = InterDimensionalRift(rift[0])
            created_rift.rect.x = rift[1]
            created_rift.rect.y = rift[2]
            self.rift_list.add(created_rift)
