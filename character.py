import math
import pyglet  # noqa
from pyglet.gl import *  # noqa
from utility import load_image, mainbatches, window_width, window_height
from collide import * # noqa
import random
from controller import Controller

blue_sprite = pyglet.image.SolidColorImagePattern(color=(0, 255, 0, 255))
green_sprite = pyglet.image.SolidColorImagePattern(color=(0, 0, 255, 255))
class Character(object):
    def __init__(self, assets):
        c = random.choice([
            ['blue', blue_sprite, assets.blue, assets.get_green],
            ['green', green_sprite, assets.green, assets.get_blue]
        ])
        c[2].append(self)
        self.get_enemies = c[3]
        self.color =  c[0]
        self.sprite = pyglet.sprite.Sprite(pyglet.image.create(5, 5, c[1]),
            random.randint(0, 500), random.randint(0, 500), batch=mainbatches[2]) # noqa
        self.collision = SpriteCollision(self.sprite)
        self.controller = Controller(self)
        self.speed  = 2
        self.energy = 100
        self.health = 100
        self.target = None

    def update(self):
        self.controller.update()
        closest = float("inf")
        closest_e = None
        for e in self.get_enemies():
            if math.hypot(self.sprite.x - e.sprite.x, self.sprite.y - e.sprite.y) < closest:
                closest_e = e
        self.target = closest_e
