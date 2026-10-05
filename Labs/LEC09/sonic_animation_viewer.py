from pico2d import *


CANVAS_WIDTH = 1200
CANVAS_HEIGHT = 600
SCALE = 4
SPRITE_WIDTH = 399
SPRITE_HEIGHT = 525
FRAME_WIDTH = 32
FRAME_HEIGHT = 40
FRAME_STEP = 34
IDLE_TOP = 39


def first_frame():
    bottom = SPRITE_HEIGHT - IDLE_TOP - FRAME_HEIGHT
    return 1, bottom, FRAME_WIDTH, FRAME_HEIGHT


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
