from pico2d import *
import game_world
import game_framework

import main_state
import norml_enemy

PIXEL_PER_METER = (10.0 /0.3)
RUN_SPEED_KMPH = 20.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)*0.1

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8


class My_Bullet:
    image = None

    def __init__(self, x = 400, y = 300, velocity = 1):
        if My_Bullet.image == None:
            My_Bullet.image = load_image('./picture/bullet.png')
        self.shoot_sound = load_wav('./music/heroineshoot.wav')
        #self.enemy_hit = load_wav('./music/enemyhit.wav')
        self.shoot_sound.set_volume(30)
        #self.enemy_hit.set_volume(10)
        self.shoot_sound.play()

        self.x, self.y, self.velocity = x, y, velocity


    def draw(self):
        self.image.draw(self.x, self.y)

    def get_bb(self):
        return self.x - 10, self.y - 20,  self.x + 10, self.y + 20

    def update(self):
        #self.y += self.velocity
        self.y += RUN_SPEED_PPS*0.2

        if self.y > 800 - 50:
            game_world.remove_object(self)

        for i in range(0, 3):
            if main_state.collide(main_state.blue_enemys1[i], self):
                main_state.blue_enemys1[i].hp -= 1
                #game_world.remove_object(main_state.blue_enemys1[i])

        if main_state.collide(main_state.bose_enemy, self):
            main_state.bose_enemy.hp -= 1
            #game_world.remove_object(main_state.bose_enemy)

        for i in range(0, 3):
            if main_state.collide(main_state.black_enemys1[i], self):
                main_state.black_enemys1[i].hp -= 1
                #game_world.remove_object(main_state.black_enemys1[i])

        if main_state.collide(main_state.red_enemy, self):
            main_state.red_enemy.hp -= 1

        if main_state.collide(main_state.green_enemy, self):
            main_state.green_enemy.hp -= 1

        if main_state.collide(main_state.special_enemy, self):
            main_state.special_enemy.hp -= 1

        for i in range(0, 2):
            if main_state.collide(main_state.black_enemys2[i], self):
                main_state.black_enemys2[i].hp -= 1

        for i in range(0, 2):
            if main_state.collide(main_state.blue_enemys2[i], self):
                main_state.blue_enemys2[i].hp -= 1
                #game_world.remove_object(main_state.blue_enemys1[i])

        if main_state.collide(main_state.red_enemy2, self):
            main_state.red_enemy2.hp -= 1

        if main_state.collide(main_state.green_enemy2, self):
            main_state.green_enemy2.hp -= 1

        if main_state.collide(main_state.special_enemy1, self):
            main_state.special_enemy1.hp -= 1

        if main_state.collide(main_state.special_enemy2, self):
            main_state.special_enemy2.hp -= 1

        if main_state.collide(main_state.red_enemy3, self):
            main_state.red_enemy3.hp -= 1

        if main_state.collide(main_state.green_enemy3, self):
            main_state.green_enemy3.hp -= 1

        for i in range(0, 3):
            if main_state.collide(main_state.black_enemys3[i], self):
                main_state.black_enemys3[i].hp -= 1

        for i in range(0, 3):
            if main_state.collide(main_state.blue_enemys3[i], self):
                main_state.blue_enemys3[i].hp -= 1


        if main_state.collide(main_state.red_enemy4, self):
            main_state.red_enemy4.hp -= 1

        if main_state.collide(main_state.green_enemy4, self):
            main_state.green_enemy4.hp -= 1


        if main_state.collide(main_state.special_enemy3, self):
            main_state.special_enemy3.hp -= 1


class Speciel_Bullet:
    image = None

    def __init__(self, x = 400, y = 300, velocity = 1):
        if Speciel_Bullet.image == None:
            Speciel_Bullet.image = load_image('./picture/special_bullet.png')
        self.shoot_sound = load_wav('./music/specialshoot.wav')
        self.shoot_sound.set_volume(30)
        self.shoot_sound.play()
        self.x, self.y, self.velocity = x, y, velocity
        self.time = 0
        self.frame = 0

    def draw(self):
        #self.image.draw(self.x, self.y)
        self.image.clip_draw(400 * int(self.frame), 0, 400, 400, self.x, self.y)

    def get_bb(self):
        return self.x - 100, self.y - 100,  self.x + 100, self.y + 100

    def update(self):
        self.x = main_state.heroine.x
        self.y = main_state.heroine.y
        self.frame = (self.frame + 0.09)% 8
        main_state.heroine.hp = 1000
        if(self.time == 0):
            self.time = get_time()

        if(get_time() - self.time > 3):
            game_world.remove_object(self)
            main_state.heroine.hp = 1

        if main_state.collide(main_state.blue_enemy, self):
            main_state.blue_enemy.hp -= 1
            #game_world.remove_object(main_state.blue_enemy)

        for i in range(0, 3):
            if main_state.collide(main_state.blue_enemys1[i], self):
                main_state.blue_enemys1[i].hp -= 1
                #game_world.remove_object(main_state.blue_enemys1[i])

        if main_state.collide(main_state.bose_enemy, self):
            main_state.bose_enemy.hp -= 1
            #game_world.remove_object(main_state.bose_enemy)

        for i in range(0, 3):
            if main_state.collide(main_state.black_enemys1[i], self):
                main_state.black_enemys1[i].hp -= 1
                #game_world.remove_object(main_state.black_enemys1[i])

        if main_state.collide(main_state.red_enemy, self):
            main_state.red_enemy.hp -= 1

        if main_state.collide(main_state.green_enemy, self):
            main_state.green_enemy.hp -= 1

        if main_state.collide(main_state.special_enemy, self):
            main_state.special_enemy.hp -= 1

        for i in range(0, 3):
            if main_state.collide(main_state.black_enemys2[i], self):
                main_state.black_enemys2[i].hp -= 1

        for i in range(0, 3):
            if main_state.collide(main_state.blue_enemys2[i], self):
                main_state.blue_enemys2[i].hp -= 1
                #game_world.remove_object(main_state.blue_enemys1[i])

        if main_state.collide(main_state.red_enemy2, self):
            main_state.red_enemy2.hp -= 1

        if main_state.collide(main_state.green_enemy2, self):
            main_state.green_enemy2.hp -= 1

        if main_state.collide(main_state.special_enemy1, self):
            main_state.special_enemy1.hp -= 1

        if main_state.collide(main_state.special_enemy2, self):
            main_state.special_enemy2.hp -= 1

        if main_state.collide(main_state.red_enemy3, self):
            main_state.red_enemy3.hp -= 1

        if main_state.collide(main_state.green_enemy3, self):
            main_state.green_enemy3.hp -= 1

        for i in range(0, 3):
            if main_state.collide(main_state.black_enemys3[i], self):
                main_state.black_enemys3[i].hp -= 1

        for i in range(0, 3):
            if main_state.collide(main_state.blue_enemys3[i], self):
                main_state.blue_enemys3[i].hp -= 1


        if main_state.collide(main_state.red_enemy4, self):
            main_state.red_enemy4.hp -= 1

        if main_state.collide(main_state.green_enemy4, self):
            main_state.green_enemy4.hp -= 1


        if main_state.collide(main_state.special_enemy3, self):
            main_state.special_enemy3.hp -= 1