from tear_manager import*
import game_engine

class UnitState:
    Stop = 0
    Idle = 1
    Move = 2
    Attack = 3
    Wait = 4
    Attacked = 5


class UnitTeam:
    Ally = 0
    Enemy = 1

#superclass
class Unit:
    def __init__(self):
        self.state = UnitState.Idle

        self.tear_type = TearType.Normal
        self.tear_manager = TearManager(self)

        self.team = None
        self.sprite = None

        self.x, self.y = 490, 280
        self.image_x, self.image_y = 32, 32

        self.speed = None
        self.move_way = None
        self.init_speed()

        self.delay = 0

        self.hp = 6

        self.time_elapsed = 0.0
        self.state_handler = \
            {
                UnitState.Stop    : self.handle_stop,
                UnitState.Idle    : self.handle_idle,
                UnitState.Move    : self.handle_move,
                UnitState.Attack  : self.handle_attack,
                UnitState.Wait    : self.handle_wait,
                UnitState.Attacked: self.handle_attacked
            }
    #overrided by subclass
    def update(self, frame_time):
        pass

    #overrided by subclass
    def draw(self, frame_time):
        pass

    def collision_update(self, unit):
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

    def detect_enemy_pos(self, enemy):
        exist_on_left = (enemy.x <= self.x) #enemy is exist on left face
        exist_on_up = (enemy.y >= self.y)   #enemy is exist on up face

        if (exist_on_left and exist_on_up):
            self.way = Way.LeftUp
        elif (exist_on_left and not exist_on_up):
            self.way = Way.LeftDown
        elif (not exist_on_left and exist_on_up):
            self.way = Way.RightUp
        elif (not exist_on_left and not exist_on_up):
            self.way = Way.RightDown

    def detect_enemy_x_pos(self, enemy):
        exist_on_left = (enemy.x <= self.x) #enemy is exist on left face

        if exist_on_left :
            self.move_way = Way.Left
        if not exist_on_left:
            self.move_way = Way.Right

    def detect_enemy_y_pos(self, enemy):
        exist_on_up = (enemy.y >= self.y)   #enemy is exist on up face

        if exist_on_up:
            self.move_way = Way.Up
        if not exist_on_up:
            self.move_way = Way.Down

    def change_state(self, state):
        self.state = state
        self.time_elapsed = 0
        pass

    def detect_enemy(self, enemy):
        pass

    def set_hp(self, amount):
        self.hp += amount

    def check_die(self):
        if self.hp <= 0:
            return True
        return False

    def check_collision(self, x1, x2, y1, y2):
        if self.state in (UnitState.Attacked,):
            return False

        if ((x1 < self.x  and x2 > self.x)
            and (y1 < self.y and y2 > self.y)):
            return True

        return False

    def init_speed(self):
        PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
        RUN_SPEED_KMPH = 20  # Km / Hour
        RUN_SPEED_MPH = (RUN_SPEED_KMPH * 1000.0 / 60.0)
        RUN_SPEED_MPS = (RUN_SPEED_MPH / 60.0)
        RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

        self.speed = RUN_SPEED_PPS

    def change_speed(self, KMPH_speed):
        PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
        RUN_SPEED_KMPH = KMPH_speed  # Km / Hour
        RUN_SPEED_MPH = (RUN_SPEED_KMPH * 1000.0 / 60.0)
        RUN_SPEED_MPS = (RUN_SPEED_MPH / 60.0)
        RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

        self.speed = RUN_SPEED_PPS
    def handle_stop(self, frame_time, unit = None):
        pass
    def handle_move(self, frame_time, unit= None):
        pass
    def handle_idle(self, frame_time, unit= None):
        pass
    def handle_attack(self, frame_time, unit= None):
        pass
    def handle_wait(self, frame_time, unit= None):
        pass
    def handle_attacked(self, frame_time, unit= None):
        pass
