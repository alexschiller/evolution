import random
import pyglet  # noqa
from pyglet.gl import *  # noqa
from collections import OrderedDict  # noqa
from time import time  # noqa
from os.path import abspath  # noqa
from pyglet.window import key # noqa
from utility import ModuleBoilerplate, window_width, window_height
from character import Character, Plant


class Assets(ModuleBoilerplate):
    def __init__(self):
        self.blue = []
        self.green = []

        self.modules = {
            'characters': [
            Plant(self, random.randint(50,window_width-50), random.randint(50,window_height-50) ),
            ],
        }

    def get_blue(self):
        return self.blue

    def get_green(self):
        return self.green

    def update(self):
        pass
        # if not random.randint(0, 120):
            # self.modules['characters'].append(Character(self))