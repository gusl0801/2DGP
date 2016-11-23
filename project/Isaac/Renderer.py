from Base import*
from pico2d import*

class Renderer:
    sprites = {}
    def __init__(self, image_path, width, height, max_frame_x, max_frame_y = 0,frameX = 0, frameY = 0, delay_on = True):
        if self.find_path(image_path) == False:
            Renderer.sprites[image_path] = load_image(image_path)

        self.key = image_path
        self.width = width
        self.height = height

        self.frameX, self.frameY = frameX, frameY

        self.max_frame_x, self.max_frame_y = max_frame_x, max_frame_y

        self.delay_on = delay_on
        self.delay = 0

    def __del__(self):
        pass

    def draw(self, x, y, w = None, h = None):
        """
        draw_rectangle(x + self.width / 2,
                       y + self.height / 2,
                       x - self.width / 2,
                       y - self.height / 2)
        """
        if w != None: w = w * self.width
        if h != None: h = h * self.height
        Renderer.sprites[self.key].clip_draw\
            (self.frameX * self.width,
             self.frameY * self.height,
             self.width, self.height, x, y, w, h)

    def draw_boundary(self, x1, x2, y1, y2):
        draw_rectangle(x1, y1, x2, y2)

    def update(self):
        if self.delay_on:
            self.delay += 1
            if self.delay > 3:
                if self.max_frame_x != 0:
                    self.frameX = (self.frameX + 1) % self.max_frame_x
                if self.max_frame_y != 0:
                    self.frameY = (self.frameY + 1) % self.max_frame_y
                self.delay = 0
        else:
                if self.max_frame_x != 0:
                    self.frameX = (self.frameX + 1) % self.max_frame_x
                if self.max_frame_y != 0:
                    self.frameY = (self.frameY + 1) % self.max_frame_y
                self.delay = 0

    def change_frameX(self, x):
        self.frameX = x

    def change_frameY(self, y):
        self.frameY = y

    def change_image(self, image_path, width, height, max_frame_x, max_frame_y = 0,frameX = 0, frameY = 0):
        del self.sprites[self.key]
        if self.find_path(image_path) == False:
            Renderer.sprites[image_path] = load_image(image_path)
        self.key = image_path
        self.width, self.height = width, height
        self.frameX, self.frameY = frameX, frameY
        self.max_frame_x, self.max_frame_y = max_frame_x, max_frame_y

    def find_path(self, image_path):
        if (image_path in Renderer.sprites) == False:
            return False
        return True

    def check_animation_end(self):
        return self.frameX + 2 > self.max_frame_x

    def set_alpha(self, alpha):
        if alpha < 0 : alpha = 0
        if alpha > 1 : alpha = 1
        Renderer.sprites[self.key].opacify(alpha)
