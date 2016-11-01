from base import*
from pico2d import*
import game_engine
import Renderer

class TearType:
    Nothing = 0
    Normal = 1

class Tear:
    game_engine = game_engine.GameEngine(100, 100, 850, 460)
    def __init__(self, unit):
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
        self.size = unit.tear_size

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

