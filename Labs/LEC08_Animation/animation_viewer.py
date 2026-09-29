from pico2d import *

open_canvas(800, 600)
char = load_image('ai_char_sheet.png')

# idle
# for x in [115, 397, 673, 967] * 5:
	# clear_canvas()
	# char.clip_draw(x, 1480, 147, 242, 400, 300)
	# update_canvas()
	# delay(0.3)

# walking
clear_canvas()
char.clip_draw(103, 1132, 163, 253, 400, 300)
update_canvas()
delay(3)

close_canvas()