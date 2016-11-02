import random
from base import Way

class MovePattern:
    MoveX = 0
    MoveY = 1
    MoveRandomly = 2
    MoveByWay = 3

"""
PIXEL_PER_METER = (10.0 / 0.3)      #10 pixel 30 cm
RUN_SPEED_KMPH = 20.0               #Km / Hour
RUN_SPEED_MPH = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPH / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)
"""

class GameEngine:
    def __init__(self, min_x = 120, min_y = 120, max_x = 835, max_y = 460):
        self.min_x, self.min_y = min_x, min_y
        self.max_x, self.max_y = max_x, max_y

        self.move_count = 0
        self.move_x = random.randint(-3, 3)
        self.move_y = random.randint(-3, 3)

        self.prev_x, self.prev_y = 0, 0

    def move(self, frame_time, speed, x, y, way = None):
        self.prev_x, self.prev_y = x, y
        distance = speed * frame_time

        if way == None:
            x = min(x + distance, self.max_x)
            y = min(y + distance, self.max_y)

        elif way != None:
            x,y = self.move_handler[way](self, x, y,distance)

        if x <= self.min_x:
            x = self.min_x
        if y <= self.min_y:
            y = self.min_y

        return x, y

    def handle_left_move(self, x, y, distance):
        x -= distance
        return x, y

    def handle_right_move(self, x, y, distance):
        x = min(x + distance, self.max_x)
        return x, y

    def handle_down_move(self, x, y, distance):
        y -= distance
        return x, y

    def handle_up_move(self, x, y, distance):
        y = min(y + distance, self.max_y)
        return x, y

    def handle_left_up_move(self, x, y, distance):
        x -= distance
        y = min(y + distance, self.max_y)
        return x,y

    def handle_left_down_move(self, x, y, distance):
        x -= distance
        y -= distance
        return x,y

    def handle_right_up_move(self, x, y, distance):
        x = min(x + distance, self.max_x)
        y = min(y + distance, self.max_y)
        return x,y

    def handle_right_down_move(self, x, y, distance):
        x = min(x + distance, self.max_x)
        y -= distance
        return x,y

    move_handler = {
        Way.Down     : handle_down_move,
        Way.Up       : handle_up_move,
        Way.Left     : handle_left_move,
        Way.Right    : handle_right_move,
        Way.LeftUp   : handle_left_up_move,
        Way.LeftDown : handle_left_down_move,
        Way.RightUp  : handle_right_up_move,
        Way.RightDown: handle_right_down_move
    }


    def move_randomly(self, x, y):
        self.prev_x, self.prev_y = x, y

        x = min(x + self.move_x, self.max_x)
        y = min(y + self.move_y, self.max_y)

        if x <= self.min_x:
            x = self.min_x
        if y <= self.min_y:
            y = self.min_y

        self.move_count += 1
        if self.move_count > 10:
            self.move_x = random.randint(-3, 3)
            self.move_y = random.randint(-3, 3)
            self.move_count = 0

        return x, y

    def undo_move(self, x, y, pattern = 0, speed = 0):
        if pattern == MovePattern.MoveX:
            x = self.prev_x

        elif pattern == MovePattern.MoveY:
            y = self.prev_y

        elif pattern == MovePattern.MoveRandomly:
            x = self.prev_x
            y = self.prev_y

            self.move_x = random.randint(-3, 3)
            self.move_y = random.randint(-3, 3)
            self.move_count = 0

        return x, y


    def collision_check(self):
        pass
