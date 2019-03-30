import pygame


class Platform(pygame.sprite.Sprite):
    def __init__(self, platform_image, x, y):
        super().__init__()
        self.image = pygame.image.load(platform_image)
        self.image = pygame.transform.scale(self.image, (75, 75))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

