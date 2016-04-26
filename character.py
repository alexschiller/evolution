import pyglet  # noqa
from pyglet.gl import *  # noqa
from utility import load_image, mainbatches, window_width, window_height, calc_vel_xy # noqa
from collide import * # noqa
import random
import math
# from controller import Controller

def mean(inp):
    return sum(inp) / float(len(inp))

green_sprite = pyglet.image.SolidColorImagePattern(color=(30, 255, 30, 255))
blue_sprite = pyglet.image.SolidColorImagePattern(color=(30, 30, 255, 255))

class Character(object):
    def __init__(self, assets):
        self.assets = assets
        self.sprites = [pyglet.sprite.Sprite(pyglet.image.create(10, 10, green_sprite),
            500, 500, batch=mainbatches[2])
        ]
        for i in range(9):
            self.make_sprite()
        # self.collision = SpriteCollision(self.sprite)
        # self.controller = Controller(self)

    def update(self):
        self.random_move()
        m = self.sprite_mean()
        for i in self.sprites:
            if math.hypot(m[0] - i.x, m[1] - i.y) > 10:
                ret = calc_vel_xy(m[0], m[1], i.x, i.y, 3)
                i.x += ret[0]
                i.y += ret[1]

    def cleanup(self):
        try:
            self.sprite.delete()
        except:
            pass
        try:
            self.assets.modules['characters'].remove(self)
        except:
            pass
        try:
            del self
        except:
            pass

    def random_move(self):
        v = random.choice(self.sprites)
        v.x += random.randint(-5, 5)
        v.y += random.randint(-5, 5)

    def sprite_mean(self):
        x = mean([m.x for m in self.sprites])
        y = mean([m.x for m in self.sprites])
        return (x, y)

    def make_sprite(self):
        m = self.sprite_mean()
        self.sprites.append(
            pyglet.sprite.Sprite(pyglet.image.create(10, 10, green_sprite),
                m[0], m[1], batch=mainbatches[2]) # noqa
        )
