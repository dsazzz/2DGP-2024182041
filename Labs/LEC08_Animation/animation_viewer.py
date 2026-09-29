from pico2d import *


open_canvas(800, 600)

try:
	while True:
		clear_canvas()
		update_canvas()
		delay(0.01)
finally:
	close_canvas()
