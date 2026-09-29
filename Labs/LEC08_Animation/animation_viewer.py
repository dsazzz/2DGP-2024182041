from pico2d import *

open_canvas(800, 600)
char = load_image('ai_char_sheet.png')

clear_canvas()
char.clip_draw(115, 1480, 147, 242, 400, 300)
update_canvas()
delay(3)

close_canvas()