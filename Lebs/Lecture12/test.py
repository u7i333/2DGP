from pico2d import *

# Boy State

PIXEL_PER_METER = (10.0 /0.3)
RUN_SPEED_KMPH = 20.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)


TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

IDLE, RUN = range(2)

# Boy Event
RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP,UP_DOWN, DOWN_DOWN, UP_UP, DOWN_UP = range(8)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYDOWN, SDLK_UP): UP_DOWN,
    (SDL_KEYDOWN, SDLK_DOWN): DOWN_DOWN,
    (SDL_KEYUP, SDLK_UP): UP_UP,
    (SDL_KEYUP, SDLK_DOWN): DOWN_UP
}

next_state_table = {
    IDLE: {RIGHT_UP: RUN, LEFT_UP: RUN, RIGHT_DOWN: RUN,LEFT_DOWN: RUN, UP_UP: RUN, DOWN_UP: RUN, UP_DOWN: RUN, DOWN_DOWN: RUN},
    RUN: {RIGHT_UP: IDLE, LEFT_UP: IDLE, RIGHT_DOWN: IDLE,LEFT_DOWN: IDLE, UP_UP: IDLE, DOWN_UP: IDLE, UP_DOWN: IDLE, DOWN_DOWN: IDLE}
}


class Heroine:

    def __init__(self):
        self.event_que = []
        self.x, self.y = 600 // 2, 90
        self.image = load_image('reimu_sheet.png')
        self.cur_state = IDLE
        self.dir = 1
        self.RIGHT = False
        self.LEFT = False
        self.UP = False
        self.DOWN = False
        self.enter_state[IDLE](self)
        self.velocityX= 0
        self.velocityY = 0


    # IDLE state functions
    def enter_IDLE(self):
        self.timer = 1000
        self.frame = 0

    def exit_IDLE(self):
        pass

    def do_IDLE(self):
        self.frame = (self.frame + 1) % 8
        self.timer -= 1

    def draw_IDLE(self):
            self.image.clip_draw(self.frame * 100, 200, 100, 100, self.x, self.y)


    # RUN state functions
    def enter_RUN(self):
        self.frame = 0
        self.dir = self.velocityX

    def exit_RUN(self):
        pass

    def do_RUN(self):
        if self.RIGHT == True:
            #self.x += 1
            self.velocityX += 0.1
        if self.LEFT == True:
            #self.x -= 1
            self.velocityX -= 0.1
        if self.UP == True:
            #self.y += 1
            self.velocityY += 0.1
        if self.DOWN == True:
            #self.y -= 1
            self.velocityY -= 0.1

        self.frame = (self.frame + 1) % 8
        self.x += self.velocityX
        self.x = clamp(25, self.x, 800-25)
        self.y += self.velocityY
        self.y = clamp(25, self.y, 800 - 25)

    def draw_RUN(self):
        if self.RIGHT == True:
            self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)
        else: #self.LEFT == True:
            self.image.clip_draw(self.frame * 100, 100, 100, 100, self.x, self.y)

    def add_event(self, event):
        self.event_que.insert(0, event)

    def change_state(self,  state):
        self.exit_state[self.cur_state](self)
        self.enter_state[state](self)
        self.cur_state = state

    enter_state = {IDLE: enter_IDLE, RUN: enter_RUN}
    exit_state = {IDLE: exit_IDLE, RUN: exit_RUN}
    do_state = {IDLE: do_IDLE, RUN: do_RUN}
    draw_state = {IDLE: draw_IDLE, RUN: draw_RUN}


    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)


    def draw(self):
        self.draw_state[self.cur_state](self)


    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)