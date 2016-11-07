from obstacle import*
from Monster import*

from Boss import *
from Item import *
from tear import*

class Room:
    image = None
    def __init__(self):
        self.rock_list = []
        self.door_list = []
        self.campfire_list = []
        self.dung_list = []
        #if RoomShape.Room_normal_one:

        if Room.image == None:
            Room.image = load_image('resource/map/map_normal.png')
        pass

    def update(self, frame_time, unit):
        for rock in self.rock_list:
            rock.check_collision(unit)

        for campfire in self.campfire_list:
            campfire.update(unit)

        for dung in self.dung_list:
            dung.check_collision(unit)

    def draw(self):
        self.image.draw(480, 270)

        for rock in self.rock_list:
            rock.draw()

        for door in self.door_list:
            door.draw()

        for campfire in self.campfire_list:
            campfire.draw()

        for dung in self.dung_list:
            dung.draw()

    def check_frame_out(self):
        pass

    def add_door(self, door):
        self.door_list.append(door)
class Room_Start(Room):
    def __init__(self):
        Room.__init__(self)

    def update(self, frame_time, unit):
        Room.update(self, frame_time, unit)

        for door in self.door_list:
            if door.check_collision(unit) != None:
                return door.connected_room
        return self

    def draw(self):
        Room.draw(self)

class Room_0(Room):
    def __init__(self):
        Room.__init__(self)

        self.tumors = [Tumor(200, 102, Way.Down), Tumor(200, 450, Way.Up)
            ,Tumor(760, 102, Way.Down), Tumor(760, 450, Way.Up)]
        self.rays = [Ray(self.tumors[1], TearType.Red_Ray),Ray(self.tumors[0], TearType.White_Ray)
                     ,Ray(self.tumors[2], TearType.Dark_Ray), Ray(self.tumors[3], TearType.Dark_Ray)]

    def update(self, frame_time, unit):
        Room.update(self, frame_time, unit)

        for tumor in self.tumors:
            tumor.update(frame_time, unit)

        for ray in self.rays:
            ray.update(frame_time)

        for door in self.door_list:
            if door.check_collision(unit) != None:
                return door.connected_room
        return self

    def draw(self):
        Room.draw(self)

        for tumor in self.tumors:
            tumor.draw()
        #for ray in self.rays:
        #    ray.draw()

class Room_1(Room):
    def __init__(self):
        Room.__init__(self)
        self.rock_list.append(Rock(490, 300, RockShape.Size_oneByone1, MapType.Normal))
        self.rock_list.append(Rock(440, 250, RockShape.Size_oneByone2, MapType.Normal))
        self.rock_list.append(Rock(490, 200, RockShape.Size_oneByone3, MapType.Normal))
        self.rock_list.append(Rock(540, 250, RockShape.Size_oneByone4, MapType.Normal))

        self.flies = [Fly() for i in range(20)]

        self.spiders = [Spider(380,280), Spider(700,380), Spider(150, 150)]

        self.tentacles = [Tentacle(120, 450), Tentacle(120, 120), Tentacle(830, 450), Tentacle(830, 120)]

    def update(self, frame_time, unit):
        Room.update(self, frame_time, unit)

        for fly in self.flies:
            fly.update(frame_time, unit)

        for tentacle in self.tentacles:
            tentacle.update(frame_time, unit)

        for spider in self.spiders:
            spider.update(frame_time, unit)

        for rock in self.rock_list:
            for spider in self.spiders:
                rock.check_collision(spider)



        for door in self.door_list:
            if door.check_collision(unit) != None:
                return door.connected_room
        return self

    def draw(self):
        Room.draw(self)

        for tentacle in self.tentacles:
            tentacle.draw()

        for fly in self.flies:
            fly.draw()

        for spider in self.spiders:
            spider.draw()

class Room_2(Room):
    def __init__(self):
        Room.__init__(self)

        self.campfire_list = [Campfire(130, 440), Campfire(130, 110), Campfire(830, 440), Campfire(830, 110)]
        self.dung_list = [Dung(490, 300), Dung(440, 250), Dung(490, 200), Dung(540, 250)]
        self.flies = [Fly() for i in range(20)]

    def update(self,frame_time,  unit):
        Room.update(self,frame_time,  unit)

        for fly in self.flies:
            fly.update(frame_time, unit)

        for door in self.door_list:
            if door.check_collision(unit) != None:
                return door.connected_room
        return self

    def draw(self):
        Room.draw(self)

        for fly in self.flies:
            fly.draw()


class Room_3(Room):
    def __init__(self):
        Room.__init__(self)

        self.rock_list.append(Rock(140, 160, RockShape.Size_oneByone1, MapType.Normal))
        self.rock_list.append(Rock(180, 160, RockShape.Size_oneByone1, MapType.Normal))
        self.rock_list.append(Rock(220, 160, RockShape.Size_oneByone5, MapType.Normal))
        self.rock_list.append(Rock(180, 110, RockShape.Size_oneByone4, MapType.Normal))
        self.rock_list.append(Rock(220, 110, RockShape.Size_oneByone1, MapType.Normal))
        self.rock_list.append(Rock(300, 140, RockShape.Size_twoBytwo, MapType.Normal))
        self.rock_list.append(Rock(140, 210, RockShape.Size_oneByone1, MapType.Normal))
        self.rock_list.append(Rock(180, 210, RockShape.Size_oneByone2, MapType.Normal))
        self.rock_list.append(Rock(220, 210, RockShape.Size_oneByone4, MapType.Normal))
        self.rock_list.append(Rock(260, 210, RockShape.Size_oneByone6, MapType.Normal))

        self.rock_list.append(Rock(790, 400, RockShape.Size_twoBytwo, MapType.Normal))
        self.rock_list.append(Rock(680, 400, RockShape.Size_twoBytwo, MapType.Normal))
        self.rock_list.append(Rock(570, 400, RockShape.Size_twoBytwo, MapType.Normal))
        self.rock_list.append(Rock(790, 140, RockShape.Size_twoBytwo, MapType.Normal))
        self.rock_list.append(Rock(680, 140, RockShape.Size_twoBytwo, MapType.Normal))

    def update(self, frame_time, unit):
        Room.update(self,frame_time,  unit)

        for door in self.door_list:
            if door.check_collision(unit) != None:
                return door.connected_room
        return self

    def draw(self):
        Room.draw(self)

class Room_4(Room):
    def __init__(self):
        Room.__init__(self)

        self.dung_list = [Dung(130, 440), Dung(130, 110), Dung(830, 440), Dung(830, 110)]

    def update(self, frame_time, unit):
        Room.update(self, frame_time, unit)

        for door in self.door_list:
            if door.check_collision(unit) != None:
                return door.connected_room
        return self

    def draw(self):
        Room.draw(self)

class Room_Boss_Monstro(Room):
    def __init__(self):
        Room.__init__(self)

        self.monstro = Monstro(480, 300)

    def update(self, frame_time, unit):
        Room.update(self,frame_time,  unit)

        self.monstro.update(frame_time, unit)

        for door in self.door_list:
            if door.check_collision(unit) != None:
                return door.connected_room
        return self

    def draw(self):
        Room.draw(self)

        self.monstro.draw()
class Room_Item_CommonCold(Room):
    def __init__(self):
        Room.__init__(self)

        self.items = [CommonCold(480, 270)]

    def update(self, frame_time, unit):
        Room.update(self,frame_time,  unit)

        for item in self.items:
            if item.update(frame_time, unit):
                self.items.remove(item)

        for door in self.door_list:
            if door.check_collision(unit) != None:
                return door.connected_room

        return self

    def draw(self):
        Room.draw(self)

        for item in self.items:
            item.draw()
class Room_Item_Martyr(Room):
    def __init__(self):
        Room.__init__(self)

        self.items = [Martyr(480, 270)]

    def update(self, frame_time, unit):
        Room.update(self,frame_time,  unit)

        for item in self.items:
            if item.update(frame_time, unit):
                self.items.remove(item)

        for door in self.door_list:
            if door.check_collision(unit) != None:
                return door.connected_room

        return self

    def draw(self):
        Room.draw(self)

        for item in self.items:
            item.draw()

def room_maker(parameter):
    if parameter == RoomType.Room_Start:
        return Room_Start()
    if parameter == RoomType.Room0:
        return Room_0()
    if parameter == RoomType.Room1:
        return Room_1()
    if parameter == RoomType.Room2:
        return Room_2()
    if parameter == RoomType.Room3:
        return Room_3()
    if parameter == RoomType.Room4:
        return Room_4()
    if parameter == RoomType.Room_Item_CommonCold:
        return Room_Item_CommonCold()
    if parameter == RoomType.Room_Item_Martyr:
        return Room_Item_Martyr()
    if parameter == RoomType.Room_Boss_Monstro:
        return Room_Boss_Monstro()







