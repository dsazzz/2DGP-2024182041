# 실습 과제 진행
import math

def draw_boy(x, y):
    clear_canvas()
    boy.draw(x, y)
    update_canvas()
    delay(0.01)
    
def move_top():
    for x in range(50, 751, 5):
        draw_boy(x, 550)
def move_right():
    pass
def move_bottom():
    pass
def move_left():
    pass
def move_circle():
    for degree in range(360):
        theta = math.radians(degree)
        x = 400 + 200 * math.cos(theta)
        y = 300 + 200 * math.sin(theta)

        clear_canvas()
        boy.draw(x, y)
        update_canvas()
        delay(0.01)
def move_rectangle():
    move_top()
    move_right()
    move_bottom()
    move_left()
def move_triangle():
    print('triangle')    


from pico2d import *

open_canvas(800, 600)
boy = load_image('character.png')


while True:
    # move_circle()
    # move_rectangle()
    # move_triangle()
    move_top()