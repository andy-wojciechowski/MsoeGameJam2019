import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, image, screen_width):
        super().__init__()
        self.image = image
        self.screen_width = screen_width
        self.rect = self.image.get_rect()
        self.horizontal_speed = 3
        self.vertical_velocity = 8
        self.mass = 1
        self.is_jumping = False
        self.is_grounded = True
        self.move_left = False
        self.move_right = False
        self.sprite_grounded_on = None

    def update(self):
        if self.move_left:
            self.rect.x += -self.horizontal_speed

        if self.move_right:
            self.rect.x += self.horizontal_speed

        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.x > self.screen_width - 25:
            self.rect.x = self.screen_width - 25

        if self.sprite_grounded_on:
            if self.rect.x > self.sprite_grounded_on.rect.x + self.sprite_grounded_on.rect.width or \
                    self.rect.x < (self.sprite_grounded_on.rect.x - self.sprite_grounded_on.rect.width):
                self.is_grounded = False

        if self.is_jumping:
            if self.vertical_velocity > 0:
                work = 0.5 * self.mass * (self.vertical_velocity * self.vertical_velocity)
            else:
                work = -(0.5 * self.mass * (self.vertical_velocity * self.vertical_velocity))

            self.rect.y -= work
            self.vertical_velocity -= 1
        else:
            self._apply_gravity()

    def stop(self):
        self.is_jumping = False
        self.vertical_velocity = 8

    def jump(self):
        self.is_jumping = True
        self.is_grounded = False

    def _apply_gravity(self):
        if not self.is_grounded:
            if self.vertical_velocity > 0:
                self.vertical_velocity = -1

            work = -(0.5 * self.mass * (self.vertical_velocity * self.vertical_velocity))
            self.rect.y -= work
            self.vertical_velocity -= 1
