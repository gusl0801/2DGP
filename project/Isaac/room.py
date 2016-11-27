from Obstacle import*
from Monster import*

from Boss import *
from Item import *
from Tear import*

class Room:
    image = None
    def __init__(self):
        self.rock_list = []
        self.door_list = []
        self.campfire_list = []
        self.dung_list = []
        self.monster_num = 0
        #if RoomShape.Room_normal_one:

        if Room.image == None:
            Room.image = load_image('resource/map/map_easy.png')
        pass

    def update(self, frame_time, unit):
        for rock in self.rock_list:
            rock.check_collision(unit)

        for campfire in self.campfire_list:
            campfire.update(unit)

        for dung in self.dung_list:
            dung.check_collision(unit)

        self.update_door_lock()

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

    def change_image(self, path):
        del (Room.image)
        Room.image = load_image(path)

    def update_door_lock(self):
        if self.monster_num == 0:
            for door in self.door_list:
                door.set_lock(False)

class Room_Start(Room):
    def __init__(self, hp):
        Room.__init__(self)

    def update(self, frame_time, unit):
        Room.update(self, frame_time, unit)

        for door in self.door_list:
            if door.check_collision(unit) != None:
                return door.connected_room
        return self

    def draw(self):
        Room.draw(self)

class Room_Tumor(Room):
    def __init__(self, hp):
        Room.__init__(self)

        self.monster_num = 4
        self.tumors = [Tumor(200, 102, Way.Down, hp), Tumor(200, 450, Way.Up, hp)
            ,Tumor(760, 102, Way.Down, hp), Tumor(760, 450, Way.Up, hp)]
        self.rays = [Ray(self.tumors[1], TearType.Red_Ray),Ray(self.tumors[0], TearType.White_Ray)
                     ,Ray(self.tumors[2], TearType.Dark_Ray), Ray(self.tumors[3], TearType.Dark_Ray)]

    def update(self, frame_time, unit):
        Room.update(self, frame_time, unit)

        for tumor in self.tumors:
            if tumor.check_die():
                self.tumors.remove(tumor)
                self.monster_num -= 1

        for tumor in self.tumors:
            tumor.update(frame_time, unit)

        #for ray in self.rays:
        #    ray.update(frame_time)

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

class Room_Spider(Room):
    def __init__(self, hp):
        Room.__init__(self)
        self.rock_list.append(Rock(490, 300, RockShape.Size_oneByone1, MapType.Normal))
        self.rock_list.append(Rock(440, 250, RockShape.Size_oneByone2, MapType.Normal))
        self.rock_list.append(Rock(490, 200, RockShape.Size_oneByone3, MapType.Normal))
        self.rock_list.append(Rock(540, 250, RockShape.Size_oneByone4, MapType.Normal))

        self.monster_num = 27
        self.flies = [Fly(hp) for i in range(20)]

        self.spiders = [Spider(380,280, hp), Spider(700,380, hp), Spider(150, 150, hp)]

        self.tentacles = [Tentacle(120, 450, hp), Tentacle(120, 120, hp), Tentacle(830, 450, hp), Tentacle(830, 120, hp)]

    def update(self, frame_time, unit):
        Room.update(self, frame_time, unit)

        for fly in self.flies:
            if fly.check_die():
                self.flies.remove(fly)
                self.monster_num -= 1

        for tentacle in self.tentacles:
            if tentacle.check_die():
                self.tentacles.remove(tentacle)
                self.monster_num -= 1

        for spider in self.spiders:
            if spider.check_die():
                self.spiders.remove(spider)
                self.monster_num -= 1

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

class Room_Fly(Room):
    def __init__(self, hp):
        Room.__init__(self)

        self.campfire_list = [Campfire(130, 440), Campfire(130, 110), Campfire(830, 440), Campfire(830, 110)]
        self.dung_list = [Dung(490, 300), Dung(440, 250), Dung(490, 200), Dung(540, 250)]
        self.flies = [Fly(hp) for i in range(20)]
        self.monster_num = 20

    def update(self,frame_time,  unit):
        Room.update(self,frame_time,  unit)

        for fly in self.flies:
            if fly.check_die():
                self.flies.remove(fly)
                self.monster_num -= 1

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


class Room_Rock(Room):
    def __init__(self, hp):
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

class Room_Dung(Room):
    def __init__(self, hp):
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

class Room_NightCrawler(Room):
    def __init__(self, hp):
        Room.__init__(self)
        self.crawlers = [NightCrawler(random.randint(200,600), random.randint(200,400), hp) for i in range(5)]
        self.monster_num = 5

    def update(self,frame_time,  unit):
        Room.update(self,frame_time,  unit)

        for crawler in self.crawlers:
            if crawler.check_die():
                self.crawlers.remove(crawler)
                self.monster_num -= 1

        for crawler in self.crawlers:
            crawler.update(frame_time, unit)

        for door in self.door_list:
            if door.check_collision(unit) != None:
                return door.connected_room
        return self

    def draw(self):
        Room.draw(self)

        for crawler in self.crawlers:
            crawler.draw()

class Room_Pacer(Room):
    def __init__(self, hp):
        Room.__init__(self)
        self.pacers = [Pacer(hp) for i in range(5)]
        self.monster_num = 5

    def update(self,frame_time,  unit):
        Room.update(self,frame_time,  unit)

        for pacer in self.pacers:
            if pacer.check_die():
                self.pacers.remove(pacer)
                self.monster_num -= 1

        for pacer in self.pacers:
            pacer.update(frame_time, unit)

        for door in self.door_list:
            if door.check_collision(unit) != None:
                return door.connected_room
        return self

    def draw(self):
        Room.draw(self)

        for pacer in self.pacers:
            pacer.draw()

class Room_HP_1(Room):
    def __init__(self, hp):
        Room.__init__(self)

        self.items = [Heart(490, 270, 1)]

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

class Room_HP_2(Room):
    def __init__(self, hp):
        Room.__init__(self)

        self.items = [Heart(490, 270, 2)]
        self.rock_list = [Rock(490, 300, RockShape.Size_oneByone1, MapType.Normal),
                          Rock(440, 250, RockShape.Size_oneByone2, MapType.Normal),
                          Rock(490, 200, RockShape.Size_oneByone3, MapType.Normal)]

        self.dung_list = [Dung(130, 440), Dung(130, 110), Dung(830, 440), Dung(830, 110)]
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

class Room_Boss_Monstro(Room):
    def __init__(self, hp):
        Room.__init__(self)

        self.monstro = Monstro(480, 300)
        self.monster_num = 1

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
    def __init__(self, hp):
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
    def __init__(self, hp):
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

class Room_Item_BloodBag(Room):
    def __init__(self, hp):
        Room.__init__(self)

        self.items = [BloodBag(480, 270)]

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

class Room_Last(Room):
    def __init__(self, hp):
        Room.__init__(self)

        self.gate = Gate()
        self.framework = None
        self.next_state = None
    def update(self, frame_time, unit):
        Room.update(self,frame_time,  unit)

        if self.gate.check_collision(unit):
            self.framework.change_state(self.next_state)
            return self

        for door in self.door_list:
            if door.check_collision(unit) != None:
                return door.connected_room

        return self

    def draw(self):
        Room.draw(self)

        self.gate.draw()
    def init_framework(self, framework):
        self.framework = framework
    def init_next_state(self, state):
        self.next_state = state

def room_maker(parameter, hp):
    if parameter == RoomType.Room_Start:
        return Room_Start(hp)
    if parameter == RoomType.Room_Tumor:
        return Room_Tumor(hp)
    if parameter == RoomType.Room_Spider:
        return Room_Spider(hp)
    if parameter == RoomType.Room_Fly:
        return Room_Fly(hp)
    if parameter == RoomType.Room_Rock:
        return Room_Rock(hp)
    if parameter == RoomType.Room_Dung:
        return Room_Dung(hp)
    if parameter == RoomType.Room_HP_1:
        return Room_HP_1(hp)
    if parameter == RoomType.Room_HP_2:
        return Room_HP_2(hp)
    if parameter == RoomType.Room_NightCrawler:
        return Room_NightCrawler(hp)
    if parameter == RoomType.Room_Pacer:
        return Room_Pacer(hp)
    if parameter == RoomType.Room_Item_CommonCold:
        return Room_Item_CommonCold(hp)
    if parameter == RoomType.Room_Item_Martyr:
        return Room_Item_Martyr(hp)
    if parameter == RoomType.Room_Item_BloodBag:
        return Room_Item_BloodBag(hp)
    if parameter == RoomType.Room_Boss_Monstro:
        return Room_Boss_Monstro(hp)
    if parameter == RoomType.Room_Last:
        return Room_Last(hp)







