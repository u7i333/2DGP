from pico2d import *
import game_world
import game_framework
import main_state
import heroine


PIXEL_PER_METER = (10.0 /0.3)
RUN_SPEED_KMPH = 20.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)*0.1 #뒤에는 삭제할것

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

class Power_Item:
    image = None

    def __init__(self, x = 400, y = 300, velocity =0.1):
        if Power_Item.image == None:
            Power_Item.image = load_image('power_item.png')
        self.x, self.y, self.velocity = x, y, velocity

    def get_bb(self):
        return self.x - 25, self.y - 25,  self.x + 25, self.y + 25

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        self.y -= RUN_SPEED_PPS*0.05
        if self.y < 25:
            game_world.remove_object(self)
        if main_state.collide(main_state.heroine, self):
            main_state.heroine.power += 1
            game_world.remove_object(self)
            # game_world.remove_object(main_state.heroine)




class lifeup_Item:
    image = None

    def __init__(self, x = 400, y = 300, velocity =0.1):
        if lifeup_Item.image == None:
            lifeup_Item.image = load_image('lifeup_item.png')
        self.x, self.y, self.velocity = x, y, velocity

    def get_bb(self):
        return self.x - 25, self.y - 25,  self.x + 25, self.y + 25

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        self.y -= RUN_SPEED_PPS*0.05
        if self.y < 25:
            game_world.remove_object(self)
        if main_state.collide(main_state.heroine, self):
            main_state.heroine.life += 1
            game_world.remove_object(self)
            # game_world.remove_object(main_state.heroine)




class Special_Item:
    image = None

    def __init__(self, x = 400, y = 300, velocity =0.1):
        if Special_Item.image == None:
            Special_Item.image = load_image('special_item.png')
        self.x, self.y, self.velocity = x, y, velocity

    def get_bb(self):
        return self.x - 25, self.y - 25,  self.x + 25, self.y + 25

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        self.y -= RUN_SPEED_PPS*0.05
        if self.y < 25:
            game_world.remove_object(self)
        if main_state.collide(main_state.heroine, self):
            main_state.heroine.special_count += 1
            game_world.remove_object(self)
            # game_world.remove_object(main_state.heroine)