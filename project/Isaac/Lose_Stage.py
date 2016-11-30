import Game_Framework
import Normal_Stage
from Isaac import *
from Room import*
from Sound import*

isaac = None
running = True
last_key = None
bgm = None
rooms = []
current_room = None
room_limits = 7
sound_manager = None

def enter():
    global isaac
    global rooms
    global current_room
    global bgm
    global sound_manager

    isaac = Isaac()

    bgm = load_music('resource/sound/easy_stage.mp3')
    bgm.set_volume(64)
    bgm.repeat_play()
    sound_manager = SoundManager()

def exit():
    global isaac
    global rooms
    global bgm
    global sound_manager

    #del(isaac)
    del(rooms)
    del(bgm)
    del(sound_manager)

def update(frame_time):
    global current_room

    if (isaac.check_die()):
        Game_Framework.change_state()
    isaac.update(frame_time)

    current_room = current_room.update(frame_time,isaac)
    delay(0.017)

def draw(frame_time):
    clear_canvas()
    current_room.draw()
    isaac.draw(frame_time)
    update_canvas()

def handle_events(frame_time):
    global last_key

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            Game_Framework.quit()

        elif (event.type, event.key)  == (SDL_KEYDOWN,SDLK_ESCAPE):
            Game_Framework.quit()
        else:
            isaac.handle_event(event)

def pause():
    pass

def resume():
    pass


