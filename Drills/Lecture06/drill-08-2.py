from pico2d import *
import random

KPU_WIDTH, KPU_HEIGHT = 1280, 1024

open_canvas(KPU_WIDTH, KPU_HEIGHT)

KPU_Ground = load_image('KPU_GROUND.PNG')
character = load_image('animation_sheet.png')

x,y = KPU_WIDTH//2, KPU_HEIGHT//2

points = [(random.randint(0,KPU_WIDTH),random.randint(0,KPU_HEIGHT))]

def Move_Rand

while True:
    clear_canvas()
    KPU_Ground.draw(KPU_WIDTH//2, KPU_HEIGHT//2)
    update_canvas()

    delay(0.02)

close_canvas()