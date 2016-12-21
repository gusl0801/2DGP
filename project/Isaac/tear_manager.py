#from Unit import*
from Tear import*
#import Isaac

class TearManager:
    def __init__(self, unit):
        self.tear_list = []
        self.unit = unit

    def append(self):
        if self.unit.tear_type in (TearType.Normal, TearType.Commond_Cold, TearType.BloodBag):
            tear = Tear(self.unit, self.unit.tear_size)
        elif self.unit.tear_type in (TearType.Red_Ray, TearType.Dark_Ray, TearType.White_Ray):
            tear = Ray(self.unit, self.unit.tear_type)
        self.tear_list.append(tear)

    def clear(self):
        self.tear_list.clear()

    def check_frame_out(self):
        for i in self.tear_list:
            if i.check_frame_out():
                i.state = TearState.Disappear

    def check_disappear(self):
        for i in self.tear_list:
            if i.check_disappear():
                self.tear_list.remove(i)

    def collision_update(self, unit):
        for i in self.tear_list:
            if unit.check_die():
                return
            if i.get_attackable():
                if isinstance(i, Tear):
                    if i.state == TearState.Disappear:
                        continue
                    if unit.check_collision(i.x - 24, i.x + 24, i.y - 24, i.y + 24):
                        i.state = TearState.Disappear
                        unit.set_hp(-1)
                        i.set_attackable(False)
                        print("tear collision")
                        if unit.get_instance("Isaac"):
                            unit.set_attacked()

                elif isinstance(i, Ray):#63, 166
                    if unit.check_collision(i.x - 31, i.x + 31, i.y - 800, i.y + 800):
                        i.state = TearState.Disappear
                        unit.set_hp(-1)
                        i.set_attackable(False)
                        print("ray")
                        if unit.get_instance("Isaac"):
                            unit.set_attacked()

    def collision_update_boss(self, boss):
        for tear in self.tear_list:
            if not tear.get_attackable():
                continue

            if boss.check_collision(tear.x - 24, tear.x + 24, tear.y - 24, tear.y + 24):
                tear.state = TearState.Disappear
                boss.set_hp(-1)
                tear.set_attackable(False)
                return True
        return False

    def collision_update_ob(self, x1, x2, y1, y2):
        for tear in self.tear_list:
            if ((x1 < tear.x and x2 > tear.x)
                and (y1 < tear.y and y2 > tear.y)):
                tear.state = TearState.Disappear

    def update(self, frame_time):
        for i in self.tear_list:
           i.update(frame_time)

    def draw(self):
        for i in self.tear_list:
            i.draw()

