from tear_manager import*
import game_engine

class UnitState:
    Stop = 0
    Idle = 1
    Move = 2
    Attack = 3
    Attacked = 4


class UnitTeam:
    Ally = 0
    Enemy = 1

#superclass
class Unit:
    PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
    RUN_SPEED_KMPH = 0.5  # Km / Hour
    RUN_SPEED_MPH = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPH / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)
    def __init__(self):
        self.state = UnitState.Stop

        self.tear_manager = TearManager(self)

        self.team = None
        self.sprite = None

        self.x, self.y = 490, 280
        self.image_x, self.image_y = 32, 32
        self.speed = Unit.RUN_SPEED_PPS

        self.delay = 0

        self.hp = 6

    #overrided by subclass
    def update(self, frame_time):
        pass

    #overrided by subclass
    def draw(self, frame_time):
        pass

    def collision_update(self, unit):
        pass

    def sprite_update(self):
        pass

    def move(self, x, y):
        self.x = min(self.x + x, 835)
        self.y = min(self.y + y, 460)

        if self.x <= 120:
            self.x = 120
        if self.y <= 120:
            self.y = 120

        #print("unit_x : %d, y : %d" % (self.x, self.y))

    #이동 전으로 되돌림
    def undo_move(self):
        pass


    def change_state(self, state):
        self.state = state

        #animation초기화, 이후 rendering 클래스로 따로 빼두자
        self.change_way(self.way)
        self.delay = 0
        self.frameBody = 0

    def check_collision(self, x1, x2, y1, y2):
        if ((x1 < self.x  and x2 > self.x)
            and (y1 < self.y and y2 > self.y)):
            return True

        return False

    #overrided by subclass
    def process_message(self):
        pass


