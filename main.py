import pygame, sys, thorpy
from pygame.locals import QUIT

pygame.init()
app = thorpy.Application((5, 5))


def start_game():
    print("Game Started")


window_surface = pygame.display.set_mode((900, 700), 0, 32)
# TODO: Update this Title
pygame.display.set_caption('Hello World')

# TODO: Add center label with game name
start_button = thorpy.make_button("Start", func=start_game)

quit_button = thorpy.make_button("Quit")
quit_button.set_as_exiter()

box = thorpy.Box.make([start_button, quit_button])
box.center()

background = thorpy.Background.make(elements=[box])
menu = thorpy.Menu(elements=background)
menu.play()

pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            app.quit()
            pygame.quit()
            sys.exit()
