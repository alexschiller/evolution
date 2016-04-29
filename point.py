import pyglet  # noqa
from pyglet.gl import *  # noqa
from utility import load_image, mainbatches, window_width, window_height, calc_vel_xy # noqa
from collide import * # noqa

white_sprite = pyglet.image.SolidColorImagePattern(color=(240, 240, 240, 255))

class Point(object):
    def __init__(self, assets, x, y):
        self.sprite = pyglet.sprite.Sprite(pyglet.image.create(5, 5, white_sprite),
            x, y, batch=mainbatches[2]) # noqa
        self.assets = assets

    @property
    def x(self):
        return self.sprite.x

    @property
    def y(self):
        return self.sprite.y
