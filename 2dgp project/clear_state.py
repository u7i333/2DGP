import game_framework
import game_world
from pico2d import *
import main_state
import title_state

name = "Clearstate"
image = None


def enter():
    global image
    image = load_image('./picture/clear.png')


def exit():
    global image
    del(image)


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if(event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif(event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.change_state(title_state)


def draw():
    clear_canvas()
    image.draw(300,400)
    update_canvas()


def update():
    pass


def pause():
    pass


def resume():
    pass
