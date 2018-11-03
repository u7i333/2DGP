from pico2d import *
import game_world
import game_framework

class Enemy_Bullet:
    image = None

    def __init__(self, x = 400, y = 300, velocity =1):
        if Enemy_Bullet.image == None:
            Enemy_Bullet.image = load_image('blue_enemy_bullet.png')
        self.x, self.y, self.velocity = x, y, velocity


    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        self.y -= self.velocity
        if self.y < 25 or self.y > 800 - 25:
            game_world.remove_object(self)