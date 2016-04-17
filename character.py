import pyglet  # noqa
from pyglet.gl import *  # noqa
from utility import load_image, mainbatches

blue_sprite = pyglet.image.SolidColorImagePattern(color=(0, 0, 255, 150))
class Character(object):
    def __init__(self):
        self.sprite = pyglet.sprite.Sprite(pyglet.image.create(50, 50, blue_sprite),
            0, 0, batch=mainbatches[2]) # noqa
