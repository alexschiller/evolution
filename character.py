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
            ['blue', blue_sprite, assets.blue, assets.get_green, assets.get_blue],
            ['green', green_sprite, assets.green, assets.get_blue, assets.get_green]
        ])
        c[2].append(self)
        self.get_enemies = c[3]
        self.get_allies = c[4]        
        self.color =  c[0]
        self.sprite = pyglet.sprite.Sprite(pyglet.image.create(5, 5, c[1]),
            random.randint(0, 500), random.randint(0, 500), batch=mainbatches[2]) # noqa
        self.collision = SpriteCollision(self.sprite)
        self.controller = Controller(self)
        self.speed  = 2
        self.energy = 300
        self.health = 100
        self.target = None

    def update(self):
        try:
            self.controller.update()
            closest = float("inf")
            closest_e = None
            self.energy -= 1

            for e in self.get_enemies():
                if math.hypot(self.sprite.x - e.sprite.x, self.sprite.y - e.sprite.y) < closest:
                    closest_e = e
            self.target = closest_e
            if self.target:
                if collide(self.collision, self.target.collision):
                    if self.energy > self.target.energy:
                        self.energy += self.target.energy
                        self.target.energy = 0
                        self.target.cleanup()     
                    else:
                        self.target.energy += self.energy
                        self.energy = 0
                        self.cleanup()
            try:
                self.sprite.scale = max(math.log(self.energy), 1)
            except:
                self.cleanup()                    
        except:
            self.cleanup()

    def cleanup(self):
        try:
            self.sprite.delete()
        except:
            print 'cleanup fail'
        try:
            self.get_allies().remove(self)
        except:
            print 'cleanup fail'
        try:
            del self
        except:
            print 'cleanup fail'