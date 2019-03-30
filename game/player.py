import pygame

PLAYER_SPEED = 1


class Player(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()

        self.delta_x = 0

    def update(self):
        self.rect.x += self.delta_x

    def move_right(self):
        self.delta_x += PLAYER_SPEED

    def move_left(self):
        self.delta_x -= PLAYER_SPEED

    def stop(self):
        self.delta_x = 0
