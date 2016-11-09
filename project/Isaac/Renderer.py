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

    def __del__(self):
        pass

    def draw(self, x, y):
        draw_rectangle(x + self.width / 2,
                           y + self.height / 2,
                           x - self.width / 2,
                           y - self.height / 2)

        Renderer.sprites[self.key].clip_draw\
            (self.frameX * self.width,
             self.frameY * self.height,
             self.width, self.height, x, y)

    def draw_boundary(self, x1, x2, y1, y2):
        draw_rectangle(x1, y1, x2, y2)

    def update(self, max_x = -1, max_y = None, delay = True):
        if delay:
            self.delay += 1
            if self.delay > 3:
                if max_x != None:
                    self.frameX = (self.frameX + 1) % max_x
                if max_y != None:
                    self.frameY = (self.frameY + 1) % max_y
                self.delay = 0
        else:
            if max_x != None:
                self.frameX = (self.frameX + 1) % max_x
            if max_y != None:
                self.frameY = (self.frameY + 1) % max_y

    def change_frameX(self, x):
        self.frameX = x

    def change_frameY(self, y):
        self.frameY = y

    def change_image(self, image_path, width, height, frameX = 0, frameY = 0):
        del self.sprites[self.key]
        if self.find_path(image_path) == False:
            Renderer.sprites[image_path] = load_image(image_path)
        self.key = image_path
        self.width, self.height = width, height
        self.frameX, self.frameY = frameX, frameY

    def find_path(self, image_path):
        if (image_path in Renderer.sprites) == False:
            return False
        return True