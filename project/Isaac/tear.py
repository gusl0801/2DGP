from Base import*
from pico2d import*
import Game_Engine
import Renderer

class TearType:
    Nothing = 0
    Normal = 1
    Dark_Ray = 2
    White_Ray = 3
    Red_Ray = 4
    Commond_Cold = 5
    BloodBag     = 6

class TearState:
    Idle      = 0
    Disappear = 1
    Wait      = 2

class Tear:
    game_engine = Game_Engine.GameEngine(100, 100, 850, 460)
    def __init__(self, unit, size = 1):
        if unit.way == Way.Down:
            self.x, self.y = unit.x, unit.y - 7
        elif unit.way == Way.Right:
            self.x, self.y = unit.x + 7, unit.y
        elif unit.way == Way.Up:
            self.x, self.y = unit.x, unit.y + 7
        elif unit.way == Way.Left:
            self.x, self.y = unit.x - 7, unit.y

        self.change_speed(30)
        self.team = unit.team
        self.way = unit.way
        self.size = size
        self.tear_type = unit.tear_type
        self.state = TearState.Idle
        self.time_elapsed = 0
        self.disappear  = False
        self.attackable = True

        if unit.tear_type == TearType.Normal:
            self.renderer = Renderer.Renderer('resource/tear/normal.png',68,64,12)
        elif unit.tear_type == TearType.Commond_Cold:
            self.renderer = Renderer.Renderer('resource/tear/common_cold.png', 68, 64,12)
        elif unit.tear_type == TearType.BloodBag:
            self.renderer = Renderer.Renderer('resource/tear/blood_bag.png', 68, 64,12)
        self.state_handler = \
            {
                TearState.Idle       : self.handle_idle,
                TearState.Disappear  : self.handle_disappear,
                TearState.Wait       : self.handle_wait
            }

    def get_instance(self):
        return TearType.Normal

    def move(self, frame_time):
        self.x, self.y = self.game_engine.move(frame_time, self.speed, self.x, self.y, self.way)

    def check_collision(self, x1, x2, y1, y2):
        if self.state not in (TearState.Idle,):
            return False
        size = 7 * self.size
        if ((x1 < self.x - size and x2 > self.x + size)
            and (y1 < self.y  - size and y2 > self.y + size)):
            self.attackable = False
            return True

        return False


    def get_attackable(self):
        return self.attackable

    def set_attackable(self, attackable):
        self.attackable = attackable
    def check_frame_out(self):
        if self.x <= 100:
            return True
        if self.y <= 100:
            return True
        if self.x >= 850:
            return True
        if self.y >= 460:
            return True

        return

    def check_disappear(self):
        return self.disappear

    def update(self, frame_time):
        self.time_elapsed += frame_time
        self.state_handler[self.state](frame_time)

    def draw(self):
        #draw_rectangle(self.x - 24, self.y - 24, self.x + 24, self.y + 24)
        self.renderer.draw(self.x, self.y, self.size, self.size)

    def change_speed(self, KMPH_speed):
        PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
        RUN_SPEED_KMPH = KMPH_speed  # Km / Hour
        RUN_SPEED_MPH = (RUN_SPEED_KMPH * 1000.0 / 60.0)
        RUN_SPEED_MPS = (RUN_SPEED_MPH / 60.0)
        RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

        self.speed = RUN_SPEED_PPS

    def handle_idle(self, frame_time):
        self.x, self.y = self.game_engine.move(frame_time, self.speed, self.x, self.y, self.way)
        if self.time_elapsed >= 1.0:
            self.state = TearState.Disappear
            self.time_elapsed = 0

    def handle_disappear(self, frame_time):
        if self.renderer.check_animation_end():
            self.disappear = True
            self.state     = TearState.Wait
        else:
            self.renderer.update()

    def handle_wait(self, frame_time):
        pass

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
        self.attackable = True

        if type == TearType.Dark_Ray:
            self.renderer = Renderer.Renderer('resource/tear/dark_ray.png', 63, 166, 4, 0, 0, frame)

        if type == TearType.White_Ray:
            self.renderer = Renderer.Renderer('resource/tear/white_ray.png', 63, 166, 4, 0, 0, frame)

        if type == TearType.Red_Ray:
            self.renderer = Renderer.Renderer('resource/tear/red_ray.png', 63, 166, 4, 0, 0, frame)

    def get_instance(self):
        return TearType.Dark_Ray

    def get_attackable(self):
        return self.attackable

    def set_attackable(self, attackable):
        self.attackable = attackable

    def move(self, frame_time):
        pass

    def check_collision(self, x1, x2, y1, y2):

        print("ray collision check")
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
        self.renderer.update()
        pass

    def draw(self):
        self.renderer.draw(self.x, self.y)


