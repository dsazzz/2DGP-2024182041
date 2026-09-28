import math
import os

from pico2d import *


class MotionDirector:
    def __init__(self, center_x, center_y):
        self.center_x = center_x
        self.center_y = center_y
        self.time = 0.0
        self.mode = 0

    def next_position(self, delta_time):
        self.time += delta_time
        phase = self.time % 18.0
        self.mode = int(phase // 6.0)
        local_time = phase % 6.0

        if self.mode == 0:
            return self.circle_position(local_time)
        if self.mode == 1:
            return self.rectangle_position(local_time)
        return self.triangle_position(local_time)

    def circle_position(self, local_time):
        angle = local_time * math.tau / 6.0
        x = self.center_x + 220 * math.cos(angle)
        y = self.center_y + 130 * math.sin(angle)
        return x, y

    def rectangle_position(self, local_time):
        perimeter = 2 * (500 + 350)
        distance = (local_time / 6.0) * perimeter
        left = self.center_x - 250
        right = self.center_x + 250
        bottom = self.center_y - 175
        top = self.center_y + 175

        if distance < 500:
            return left + distance, top
        distance -= 500
        if distance < 350:
            return right, top - distance
        distance -= 350
        if distance < 500:
            return right - distance, bottom
        return left, bottom + (distance - 500)

    def triangle_position(self, local_time):
        vertices = (
            (self.center_x, self.center_y + 230),
            (self.center_x - 250, self.center_y - 180),
            (self.center_x + 250, self.center_y - 180),
        )
        progress = (local_time / 6.0) * 3
        edge = min(int(progress), 2)
        amount = progress - edge
        start_x, start_y = vertices[edge]
        end_x, end_y = vertices[(edge + 1) % 3]
        return (
            start_x + (end_x - start_x) * amount,
            start_y + (end_y - start_y) * amount,
        )


def draw_character(character, x, y):
    clear_canvas()
    character.draw(x, y)
    update_canvas()


open_canvas(800, 600)
character_path = os.path.join(os.path.dirname(__file__), 'character.png')
character = load_image(character_path)
director = MotionDirector(400, 300)

while True:
    x, y = director.next_position(0.02)
    draw_character(character, x, y)
    delay(0.02)
