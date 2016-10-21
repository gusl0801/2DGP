from base import*
from pico2d import*

class TearType:
    Nothing = 0
    Normal = 1

class Tear:
    def __init__(self, unit):
        if unit.way == Way.Down:
            self.x, self.y = unit.x, unit.y - 7
        elif unit.way == Way.Right:
            self.x, self.y = unit.x + 7, unit.y
        elif unit.way == Way.Up:
            self.x, self.y = unit.x, unit.y + 7
        elif unit.way == Way.Left:
            self.x, self.y = unit.x - 7, unit.y

        self.speed = 5
        self.team = unit.team
        self.way = unit.way
        self.size = unit.tear_size

        if unit.tear_type == TearType.Normal:
            self.image = load_image('resource/tear/normal.png')

    def move(self, x, y):
        self.x = self.x + x
        self.y = self.y + y

        #print("tear_x : %d, y : %d" % (self.x, self.y))

    def check_collision(self, x1, x2, y1, y2):
        if ((x1 < self.x  and x2 > self.x)
            and (y1 < self.y and y2 > self.y)):
            return True

        return False

    def check_frame_out(self):
        if self.x < 100:
            return True
        if self.y < 100:
            return True
        if self.x > 850:
            return True
        if self.y > 460:
            return True

        return False

    def update(self):
        if self.way == Way.Down:
            self.move(0, -self.speed)
        elif self.way == Way.Right:
            self.move(self.speed, 0)
        elif self.way == Way.Up:
            self.move(0, self.speed)
        elif self.way == Way.Left:
            self.move(-self.speed, 0)

    def draw(self):
        self.image.clip_draw(self.size * 48, 0, 48, 48, self.x, self.y)

