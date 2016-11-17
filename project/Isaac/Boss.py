from unit import*
import Renderer
import game_engine
import random

class Monstro(Unit):
    class Monstro_Phase:
        Shot = 0
        FlyAttack = 1
    def __init__(self,x, y):
        Unit.__init__(self)

        self.way = Way.Left
        self.speed_x, self.speed_y
        self.state = UnitState.Wait
        self.frameX, self.frameY = 0, 3
        self.x, self.y = x, y
        self.renderer = Renderer.Renderer('resource/monster/Monstro.png', 118, 141, 3, 1)
        self.game_engine = game_engine.GameEngine()
        self.dest_x, self.dest_y = None, None

    def update(self,frame_time,unit):
        self.time_elapsed += frame_time
        self.state_handler[self.state](frame_time, unit)

    def draw(self):
        self.renderer.draw(self.x, self.y)
        #self.sprite.clip_draw(self.frameX * 118, self.frameY * 141, 118, 141 , self.x, self.y)

    def detect_enemy(self, enemy):
        x_axis_check = (enemy.x >= self.x)
        y_axis_check = (enemy.y >= self.y)

        if x_axis_check and y_axis_check:
            self.way = Way.RightUp
        elif x_axis_check and not y_axis_check:
            self.way = Way.RightDown
        elif not x_axis_check and y_axis_check:
            self.way = Way.LeftUp
        elif not x_axis_check and not y_axis_check:
            self.way = Way.LeftDown

    def handle_move(self, frame_time, unit):
        if self.renderer.frameX < 3:
            self.renderer.update(4)
        self.game_engine.jump(frame_time, self)
        if self.time_elapsed > 0.6:
            if random.randint(0, 1) == 0:
                self.change_state(UnitState.Move)
                self.set_destination(unit)
                #self.change_state(UnitState.Wait)
            else:
                self.change_state(UnitState.Move)
                self.set_destination(unit)
                #self.change_state(UnitState.Attack)


    def handle_attack(self, frame_time, unit):
        if self.time_elapsed > 0.2:
            self.change_state(UnitState.Move)
            self.set_destination(unit)
            self.tear_manager.clear()

    def handle_wait(self, frame_time, unit):
        if self.time_elapsed > 0.1:
            if(random.randint(0, 1) == 0):
                self.change_state(UnitState.Move)
                self.set_destination(unit)
                #self.change_state(UnitState.Attack)
            else:
                self.change_state(UnitState.Move)
                self.set_destination(unit)
    def change_state(self, state):
        self.state = state
        self.time_elapsed = 0
        #self.renderer.frameX = 0

    def set_destination(self, unit):
        self.dest_x, self.dest_y = unit.x, unit.y
        #self.speed_x = (self.x - self.dest_x)
        #self.speed_y = (self.y - self.dest_y)
        print("dest_x, x, speed : ", self.dest_x, self.x, self.speed_x)
        print("dest_y, y, speed : ", self.dest_y, self.y, self.speed_y)

    def handle_attacked(self, frame_time, unit):
        pass

    def init_speed(self):
        PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
        RUN_SPEED_KMPH = 10  # Km / Hour
        RUN_SPEED_MPH = (RUN_SPEED_KMPH * 1000.0 / 60.0)
        RUN_SPEED_MPS = (RUN_SPEED_MPH / 60.0)
        RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

        self.speed_x = RUN_SPEED_PPS

        RUN_SPEED_KMPH = 20  # Km / Hour
        RUN_SPEED_MPH = (RUN_SPEED_KMPH * 1000.0 / 60.0)
        RUN_SPEED_MPS = (RUN_SPEED_MPH / 60.0)
        RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

        self.speed_y = RUN_SPEED_PPS