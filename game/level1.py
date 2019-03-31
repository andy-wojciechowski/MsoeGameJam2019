import pygame
from core.level import Level
from core.platform import Platform
from game.interdimensionalrift import InterDimensionalRift


class Level1(Level):
    def __init__(self, player):
        super().__init__(player, 600)

        self.player.rect.x = 10
        self.player.rect.y = 600

        self._setup_rifts()
        self._setup_platforms()

    def _setup_rifts(self):
        crate_image = pygame.image.load("img/RTS_Crate.png").convert()
        crate_image = pygame.transform.scale(crate_image, (75, 75))
        burning_crate = pygame.image.load("img/burning_crate00.png").convert()
        burning_crate = pygame.transform.scale(burning_crate, (75, 75))
        burning_crate.set_alpha(255)
        all_rift_images = [burning_crate, crate_image]
        level_rifts = [(all_rift_images, 150, 590),
                       (all_rift_images, 800, 373)]
        for rift in level_rifts:
            created_rift = InterDimensionalRift(rift[0])
            created_rift.rect.x = rift[1]
            created_rift.rect.y = rift[2]
            self.rift_list.add(created_rift)

    def _setup_platforms(self):
        level_platforms = [("img/Grass.png", 3, 775, 450),
                           ("img/Grass.png", 2, 575, 280)]
        for platform in level_platforms:
            platform_sprites = pygame.sprite.Group()
            current_x = platform[2]
            for _ in range(platform[1]):
                created_platform = Platform(platform[0], current_x, platform[3])
                platform_sprites.add(created_platform)
                current_x += created_platform.rect.width
            self.platform_list.append(platform_sprites)
