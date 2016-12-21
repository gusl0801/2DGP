import Game_Framework

from Sound import*
import Title_Scene

running = True
last_key = None
bgm = None
sound_manager = None
background = None
cry = None

def enter():
    global bgm
    global sound_manager
    global background
    global cry

    background = load_image("resource/win.png")
    cry = load_image("resource/cry.png")
    bgm = load_music('resource/sound/easy_stage.mp3')
    bgm.set_volume(64)
    bgm.repeat_play()
    sound_manager = SoundManager()

def exit():
    global bgm
    global sound_manager
    global background
    global cry

    del(cry)
    del(background)
    del(bgm)
    del(sound_manager)

def update(frame_time):
    global current_room

    delay(0.017)

def draw(frame_time):
    clear_canvas()
    background.draw(480,270, 960, 540)
    update_canvas()

def handle_events(frame_time):
    global last_key

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            Game_Framework.quit()

        elif (event.type, event.key)  == (SDL_KEYDOWN,SDLK_ESCAPE):
            Game_Framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            Game_Framework.change_state(Title_Scene)

def pause():
    pass

def resume():
    pass


