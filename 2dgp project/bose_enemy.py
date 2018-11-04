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


class Bose_enemy:

    def __init__(self,x = 400 ,y = 300):
        Bose_enemy.image = load_image('bose_enemy.png')
        self.x , self.y = x, y
        self.frame = 0
        self.bulletdir = 1
        self.count = 0
        self.time = get_time()
        self.framecount = 0

    def shoot_enemy_bullet(self):
        pass

    def draw(self):
        self.image.clip_draw(int(self.frame) * 100, 100, 100, 100, self.x, self.y) # 300,800



    def update(self):
        self.frame = (self.frame + 0.1) % 4

        if(get_time() - self.time > 1):
            Bose_enemy.shoot_enemy_bullet(self)
            self.time = get_time()

        if(self.count == 0):
            self.y = self.y - 1
            if(self.y < 750):
                self.count = 1

        if(self.count == 1):
            self.x -= 1
            self.y -= 0.3
            if (self.x < 50):
                 self.count = 2

        if (self.count == 2):
            self.x += 1
            if (self.x > 550):
                self.count = 3

        if(self.count == 3):
            self.x -= 1
            self.y += 0.3
            if(self.x <= 300):
                self.count = 5

        if self.x <= 25:
            game_world.remove_object(self)
