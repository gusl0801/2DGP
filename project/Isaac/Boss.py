from unit import*
import Renderer
import game_engine

class Monstro(Unit):
    class Monstro_Phase:
        Shot = 0
        FlyAttack = 1
    def __init__(self,x, y):
        Unit.__init__(self)

        self.state = UnitState.Move
        self.frameX, self.frameY = 0, 3
        self.x, self.y = x, y
        self.renderer = Renderer.Renderer('resource/monster/Monstro.png', 118, 141, 0, 3)
        self.game_engine = game_engine.GameEngine()

    def update(self,frame_time,unit):
        self.delay += 1

        self.state_handler[self.state](frame_time, unit)

    def draw(self):
        self.renderer.draw(self.x, self.y)
        #self.sprite.clip_draw(self.frameX * 118, self.frameY * 141, 118, 141 , self.x, self.y)

    def detect_enemy(self, enemy):
        x_axis_check = (enemy.x >= self.x)
        y_axis_check = (enemy.y >= self.y)

        if x_axis_check and y_axis_check:
            self.move_way = Way.RightUp
        elif x_axis_check and not y_axis_check:
            self.move_way = Way.RightDown
        elif not x_axis_check and y_axis_check:
            self.move_way = Way.LeftUp
        elif not x_axis_check and not y_axis_check:
            self.move_way = Way.LeftDown

    def handle_move(self, frame_time, unit):
        self.renderer.update(2)
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