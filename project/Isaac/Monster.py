from Unit import *
import random
import Renderer

class Spider(Unit):
    def __init__(self, x, y, hp = 0):
        Unit.__init__(self, 5)
        self.team == UnitTeam.Enemy
        self.x, self.y = x, y
        self.hp = 3 + hp

        self.game_engine = Game_Engine.GameEngine()
        self.renderer = Renderer.Renderer('resource/monster/spider.png', 53, 53, 5)

    def update(self, frame_time, unit):
        unit.tear_manager.collision_update(self)

        self.x, self.y = self.game_engine.move_randomly(self.x, self.y, frame_time)
        self.renderer.update()

        self.collision_update(unit)

    def get_collision_box(self):
        return self.x - 26, self.y, self.x + 26, self.y + 53

    def collision_update(self, unit):
        if unit.check_collision(self.x - 26, self.x + 26, self.y, self.y + 53):
            unit.undo_move()
            unit.change_state(UnitState.Attacked)
            unit.set_hp(-1)
    def draw(self):
        self.renderer.draw(self.x, self.y)

class Tentacle(Unit):
    def __init__(self, x, y, hp = 0):
        Unit.__init__(self)
        self.x, self.y = x, y
        self.renderer = Renderer.Renderer(
            'resource/monster/tentacle.png', 48, 96, 6)
        self.hp = 3 + hp

    def update(self, frame_time, unit):
        unit.tear_manager.collision_update(self)

        self.renderer.update()
        self.collision_update(unit)

    def get_collision_box(self):
        return self.x - 24, self.y - 24, self.x + 24, self.y - 48

    def collision_update(self, unit):
        if unit.check_collision(self.x - 24, self.x + 24, self.y - 24, self.y + 48):
            unit.undo_move()
            unit.change_state(UnitState.Attacked)
            unit.set_hp(-1)

    def draw(self):
        self.renderer.draw(self.x, self.y)

class Fly(Unit):
    def __init__(self,hp = 0):
        Unit.__init__(self, 5)
        self.x = random.randint(120, 830)
        self.y = random.randint(120, 430)
        self.hp = 2 + hp

        self.game_engine = Game_Engine.GameEngine()

        if random.randint(0, 1) == 0:
            self.renderer = Renderer.Renderer(
                'resource/monster/fly_base.png', 32, 32, 2)
        else:
            self.renderer = Renderer.Renderer(
                'resource/monster/fly_yellow.png', 32, 32, 2)

    def update(self, frame_time, unit):
        unit.tear_manager.collision_update(self)
        self.x, self.y = self.game_engine.move_randomly(self.x, self.y, frame_time)
        self.renderer.update()
        self.collision_update(unit)

    def get_collision_box(self):
        return self.x - 16, self.y, self.x + 16, self.y + 32

    def collision_update(self, unit):
        if unit.check_collision(self.x - 16, self.x + 16, self.y, self.y + 32):
            unit.undo_move()
            unit.change_state(UnitState.Attacked)
            unit.set_hp(-1)

    def draw(self):
        self.renderer.draw(self.x, self.y)

class Tumor(Unit):
    def __init__(self, x, y, way, hp = 0):
        Unit.__init__(self, 5)
        self.x, self.y = x, y
        self.hp = 3 + hp
        self.state = UnitState.Move
        self.change_speed(5)
        self.way = way
        self.move_way = way
        self.tear_type = 2
        self.game_engine = Game_Engine.GameEngine()
        self.renderer = Renderer.Renderer\
                ('resource/monster/tumor.png', 70, 67, 3, 0, 0, (self.way))

    def update(self, frame_time, unit):
        self.time_elapsed += frame_time

        unit.tear_manager.collision_update(self)
        self.tear_manager.collision_update(unit)

        self.collision_update(unit)
        self.tear_manager.update(frame_time)

        self.state_handler[self.state](frame_time,unit)


    def attack(self, unit):
        pass

    def draw(self):
        self.renderer.draw(self.x, self.y)
        self.tear_manager.draw()

    def collision_update(self, unit):
        if unit.check_collision(self.x - 45, self.x + 45, self.y - 0, self.y + 67):
            unit.undo_move()
            unit.change_state(UnitState.Attacked)
            unit.set_hp(-1)

    def get_collision_box(self):
        return self.x - 45, self.y - 30, self.x + 45, self.y + 67

    def detect_enemy(self, enemy):
        x_axis_check = (enemy.x > self.x - 30 and enemy.x < self.x + 30)
        if x_axis_check:
            self.change_state(UnitState.Wait)

    def change_state(self, state):
        self.state = state
        self.time_elapsed = 0.0

        self.renderer.change_frameX(0)
        if state in (UnitState.Move,):
            self.renderer.change_frameY(self.way)

        if state in (UnitState.Attack,):
            #print(self.y)
            self.renderer.change_frameY(self.way - 2)
            if (self.y == 120):
                self.y = 230
                self.tear_manager.append()
                self.y = 120
            elif (self.y == 450):
                self.y = 320
                self.tear_manager.append()
                self.y = 450
            self.tear_manager.append()

    def handle_move(self, frame_time, unit):
        self.renderer.update()
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

class NightCrawler(Unit):
    def __init__(self, x, y, hp = 0):
        Unit.__init__(self, 5)
        self.x, self.y = x, y
        self.hp = 3 + hp

        self.time_elapsed = random.randint(0, 10) / 10.0
        self.state = UnitState.Move
        self.change_speed(5)
        self.way = random.randint(0, 3)
        self.tear_size = 1.0
        self.tear_type = TearType.BloodBag
        self.game_engine = Game_Engine.GameEngine()
        self.renderer = Renderer.Renderer\
                ('resource/monster/nightcrawler.png', 48, 48, 5)

    def update(self, frame_time, unit):
        self.time_elapsed += frame_time

        self.tear_manager.check_frame_out()
        self.tear_manager.check_disappear()

        unit.tear_manager.collision_update(self)
        self.tear_manager.collision_update(unit)

        if self.state not in (UnitState.Wait,):
            self.collision_update(unit)
            #unit.tear_manager.collision_update(self)
        self.tear_manager.update(frame_time)

        self.state_handler[self.state](frame_time,unit)

    def attack(self, unit):
        pass

    def draw(self):
        if (self.state not in (UnitState.Wait,)):
            self.renderer.draw(self.x, self.y)
        self.tear_manager.draw()

    def collision_update(self, unit):
        if unit.check_collision(self.x - 35, self.x + 35, self.y - 30, self.y + 67):
            unit.undo_move()
            unit.change_state(UnitState.Attacked)
            unit.set_hp(-1)

    def get_collision_box(self):
        return self.x - 35, self.y - 30, self.x + 35, self.y - 67

    def change_state(self, state):
        self.state = state
        self.time_elapsed = 0.0

        self.renderer.change_frameX(0)

    def handle_move(self, frame_time, unit):
        if self.time_elapsed >= 2.0:
            self.change_state(UnitState.Wait)
            return
        self.renderer.update()
        self.x, self.y = self.game_engine.move_randomly(self.x, self.y, frame_time)

    def handle_attack(self, frame_time, unit):
        if self.time_elapsed > 0.5:
            self.way = Way.Up
            self.tear_manager.append()

            self.way = Way.Down
            self.tear_manager.append()

            self.way = Way.Left
            self.tear_manager.append()

            self.way = Way.Right
            self.tear_manager.append()

            self.change_state(UnitState.Move)

    def handle_wait(self, frame_time, unit):
        if self.time_elapsed > 1.0:
            self.change_state(UnitState.Attack)
            self.x = random.randint(120, 830)
            self.y = random.randint(120, 430)

    def handle_attacked(self, frame_time, unit):
        pass

class Pacer(Unit):
    def __init__(self,hp = 0):
        Unit.__init__(self, 5)
        self.state = UnitState.Move
        self.x = random.randint(120, 830)
        self.y = random.randint(120, 430)
        self.hp = 2 + hp

        self.game_engine = Game_Engine.GameEngine()

        self.tear_size = 1
        self.tear_type = TearType.BloodBag
        self.renderer = Renderer.Renderer(
            'resource/monster/pacer.png', 43, 24, 10)

    def update(self, frame_time, unit):
        self.time_elapsed += frame_time

        self.tear_manager.update(frame_time)

        self.tear_manager.check_frame_out()
        self.tear_manager.check_disappear()

        unit.tear_manager.collision_update(self)
        self.tear_manager.collision_update(unit)
        self.collision_update(unit)
        self.state_handler[self.state](frame_time, unit)

    def get_collision_box(self):
        return self.x - 21, self.y - 12, self.x + 21, self.y + 12

    def collision_update(self, unit):
        if unit.check_collision(self.x - 21, self.x + 21, self.y - 12, self.y + 20):
            print("pacer collide")
            unit.undo_move()
            unit.change_state(UnitState.Attacked)
            unit.set_hp(-1)

    def check_collision(self, x1, x2, y1, y2):
        if ((x1 < self.x  and x2 > self.x)
            and (y1 < self.y and y2 > self.y)):
            return True

        return False

    def change_state(self, state):
        self.time_elapsed = 0
        self.state = state

    def draw(self):
        #draw_rectangle(self.x - 21, self.y - 12, self.x + 21, self.y + 12)
        self.tear_manager.draw()
        self.renderer.draw(self.x, self.y)

    def handle_move(self, frame_time, unit):
        if self.time_elapsed > 1.0:
            self.change_state(UnitState.Attack)
            return
        self.renderer.update()
        self.x, self.y = self.game_engine.move_randomly(self.x, self.y, frame_time)

    def handle_attack(self, frame_time, unit):
        self.way = Way.Up
        self.tear_manager.append()

        self.way = Way.Down
        self.tear_manager.append()

        self.way = Way.Left
        self.tear_manager.append()

        self.way = Way.Right
        self.tear_manager.append()

        self.change_state(UnitState.Wait)

    def handle_wait(self, frame_time, unit):
        if self.time_elapsed > 0.2:
            self.change_state(UnitState.Move)


