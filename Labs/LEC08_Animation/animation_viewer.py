from pico2d import *

open_canvas(800, 600)
char = load_image('ai_char_sheet.png')

for x in [115, 397, 673] * 5:
	clear_canvas()
	char.clip_draw(x, 1480, 147, 242, 400, 300)
	update_canvas()
	delay(0.3)

close_canvas()