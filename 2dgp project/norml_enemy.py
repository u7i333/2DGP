from pico2d import *
import game_framework
import game_world

PIXEL_PER_METER = (10.0 /0.3)
RUN_SPEED_KMPH = 20.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)


TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8


class Blue_enemy:

    def __init__(self,x = 400 ,y = 300):
        Blue_enemy.image = load_image('blue_enemy(L).png')
        self.x , self.y = x, y
        self.frame = 0

    def draw(self):
        self.image.clip_draw(int(self.frame) * 50, 0, 50, 50, self.x, self.y)


    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
        self.x = self.x - 0.1
        if self.x <= 25:
            game_world.remove_object(self)