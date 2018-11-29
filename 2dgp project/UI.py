from pico2d import *
import game_world
import game_framework
import main_state
import heroine


class Life_UI:
    image = None

    def __init__(self, x = 400, y = 300, velocity =0.1):
        if Life_UI.image == None:
            Life_UI.image = load_image('life_ui.png')
        self.x, self.y, self.velocity = x, y, velocity


    def draw(self):
        for i in range(0,main_state.heroine.life):
            self.image.draw(self.x + 20*i, self.y)

    def update(self):
        pass


class Special_UI:
    image = None

    def __init__(self, x = 400, y = 300, velocity =0.1):
        if Special_UI.image == None:
            Special_UI.image = load_image('special_ui.png')
        self.x, self.y, self.velocity = x, y, velocity


    def draw(self):
        for i in range(0,main_state.heroine.special_count):
            self.image.draw(self.x - 30*i, self.y)

    def update(self):
        pass