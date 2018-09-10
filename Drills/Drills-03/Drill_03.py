from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x=400
y=90
r=0

while(True):
    while(x<800):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x = x+2
        delay(0.02)
    while(y<600):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        y = y+2
        delay(0.02)
    while(x>0):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x = x-2
        delay(0.02)
    while(y>90):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        y = y-2
        delay(0.02)
    while(x<400):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x = x+2
        delay(0.02)
    r = 270
    while(r<630):
        radian = math.radians(r)
        clear_canvas_now()
        grass.draw_now(400,30)
        x = 400+220*math.cos(radian)
        y = 300+220*math.sin(radian)
        character.draw_now(x,y)
        r=r+1
        delay(0.02)
    
