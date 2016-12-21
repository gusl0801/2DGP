from Unit import*
import Renderer
import Game_Engine
import random

class Monstro(Unit):
    class Monstro_Phase:
        Shot = 0
        FlyAttack = 1
    def __init__(self,x, y):
        Unit.__init__(self, 5)

        self.way = Way.Left
        self.state = UnitState.Wait
        self.x, self.y = x, y

        self.speed_x, self.speed_y = None, None
        self.init_speed()

        self.renderer = Renderer.Renderer('resource/monster/Monstro.png', 118, 141, 3, 1)
        self.game_engine = Game_Engine.GameEngine()
        self.dest_x, self.dest_y = None, None

    def update(self,frame_time,unit):
        self.time_elapsed += frame_time
        self.state_handler[self.state](frame_time, unit)

    def draw(self):
        self.renderer.draw(self.x, self.y)

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
            self.renderer.update()
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


class Mom(Unit):
    Wait        = 0
    Shadow      = 1
    Attack_Hand = 2
    Attack_Foot = 3
    Attack_Tear = 4
    def __init__(self,x, y):
        Unit.__init__(self, 5)

        self.way = Way.Left
        self.state = Mom.Wait
        self.x, self.y = x, y

        self.speed_x, self.speed_y = None, None
        self.frame_x, self.frame_y = 0, 0
        self.delay = 0
        self.init_speed()
        self.ways = []
        self.tear_size = 1
        self.tear_type = TearType.BloodBag
        self.hp = 100
        self.attack_pos_x, self.attack_pos_y = 0, 0

        self.shadow = load_image('resource/UI/shadow.png')
        self.sprite = load_image('resource/monster/mom.png')
        self.game_engine = Game_Engine.GameEngine()
        self.state_handler = {
            Mom.Attack_Hand : self.handle_hand_attack,
            Mom.Attack_Foot : self.handle_foot_attack,
            Mom.Attack_Tear : self.handle_tear_attack,
            Mom.Wait        : self.handle_wait,
            Mom.Shadow      : self.handle_shadow
        }
        self.collision_handler = {
            Mom.Attack_Hand: self.handle_hand_collision,
            Mom.Attack_Foot: self.handle_foot_collision,
            Mom.Attack_Tear: self.handle_tear_collision,
            Mom.Wait: self.handle_wait_collision,
            Mom.Shadow: self.handle_shadow_collision
        }

    def update(self, frame_time, unit):
        print(self.hp)
        self.time_elapsed += frame_time

        self.tear_manager.update(frame_time)

        self.tear_manager.check_frame_out()
        self.tear_manager.check_disappear()

        unit.tear_manager.collision_update_boss(self)
        self.tear_manager.collision_update(unit)

        self.collision_handler[self.state](unit)
        self.state_handler[self.state](unit)

    def draw(self):
        #clip_draw(self, left, bottom, width, height, x, y, w=None, h=None):
        self.tear_manager.draw()
        if self.state == Mom.Wait:
            self.sprite.clip_draw(0, 0, 128, 87, 85, 280, 180, 130)
            self.sprite.clip_draw(0, 0, 128, 87, 880, 270, 180, 130)
            self.sprite.clip_draw(0, 0, 128, 87, 490, 480, 180, 130)
            self.sprite.clip_draw(0, 0, 128, 87, 490, 65, 180, 130)
        elif self.state == Mom.Attack_Tear:
            self.sprite.clip_draw(128, 87, 128, 87, 85, 280, 180, 130)
            self.sprite.clip_draw(256, 87, 128, 87, 880, 270, 180, 130)
            self.sprite.clip_draw(0, 87, 128, 87, 490, 480, 180, 130)
            self.sprite.clip_draw(384, 87, 128, 87, 490, 65, 180, 130)
        elif self.state == Mom.Attack_Foot:
            self.sprite.clip_draw(0, 525, 128, 175, self.attack_pos_x, self.attack_pos_y, 230, 350)
        elif self.state == Mom.Attack_Hand:
            self.sprite.clip_draw(self.frame_x * 102, 350 - self.frame_y * 175, 102, 175, self.attack_pos_x, self.attack_pos_y, 204, 350)
        elif self.state == Mom.Shadow:
            self.shadow.draw(self.attack_pos_x, self.attack_pos_y - 100, 250, 100)

    def handle_attack(self, frame_time, unit):
        if self.time_elapsed > 0.2:
            self.change_state(UnitState.Move)
            self.tear_manager.clear()

    def handle_wait(self, frame_time, unit):
        if self.time_elapsed > 0.1:
            if(random.randint(0, 1) == 0):
                self.change_state(UnitState.Move)
            else:
                self.change_state(UnitState.Move)

    def detect_enemy(self, enemy):
        self.attack_pos_x = enemy.x
        self.attack_pos_y = enemy.y + 100

    def change_state(self, state):
        self.state = state
        self.time_elapsed = 0
        #self.renderer.frameX = 0

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

    def handle_hand_attack(self, unit):
        self.delay += 1

        if self.delay > 4:
            self.frame_x += 1
            if self.frame_x > 4:
                self.frame_y += 1
                self.frame_x = 0
                if self.frame_y > 1:
                    self.frame_y = 0
                    self.time_elapsed = 0
                    self.frame_x = self.frame_y = 0
                    self.state = Mom.Wait
            self.delay = 0

    def handle_foot_attack(self, unit):
        if self.time_elapsed > 2:
            self.time_elapsed = 0
            self.frame_x = self.frame_y = 0
            self.state = Mom.Wait

    def handle_wait(self, unit):
        if self.time_elapsed > 2:
            self.time_elapsed = 0
            self.frame_x = self.frame_y = 0
            if random.randint(0,1) == 0:
                self.state = Mom.Shadow
                self.detect_enemy(unit)
            else:
                self.state = Mom.Attack_Tear
                self.shot_tear()

    def handle_tear_attack(self, unit):
        if self.time_elapsed > 2:
            self.time_elapsed = 0
            self.frame_x = self.frame_y = 0
            self.state = Mom.Wait
            self.tear_manager.clear()

    def handle_shadow(self, unit):
        if self.time_elapsed > 1.0:
            self.time_elapsed = 0
            self.frame_x = self.frame_y = 0
            self.state = random.randint(2,3)

    def handle_tear_collision(self, unit):
        if unit.check_collision(95 - 32, 95 + 32, 280 - 42, 280 + 42):
            unit.undo_move()
            unit.change_state(UnitState.Attacked)
            unit.set_hp(-1)

        elif unit.check_collision(860 - 32, 860 + 32, 270 - 42, 270 + 42):
            unit.undo_move()
            unit.change_state(UnitState.Attacked)
            unit.set_hp(-1)

        elif unit.check_collision(490 - 32, 490 + 32, 80 - 42, 80 + 42):
            unit.undo_move()
            unit.change_state(UnitState.Attacked)
            unit.set_hp(-1)

        elif unit.check_collision(490 - 32, 490 + 32, 480 - 42, 480 + 42):
            unit.undo_move()
            unit.change_state(UnitState.Attacked)
            unit.set_hp(-1)

    def handle_hand_collision(self, unit):
        if unit.check_collision(480 - 80,  480 + 80, 250 - 50, 250 + 50):
            unit.undo_move()
            unit.change_state(UnitState.Attacked)
            unit.set_hp(-1)

    def handle_foot_collision(self, unit):
        if unit.check_collision(480 - 120, 480 + 60, 250 - 70, 250 + 70):
            unit.undo_move()
            unit.change_state(UnitState.Attacked)
            unit.set_hp(-1)

    def handle_wait_collision(self, unit):
        if unit.check_collision(95 - 32, 95 + 32, 280 - 42, 280 + 42):
            unit.undo_move()
            unit.change_state(UnitState.Attacked)
            unit.set_hp(-1)

        elif unit.check_collision(860 - 32, 860 + 32, 270 - 42, 270 + 42):
            unit.undo_move()
            unit.change_state(UnitState.Attacked)
            unit.set_hp(-1)

        elif unit.check_collision(490 - 32, 490 + 32, 80 - 42, 80 + 42):
            unit.undo_move()
            unit.change_state(UnitState.Attacked)
            unit.set_hp(-1)

        elif unit.check_collision(490 - 32, 490 + 32, 480 - 42, 480 + 42):
            unit.undo_move()
            unit.change_state(UnitState.Attacked)
            unit.set_hp(-1)

    def handle_shadow_collision(self, unit):
        pass

    def check_collision(self, x1, x2, y1, y2):
        if self.state in (Mom.Wait, Mom.Attack_Tear):
            if self.collision_check(x1, y1, x2, y2, 75 - 32, 280 - 42, 75 + 32, 280 + 42):
                return True
            if self.collision_check(x1, y1, x2, y2, 880 - 32, 270 - 42, 880 + 32, 270 + 42):
                return True
            if self.collision_check(x1, y1, x2, y2, 490 - 32, 50 - 42, 490 + 32, 50 + 42):
                return True
            if self.collision_check(x1, y1, x2, y2, 490 - 32, 500 - 42, 490 + 32, 500 + 42):
                return True

        elif self.state in (Mom.Attack_Hand,):
            if self.collision_check(x1, y1, x2, y2,
                self.attack_pos_x - 120, self.attack_pos_y - 170,
                self.attack_pos_x + 60, self.attack_pos_y - 30):
                return True
        elif self.state in (Mom.Attack_Foot,):
            if self.collision_check(x1, y1, x2, y2,
                self.attack_pos_x - 80, self.attack_pos_y - 150,
                self.attack_pos_x + 80, self.attack_pos_y - 50):
                return True
        return False

    #draw_rectangle(480 - 120, 250 - 70, 480 + 60, 250 + 70)
    #draw_rectangle(480 - 80, 250 - 50, 480 + 80, 250 + 50)

    def collision_check(self, left_a, bottom_a, right_a, top_a, left_b,bottom_b, right_b,top_b):
        left_a, bottom_a, right_a, top_a
        left_b, bottom_b, right_b, top_b

        if left_a > right_b: return False
        if right_a < left_b: return False
        if top_a < bottom_b: return False
        if bottom_a > top_b: return False
        return True

    def shot_tear(self):
        self.way = Way.Up
        self.x, self.y = 490, 90
        self.tear_manager.append()

        self.way = Way.Down
        self.x, self.y = 490, 440
        self.tear_manager.append()

        self.way = Way.Left
        self.x, self.y = 840, 270
        self.tear_manager.append()

        self.way = Way.Right
        self.x, self.y = 125, 270
        self.tear_manager.append()