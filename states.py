import pyglet  # noqa
from pyglet.gl import *  # noqa
from collections import OrderedDict  # noqa
from time import time  # noqa
from os.path import abspath  # noqa
from utility import * # noqa
from pyglet.window import key # noqa
from evolution import Assets
from character import * # noqa
from point import Point

class State(object):
    def __init__(self, assets, manager):
        self.manager = manager
        self.assets = assets
        self.batches = mainbatches

    def update(self):
        for c in self.assets.modules['characters']:
            c.update()
        self.assets.update()

    def draw(self):
        self.assets.draw()

        for batch in self.batches:
            batch.draw()  # player is a module or not, note

    def on_mouse_release(self, x, y, button, modifiers):
        self.assets.on_mouse_release(x, y, button, modifiers)
        self.assets.frame.x = -500
        self.assets.frame.y = -500
        self.assets.evaluate_points()
        self.assets.points = []

    def on_mouse_press(self, x, y, button, modifiers):
        self.assets.on_mouse_press(x, y, button, modifiers)
        self.assets.frame.x = round(x / 10.0) * 10 + 95
        self.assets.frame.y = round(y / 10.0) * 10 + 95

    def on_mouse_motion(self, x, y, dx, dy):
        self.assets.on_mouse_motion(x, y, dx, dy)

    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        self.assets.on_mouse_drag(x, y, dx, dy, buttons, modifiers)
        self.assets.points.append(Point(self.assets, x, y))

    def on_key_press(self, symbol, modifiers):
        self.assets.on_key_press(symbol, modifiers)

    def on_key_release(self, symbol, modifiers):
        self.assets.on_key_release(symbol, modifiers)

    def on_mouse_scroll(self, x, y, scroll_x, scroll_y):
        pass

    def tostring(self):
        pass


class StateManager(object):
    def __init__(self):
        self.currentstate = State(Assets(), self)  # replace none with some form of assests
        self.selectstate = None
        self.mainstate = None
        self.menustate = None

    def update(self):
        self.currentstate.update()

    def draw(self):
        self.currentstate.draw()

    def on_mouse_release(self, x, y, button, modifiers):
        self.currentstate.on_mouse_release(x, y, button, modifiers)

    def on_mouse_press(self, x, y, button, modifiers):
        self.currentstate.on_mouse_press(x, y, button, modifiers)

    def on_mouse_motion(self, x, y, dx, dy):
        self.currentstate.on_mouse_motion(x, y, dx, dy)

    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        self.currentstate.on_mouse_drag(x, y, dx, dy, buttons, modifiers)

    def on_key_press(self, symbol, modifiers):
        self.currentstate.on_key_press(symbol, modifiers)

    def on_key_release(self, symbol, modifiers):
        self.currentstate.on_key_release(symbol, modifiers)

    def on_mouse_scroll(self, x, y, scroll_x, scroll_y):
        self.currentstate.on_mouse_scroll(x, y, scroll_x, scroll_y)

    def tostring(self):
        return self.currentstate.tostring()
