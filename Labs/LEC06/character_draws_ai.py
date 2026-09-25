import math

from pico2d import *

CENTER = (400, 300)
RADIUS = 200
STEPS = 100


def draw_boy(x, y):
    clear_canvas()
    boy.draw(x, y)
    update_canvas()
    delay(0.01)


def move_path(points):
    for x, y in points:
        draw_boy(round(x), round(y))


def line_points(start, end, steps=STEPS):
    for step in range(steps + 1):
        ratio = step / steps
        x = start[0] + (end[0] - start[0]) * ratio
        y = start[1] + (end[1] - start[1]) * ratio
        yield x, y


def circle_points():
    for degree in range(360):
        theta = math.radians(degree)
        x = CENTER[0] + RADIUS * math.cos(theta)
        y = CENTER[1] + RADIUS * math.sin(theta)
        yield x, y


def polygon_points(vertices):
    for start, end in zip(vertices, vertices[1:]):
        yield from line_points(start, end)


def move_circle():
    move_path(circle_points())


def move_rectangle():
    corners = ((50, 550), (750, 550), (750, 50), (50, 50), (50, 550))
    move_path(polygon_points(corners))


def move_triangle():
    vertices = ((100, 100), (700, 100), (400, 500), (100, 100))
    move_path(polygon_points(vertices))


open_canvas(800, 600)
boy = load_image('character.png')

while True:
    move_circle()
    move_rectangle()
    move_triangle()

