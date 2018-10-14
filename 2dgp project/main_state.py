import random
import json
import os

from pico2d import *

import game_framework
import title_state
#import pause_state
import senior_pause_state


name = "MainState"


map = None

class Map:
    def __init__(self):
        self.image = load_image('shooting_ground.png')

    def draw(self):
        self.image.draw(300, 400)




def enter():
    global map
    map = Map()




def exit():
    global map
    del(map)


def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.push_state(senior_pause_state)



def update():
    pass


def draw():
    clear_canvas()
    map.draw()
    update_canvas()





