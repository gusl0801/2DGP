import Game_Framework
import Easy_Stage
from pico2d import*

name = "TitleState"
image = None
press = None
pressX, pressY = 480, 440
bgm = None
press_move_up = False

def enter():
    global image
    global press
    global bgm

    image = load_image("resource/title.png")
    press = load_image("resource/title_text.png")

    bgm = load_music('resource/sound/title_stage.mp3')
    bgm.set_volume(64)
    bgm.repeat_play()

def exit():
    global image
    global press
    global bgm

    del(image)
    del(press)
    del (bgm)

def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            Game_Framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_SPACE:
                Game_Framework.change_state(Easy_Stage)
            elif event.key == SDLK_ESCAPE:
                Game_Framework.quit()

def draw(frame_time):
    clear_canvas()
    image.draw(480, 270)
    press.draw(pressX, pressY)
    update_canvas()

def update(frame_time):
    global pressY
    global press_move_up

    if press_move_up:
        pressY = min(pressY + 0.05, 440.0)

        if pressY == 440:
            press_move_up = False

    else:
        pressY = max(pressY - 0.05, 420.0)

        if pressY == 420:
            press_move_up = True

def pause():
    pass

def resume():
    pass