from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024

def handle_events():
    global running
    global mousex, mousey
    global movex, movey
    global x,y
    global frame

    count = 0
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            mousex, mousey = event.x, KPU_HEIGHT - 1 - event.y
        elif event.type == SDL_MOUSEBUTTONDOWN:
            mousex, mousey = event.x, KPU_HEIGHT - 1 - event.y
            movex = mousex - x
            movey = mousey - y
            while count < 10:
                clear_canvas()
                kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
                if(movex > 0):
                    character.clip_draw(frame * 100, 100 , 100, 100, x, y)
                else:
                    character.clip_draw(frame * 100, 0, 100, 100, x, y)
                x = x + movex/ 10
                y = y + movey/ 10
                count = count +1
                frame = (frame + 1) % 8
                update_canvas()
                delay(0.02)

        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
mousecursor = load_image('hand_arrow.png')

running = True
mousex, mousey = KPU_WIDTH // 2, KPU_HEIGHT // 2
global x, y
x,y = KPU_WIDTH // 2, KPU_HEIGHT // 2
frame = 0
hide_cursor()


while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    mousecursor.draw(mousex, mousey)
    update_canvas()
    frame = (frame + 1) % 8
    delay(0.02)
    handle_events()


close_canvas()

