import Renderer
import Game_Engine
from Base import*

class ItemState:
    Noting = 0,
    #획득
    #소멸

class Item:
    def __init__(self,x,y, path, width, height, max_frame_x, max_frame_y = 0):
        self.x, self.y = x,y
        self.renderer = Renderer.Renderer(path, width, height, max_frame_x, max_frame_y)
        self.game_engine = Game_Engine.GameEngine()
        self.speed = None
        self.change_speed(1)
        self.way = Way.Up
        self.time_elapsed = 0.0
        pass

    def change_speed(self, KMPH_speed):
        PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
        RUN_SPEED_KMPH = KMPH_speed  # Km / Hour
        RUN_SPEED_MPH = (RUN_SPEED_KMPH * 1000.0 / 60.0)
        RUN_SPEED_MPS = (RUN_SPEED_MPH / 60.0)
        RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

        self.speed = RUN_SPEED_PPS

    def draw(self):
        self.renderer.draw(self.x, self.y)
        pass

    def update(self, frame_time, unit):
        self.time_elapsed += frame_time
        self.renderer.update()
        pass

    def move(self, frame_time):
        if self.way in (Way.Down,):
            self.x, self.y = self.game_engine.move(frame_time, self.speed, self.x, self.y, self.way)
        elif self.way in (Way.Up,):
            self.x, self.y = self.game_engine.move(frame_time, self.speed, self.x, self.y, self.way)

        if (self.time_elapsed > 1.0 and self.way == Way.Up):
            self.way = Way.Down
            self.time_elapsed = 0.0

        elif (self.time_elapsed > 1.0 and self.way == Way.Down):
            self.way = Way.Up
            self.time_elapsed = 0.0

    def collision_update(self, unit):
        pass

class Heart(Item):
    def __init__(self,x,y, amount):
        #Item.__init__(self,x,y, "resource/item/hp_heart.png", 24, 24)
        self.amount = amount
        self.x, self.y = x, y
        self.renderer = Renderer.Renderer("resource/item/hp_heart.png", 24, 24, amount - 1)
        self.speed = None
        self.change_speed(1)
        self.way = Way.Up
        self.time_elapsed = 0.0
        self.game_engine = Game_Engine.GameEngine()

    def draw(self):
        #Item.draw(self)
        self.renderer.draw(self.x, self.y)

    def update(self, frame_time, unit):
        Item.update(self, frame_time, unit)
        self.move(frame_time)
        return self.collision_update(unit)

    def collision_update(self, unit):
        if unit.check_collision(self.x - 20, self.x + 20, self.y - 20, self.y + 40):
            unit.set_hp(self.amount)
            return True
        return False


class Key(Item):
    def __init__(self, x, y):
        Item.__init__(self,x,y, "",0,0)

    def draw(self):
        Item.draw(self)

    def update(self, frame_time, unit):
        Item.update(self, frame_time, unit)

class CommonCold(Item):
    def __init__(self,x,y):
        Item.__init__(self, x, y, "resource/Item/common_cold.png",40,37, 0)

    def draw(self):
        Item.draw(self)
        #self.renderer.draw_boundary(self.x - 20, self.x + 20, self.y - 20, self.y + 20)

    def update(self, frame_time, unit):

        Item.update(self, frame_time, unit)
        self.move(frame_time)
        return self.collision_update(unit)

    def collision_update(self, unit):
        if unit.check_collision(self.x - 20, self.x + 20, self.y - 20, self.y + 40):
            unit.change_type(ItemType.CommonCold)
            return True

        return False

class Martyr(Item):
    def __init__(self,x,y):
        Item.__init__(self, x, y, "resource/Item/Martyr.png",40,37, 0)

    def draw(self):
        Item.draw(self)
        #self.renderer.draw_boundary(self.x - 20, self.x + 20, self.y - 20, self.y + 20)

    def update(self, frame_time, unit):

        Item.update(self, frame_time, unit)
        self.move(frame_time)
        return self.collision_update(unit)

    def collision_update(self, unit):
        if unit.check_collision(self.x - 20, self.x + 20, self.y - 20, self.y + 40):
            unit.change_type(ItemType.Martyr)
            return True

        return False

class BloodBag(Item):
    def __init__(self,x,y):
        Item.__init__(self, x, y, "resource/Item/blood_bag.png",40,37, 0)

    def draw(self):
        Item.draw(self)
        #self.renderer.draw_boundary(self.x - 20, self.x + 20, self.y - 20, self.y + 20)

    def update(self, frame_time, unit):

        Item.update(self, frame_time, unit)
        self.move(frame_time)
        return self.collision_update(unit)

    def collision_update(self, unit):
        if unit.check_collision(self.x - 20, self.x + 20, self.y - 20, self.y + 40):
            unit.change_type(ItemType.BloodBag)
            return True

        return False
