import Game_Framework
from Isaac import *
from Room import*
import Normal_Stage
from Sound import*
import Title_Scene
import Lose_Stage
import Win_Stage

isaac = None
running = True
last_key = None
bgm = None
rooms = []
current_room = None
room_limits = 5
sound_manager = None

def enter():
    global isaac
    global rooms
    global current_room
    global bgm
    global sound_manager

    Room.change_image(Room,'resource/map/map_hard.png')
    isaac = Normal_Stage.isaac
    isaac.init_position()

    del(Normal_Stage.isaac)
    init_rooms()

    bgm = load_music('resource/sound/hard_stage.mp3')
    bgm.set_volume(64)
    bgm.repeat_play()
    sound_manager = SoundManager()

def exit():
    global isaac
    global rooms
    global bgm
    global sound_manager

    del(isaac)
    del(rooms)
    del(bgm)
    del(sound_manager)

def update(frame_time):
    global current_room

    if (isaac.check_die()):
        Game_Framework.change_state(Lose_Stage)

    if (current_room.is_ending()):
        Game_Framework.change_state(Win_Stage)

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

def init_rooms():
    global rooms
    global current_room
    way = random.randint(0, 3)
    index = 0
    random_num = 0
    exist_boss_room = False

    # first_room_setting_ ::start
    rooms = [room_maker(RoomType.Room_Start, 4)]
    rooms.append(room_maker(random.randint(1, 9), 4))
    connect_rooms(index, index + 1, way)

    # connect item-room   ::start
    way = calculate_door_way(way)
    random_num = random.randint(21, 23)
    if random_num == RoomType.Room_Item_CommonCold:
        rooms.append(room_maker(RoomType.Room_Item_CommonCold, 4))
        connect_rooms(0,  2, way)
    elif random_num == RoomType.Room_Item_Martyr:
        rooms.append(room_maker(RoomType.Room_Item_Martyr, 4))
        connect_rooms(0,  2, way)
    elif random_num == RoomType.Room_Item_BloodBag:
        rooms.append(room_maker(RoomType.Room_Item_BloodBag, 4))
        connect_rooms(0, 2, way)
    else:
        rooms.append(room_maker(RoomType.Room_Item_Martyr, 4))
        connect_rooms(0, 2, way)
    # connect item-room   ::end

    index = 2
    current_room = rooms[0]
    # first_room_setting_ ::end

    # randomly makes rooms and connect them  :: start
    while True:
        if index > room_limits :
            if not exist_boss_room:
                way = calculate_door_way(way)
                random_num = random.randint(0, 0)
                if random_num == 0:
                    rooms.append(room_maker(RoomType.Room_Boss_Mom, 4))
                    connect_rooms(index, index + 1, way)
                    index += 1
                    exist_boss_room = True
            #here
            break
        else:
            way = calculate_door_way(way)
            rooms.append(room_maker(random.randint(1, 9),4))
            connect_rooms(index, index + 1, way)
            index += 1

    # create last room ::start
    way = calculate_door_way(way)
    rooms.append(room_maker(RoomType.Room_Boss_Mom, 4))
    connect_rooms(index, index + 1, way)
    # create last room ::end
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

def calculate_door_way(way):
    while True:
        temp = random.randint(0, 3)
        if way == Way.Left and temp not in(Way.Right, Way.Left):
            break;
        if way == Way.Right and temp not in (Way.Left, Way.Right):
            break;
        if way == Way.Up and temp not in(Way.Down, Way.Up):
            break;
        if way == Way.Down and temp not in(Way.Up, Way.Down):
            break;
    return temp


