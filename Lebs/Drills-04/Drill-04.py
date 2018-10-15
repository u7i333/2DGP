from pico2d import *
open_canvas()
grass = load_image('grass.png')
character = load_image('animation_sheet.png')

x=0
frame = 0
buho=1
sheatnum=1

while(True):
    clear_canvas()
    grass.draw(400,30)
    character.clip_draw(frame * 100, 100*sheatnum , 100, 100, x, 90)
    update_canvas()
    frame = (frame+1) %8
    x += (buho*5)
    delay(0.05)
    if(x>=800):
        sheatnum = 0
        buho = -1*buho
    if(x<=0):
        sheatnum = 1
        buho = -1*buho
    get_events()
