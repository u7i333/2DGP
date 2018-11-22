import random
from pico2d import *
import game_world
import game_framework

class Ball:
    image = None

    def __init__(self):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.x, self.y, self.fall_speed = random.randint(0, 1800-1), random.randint(0, 1100), 0

    def get_bb(self):
        return self.x - self.bg.window_left - 10, self.y - self.bg.window_bottom - 10, self.x - self.bg.window_left + 10, self.y - self.bg.window_bottom + 10


    def draw(self):
        cx = self.x - self.bg.window_left
        cy = self.y - self.bg.window_bottom
        self.image.draw(cx, cy)
        draw_rectangle(*self.get_bb())

    def update(self):
        pass
        #self.y -= self.fall_speed * game_framework.frame_time


    def set_backgorund(self, bg):
        self.bg = bg
        #self.x = self.bg.w / 2*
        #self.y = self.bg.h / 2