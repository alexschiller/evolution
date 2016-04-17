import pyglet  # noqa
from pyglet.gl import *  # noqa
from collections import OrderedDict  # noqa
from time import time  # noqa


class Button(object):
    def __init__(self, dictionary):  # dictionary = {'images': [0,1,2], 'batch': batch, 'func': function, 'label': string, 'x': int, 'y': int,}
        self.sprite = pyglet.sprite.Sprite(
            dictionary['images'][1],
            dictionary['x'], dictionary['y'], batch=dictionary['batch']
        )
        self.button_img = dictionary['images']  # upsprite, hoversprite, downsprite
        try:
            self.label = pyglet.text.Label(
                dictionary['label'],
                font_name='Times New Roman',
                font_size=14,
                x=self.sprite.x,
                y=self.sprite.y,
                anchor_x='center',
                anchor_y='center',
                batch=dictionary['labelbatch']
            )
        except:
            pass

        self.flag = 0
        self.func = dictionary['func']

    def update(self):
        pass

    def draw(self):
        pass

    def on_mouse_release(self, x, y, button, modifiers):
        if (self.sprite.x - self.sprite.width / 2 < x and
                x < self.sprite.x + self.sprite.width / 2 and
                self.sprite.y - self.sprite.height / 2 < y and
                y < self.sprite.y + self.sprite.height / 2):
            if self.flag:
                # try:
                self.func()
                # except:
                # pass
            else:
                self.flag = 0

    def on_mouse_press(self, x, y, button, modifiers):
        if (self.sprite.x - self.sprite.width / 2 < x and
                x < self.sprite.x + self.sprite.width / 2 and
                self.sprite.y - self.sprite.height / 2 < y and
                y < self.sprite.y + self.sprite.height / 2):
            self.flag = 1
            self.sprite.image = self.button_img[2]
        else:
            self.flag = 0

    def on_mouse_motion(self, x, y, dx, dy):
        if (self.sprite.x - self.sprite.width / 2 < x and
                x < self.sprite.x + self.sprite.width / 2 and
                self.sprite.y - self.sprite.height / 2 < y and
                y < self.sprite.y + self.sprite.height / 2):
            self.sprite.image = self.button_img[1]
        else:
            self.sprite.image = self.button_img[0]

    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        pass

    def on_key_press(self, symbol, modifiers):
        pass

    def on_key_release(self, symbol, modifiers):
        pass


class AlertButton(Button):
    def __init__(self, dictionary):
        super(AlertButton, self).__init__(dictionary)
        self.id = dictionary['id']

    def on_mouse_release(self, x, y, button, modifiers):
        if (self.sprite.x - self.sprite.width / 2 < x and
                x < self.sprite.x + self.sprite.width / 2 and
                self.sprite.y - self.sprite.height / 2 < y and
                y < self.sprite.y + self.sprite.height / 2):
            if self.flag:
                try:
                    self.func(self.id)
                except:
                    pass
                else:
                    self.flag = 0


class Module(object):
    def __init__(self, *args, **kwargs):
        self.buttons = []
        self.sprites = []
        self.batches = [pyglet.graphics.Batch(), pyglet.graphics.Batch(), pyglet.graphics.Batch(), ]

    def update(self):
        for button in self.buttons:
            button.update()

    def add_button(self, button_dictionary, alert=False):
        button_dictionary['batch'] = self.batches[1]
        button_dictionary['labelbatch'] = self.batches[2]
        if alert:
            self.buttons.append(AlertButton(button_dictionary))
        else:
            self.buttons.append(Button(button_dictionary))

    def draw(self):
        for batch in self.batches:
            batch.draw()

    def on_mouse_release(self, x, y, button, modifiers):
        for button in self.buttons:
            button.on_mouse_release(x, y, button, modifiers)

    def on_mouse_press(self, x, y, button, modifiers):
        for button in self.buttons:
            button.on_mouse_press(x, y, button, modifiers)

    def on_mouse_motion(self, x, y, dx, dy):
        for button in self.buttons:
            button.on_mouse_motion(x, y, dx, dy)

    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        for button in self.buttons:
            button.on_mouse_drag(x, y, dx, dy, buttons, modifiers)

    def on_key_press(self, symbol, modifiers):
        for button in self.buttons:
            button.on_key_press(symbol, modifiers)

    def on_mouse_scroll(self, x, y, scroll_x, scroll_y):
        pass

    def on_key_release(self, symbol, modifiers):
        for button in self.buttons:
            button.on_key_release(symbol, modifiers)


class ScrollModule(Module):
    def __init__(self, *args, **kwargs):
        super(ScrollModule, self).__init__(args, kwargs)
        self.scroll_buttons = []

    def on_mouse_scroll(self, x, y, scroll_x, scroll_y):
        for button in self.scroll_buttons:
            # button.sprite.x += scroll_x
            button.sprite.y += scroll_y
            try:
                button.label.y += scroll_y
            except:
                pass

    def add_scroll_button(self, button_dictionary, alert=False):
        button_dictionary['batch'] = self.batches[1]
        button_dictionary['labelbatch'] = self.batches[2]
        if alert:
            b = AlertButton(button_dictionary)
            self.scroll_buttons.append(b)
            self.buttons.append(b)
        else:
            b = Button(button_dictionary)
            self.scroll_buttons.append(b)
            self.buttons.append(b)
