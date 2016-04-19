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

def calc_vel_xy(tar_x, tar_y, start_x, start_y, velocity):
    dif_y = tar_y - start_y
    dif_x = tar_x - start_x
    try:
        dir_y = dif_y / abs(dif_y)
    except:
        dir_y = 1
    try:
        dir_x = dif_x / abs(dif_x)
    except:
        dir_x = 1
    try:
        perc = float(abs(dif_y)) / (abs(dif_y) + abs(dif_x))
    except:
        perc = .1
    vel_y = perc * velocity * dir_y
    vel_x = (velocity - abs(vel_y)) * dir_x
    return (vel_x, vel_y)


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
