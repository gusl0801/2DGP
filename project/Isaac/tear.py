from base import*
from pico2d import*
import game_engine
import Renderer

class TearType:
    Nothing = 0
    Normal = 1
    Dark_Ray = 2
    White_Ray = 3
    Red_Ray = 4

class Tear:
    game_engine = game_engine.GameEngine(100, 100, 850, 460)
    def __init__(self, unit, size = 5):
        if unit.way == Way.Down:
            self.x, self.y = unit.x, unit.y - 7
        elif unit.way == Way.Right:
            self.x, self.y = unit.x + 7, unit.y
        elif unit.way == Way.Up:
            self.x, self.y = unit.x, unit.y + 7
        elif unit.way == Way.Left:
            self.x, self.y = unit.x - 7, unit.y

        self.speed = unit.speed
        self.team = unit.team
        self.way = unit.way
        self.size = size

        if unit.tear_type == TearType.Normal:
            self.renderer = Renderer.Renderer('resource/tear/normal.png',48,48, self.size)

    def move(self, frame_time):
        self.x, self.y = self.game_engine.move(frame_time, self.speed, self.x, self.y, self.way)

    def check_collision(self, x1, x2, y1, y2):
        if ((x1 < self.x  and x2 > self.x)
            and (y1 < self.y and y2 > self.y)):
            return True

        return False

    def check_frame_out(self):
        if self.x <= 100:
            return True
        if self.y <= 100:
            return True
        if self.x >= 850:
            return True
        if self.y >= 460:
            return True

        return False

    def update(self ,frame_time):
        self.x, self.y = self.game_engine.move(frame_time, self.speed, self.x, self.y, self.way)
        #self.move_handler[self.way](self, frame_time)

    def draw(self):
        self.renderer.draw(self.x, self.y)

class Ray:
    def __init__(self, unit, type):
        frame = 0
        if unit.way == Way.Down:
            frame = 0
            self.x, self.y = unit.x - 3, unit.y + 100
        elif unit.way == Way.Right:
            self.x, self.y = unit.x + 7, unit.y
        elif unit.way == Way.Up:
            frame = 1
            self.x, self.y = unit.x - 3, unit.y - 80
        elif unit.way == Way.Left:
            self.x, self.y = unit.x - 7, unit.y

        self.team = unit.team
        self.way = unit.way

        if type == TearType.Dark_Ray:   #dark_ray_small :: 31, 64, big :: 63, 128
            self.renderer = Renderer.Renderer('resource/tear/dark_ray.png', 63, 166, 0, frame)

        if type == TearType.White_Ray:  #white_ray :: 110, 256, small :: 62, 154
            self.renderer = Renderer.Renderer('resource/tear/white_ray.png', 63, 166, 0, frame)

        if type == TearType.Red_Ray:
            self.renderer = Renderer.Renderer('resource/tear/red_ray.png', 63, 166, 0, frame)

    def move(self, frame_time):
        pass

    def check_collision(self, x1, x2, y1, y2):
        if ((x1 < self.x and x2 > self.x)
            and (y1 < self.y and y2 > self.y)):
            return True

        return False

    def check_frame_out(self):
        if self.x <= 100:
            return True
        if self.y <= 100:
            return True
        if self.x >= 850:
            return True
        if self.y >= 460:
            return True

        return False

    def update(self, frame_time):
        self.renderer.update(4)
        pass

    def draw(self):
        self.renderer.draw(self.x, self.y)


