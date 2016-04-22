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

class Plant(object):
    def __init__(self, assets, x, y):
        self.assets = assets
        self.sprite = pyglet.sprite.Sprite(pyglet.image.create(10, 10, green_sprite),
            x, y, batch=mainbatches[2]) # noqa
        self.collision = SpriteCollision(self.sprite)
        self.cat = 'plant'
        self.energy = random.randint(1, 99)

    def update(self):
        flag = 0
        for e in self.assets.modules['characters']:
            if self != e:
                if collide(self.collision, e.collision):
                    flag = 1
                    e.energy += self.energy
                    self.cleanup()
                    return
        if not flag:
            if self.energy <= 0:
                self.cleanup()
                return
            if self.energy < 100:
                self.energy += 1
            if self.energy >= 50:
                self.energy = 25
                self.assets.modules['characters'].append(
                    Plant(self.assets, self.sprite.x + random.randint(-20, 20), self.sprite.y + random.randint(-20, 20))
                )
        try:
            self.sprite.scale = self.energy / 90.0 + .10
        except:
            self.cleanup()
            return

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
