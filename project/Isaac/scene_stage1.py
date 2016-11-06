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
    init_rooms()
    """
    rooms.append(Room_0())

    rooms.append(Room_4())
    rooms.append(Room_2())
    rooms.append(Room_3())
    rooms.append(Room_Boss_Monstro())
    rooms.append(Room_1())
    rooms.append(Room_Item_CommonCold())
    current_room = rooms[0]

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
    """

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

def update(frame_time):
    global current_room

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
            game_framework.quit()

        elif (event.type, event.key)  == (SDL_KEYDOWN,SDLK_ESCAPE):
            game_framework.quit()

        else:
            isaac.handle_event(event)

def pause():
    pass

def resume():
    pass

def init_rooms():
    global rooms
    global current_room
    way = random.randint(0, 3)
    index = 0
    count = 0

    # first_room_setting_ ::start
    rooms = [room_maker(RoomType.Room_Start)]
    rooms.append(room_maker(random.randint(1, 7)))
    connect_rooms(index, index + 1, way)
    current_room = rooms[0]
    index += 1
    # first_room_setting_ ::end

    # randomly makes rooms and connect them  :: start
    while count < 15:
        temp = random.randint(0, 3)
        while temp == way:
            temp = random.randint(0, 3)
        way = temp

        rooms.append(room_maker(random.randint(1, 7)))
        connect_rooms(index, index + 1, random.randint(0, 3))
        index += 1
        count += 1
    # :: end

def connect_rooms(index1, index2, way, map_type = MapType.Normal):
    global rooms
    opposite = None

    if way in (Way.Down,):
        opposite = Way.Up
    elif way in (Way.Up,):
        opposite = Way.Down
    elif way in (Way.Left,):
        opposite = Way.Right
    elif way in (Way.Right,):
        opposite = Way.Left

    rooms[index1].add_door(Door(way, map_type, rooms[index2]))
    rooms[index2].add_door(Door(opposite, map_type, rooms[index1]))


