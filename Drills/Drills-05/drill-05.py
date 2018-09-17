from pico2d import *

open_canvas()
grass = load_image('grass.png')
character = load_image('animation_sheet.png')

def move_to_203_535():
    fromx, fromy = 800//2, 90
    tox, toy = 203, 535
    incre_or_decre_x = (tox - fromx)/50
    incre_or_decre_y = (toy - fromy)/50
    frame = 0

    while (fromx > tox and fromy < toy):
        clear_canvas()
        grass.draw(400,30)
        character.clip_draw(frame*100, 0, 100, 100, fromx, fromy)
        update_canvas()
        frame = (frame+1)%8
        fromx += incre_or_decre_x
        fromy += incre_or_decre_y
        delay(0.05)
        get_events()

def move_to_132_243():
    fromx, fromy = 203, 535
    tox, toy = 132, 243
    incre_or_decre_x = (tox - fromx) / 50
    incre_or_decre_y = (toy - fromy) / 50
    frame = 0

    while (fromx > tox and fromy > toy):
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 0, 100, 100, fromx, fromy)
        update_canvas()
        frame = (frame + 1) % 8
        fromx += incre_or_decre_x
        fromy += incre_or_decre_y
        delay(0.05)
        get_events()

def move_to_535_470():
    fromx, fromy = 132, 243
    tox, toy = 535, 470
    incre_or_decre_x = (tox - fromx) / 50
    incre_or_decre_y = (toy - fromy) / 50
    frame = 0

    while (fromx < tox and fromy < toy):
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 100, 100, 100, fromx, fromy)
        update_canvas()
        frame = (frame + 1) % 8
        fromx += incre_or_decre_x
        fromy += incre_or_decre_y
        delay(0.05)
        get_events()

def movo_to_477_203():
    fromx, fromy = 535, 470
    tox, toy = 477, 203
    incre_or_decre_x = (tox - fromx) / 50
    incre_or_decre_y = (toy - fromy) / 50
    frame = 0

    while (fromx > tox and fromy > toy):
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 0, 100, 100, fromx, fromy)
        update_canvas()
        frame = (frame + 1) % 8
        fromx += incre_or_decre_x
        fromy += incre_or_decre_y
        delay(0.05)
        get_events()


def movo_to_715_136():
    fromx, fromy = 477, 203
    tox, toy = 715, 136
    incre_or_decre_x = (tox - fromx) / 50
    incre_or_decre_y = (toy - fromy) / 50
    frame = 0

    while (fromx < tox and fromy > toy):
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 100, 100, 100, fromx, fromy)
        update_canvas()
        frame = (frame + 1) % 8
        fromx += incre_or_decre_x
        fromy += incre_or_decre_y
        delay(0.05)
        get_events()

def movo_to_316_225():
    fromx, fromy = 715, 136
    tox, toy = 316, 225
    incre_or_decre_x = (tox - fromx) / 50
    incre_or_decre_y = (toy - fromy) / 50
    frame = 0

    while (fromx > tox and fromy < toy):
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 0, 100, 100, fromx, fromy)
        update_canvas()
        frame = (frame + 1) % 8
        fromx += incre_or_decre_x
        fromy += incre_or_decre_y
        delay(0.05)
        get_events()


def movo_to_510_92():
    fromx, fromy = 316, 225
    tox, toy = 510, 92
    incre_or_decre_x = (tox - fromx) / 50
    incre_or_decre_y = (toy - fromy) / 50
    frame = 0

    while (fromx < tox and fromy > toy):
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 100, 100, 100, fromx, fromy)
        update_canvas()
        frame = (frame + 1) % 8
        fromx += incre_or_decre_x
        fromy += incre_or_decre_y
        delay(0.05)
        get_events()


def movo_to_692_518():
    pass

def movo_to_682_332():
    pass

def movo_to_712_349():
    pass

def movo_to_start():
    pass

def move_character():
    #move_to_203_535()
    #move_to_132_243()
    #move_to_535_470()
    #movo_to_477_203()
    #movo_to_715_136()
    #movo_to_316_225()
    movo_to_510_92()
    movo_to_692_518()
    movo_to_682_332()
    movo_to_712_349()
    movo_to_start()

while(True):
    move_character()

close_canvas()