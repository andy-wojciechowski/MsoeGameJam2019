import pygame


class Platform(pygame.sprite.Sprite):
    def __init__(self, platform_image, x, y):
        super().__init__()
        self.image = pygame.image.load(platform_image)
        self.image = pygame.transform.scale(self.image, (75, 75))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def handle_player_collision(self, player):
        if player.is_jumping and player.rect.y >= (self.rect.y - self.rect.height):
            player.rect.y = self.rect.y - self.rect.height + 20
            player.stop()
            player.is_grounded = True
            player.sprite_grounded_on = self
