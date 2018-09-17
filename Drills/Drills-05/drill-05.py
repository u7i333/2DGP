from pico2d import *

def move_character():
    pass

open_canvas()
grass = load_image('grass.png')
character = load_image('animation_sheet.png')

while True:
    move_character()

close_canvas()