from pico2d import *

open_canvas(800, 600)
char = load_image('ai_char_sheet.png')

clear_canvas()
char.clip_draw(110, 784, 182, 255, 400, 300, 364, 510)
update_canvas()
delay(3)

close_canvas()