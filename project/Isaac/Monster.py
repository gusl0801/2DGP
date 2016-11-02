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

        self.change_speed(10)
        self.way = way
        self.game_engine = game_engine.GameEngine()
        self.renderer = Renderer.Renderer\
                ('resource/monster/tumor.png', 70, 67, 0, (Way.WayCount - 4 - self.way + 1))

    def update(self, frame_time, unit):
        unit.tear_manager.collision_update(self)
        self.collision_update(unit)

        if self.state in (UnitState.Move, UnitState.Idle, UnitState.Attacked):
            self.detect_enemy(unit)
            self.renderer.update(3)
            self.detect_enemy_pos(unit)
            self.x, self.y = self.game_engine.move(frame_time, self.speed, self.x, self.y, self.way)

        elif self.state in (UnitState.Attack,):
            pass

    def attack(self, unit):
        pass

    def draw(self):
        self.renderer.draw(self.x, self.y)

    def collision_update(self, unit):
        if unit.check_collision(self.x - 35, self.x + 35, self.y - 30, self.y + 67):
            unit.undo_move()

    def detect_enemy(self, enemy):
        x_axis_check = (enemy.x > self.x - 50 and enemy.x < self.x + 50)
        if x_axis_check:
            pass
            #print("x_axis_check is true")
            #self.state = UnitState.Attack




