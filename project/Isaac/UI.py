from pico2d import*
import Renderer
"""
In boss stage, Show Boss's hp
Show isaac's hp anytime

If can do, add item gage
"""

class UI_Manager:
    def __init__(self):
        self.hp_image = load_image('resource/UI/hp.png')
        self.hp = None

    def draw(self, frame_time, unit):
        self.draw_heart(unit)
        pass

    def update(self, frame_time):
        pass

    def draw_heart(self, unit):
        # 가로 15, 세로 14
        self.hp = unit.hp

        hp = unit.hp
        x = 60
        y = 480
        while hp > 0:
            if hp - 2 >= 0:
                self.hp_image.clip_draw(0, 0, 15, 14, x, y, 30, 28)
                hp -= 2
            else:
                self.hp_image.clip_draw(15, 0, 15, 14, x, y, 30, 28)
                hp -= 1
            x += 30