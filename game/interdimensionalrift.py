import pygame


class InterDimensionalRift(pygame.sprite.Sprite):
    def __init__(self, possible_images):
        super().__init__()
        self.possible_images = possible_images
        self.current_image_number = 0
        self.image = self.possible_images[self.current_image_number].copy()
        self.rect = self.image.get_rect()
        self.is_closed = False
        self.horizontal_speed = 3

    def update(self):
        if not self.is_closed:
            if self.image.get_alpha() == 0:
                self.current_image_number += 1
                if self.current_image_number > len(self.possible_images) - 1:
                    self.current_image_number = 0
                self.image = self.possible_images[self.current_image_number].copy()

                old_x = self.rect.x
                old_y = self.rect.y
                self.rect = self.image.get_rect()
                self.rect.x = old_x
                self.rect.y = old_y
            else:
                self.image.set_alpha(self.image.get_alpha() - 1)
                pygame.time.delay(3)

    def handle_player_collision(self, player):
        if not self.is_closed and not player.is_jumping and not player.sprite_grounded_on == self:
            if player.rect.x >= (self.rect.x - self.rect.width) and player.move_right:
                player.rect.x = self.rect.x - self.rect.width + 20
                player.stop()
            if player.rect.x <= (self.rect.x + self.rect.width) and player.move_left:
                player.rect.x = self.rect.x + self.rect.width - 15
                player.stop()
        elif player.is_jumping and player.rect.y >= (self.rect.y - self.rect.height):
            player.rect.y = self.rect.y - self.rect.height + 20
            player.stop()
            player.is_grounded = True
            player.sprite_grounded_on = self
            player.sprite_grounded_on_multiplier = 1
        elif self.is_closed and not player.is_jumping and not player.sprite_grounded_on == self:
            if player.rect.x >= (self.rect.x - self.rect.width) and player.move_right:
                self.rect.x += self.horizontal_speed
            if player.rect.x >= self.rect.x and player.move_left:
                self.rect.x -= self.horizontal_speed

    def close(self):
        self.is_closed = True
        self.image.set_alpha(255)
