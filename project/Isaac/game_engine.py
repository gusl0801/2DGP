import random
from base import Way

class MovePattern:
    MoveX = 0
    MoveY = 1
    MoveRandomly = 2
    MoveByWay = 3

class GameEngine:
    def __init__(self, min_x = 120, min_y = 120, max_x = 835, max_y = 460):
        self.min_x, self.min_y = min_x, min_y
        self.max_x, self.max_y = max_x, max_y

        self.move_count = 0
        self.move_x = random.randint(-3, 3)
        self.move_y = random.randint(-3, 3)

    def move(self, speed, x, y, way = None):
        if not way:
            x = min(x + speed, self.max_x)
            y = min(y + speed, self.max_y)

            if x <= self.min_x:
                x = self.min_x
            if y <= self.min_y:
                y = self.min_y
        else:
            if way == Way.Left:
                pass
            elif way == Way.Right:
                pass
            elif way == Way.Down:
                pass
            elif way == Way.Up:
                pass

        return x, y

    """
    함수 오버로딩이 지원되지 않아서 생략

    def move(self, unit):
        unit.x = min(unit.x + unit.speed, self.max_x)
        y = min(unit.y + unit.speed, self.max_y)

        if unit.x <= self.min_x:
            unit.x = self.min_x
        if unit.y <= self.min_y:
            unit.y = self.min_y
    """

    def move_randomly(self, x, y):
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
            x -= speed

        elif pattern == MovePattern.MoveY:
            y -= speed

        elif pattern == MovePattern.MoveRandomly:
            x -= self.move_x
            y -= self.move_y

            self.move_x = random.randint(-3, 3)
            self.move_y = random.randint(-3, 3)
            self.move_count = 0

        return x, y

    def collision_check(self):
        pass
