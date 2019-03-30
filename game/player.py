import pygame

PLAYER_SPEED = 1


class Player(pygame.sprite.Sprite):
    def __init__(self, image, screen_width, screen_height):
        super().__init__()
        self.image = image
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.rect = self.image.get_rect()

        self.delta_x = 0

    def update(self):
        self.rect.x += self.delta_x
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.x > self.screen_width - 25:
            self.rect.x = self.screen_width - 25

    def move_right(self):
        self.delta_x += PLAYER_SPEED

    def move_left(self):
        self.delta_x -= PLAYER_SPEED

    def stop(self):
        self.delta_x = 0
