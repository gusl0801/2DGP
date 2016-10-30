import Renderer

class ItemState:
    Noting = 0,
    #획득
    #소멸

class Item:
    def __init__(self,x,y):
        self.x, self.y = x,y
        self.renderer = Renderer.Renderer()
        pass

    def draw(self):
        self.renderer.update()
        pass

    def update(self):
        pass