from pico2d import *
import game_framework
import game_world
from enemy_bullet import Star_Bullet
from enemy_bullet import Bose_Laser_Bullet
from enemy_bullet import Special_Enemy_Bullet
from enemy_bullet import Red_Enemy_Bullet
from enemy_bullet import Blue_Enemy_Bullet
import main_state

PIXEL_PER_METER = (10.0 /0.3)
RUN_SPEED_KMPH = 20.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)*0.1 #뒤에는 삭제할것

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

class Dead_anime:
    image = None

    def __init__(self, x = 400, y = 300, velocity =0.1):
        if Dead_anime.image == None:
            Dead_anime.image = load_image('./picture/dead_anime.png')
        self.x, self.y, self.velocity = x, y, velocity
        self.frame = 0

    def draw(self):
        self.image.clip_draw(int(self.frame) * 40, 0, 40, 40, self.x, self.y)

    def update(self):
        self.frame = (self.frame+0.1)%5
        if(self.frame > 4):
            game_world.remove_object(self)

class Bose_enemy:

    def __init__(self,x = 400 ,y = 300):
        Bose_enemy.image = load_image('./picture/bose_enemy.png')
        self.deadsound = load_wav('./music/bosedead.wav')
        self.deadsound.set_volume(30)
        self.x , self.y = x, y
        self.frame = 0
        self.bulletdir = 1
        self.count = 0
        self.time = get_time()
        self.framecount = 0
        self.velocity = RUN_SPEED_PPS * 0.05
        self.bulletcolor = 0
        self.lasertimer = 0
        self.count3count = 0
        self.count6dir = 1
        self.count6count = 0
        self.lasercount = 0
        self.phase = 0
        self.hp = 5000
        self.sparkcount = 0

    def shoot_enemy_bullet(self):
        enemy_bullet = Star_Bullet(self.x, self.y, self.bulletdir, self.bulletcolor)
        enemy_bullet2 = Red_Enemy_Bullet(self.x, self.y,self.bulletdir * RUN_SPEED_PPS * 0.01)
        game_world.add_object(enemy_bullet, 1)
        if(self.phase >= 1):
            game_world.add_object(enemy_bullet2, 1)


    def get_bb(self):
        return self.x - 50, self.y - 50,  self.x + 50, self.y + 50

    def shoot_laser_bullet(self):
        enemy_laser_bullet = Bose_Laser_Bullet(self.x,self.y)
        game_world.add_object(enemy_laser_bullet, 1)
        enemy_laser_bullet.frame

    def shoot_special_bullet(self):
        enemy_bullet1 = Special_Enemy_Bullet(self.x, self.y, 1,1)
        enemy_bullet2 = Special_Enemy_Bullet(self.x, self.y, 0.5, 1)
        enemy_bullet3 = Special_Enemy_Bullet(self.x, self.y, 0, 1)
        enemy_bullet4 = Special_Enemy_Bullet(self.x, self.y, -0.5, 1)
        enemy_bullet5 = Special_Enemy_Bullet(self.x, self.y, -1, 1)
        enemy_bullet6 = Blue_Enemy_Bullet(self.x - 200, self.y)
        enemy_bullet7 = Blue_Enemy_Bullet(self.x - 100, self.y)
        enemy_bullet8 = Blue_Enemy_Bullet(self.x + 100, self.y)
        enemy_bullet9 = Blue_Enemy_Bullet(self.x + 200, self.y)
        game_world.add_object(enemy_bullet1, 1)
        game_world.add_object(enemy_bullet2, 1)
        game_world.add_object(enemy_bullet3, 1)
        game_world.add_object(enemy_bullet4, 1)
        game_world.add_object(enemy_bullet5, 1)
        if(self.phase >= 1):
            game_world.add_object(enemy_bullet6, 1)
            game_world.add_object(enemy_bullet7, 1)
            game_world.add_object(enemy_bullet8, 1)
            game_world.add_object(enemy_bullet9, 1)

    def draw(self):
        if self.velocity == 0:
            self.image.clip_draw(int(self.frame) * 100, 100, 100, 100, self.x, self.y) # 300,800
        else:
            self.image.clip_draw(int(self.frame) * 100, 0, 100, 100, self.x, self.y)  # 300,800



    def update(self):
        self.frame = (self.frame + 0.01) % 4

        if(self.hp < 2000):
            self.phase = 1

        if(self.hp < 10):
            self.deadsound.play()

        if(self.hp < 0):
            game_world.remove_object(self)

        if (self.count == 0):
            #self.velocity = 0.5
            self.y = self.y - self.velocity
            if (self.y < 750):
                self.count = 1


        if(get_time() - self.time > 0.35 and self.count < 4):
            Bose_enemy.shoot_enemy_bullet(self)
            self.bulletcolor = (self.bulletcolor+1)%7
            self.time = get_time()

        if(self.count == 1):
            self.x -= self.velocity
            self.y -= self.velocity*0.5
            if (self.x < 50):
                 self.count = 2

        if (self.count == 2):
            #self.velocity = 0
            self.x += self.velocity
            if (self.x > 550):
                self.count = 3

        if(self.count == 3):
            #self.velocity = 0.5
            self.x -= self.velocity
            self.y += self.velocity*0.5

            if(self.x <= 300):
                if(self.count3count < 3):
                    self.count3count += 1
                    self.count = 1
                if(self.count3count == 3):
                    self.count3count = 0
                    self.count = 4
                    #self.velocity = 0

        if(self.count == 4 and self.hp < 1500):
            if(self.sparkcount == 0):
                Bose_enemy.shoot_laser_bullet(self)
                self.sparkcount = 1
            if(self.lasertimer == 0):
                self.lasertimer = get_time()
            if(get_time() - self.lasertimer > 3):
                self.lasertimer = 0
                self.count = 5
                self.sparkcount = 0
        elif (self.count == 4):
            self.count = 5

        if (self.count == 5):
            if(get_time()- self.time > 3.1):
                self.time = get_time()
            if (get_time() - self.time > 3):
                self.count = 6
                self.time = get_time()

        if(self.count == 6):
            #self.velocity = 0.5
            self.x += self.velocity * self.count6dir
            if(self.x > 550):
                self.count6dir = -1
            if(self.x < 50):
                self.count6dir = 1
                self.count6count += 1
            if (get_time() - self.time > 0.7):
                Bose_enemy.shoot_special_bullet(self)
                self.time = get_time()
            if(self.count6count == 5):
                self.count = 7
                self.count6count = 0

        if(self.count == 7):
            #self.velocity = 0.5
            self.x += self.velocity

            if (self.x >= 300):
                self.count = 8
                #self.velocity = 0

        if (self.count == 8 and self.hp < 2500):
            if (self.sparkcount == 0):
                Bose_enemy.shoot_laser_bullet(self)
                self.sparkcount = 1
            if (self.lasertimer == 0):
                self.lasertimer = get_time()
            if (get_time() - self.lasertimer > 3):
                self.lasertimer = 0
                self.count = 9
                self.sparkcount = 0
        elif(self.count == 8):
            self.count = 0

        if (self.count == 9):
            if (get_time() - self.time > 3.1):
                self.time = get_time()
            if (get_time() - self.time > 3):
                self.count = 0
                self.time = get_time()

        if self.x <= 25:
            game_world.remove_object(self)
