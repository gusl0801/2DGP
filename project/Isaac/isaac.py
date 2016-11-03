from unit import*
import game_engine
import Renderer

lask_key = None
class Isaac(Unit):      #sub class
    def __init__(self):
        Unit.__init__(self)
        self.tear_size = 5

        self.team = UnitTeam.Ally

        self.way = Way.Down
        self.next_way = self.way

        self.frameHead, self.frameBody = 0, 0
        self.sprite = load_image('resource/character/isaac_normal/isaac_base.png')
        self.game_engine = game_engine.GameEngine()

        self.renderer = Renderer.Renderer('resource/character/isaac_normal/isaac_base.png', 56, 75)

    def draw(self, frame_time):
        #draw_rectangle(self.x - 28, self.y - 37, self.x + 28, self.y + 37)
        if self.way in (Way.Up, Way.LeftUp, Way.RightUp):
            self.sprite.clip_draw(self.frameBody * 45, 150, 45, 75, self.x, self.y)
            self.sprite.clip_draw(self.frameHead * 56, 225, 56, 75, self.x, self.y + 13)

        elif self.way in (Way.Down, Way.LeftDown, Way.RightDown):
            self.sprite.clip_draw(self.frameBody * 45, 150, 45, 75, self.x, self.y)
            self.sprite.clip_draw(self.frameHead * 56, 225, 56, 75, self.x + 1, self.y + 13)

        else:
            self.sprite.clip_draw(self.frameBody * 45, self.way * 75, 45, 75, self.x, self.y)
            self.sprite.clip_draw(self.frameHead * 56, 225, 56, 75, self.x, self.y + 13)
        self.tear_manager.draw()

        #self.renderer.draw(self.x, self.y)

    def update(self,frame_time):
        #self.renderer.update()
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

    def change_way(self, way):
        self.way = way
        self.delay = 0

        if self.way in (Way.Down, Way.RightDown, Way.LeftDown):
            self.frameHead = 0
        elif self.way == Way.Right:
            self.frameHead = 2
        elif self.way == Way.Up:
            self.frameHead = 4
        elif self.way == Way.Left:
            self.frameHead = 6

    def change_state(self, state):
        self.state = state
        self.change_way(self.way)
        self.delay = 0
        self.frameBody = 0

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
        """
        if self.way == Way.Down:
            self.move(0, self.speed)
        elif self.way == Way.Right:
            self.move(-self.speed, 0)
        elif self.way == Way.Up:
            self.move(0, -self.speed)
        elif self.way == Way.Left:
            self.move(self.speed, 0)
        """
        if self.way in (Way.Down, Way.Up):
            self.x, self.y = self.game_engine.undo_move(self.x, self.y, game_engine.MovePattern.MoveY)
        elif self.way in (Way.Right, Way.Left):
            self.x, self.y = self.game_engine.undo_move(self.x, self.y, game_engine.MovePattern.MoveX)

    def handle_attack(self, frame_time, unit = None):
        self.delay += 1

        if self.delay >= 5:
            self.frameHead += 1
            self.delay = 0

            if (self.frameHead % 2) == 0:
                self.change_way(self.way)
                self.change_state(UnitState.Stop)

    def handle_attacked(self, frame_time, unit = None):
        pass

    def handle_move(self, frame_time, unit = None):
        """
        if self.way in (Way.LeftUp, Way.LeftDown, Way.RightDown, Way.RightDown):
            self.way = self.next_way
            self.time_elapsed = 0.0
        """
        self.frameBody = (self.frameBody + 1) % 10
        self.x, self.y = self.game_engine.move(frame_time, self.speed, self.x, self.y, self.way)


