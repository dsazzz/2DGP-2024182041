from pico2d import *


CANVAS_WIDTH = 1200
CANVAS_HEIGHT = 600
SCALE = 4
FRAME_TIME = 0.08
REPEAT_COUNT = 5
ACTION_PAUSE = 1.0

MOVING_ACTIONS = ("run", "spin", "roll", "dash1", "dash2")


def make_frames():
    return {
        "idle": [
            (1, 447, 29, 39), (31, 447, 26, 38), (58, 447, 29, 39),
            (87, 447, 29, 38), (118, 447, 30, 38), (150, 447, 30, 38),
            (182, 447, 29, 38), (211, 448, 29, 38), (240, 448, 29, 38),
            (270, 448, 24, 32), (302, 448, 29, 26),
        ],
        "run": [
            (8, 408, 26, 37), (37, 408, 27, 37), (65, 407, 31, 38),
            (97, 408, 37, 37), (135, 410, 32, 35), (170, 408, 32, 38),
            (206, 408, 26, 38), (238, 408, 24, 37), (263, 408, 30, 37),
            (295, 408, 36, 37), (334, 409, 32, 36), (370, 408, 29, 38),
        ],
        "stand": [
            (1, 361, 33, 40), (39, 362, 35, 39), (89, 362, 35, 38),
            (130, 362, 34, 42), (181, 362, 34, 41), (228, 363, 33, 40),
        ],
        "spin": [
            (1, 326, 29, 30), (35, 327, 29, 31), (67, 327, 30, 29),
            (98, 327, 31, 29), (131, 327, 29, 30), (162, 326, 29, 31),
            (193, 326, 30, 29), (230, 326, 31, 29), (268, 325, 30, 30),
        ],
        "roll": [
            (1, 292, 30, 27), (36, 292, 29, 27), (70, 292, 29, 27),
            (105, 292, 29, 27), (139, 292, 29, 27), (174, 292, 29, 27),
        ],
        "dash1": [
            (1, 251, 29, 35), (36, 251, 30, 35), (74, 251, 31, 35),
            (111, 251, 31, 36), (149, 251, 30, 35), (186, 251, 31, 36),
        ],
        "dash2": [
            (1, 207, 29, 35), (36, 207, 30, 35), (72, 208, 39, 31),
            (123, 208, 39, 32), (172, 208, 39, 31), (218, 208, 38, 32),
        ],
        "brake": [
            (1, 154, 24, 45), (31, 154, 29, 44), (65, 154, 20, 44),
            (90, 155, 25, 43), (119, 155, 25, 43), (149, 154, 20, 44),
            (184, 156, 40, 28), (232, 157, 39, 27),
        ],
        "pose": [
            (1, 108, 27, 38), (31, 110, 31, 36), (64, 110, 31, 36),
            (99, 110, 33, 38), (136, 110, 32, 36), (176, 110, 33, 36),
            (217, 110, 33, 36), (254, 111, 33, 36),
        ],
        "celebrate": [
            (6, 56, 34, 40), (49, 56, 34, 43), (96, 59, 23, 39),
            (125, 59, 23, 39),
        ],
    }


def action_names(frames):
    return tuple(frames.keys())


def validate_frames(frames):
    assert sum(len(action_frames) for action_frames in frames.values()) == 76
    for action_frames in frames.values():
        for left, bottom, width, height in action_frames:
            assert left >= 0
            assert bottom >= 0
            assert width > 0
            assert height > 0


def validate_configuration():
    assert CANVAS_WIDTH == 1200
    assert CANVAS_HEIGHT == 600
    assert SCALE == 4
    assert REPEAT_COUNT == 5
    assert ACTION_PAUSE == 1.0


def next_position(action, x, direction, delta):
    if action not in MOVING_ACTIONS:
        return CANVAS_WIDTH / 2, 1
    x += direction * 180 * delta
    if x >= CANVAS_WIDTH - 100:
        return CANVAS_WIDTH - 100, -1
    if x <= 100:
        return 100, 1
    return x, direction


def is_exit_event(event):
    return event.type == SDL_QUIT or (
        event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE
    )


def should_exit():
    return any(is_exit_event(event) for event in get_events())


def draw_frame(sprite_sheet, frame, x, y):
    left, bottom, width, height = frame
    sprite_sheet.clip_draw(
        left, bottom, width, height, x, y, width * SCALE, height * SCALE
    )


def render(sprite_sheet, frame, x, y):
    clear_canvas()
    draw_frame(sprite_sheet, frame, x, y)
    update_canvas()


def main():
    open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    sprite_sheet = load_image("sonic-sprite.png")
    frames = make_frames()
    validate_configuration()
    validate_frames(frames)
    x = CANVAS_WIDTH / 2
    y = CANVAS_HEIGHT / 2
    direction = 1
    while True:
        if should_exit():
            close_canvas()
            return
        clear_canvas()
        for action in action_names(frames):
            for _ in range(REPEAT_COUNT):
                previous_time = get_time()
                for frame in frames[action]:
                    if should_exit():
                        close_canvas()
                        return
                    current_time = get_time()
                    x, direction = next_position(
                        action, x, direction, current_time - previous_time
                    )
                    previous_time = current_time
                    render(sprite_sheet, frame, x, y)
                    delay(FRAME_TIME)
            delay(ACTION_PAUSE)


if __name__ == "__main__":
    main()
