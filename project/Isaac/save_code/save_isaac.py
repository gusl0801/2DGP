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