import game_framework
from pico2d import *
import main_state

name = "PauseState"


def enter():
    global image
    image = load_image('pause.png')


def exit():
    global image
    del(image)

def handle_events():
    pass


def draw():
    clear_canvas()
    image.draw(400,300)
    update_canvas()


def update():
    pass


def pause():
    pass


def resume():
    pass

