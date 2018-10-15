from pico2d import *
import random

KPU_WIDTH, KPU_HEIGHT = 1280, 1024

open_canvas(KPU_WIDTH, KPU_HEIGHT)

KPU_Ground = load_image('KPU_GROUND.PNG')
character = load_image('animation_sheet.png')

x,y = KPU_WIDTH//2, KPU_HEIGHT//2
frame = 0

size = 10
points = [(random.randint(-500,500),random.randint(-350,350)) for i in range(size)]

def move_random(p1,p2)
    for i in range(0,100+1,2):
        t = i / 100
        x = (1 - t) * p1[0] + t * p2[0]
        y = (1 - t) * p1[1] + t * p2[1]
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)

while True:
    clear_canvas()
    KPU_Ground.draw(KPU_WIDTH//2, KPU_HEIGHT//2)
    move_random(points[n-1],points[n])
    n = (n + 1) % size
    update_canvas()
    frame = (frame+1) % 8
    delay(0.02)

close_canvas()