import pyglet  # noqa
from pyglet.gl import *  # noqa
from collections import OrderedDict  # noqa
from time import time  # noqa
from os.path import abspath  # noqa
from pyglet.window import key # noqa

mainbatches = [pyglet.graphics.Batch(), pyglet.graphics.Batch(), pyglet.graphics.Batch()]

window_height = 800
window_width = 1400
x_offset = 345
y_offset = 45
scale = 1

image_dict = {}


def load_image(image, anchor=True):
    # try
    # return image_dict[image]
    # except:
    img = pyglet.image.load('images/' + image)
    if anchor:
        img.anchor_x = img.width // 2
        img.anchor_y = img.height // 2
    image_dict[image] = img
    return img


class ModuleBoilerplate(object):
    def __init__(self, *args, **kwargs):
        pass

    def update(self):
        pass

    def draw(self):
        pass

    def on_mouse_release(self, x, y, button, modifiers):
        pass

    def on_mouse_press(self, x, y, button, modifiers):
        pass

    def on_mouse_motion(self, x, y, dx, dy):
        pass

    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        pass

    def on_key_press(self, symbol, modifiers):
        pass

    def on_key_release(self, symbol, modifiers):
        pass
