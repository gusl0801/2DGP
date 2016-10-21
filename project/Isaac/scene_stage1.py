import game_framework
from isaac import *
from room import*

isaac = None
running = True
last_key = None
bgm = None
rooms = []
current_room = None

def enter():
    global isaac
    global rooms
    global current_room
    global bgm

    isaac = Isaac()

    rooms.append(Room_0())
    current_room = rooms[0]

    rooms.append(Room_4())
    rooms.append(Room_2())
    rooms.append(Room_3())
    rooms.append(Room_5())
    rooms.append(Room_1())

    rooms[0].add_door(Door(Way.Up, MapType.Normal, rooms[1]))
    rooms[1].add_door(Door(Way.Down, MapType.Normal, rooms[0]))

    rooms[1].add_door(Door(Way.Right, MapType.Normal, rooms[2]))
    rooms[2].add_door(Door(Way.Left, MapType.Normal, rooms[1]))

    rooms[2].add_door(Door(Way.Down, MapType.Normal, rooms[3]))
    rooms[3].add_door(Door(Way.Up, MapType.Normal, rooms[2]))

    rooms[3].add_door(Door(Way.Down, MapType.Normal, rooms[5]))
    rooms[5].add_door(Door(Way.Up, MapType.Normal, rooms[3]))

    rooms[4].add_door(Door(Way.Right, MapType.Normal, rooms[0]))
    rooms[0].add_door(Door(Way.Left, MapType.Normal, rooms[4]))

    bgm = load_music('resource/sound/easy_stage.mp3')
    bgm.set_volume(64)
    bgm.repeat_play()

def exit():
    global isaac
    global rooms
    global bgm

    del(isaac)
    del(rooms)
    del(bgm)

def update():
    global current_room

    isaac.update()

    current_room = current_room.update(isaac)
    delay(0.017)

def draw():
    clear_canvas()
    current_room.draw()
    isaac.draw()
    update_canvas()

def handle_events():
    global last_key

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key != None:
                last_key = event.key
                print(last_key)

            if event.key == SDLK_d:
                isaac.change_way(Way.Right)
                isaac.change_state(UnitState.Move)

            elif event.key == SDLK_a:
                isaac.change_way(Way.Left)
                isaac.change_state(UnitState.Move)

            elif event.key == SDLK_w:
                isaac.change_way(Way.Up)
                isaac.change_state(UnitState.Move)

            elif event.key == SDLK_s:
                isaac.change_way(Way.Down)
                isaac.change_state(UnitState.Move)

            elif event.key == SDLK_UP:
                isaac.change_way(Way.Up)
                isaac.change_state(UnitState.Attack)
                isaac.shot_tear()

            elif event.key == SDLK_DOWN:
                isaac.change_way(Way.Down)
                isaac.change_state(UnitState.Attack)
                isaac.shot_tear()

            elif event.key == SDLK_LEFT:
                isaac.change_way(Way.Left)
                isaac.change_state(UnitState.Attack)
                isaac.shot_tear()

            elif event.key == SDLK_RIGHT:
                isaac.change_way(Way.Right)
                isaac.change_state(UnitState.Attack)
                isaac.shot_tear()

            elif event.key == SDLK_ESCAPE:
                game_framework.quit()

        elif event.type == SDL_KEYUP:
            if (event.key == SDLK_w
                or event.key == SDLK_d
                or event.key == SDLK_s
                or event.key == SDLK_a):

                if last_key == event.key:
                    isaac.change_state(UnitState.Stop)
                    last_key = None
"""
눈물 발사 간격
이 전에 입력이 들어오면
저장
일정 간격 이후에 발사?
"""

def pause():
    pass

def resume():
    pass



