import random # noqa
import pyglet  # noqa
from pyglet.gl import *  # noqa
from collections import OrderedDict  # noqa
from time import time  # noqa
from os.path import abspath  # noqa
from pyglet.window import key # noqa
from utility import ModuleBoilerplate, window_width, window_height # noqa
from character import Character, Plant # noqa


class Assets(ModuleBoilerplate):
    def __init__(self):
        self.blue = []
        self.green = []

        self.modules = {
            'characters': [
            ],
        }

    def get_blue(self):
        return self.blue

    def get_green(self):
        return self.green

    def update(self):
        pass
