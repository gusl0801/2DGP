from unit import *
import random
import Renderer

class Spider(Unit):
    def __init__(self, x, y):
        Unit.__init__(self)
        self.team == UnitTeam.Enemy
        self.x, self.y = x, y

        self.game_engine = game_engine.GameEngine()
        self.renderer = Renderer.Renderer('resource/monster/spider.png', 53, 53)

    def update(self, frame_time, unit):
        unit.tear_manager.collision_update(self)

        self.x, self.y = self.game_engine.move_randomly(self.x, self.y)
        self.renderer.update(5)

        self.collision_update(unit)

    def collision_update(self, unit):
        if unit.check_collision(self.x - 26, self.x + 26, self.y, self.y + 53):
            unit.undo_move()

    def draw(self):
        self.renderer.draw(self.x, self.y)

class Tentacle(Unit):
    def __init__(self, x, y):
        Unit.__init__(self)
        self.x, self.y = x, y
        self.renderer = Renderer.Renderer(
            'resource/monster/tentacle.png', 48, 96)

    def update(self, frame_time, unit):
        unit.tear_manager.collision_update(self)

        self.renderer.update(6)
        self.collision_update(unit)

    def collision_update(self, unit):
        if unit.check_collision(self.x - 24, self.x + 24, self.y - 24, self.y + 48):
            unit.undo_move()

    def draw(self):
        self.renderer.draw(self.x, self.y)

class Fly(Unit):
    def __init__(self):
        Unit.__init__(self)
        self.x = random.randint(120, 830)
        self.y = random.randint(120, 430)

        self.game_engine = game_engine.GameEngine()

        if random.randint(0, 1) == 0:
            self.renderer = Renderer.Renderer(
                'resource/monster/fly_base.png', 32, 32)
        else:
            self.renderer = Renderer.Renderer(
                'resource/monster/fly_yellow.png', 32, 32)

    def update(self, frame_time, unit):
        unit.tear_manager.collision_update(self)
        self.x, self.y = self.game_engine.move_randomly(self.x, self.y)
        self.renderer.update(2)
        self.collision_update(unit)


    def collision_update(self, unit):
        if unit.check_collision(self.x - 16, self.x + 16, self.y, self.y + 32):
            unit.undo_move()

    def draw(self):
        self.renderer.draw(self.x, self.y)

class Tumor(Unit):
    def __init__(self, x, y, way):
        Unit.__init__(self)
        self.x, self.y = x, y

        self.state = UnitState.Move
        self.change_speed(5)
        self.way = way
        self.move_way = way
        self.tear_type = random.randint(0,2) + 2

        self.game_engine = game_engine.GameEngine()
        self.renderer = Renderer.Renderer\
                ('resource/monster/tumor.png', 70, 67, 0, (self.way))
                #('resource/monster/tumor.png', 70, 67, 0, (Way.WayCount - 4 - self.way + 1),)

    def update(self, frame_time, unit):
        self.time_elapsed += frame_time

        unit.tear_manager.collision_update(self)
        self.collision_update(unit)
        self.tear_manager.update(frame_time)

        self.state_handler[self.state](self,frame_time,unit)

    def attack(self, unit):
        pass

    def draw(self):
        self.renderer.draw(self.x, self.y)
        self.tear_manager.draw()
        #print("%d, %d %d" % (id(self),self.state, self.way))

    def collision_update(self, unit):
        if unit.check_collision(self.x - 35, self.x + 35, self.y - 30, self.y + 67):
            unit.undo_move()

    def detect_enemy(self, enemy):
        x_axis_check = (enemy.x > self.x - 50 and enemy.x < self.x + 50)
        if x_axis_check:
            self.change_state(UnitState.Wait)

    def change_state(self, state):
        self.state = state
        self.time_elapsed = 0.0

        self.renderer.change_frameX(0)
        if state in (UnitState.Move,):
            self.renderer.change_frameY(self.way)

        if state in (UnitState.Attack,):
            self.renderer.change_frameY(self.way - 2)
            self.tear_manager.append()

    def handle_move(self, frame_time, unit):
        self.renderer.update(3)
        self.detect_enemy_x_pos(unit)
        self.detect_enemy(unit)
        self.x, self.y = self.game_engine.move(frame_time, self.speed, self.x, self.y, self.move_way)

    def handle_attack(self, frame_time, unit):
        if self.time_elapsed > 1.0:
            self.change_state(UnitState.Move)
            self.tear_manager.clear()

    def handle_wait(self, frame_time, unit):
        if self.time_elapsed > 1.0:
            self.change_state(UnitState.Attack)
            self.time_elapsed = 0.0

    def handle_attacked(self, frame_time, unit):
        pass

    state_handler = \
        {
            UnitState.Move: handle_move,
            UnitState.Attack: handle_attack,
            UnitState.Wait: handle_wait,
            UnitState.Attacked: handle_attacked
        }



