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

class Blue_Enemy_Bullet:
    image = None

    def __init__(self, x = 400, y = 300, velocity =0.1):
        if Blue_Enemy_Bullet.image == None:
            Blue_Enemy_Bullet.image = load_image('./picture/blue_enemy_bullet.png')
        self.shoot_sound = load_wav('./music/normalenemybullet.wav')
        self.shoot_sound.set_volume(10)
        self.shoot_sound.play()
        self.x, self.y, self.velocity = x, y, velocity

    def get_bb(self):
        return self.x - 5, self.y - 5,  self.x + 5, self.y + 5

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        self.y -= RUN_SPEED_PPS*0.05
        if self.y < 25 or self.y > 800 - 25:
            game_world.remove_object(self)
        if main_state.collide(main_state.heroine, self):
            main_state.heroine.hp -= 1
            # game_world.remove_object(main_state.heroine)


class Black_Enemy_Bullet:
    image = None

    def __init__(self, x = 400, y = 300, velocity =0.1):
        if Black_Enemy_Bullet.image == None:
            Black_Enemy_Bullet.image = load_image('./picture/black_enemy_bullet.png')
        self.x, self.y, self.velocity = x, y, velocity
        self.shoot_sound = load_wav('./music/normalenemybullet.wav')
        self.shoot_sound.set_volume(10)
        self.shoot_sound.play()

    def get_bb(self):
        return self.x - 5, self.y - 5, self.x + 5, self.y + 5

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        self.y -= RUN_SPEED_PPS*0.05
        if self.y < 25 or self.y > 800 - 25:
            game_world.remove_object(self)
        if main_state.collide(main_state.heroine, self):
            main_state.heroine.hp -= 1
            # game_world.remove_object(main_state.heroine)



class Red_Enemy_Bullet:
    image = None

    def __init__(self, x = 400, y = 300, velocity =0.1):
        if Red_Enemy_Bullet.image == None:
            Red_Enemy_Bullet.image = load_image('./picture/red_enemy_bullet.png')
        self.x, self.y, self.velocity = x, y, velocity
        self.hx, self.hy = main_state.heroine.x, main_state.heroine.y
        self.countx = (self.hx - self.x)/900 * RUN_SPEED_PPS*0.05
        self.county = (self.hy - self.y)/900 * RUN_SPEED_PPS*0.05
        self.shoot_sound = load_wav('./music/normalenemybullet.wav')
        self.shoot_sound.set_volume(30)
        self.shoot_sound.play()

    def get_bb(self):
        return self.x - 5, self.y - 5, self.x + 5, self.y + 5


    def draw(self):
        self.image.draw(self.x, self.y)


    def update(self):
        self.x += self.countx
        self.y += self.county

        if self.y < 25 or self.y > 800 - 25 or self.x < 25 or self.y> 800-25 :
            game_world.remove_object(self)
        if main_state.collide(main_state.heroine, self):
            main_state.heroine.hp -= 1
            # game_world.remove_object(main_state.heroine)



class Green_Enemy_Bullet:
    image = None

    def __init__(self, x = 400, y = 300, velocity =0.1):
        if Green_Enemy_Bullet.image == None:
            Green_Enemy_Bullet.image = load_image('./picture/green_enemy_bullet.png')
        self.x, self.y, self.velocity = x, y, velocity
        self.hx, self.hy = main_state.heroine.x, main_state.heroine.y
        self.countx = (self.hx - self.x) / 900 * RUN_SPEED_PPS*0.05
        self.county = (self.hy - self.y) / 900 * RUN_SPEED_PPS*0.05
        self.shoot_sound = load_wav('./music/normalenemybullet.wav')
        self.shoot_sound.set_volume(30)
        self.shoot_sound.play()

    def get_bb(self):
        return self.x - 5, self.y - 5, self.x + 5, self.y + 5

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        self.x += self.countx
        self.y += self.county

        if self.y < 25 or self.y > 800 - 25:
            game_world.remove_object(self)
        if main_state.collide(main_state.heroine, self):
            main_state.heroine.hp -= 1
            #game_world.remove_object(main_state.heroine)

class Special_Enemy_Bullet:
    image = None

    def __init__(self, x = 400, y = 300, velocityx= 1, velocityy= 1  ):
        if Special_Enemy_Bullet.image == None:
            Special_Enemy_Bullet.image = load_image('./picture/special_enemy_bullet.png')
        self.x, self.y, self.velocityx, self.velocityy = x, y, velocityx, velocityy
        self.shoot_sound = load_wav('./music/specialenemybullet.wav')
        self.shoot_sound.set_volume(6)
        self.shoot_sound.play()

    def draw(self):
        self.image.draw(self.x, self.y)


    def get_bb(self):
        return self.x - 5, self.y - 5,  self.x + 5, self.y + 5

    def update(self):
        self.x -= self.velocityx
        self.y -= self.velocityy

        if self.y < 25 or self.y > 800 - 25:
            game_world.remove_object(self)
        if main_state.collide(main_state.heroine, self):
            main_state.heroine.hp -= 1
            # game_world.remove_object(main_state.heroine)



class Star_Bullet:
    image = None

    def __init__(self, x = 400, y = 300, velocity =1, frame = 0):
        if Star_Bullet.image == None:
            Star_Bullet.image = load_image('./picture/star_bullet.png')
        self.x, self.y, self.velocity, self.frame = x, y, velocity, frame
        self.shoot_sound = load_wav('./music/starbullet.wav')
        self.shoot_sound.set_volume(30)
        self.shoot_sound.play()

    def draw(self):
        self.image.clip_draw(int(self.frame) * 50, 0, 50, 50, self.x, self.y)

    def get_bb(self):
        return self.x - 10, self.y - 10,  self.x + 10, self.y + 10

    def update(self):
        self.y -= RUN_SPEED_PPS*0.05
        if self.y < 25 or self.y > 800 - 25:
            game_world.remove_object(self)
        if main_state.collide(main_state.heroine, self):
            main_state.heroine.hp -= 1
            #game_world.remove_object(main_state.heroine)


class Bose_Laser_Bullet:
    image = None

    def __init__(self, x = 400, y = 300, velocity =1):
        if Bose_Laser_Bullet.image == None:
            Bose_Laser_Bullet.image = load_image('./picture/master_spark.png')
        self.x, self.y, self.velocity = x, y, velocity
        self.frame = 0
        self.bullettime = get_time()
        self.time = 0
        self.count = 0
        self.shoot_sound = load_wav('./music/laserbullet.wav')
        self.shoot_sound.set_volume(30)

    def get_bb(self):
        return self.x - 150, self.y - 775,  self.x + 150, self.y - 175

    def draw(self):
        #self.image.clip_draw(125 - self.drawframeX, 0, 50+self.sizeframeX, 50+self.sizeframeY, self.x, self.y-400)
        self.image.clip_draw(300 * self.frame, 0, 300, 750, self.x, self.y-400)


    def update(self):

        if(self.frame < 19):
            if get_time() - self.bullettime > 0.05:
                self.frame = (self.frame + 1)
                self.bullettime = get_time()

        if (self.frame == 5 ):
            self.shoot_sound.play()

        if(self.frame == 19):
            if(self.time == 0):
                self.time = get_time()
                self.frame = 19
            if(get_time()-self.time > 2):
                game_world.remove_object(self)


        if self.frame > 15:
            if main_state.collide(main_state.heroine, self):
                main_state.heroine.hp -= 1
                # game_world.remove_object(main_state.heroine)

