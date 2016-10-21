from base import*
from pico2d import*

class Renderer:
    sprites = {}
    def __init__(self, image_path, width, height, frameX = 0, frameY = 0):
        if self.find_path(image_path) == False:
            Renderer.sprites[image_path] = load_image(image_path)

        self.key = image_path
        self.width = width
        self.height = height

        self.frameX = frameX
        self.frameY = frameY

        self.delay = 0
    def draw(self, x, y):
        Renderer.sprites[self.key].clip_draw\
            (self.frameX * self.width, self.frameY * self.height, self.width, self.height, x, y)

    def update(self, max_x = -1, max_y = None):
        self.delay += 1
        if self.delay > 3:
            if max_x != None:
                self.frameX = (self.frameX + 1) % max_x
            if max_y != None:
                self.frameY = (self.frameY + 1) % max_y
            self.delay = 0

    def change_frameX(self, x):
        self.frameX = x

    def change_frameY(self, y):
        self.frameY = y

    def find_path(self, image_path):
        if (image_path in Renderer.sprites) == False:
            return False
        return True