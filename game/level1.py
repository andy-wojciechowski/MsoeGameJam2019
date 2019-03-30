import pygame
from core.level import Level
from core.platform import Platform
from game.interdimensionalrift import InterDimensionalRift


class Level1(Level):
    def __init__(self, player):
        super().__init__(player)

        self.player.rect.x = 10
        self.player.rect.y = 369

        self._setup_platforms()
        self._setup_rifts()

    def _setup_platforms(self):
        level_platforms = [(1000, 350, 0, 400)]
        for platform in level_platforms:
            created_platform = Platform(platform[0], platform[1])
            created_platform.rect.x = platform[2]
            created_platform.rect.y = platform[3]
            self.player.sprite_grounded_on = created_platform
            self.platform_list.add(created_platform)

    def _setup_rifts(self):
        crate_image = pygame.image.load("RTS_Crate.png").convert()
        crate_image = pygame.transform.scale(crate_image, (50, 50))
        all_rift_images = [pygame.image.load("barrel.png").convert(), crate_image]
        level_rifts = [(all_rift_images, 150, 335)]
        for rift in level_rifts:
            created_rift = InterDimensionalRift(rift[0])
            created_rift.rect.x = rift[1]
            created_rift.rect.y = rift[2]
            self.rift_list.add(created_rift)
