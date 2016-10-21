
from pico2d import*
from base import*

class Rock:
    image = None
    def __init__(self, x, y, shape, map_type):
        self.x , self.y = x, y
        self.shape = shape

        if map_type == MapType.Normal:
            if Rock.image == None:
                Rock.image = load_image('resource/map/rock_normal.png')
        pass

    def draw(self):
        if self.shape == RockShape.Size_oneByone1:
            self.image.clip_draw(0, 384, 64, 64, self.x, self.y)
        elif self.shape == RockShape.Size_oneByone2:
            self.image.clip_draw(64, 384, 64, 64, self.x, self.y)
        elif self.shape == RockShape.Size_oneByone3:
            self.image.clip_draw(0, 320, 64, 64, self.x, self.y)
        elif self.shape == RockShape.Size_oneByone4:
            self.image.clip_draw(64, 320, 64, 64, self.x, self.y)
        elif self.shape == RockShape.Size_oneByone5:
            self.image.clip_draw(64, 256, 64, 64, self.x, self.y)
        elif self.shape == RockShape.Size_oneByone6:
            self.image.clip_draw(64, 192, 64, 64, self.x, self.y)
        elif self.shape == RockShape.Size_twoByone:
            self.image.clip_draw(0, 192, 64, 128, self.x, self.y)
        elif self.shape == RockShape.Size_oneBytwo:
            self.image.clip_draw(0, 128, 128, 64, self.x, self.y)
        elif self.shape == RockShape.Size_twoBytwo:
            self.image.clip_draw(0, 0, 128, 128, self.x, self.y)

    def check_collision(self, unit):


        if self.shape == RockShape.Size_oneBytwo:
            unit.tear_manager.collision_update_ob(elf.x - 64, self.x + 64, self.y - 32, self.y + 32)
            if unit.check_collision(self.x - 64, self.x + 64, self.y - 32, self.y + 32):
                unit.undo_move()
            return
        if self.shape == RockShape.Size_twoByone:
            unit.tear_manager.collision_update_ob(elf.x - 32, self.x + 32, self.y - 64, self.y + 64)
            if unit.check_collision(self.x - 32, self.x + 32, self.y - 64, self.y + 64):
                unit.undo_move()
            return
        if self.shape == RockShape.Size_twoBytwo:
            unit.tear_manager.collision_update_ob(self.x - 64, self.x + 64, self.y - 54, self.y + 90)
            if unit.check_collision(self.x - 64, self.x + 64, self.y - 54, self.y + 90):
                unit.undo_move()
            return

        unit.tear_manager.collision_update_ob(self.x - 32, self.x + 32, self.y, self.y + 64)
        if unit.check_collision(self.x - 32, self.x + 32, self.y, self.y + 64):
            unit.undo_move()

    def check_point_collision(self, x1, x2, y1, y2):
        if ((x1 < self.x  and x2 > self.x)
            and (y1 < self.y and y2 > self.y)):
            return True

        return False
        #unit 가로 80 세로 100
        #rock 가로 64 세로 64(칸당)

class Dung:
    sprite = None
    def __init__(self, x, y, shape = DungShape.Brown):
        if Dung.sprite == None:
            Dung.sprite = load_image('resource/obstacle/dung.png')
        self.hp = 5
        self.x, self.y = x, y
        self.shape = shape

    def update(self, unit):

        pass

    def draw(self):
        self.sprite.clip_draw((5 - self.hp) * 64, self.shape * 64, 64, 64, self.x, self.y)

    def check_collision(self, unit):
        unit.tear_manager.collision_update_ob(self.x - 32, self.x + 32, self.y, self.y + 64)

        if unit.check_collision(self.x - 32, self.x + 32, self.y, self.y + 64):
            unit.undo_move()


class Campfire:
    sprite_wood = None
    sprite_fire = None
    def __init__(self, x, y):
        if Campfire.sprite_wood == None:
           self.sprite_wood = load_image('resource/obstacle/wood.png')
        if Campfire.sprite_fire == None:
           self.sprite_fire = load_image('resource/obstacle/fire_red.png')
        self.x, self. y = x, y
        self.frame_wood = Point(0, 0)
        self.frame_fire = Point(0, 0)
        self.delay = 0

    def update(self, unit):
        self.delay += 1

        if self.delay > 2:
            self.delay = 0
            self.frame_fire.x = (self.frame_fire.x + 1) % 6

        self.check_collision(unit)
        unit.tear_manager.collision_update_ob(self.x - 32, self.x + 32, self.y, self.y + 50)
        pass

    def draw(self):
        self.sprite_wood.clip_draw(self.frame_wood.x * 64, 192, 64, 64, self.x, self.y)
        self.sprite_fire.clip_draw(self.frame_fire.x * 96, 96, 96, 96, self.x, self.y + 35)
        pass

    def check_collision(self, unit):
        if unit.check_collision(self.x - 32, self.x + 32, self.y, self.y + 50):
            unit.undo_move()
class Door:
    image = None

    def __init__(self, way, map_type, room = None):
        if way == Way.Left:
            self.x, self.y = 72, 270
        elif way == Way.Right:
            self.x, self.y = 888, 270
        elif way == Way.Up:
            self.x, self.y = 490, 480
        elif way == Way.Down:
            self.x, self.y = 490, 55

        self.way = way
        self.connected_room = room

        if map_type == MapType.Normal:
            if Door.image == None:
                Door.image = load_image('resource/map/door_normal.png')
        """
        elif map_type == MapType.blood:
            self.image = load_image('')
        elif map_type == MapType.boss:
            self.image = load_image('')
        """

    def draw(self):
        if self.way == Way.Up:
            self.image.clip_draw(0, 100, 100, 60, self.x, self.y)
        elif self.way == Way.Down:
            self.image.clip_draw(100, 100, 100, 60, self.x, self.y)
        elif self.way == Way.Left:
            self.image.clip_draw(0, 0, 60, 100, self.x, self.y)
        elif self.way == Way.Right:
            self.image.clip_draw(60, 0, 60, 100, self.x, self.y)

    def check_collision(self, unit):
       if unit.check_collision(self.x - 70, self.x + 50, self.y - 25, self.y + 70):
            unit.change_room(self.way)
            return self.connected_room
       return None

    def connect_room(self, room):
        self.conntected_room = room