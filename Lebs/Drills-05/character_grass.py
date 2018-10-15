from pico2d import *

open_canvas()

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

grass.draw_now(400,30)
character.draw_now(300,90)

delay(5)

close_canvas()
