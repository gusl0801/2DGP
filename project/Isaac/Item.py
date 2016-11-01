import Renderer

class ItemState:
    Noting = 0,
    #획득
    #소멸

class Item:
    def __init__(self,x,y, path):
        self.x, self.y = x,y
        self.renderer = Renderer.Renderer(path)
        pass

    def draw(self):
        self.renderer.update()
        pass

    def update(self, frame):
        self.renderer.update(frame)
        pass

class Heart(Item):
    def __init__(self,x,y):
        Item.__init__(self,x,y, "")

    def draw(self):
        Item.draw(self)

    def update(self):
        Item.update(self, 0)


class Key(Item):
    def __init__(self, x, y):
        Item.__init__(self,x,y, "")

    def draw(self):
        Item.draw(self)

    def update(self):
        Item.update(self, 0)


