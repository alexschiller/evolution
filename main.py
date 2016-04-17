import pyglet  # noqa
from pyglet.gl import *  # noqa
from collections import OrderedDict  # noqa
from time import time  # noqa
from os.path import abspath  # noqa
from pyglet.window import key # noqa
import cProfile # noqa
import pstats # noqa
import StringIO # noqa
from time import time, sleep # noqa
from utility import window_height, window_width
from states import StateManager


class Game(pyglet.window.Window):
    def __init__(self, height, width):
        super(Game, self).__init__(width, height, caption='Acceptable Loss')
        self.pr = cProfile.Profile()
        self.pr.enable()
        pyglet.gl.glClearColor(.8, .8, .8, 1)
        self.alive = True
        self.framerate = 0, time()
        self.count = 0
        self.statemanager = StateManager()

    def render(self, *args):
        self.statemanager.update()
        self.clear()
        self.statemanager.draw()
        self.flip()

    def on_draw(self):
        self.render()

    def on_close(self):
        self.alive = False

    # def on_key_press(self, symbol, modkey):
    #     self.state_manager.current.on_key_press(symbol, modkey)

    # def on_key_release(self, symbol, modkey):
    #     self.state_manager.current.on_key_release(symbol, modkey)

    def on_mouse_release(self, x, y, button, modifiers):
        self.statemanager.on_mouse_release(x, y, button, modifiers)

    def on_mouse_press(self, x, y, button, modifiers):
        self.statemanager.on_mouse_press(x, y, button, modifiers)

    def on_mouse_motion(self, x, y, dx, dy):
        self.statemanager.on_mouse_motion(x, y, dx, dy)

    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        self.statemanager.on_mouse_drag(x, y, dx, dy, buttons, modifiers)

    def on_mouse_scroll(self, x, y, scroll_x, scroll_y):
        self.statemanager.on_mouse_scroll(x, y, scroll_x, scroll_y)

    def run(self):
        while self.alive:
            event = self.dispatch_events()
            if event:
                print(event)
            self.render()

game = Game(window_height, window_width)

if __name__ == '__main__':
    pyglet.clock.set_fps_limit(10)

    game.run()
