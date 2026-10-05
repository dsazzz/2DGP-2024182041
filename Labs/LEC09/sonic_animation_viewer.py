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
FRAME_TIME = 0.08
REPEAT_COUNT = 5
ACTION_PAUSE = 1.0

ACTION_STRIPS = (
    ("idle", 10, 39),
    ("run", 10, 79),
    ("jump", 6, 121),
    ("roll", 8, 167),
    ("spin", 6, 206),
    ("fall", 8, 238),
    ("attack", 8, 283),
    ("brake", 6, 326),
    ("pose", 6, 377),
    ("celebrate", 8, 426),
)
MOVING_ACTIONS = ("run", "roll", "spin", "attack", "brake")


def first_frame():
    bottom = SPRITE_HEIGHT - IDLE_TOP - FRAME_HEIGHT
    return 1, bottom, FRAME_WIDTH, FRAME_HEIGHT


def idle_frames():
    bottom = SPRITE_HEIGHT - IDLE_TOP - FRAME_HEIGHT
    return [
        (1 + index * FRAME_STEP, bottom, FRAME_WIDTH, FRAME_HEIGHT)
        for index in range(10)
    ]


def make_frames():
    frames = {}
    for action, count, top in ACTION_STRIPS:
        bottom = SPRITE_HEIGHT - top - FRAME_HEIGHT
        frames[action] = [
            (1 + index * FRAME_STEP, bottom, FRAME_WIDTH, FRAME_HEIGHT)
            for index in range(count)
        ]
    return frames


def action_names():
    return tuple(action for action, _, _ in ACTION_STRIPS)


def validate_frames(frames):
    assert sum(len(action_frames) for action_frames in frames.values()) == 76
    for action_frames in frames.values():
        for left, bottom, width, height in action_frames:
            assert 0 <= left <= SPRITE_WIDTH - width
            assert 0 <= bottom <= SPRITE_HEIGHT - height


def next_x(action, x, direction, delta):
    if action not in MOVING_ACTIONS:
        return x, direction
    x += direction * 180 * delta
    if x >= CANVAS_WIDTH - 100:
        return CANVAS_WIDTH - 100, -1
    if x <= 100:
        return 100, 1
    return x, direction


def draw_frame(sprite_sheet, frame, x, y):
    left, bottom, width, height = frame
    sprite_sheet.clip_draw(
        left, bottom, width, height, x, y, width * SCALE, height * SCALE
    )


def main():
    open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    sprite_sheet = load_image("sonic-sprite.png")
    frames = make_frames()
    validate_frames(frames)
    while True:
        for event in get_events():
            if event.type == SDL_QUIT or (
                event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE
            ):
                close_canvas()
                return
        clear_canvas()
        for action in action_names():
            for _ in range(REPEAT_COUNT):
                for frame in frames[action]:
                    clear_canvas()
                    draw_frame(
                        sprite_sheet, frame, CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2
                    )
                    update_canvas()
                    delay(FRAME_TIME)
            delay(ACTION_PAUSE)


if __name__ == "__main__":
    main()
