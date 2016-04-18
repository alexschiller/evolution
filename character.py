import pyglet  # noqa
from pyglet.gl import *  # noqa
from utility import load_image, mainbatches, window_width, window_height
from collide import * # noqa
import random


blue_sprite = pyglet.image.SolidColorImagePattern(color=(0, 0, 255, 150))
class Character(object):
    def __init__(self):
        self.sprite = pyglet.sprite.Sprite(pyglet.image.create(5, 5, blue_sprite),
            random.randint(0,500), random.randint(0,500), batch=mainbatches[2]) # noqa
        self.collision = SpriteCollision(self.sprite)

        self.color = 'blue'
        self.speed  = 2
        self.energy = 100
        self.health = 100

    def update(self):
        pass