from unit import*

class Monstro(Unit):
    class Monstro_Phase:
        Shot = 0
        FlyAttack = 1
    def __init__(self,x, y):
        Unit.__init__(self)

        self.frameX, self.frameY = 0, 3
        self.x, self.y = x, y
        self.sprite = load_image('resource/monster/Monstro.png')

    def update(self,frame_time,unit):
        self.delay += 1

        if self.state == UnitState.Stop:
            if self.delay > 5:
                self.delay = 0
                self.frameX = (self.frameX + 1) % 3


    def draw(self):
        self.sprite.clip_draw(self.frameX * 118, self.frameY * 141, 118, 141 , self.x, self.y)