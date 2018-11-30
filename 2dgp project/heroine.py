import game_framework
from pico2d import *
from my_bullet import My_Bullet
from my_bullet import Speciel_Bullet
import main_state
import gameover_state
import random
import game_world

PIXEL_PER_METER = (10.0 /0.3)
RUN_SPEED_KMPH = 20.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER) * 1.5

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8


RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, UP_DOWN, DOWN_DOWN, UP_UP, DOWN_UP,DOWN_X,DOWN_SPACE = range(10)


key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYDOWN, SDLK_UP): UP_DOWN,
    (SDL_KEYDOWN, SDLK_DOWN): DOWN_DOWN,
    (SDL_KEYUP, SDLK_UP): UP_UP,
    (SDL_KEYUP, SDLK_DOWN): DOWN_UP,
    (SDL_KEYDOWN, SDLK_x): DOWN_X,
    (SDL_KEYDOWN, SDLK_SPACE): DOWN_SPACE,
}

class IdleState:

    @staticmethod
    def enter(heroine, event):
        if event == RIGHT_DOWN:
            heroine.velocityX += RUN_SPEED_PPS
        elif event == LEFT_DOWN:
            heroine.velocityX -= RUN_SPEED_PPS
        elif event == RIGHT_UP:
            heroine.velocityX -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            heroine.velocityX += RUN_SPEED_PPS
        if event == UP_DOWN:
            heroine.velocityY += RUN_SPEED_PPS
        elif event == DOWN_DOWN:
            heroine.velocityY -= RUN_SPEED_PPS
        elif event == UP_UP:
            heroine.velocityY -= RUN_SPEED_PPS
        elif event == DOWN_UP:
            heroine.velocityY += RUN_SPEED_PPS
        heroine.dir = clamp(-1, heroine.velocityX, 1)


    @staticmethod
    def exit(heroine, event):
        if event == DOWN_X:
            heroine.shoot_bullet()

    @staticmethod
    def do(heroine):
        heroine.frame = (heroine.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8

    @staticmethod
    def draw(heroine):
        if heroine.dir == 1:
            heroine.image.clip_draw(int(heroine.frame) * 100, 200, 100, 100, heroine.x, heroine.y)
        else:
            heroine.image.clip_draw(int(heroine.frame) * 100, 200, 100, 100, heroine.x, heroine.y)

class RunState:

    @staticmethod
    def enter(heroine, event):
        if event == RIGHT_DOWN:
            heroine.velocityX += RUN_SPEED_PPS
        elif event == LEFT_DOWN:
            heroine.velocityX -= RUN_SPEED_PPS
        elif event == RIGHT_UP:
            heroine.velocityX -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            heroine.velocityX += RUN_SPEED_PPS
        if event == UP_DOWN:
            heroine.velocityY += RUN_SPEED_PPS
        elif event == DOWN_DOWN:
            heroine.velocityY -= RUN_SPEED_PPS
        elif event == UP_UP:
            heroine.velocityY -= RUN_SPEED_PPS
        elif event == DOWN_UP:
            heroine.velocityY += RUN_SPEED_PPS
        heroine.dir = clamp(-1, heroine.velocityX, 1)
        pass

    @staticmethod
    def exit(heroine, event):
        if event == DOWN_X:
            heroine.shoot_bullet()
        if event == DOWN_SPACE:
            heroine.shoot_special_bullet()

    @staticmethod
    def do(heroine):
        heroine.frame = (heroine.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        heroine.x += heroine.velocityX * game_framework.frame_time
        heroine.x = clamp(10, heroine.x, 600 - 25)
        heroine.y += heroine.velocityY * game_framework.frame_time
        heroine.y = clamp(10, heroine.y, 800 - 25)

    @staticmethod
    def draw(heroine):
        if heroine.dir == 1:
            heroine.image.clip_draw(int(heroine.frame) * 100, 0, 100, 100, heroine.x, heroine.y)
        elif heroine.dir == 0:
            heroine.image.clip_draw(int(heroine.frame) * 100, 200, 100, 100, heroine.x, heroine.y)
        else:
            heroine.image.clip_draw(int(heroine.frame) * 100, 100, 100, 100, heroine.x, heroine.y)


next_state_table = {
    IdleState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, RIGHT_DOWN: RunState, LEFT_DOWN: RunState, UP_UP: IdleState, DOWN_UP: IdleState, UP_DOWN: RunState, DOWN_DOWN: RunState, DOWN_X : IdleState, DOWN_SPACE : IdleState},
    RunState: {RIGHT_UP: RunState, LEFT_UP: RunState, LEFT_DOWN: RunState, RIGHT_DOWN: RunState, UP_UP: RunState, DOWN_UP: RunState, UP_DOWN: RunState, DOWN_DOWN: RunState, DOWN_X: RunState, DOWN_SPACE : RunState }

}

class Dead_anime:


    def __init__(self, x = 400, y = 300, velocity =0.1):

        Dead_anime.image = load_image('./picture/heroine_dead.png')
        self.x, self.y, self.velocity = x, y, velocity
        self.frame = 0

    def draw(self):
        self.image.clip_draw(int(self.frame) * 100, 0, 100, 100, self.x, self.y)

    def update(self):
        self.frame = (self.frame+0.2)%10
        if(self.frame > 9):
            game_world.remove_object(self)


class Heroine:

    def __init__(self):
        self.x, self.y = 600 // 2, 50
        self.image = load_image('./picture/reimu_sheet.png')
        self.dead_sound = load_wav('./music/heroinedead.wav')
        self.dead_sound.set_volume(30)
        self.dir = 1
        self.bulletdir = 1
        self.velocityX = 0
        self.velocityY = 0
        self.frame = 0
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)
        self.special_count = 3
        self.hp = 1
        self.life = 3
        self.power = 1
        self.lifcount = 0
        self.lifetime = 0

    def shoot_bullet(self):
        if(self.power != 2):
            bullet = My_Bullet(self.x, self.y, self.bulletdir*RUN_SPEED_PPS * 0.05)
            game_world.add_object(bullet, 1)

        if(self. power > 1):
            bullet2 = My_Bullet(self.x - 30, self.y - 20, self.bulletdir*RUN_SPEED_PPS * 0.05)
            bullet3 = My_Bullet(self.x + 30, self.y - 20, self.bulletdir * RUN_SPEED_PPS * 0.05)
            game_world.add_object(bullet2, 1)
            game_world.add_object(bullet3, 1)

    def shoot_special_bullet(self):
        if(self.special_count > 0):
            bullet = Speciel_Bullet (self.x, self.y, self.bulletdir * RUN_SPEED_PPS * 0.05)
            game_world.add_object(bullet, 1)
            self.special_count = self.special_count -1

    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

        if (self.hp < 0):
            self.dead_sound.play()
            dead_anime = Dead_anime(self.x, self.y)
            game_world.add_object(dead_anime, 1)
            self.life -= 1
            self.hp = 1
            self.x = 300
            self.y = 50
            self.lifcount = 1
            self.special_count = 3


        if (self.lifcount == 1):
            self.hp = 1000
            if(self.lifetime == 0):
                self.lifetime = get_time()
                #self.hp = 1000

            if(get_time() - self.lifetime > 3):
                self.hp = 1
                self.lifetime = 0
                self.lifcount =0

            if(self.life < 0):
                game_world.remove_object(self)

    def draw(self):
        self.cur_state.draw(self)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

    def get_bb(self):
        return self.x - 30, self.y - 30,  self.x + 30, self.y + 30

