from unit import*
import game_engine
import Renderer
import UI

lask_key = None
class Isaac(Unit):      #sub class
    def __init__(self):
        Unit.__init__(self)
        self.tear_size = 5

        self.team = UnitTeam.Ally

        self.way = Way.Down
        self.image_y = 0
        self.next_way = self.way

        self.game_engine = game_engine.GameEngine()

        self.UI = UI.UI_Manager();

        self.head_renderer = Renderer.Renderer('resource/character/normal_head.png', 54, 40, 0, 1)
        self.body_renderer = Renderer.Renderer('resource/character/normal_body.png', 43, 24, 0, 2)

        #self.head_renderer = Renderer.Renderer('resource/character/common_cold_head.png', 53, 42, 0, 1)
        #self.body_renderer = Renderer.Renderer('resource/character/common_cold_body.png', 43, 26, 0, 2)

    def draw(self, frame_time):

        self.body_renderer.draw(self.x, self.y - 20 - self.image_y)

        self.head_renderer.draw(self.x, self.y)

        self.tear_manager.draw()
        self.UI.draw(frame_time, self)


    def update(self,frame_time):
        self.time_elapsed += frame_time

        self.tear_manager.update(frame_time)
        self.tear_manager.check_frame_out()

        self.state_handler[self.state](frame_time)

    def handle_event(self, event):
        global last_key

        if event.type == SDL_KEYDOWN:
            if event.key != None:
                last_key = event.key

            if event.key in (SDLK_d,):
                self.change_way(Way.Right)
                self.next_way = Way.Right
                self.change_state(UnitState.Move)

            elif event.key in (SDLK_a,):
                self.change_way(Way.Left)
                self.next_way = Way.Left
                self.change_state(UnitState.Move)

            elif event.key in (SDLK_w,):
                self.change_way(Way.Up)
                self.next_way = Way.Up
                self.change_state(UnitState.Move)

            elif event.key in (SDLK_s,):
                self.change_way(Way.Down)
                self.next_way = Way.Down
                self.change_state(UnitState.Move)

            elif event.key == SDLK_UP:
                self.change_way(Way.Up)
                self.change_state(UnitState.Attack)
                self.shot_tear()

            elif event.key == SDLK_DOWN:
                self.change_way(Way.Down)
                self.change_state(UnitState.Attack)
                self.shot_tear()

            elif event.key == SDLK_LEFT:
                self.change_way(Way.Left)
                self.change_state(UnitState.Attack)
                self.shot_tear()

            elif event.key == SDLK_RIGHT:
                self.change_way(Way.Right)
                self.change_state(UnitState.Attack)
                self.shot_tear()

        elif event.type == SDL_KEYUP:
            if (event.key, self.way) == (SDLK_w, Way.Up):
                self.change_state(UnitState.Stop)
            elif (event.key, self.way) == (SDLK_a, Way.Left):
                self.change_state(UnitState.Stop)
            elif (event.key, self.way) == (SDLK_s, Way.Down):
                self.change_state(UnitState.Stop)
            elif (event.key, self.way) == (SDLK_d, Way.Right):
                self.change_state(UnitState.Stop)

        if (event.type, self.way):
            pass

    def get_collision_box(self):
        return self.x - 27, self.y - 28, self.x + 27, self.y + 24

    def change_type(self, item_type):
        if item_type == ItemType.CommonCold:
            self.head_renderer.change_image('resource/character/common_cold_head.png', 53, 42, 0, 1)
            self.body_renderer.change_image('resource/character/common_cold_body.png', 43, 26, 0, 2)
            self.image_y = 0

        elif item_type == ItemType.Martyr:
            self.head_renderer.change_image('resource/character/martyr_head.png', 54, 50, 0, 1)
            self.body_renderer.change_image('resource/character/normal_body.png', 43, 24, 0, 2)
            self.image_y = 5
            self.tear_size += 2

    def change_way(self, way):
        self.way = way
        self.delay = 0

        self.head_renderer.change_frameX(0)
        self.head_renderer.change_frameY(3 - self.way) #3 means WayCount not including diagonal way

        self.body_renderer.change_frameX(0)
        self.body_renderer.change_frameY(self.way)

    def change_state(self, state):
        self.state = state
        self.change_way(self.way)
        self.delay = 0

    def shot_tear(self):
        self.tear_manager.append()

    def change_room(self, way):
        if way == Way.Left:
            self.x = 810
        elif way == Way.Right:
            self.x = 150
        elif way == Way.Up:
            self.y = 130
        elif way == Way.Down:
            self.y = 450

        self.tear_manager.clear()

    def undo_move(self):
        if self.way in (Way.Down, Way.Up):
            self.x, self.y = self.game_engine.undo_move(self.x, self.y, game_engine.MovePattern.MoveY)
        elif self.way in (Way.Right, Way.Left):
            self.x, self.y = self.game_engine.undo_move(self.x, self.y, game_engine.MovePattern.MoveX)

    def handle_attack(self, frame_time, unit = None):
        self.delay += 1

        self.head_renderer.update(2)
        if self.delay >= 5:
            self.delay = 0

            if (self.head_renderer.frameX % 2) == 0:
                self.change_way(self.way)
                self.change_state(UnitState.Stop)

    def handle_attacked(self, frame_time, unit = None):
        pass

    def handle_move(self, frame_time, unit = None):
        self.body_renderer.update(10, None,False)
        self.x, self.y = self.game_engine.move(frame_time, self.speed, self.x, self.y, self.way)


