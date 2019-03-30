import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, image, screen_width):
        super().__init__()
        self.image = image
        self.screen_width = screen_width
        self.rect = self.image.get_rect()
        self.horizontal_speed = 1
        self.delta_x = 0
        self.vertical_velocity = 8
        self.mass = 1
        self.is_jumping = False

    def update(self):
        self.rect.x += self.delta_x
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.x > self.screen_width - 25:
            self.rect.x = self.screen_width - 25

        if self.is_jumping:
            if self.vertical_velocity > 0:
                work = 0.5 * self.mass * (self.vertical_velocity * self.vertical_velocity)
            else:
                work = -(0.5 * self.mass * (self.vertical_velocity * self.vertical_velocity))

            self.rect.y -= work
            self.vertical_velocity -= 1

    def move_right(self):
        self.delta_x += self.horizontal_speed

    def move_left(self):
        self.delta_x -= self.horizontal_speed

    def stop(self):
        self.delta_x = 0
        self.is_jumping = False
        self.vertical_velocity = 8

    def jump(self):
        self.is_jumping = True
