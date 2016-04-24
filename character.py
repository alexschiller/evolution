import pyglet  # noqa
from pyglet.gl import *  # noqa
from utility import load_image, mainbatches, window_width, window_height # noqa
from collide import * # noqa
import random
from controller import Controller

green_sprite = pyglet.image.SolidColorImagePattern(color=(30, 255, 30, 255))
blue_sprite = pyglet.image.SolidColorImagePattern(color=(30, 30, 255, 255))
class Character(object):
    def __init__(self, assets, *args, **kwargs):
        self.assets = assets
        self.sprite = pyglet.sprite.Sprite(pyglet.image.create(10, 10, green_sprite),
            random.randint(0, 500), random.randint(0, 500), batch=mainbatches[2]) # noqa
        self.collision = SpriteCollision(self.sprite)
        self.controller = Controller(self)
        self.speed = .5
        self.energy = 500
        self.health = 100
        self.target = None

    def update(self):
        pass

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
