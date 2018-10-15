from pico2d import *
import random

KPU_WIDTH, KPU_HEIGHT = 1280, 1024

open_canvas(KPU_WIDTH, KPU_HEIGHT)

KPU_Ground = load_image('KPU_GROUND.PNG')
character = load_image('animation_sheet.png')

x,y = KPU_WIDTH//2, KPU_HEIGHT//2

frame = 0
points = [(random.randint(-500,500),random.randint(-350,350)) for i in range(size)]
n = 1

def Move_Rand():
    pass

while True:
    clear_canvas()
    KPU_Ground.draw(KPU_WIDTH//2, KPU_HEIGHT//2)
    update_canvas()
    delay(0.02)

close_canvas()