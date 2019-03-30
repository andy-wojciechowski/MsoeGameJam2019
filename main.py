import pygame, thorpy


def start_game():
    print("Game Started")


def main():
    app = thorpy.Application((1024, 768), caption="Hello World")

    # TODO: Add center label with game name
    start_button = thorpy.make_button("Start", func=start_game)

    quit_button = thorpy.make_button("Quit")
    quit_button.set_as_exiter()

    box = thorpy.Box.make([start_button, quit_button])
    box.center()

    background = thorpy.Background.make(elements=[box])

    menu = thorpy.Menu(elements=background)
    menu.play()
    app.quit()


if __name__ == "__main__":
    main()
