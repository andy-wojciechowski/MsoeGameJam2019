import pygame

ALPHA_INCREMENT = 1


class InterDimensionalRift(pygame.sprite.Sprite):
    def __init__(self, possible_images):
        super().__init__()
        self.possible_images = possible_images
        self.current_image_number = 0
        self.image = self.possible_images[self.current_image_number].copy()
        self.rect = self.image.get_rect()
        self.is_closed = False

    def update(self):
        if not self.is_closed:
            print(self.image.get_alpha())
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

    def close(self):
        self.is_closed = True
        self.image.set_alpha(255)
