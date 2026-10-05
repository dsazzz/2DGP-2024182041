from pico2d import *


CANVAS_WIDTH = 1200
CANVAS_HEIGHT = 600
SCALE = 4


def main():
    open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    sprite_sheet = load_image("sonic-sprite.png")
    while True:
        for event in get_events():
            if event.type == SDL_QUIT or (
                event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE
            ):
                close_canvas()
                return


if __name__ == "__main__":
    main()
