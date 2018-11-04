from pico2d import *
import game_world
import game_framework

class Blue_Enemy_Bullet:
    image = None

    def __init__(self, x = 400, y = 300, velocity =1):
        if Blue_Enemy_Bullet.image == None:
            Blue_Enemy_Bullet.image = load_image('blue_enemy_bullet.png')
        self.x, self.y, self.velocity = x, y, velocity


    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        self.y -= self.velocity
        if self.y < 25 or self.y > 800 - 25:
            game_world.remove_object(self)


class Black_Enemy_Bullet:
    image = None

    def __init__(self, x = 400, y = 300, velocity =1):
        if Black_Enemy_Bullet.image == None:
            Black_Enemy_Bullet.image = load_image('black_enemy_bullet.png')
        self.x, self.y, self.velocity = x, y, velocity


    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        self.y -= self.velocity
        if self.y < 25 or self.y > 800 - 25:
            game_world.remove_object(self)


class Red_Enemy_Bullet:
    image = None

    def __init__(self, x = 400, y = 300, velocity =1):
        if Red_Enemy_Bullet.image == None:
            Red_Enemy_Bullet.image = load_image('red_enemy_bullet.png')
        self.x, self.y, self.velocity = x, y, velocity

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        self.y -= self.velocity
        if self.y < 25 or self.y > 800 - 25:
            game_world.remove_object(self)


class Green_Enemy_Bullet:
    image = None

    def __init__(self, x = 400, y = 300, velocity =1):
        if Green_Enemy_Bullet.image == None:
            Green_Enemy_Bullet.image = load_image('green_enemy_bullet.png')
        self.x, self.y, self.velocity = x, y, velocity

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        self.y -= self.velocity
        if self.y < 25 or self.y > 800 - 25:
            game_world.remove_object(self)


class Star_Bullet:
    image = None

    def __init__(self, x = 400, y = 300, velocity =1, frame = 0):
        if Star_Bullet.image == None:
            Star_Bullet.image = load_image('star_bullet.png')
        self.x, self.y, self.velocity, self.frame = x, y, velocity, frame

    def draw(self):
        self.image.clip_draw(int(self.frame) * 50, 0, 50, 50, self.x, self.y)

    def update(self):
        self.y -= self.velocity*5
        if self.y < 25 or self.y > 800 - 25:
            game_world.remove_object(self)

class Bose_Laser_Bullet:
    image = None

    def __init__(self, x = 400, y = 300, velocity =1, frame = 0):
        if Star_Bullet.image == None:
            Star_Bullet.image = load_image('star_bullet.png')
        self.x, self.y, self.velocity, self.frame = x, y, velocity, frame

    def draw(self):
        self.image.clip_draw(int(self.frame) * 50, 0, 50, 50, self.x, self.y)

    def update(self):
        self.y -= self.velocity*5
        if self.y < 25 or self.y > 800 - 25:
            game_world.remove_object(self)