from unit import*


class Isaac(Unit):      #sub class
    def __init__(self):
        Unit.__init__(self)
        self.tear_type = TearType.Normal

        self.team = UnitTeam.Ally
        self.frameHead, self.frameBody = 0, 0
        self.way = Way.Down
        self.tear_size = 5
        self.sprite = load_image('resource/character/isaac_normal/isaac_base.png')

    def draw(self):
        #draw_rectangle(self.x - 28, self.y - 37, self.x + 28, self.y + 37)
        if self.way == Way.Up:
            self.sprite.clip_draw(self.frameBody * 45, 150, 45, 75, self.x, self.y)
            self.sprite.clip_draw(self.frameHead * 56, 225, 56, 75, self.x, self.y + 13)

        elif self.way == Way.Down:
            self.sprite.clip_draw(self.frameBody * 45, 150, 45, 75, self.x, self.y)
            self.sprite.clip_draw(self.frameHead * 56, 225, 56, 75, self.x + 1, self.y + 13)

        else:
            self.sprite.clip_draw(self.frameBody * 45, self.way * 75, 45, 75, self.x, self.y)
            self.sprite.clip_draw(self.frameHead * 56, 225, 56, 75, self.x, self.y + 13)
        self.tear_manager.draw()

    def update(self):
        self.tear_manager.update()
        self.tear_manager.check_frame_out()

        if self.state == UnitState.Stop:
            return

        if self.state == UnitState.Attack:
            self.delay += 1

            if self.delay >= 5:
                self.frameHead += 1
                self.delay = 0

                if (self.frameHead % 2) == 0:
                    self.change_way(self.way)
                    self.change_state(UnitState.Stop)

        if self.state == UnitState.Move:
            self.frameBody = (self.frameBody + 1) % 10

            if self.way == Way.Down:
                self.move(0, -self.speed)
            elif self.way == Way.Right:
                self.move(self.speed, 0)
            elif self.way == Way.Up:
                self.move(0, self.speed)
            elif self.way == Way.Left:
                self.move(-self.speed, 0)

    def change_way(self, way):
        self.way = way
        self.delay = 0

        if self.way == Way.Down:
            self.frameHead = 0
        elif self.way == Way.Right:
            self.frameHead = 2
        elif self.way == Way.Up:
            self.frameHead = 4
        elif self.way == Way.Left:
            self.frameHead = 6

    def process_message(self, event):
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                self.changeWay(Way.Right)

            elif event.key == SDLK_LEFT:
                self.changeWay(Way.Left)

            elif event.key == SDLK_UP:
                self.changeWay(Way.Up)

            elif event.key == SDLK_DOWN:
                self.changeWay(Way.Down)

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
        if self.way == Way.Down:
            self.move(0, self.speed)
        elif self.way == Way.Right:
            self.move(-self.speed, 0)
        elif self.way == Way.Up:
            self.move(0, -self.speed)
        elif self.way == Way.Left:
            self.move(self.speed, 0)
