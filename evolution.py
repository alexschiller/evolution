import random # noqa
import pyglet  # noqa
from pyglet.gl import *  # noqa
from collections import OrderedDict  # noqa
from time import time  # noqa
from os.path import abspath  # noqa
from pyglet.window import key # noqa
from utility import ModuleBoilerplate, window_width, window_height, load_image, mainbatches # noqa
from character import Character # noqa

class Assets(ModuleBoilerplate):
    def __init__(self):
        self.points = []
        self.frame = pyglet.sprite.Sprite(load_image('frame.png'),
            -500, -500, batch=mainbatches[2]) # noqa

        self.modules = {
            'characters': [],
        }

    def update(self):
        pass
