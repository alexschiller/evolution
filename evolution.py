import random # noqa
import pyglet  # noqa
from pyglet.gl import *  # noqa
from collections import OrderedDict  # noqa
from time import time  # noqa
from os.path import abspath  # noqa
from pyglet.window import key # noqa
from utility import ModuleBoilerplate, window_width, window_height # noqa
from character import Character


class Assets(ModuleBoilerplate):
    def __init__(self):
        self.modules = {
            'characters': [Character(self)],
        }

    def update(self):
        pass
