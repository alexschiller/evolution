import math
from utility import calc_vel_xy, window_width, window_height
import itertools
import random
from functools import partial

class Controller(object):
    def __init__(self, puppet):
        self.puppet = puppet
        self.move_target = None

    def update_target(self):
        if self.target:
            self.puppet.mx = self.target.sx
            self.puppet.my = self.target.sy
            if not self.target.alive:
                self.target = None

    @property
    def sx(self):
        return self.puppet.sprite.x

    @property
    def sy(self):
        return self.puppet.sprite.y

    def clear_movement(self):
        self.move_target = None
        self.mouse_target_sprite = None

    def set_move_to(self, x, y, scale=0):
        self.move_target = [x, y]
        self.puppet.mx = x
        self.puppet.my = y

    def check_dist_to_location(self, dx, dy):
        if abs(dx) + abs(dy) <= self.puppet.speed:
            return True
        return False

    def move(self, mx, my):
        self.last_mx = mx
        self.last_my = my
        self.puppet.sprite.x += mx
        self.puppet.sprite.y += my

    def update_movement(self):
        if self.move_target:

            dx = float(self.move_target[0]) - self.sx
            dy = float(self.move_target[1]) - self.sy

            if self.check_dist_to_location(dx, dy):
                ret = calc_vel_xy(self.move_target[0], self.move_target[1],
                    self.sx, self.sy, abs(dx) + abs(dy))
                # if reached target clear
                self.clear_movement()
            else:
                ret = calc_vel_xy(self.move_target[0], self.move_target[1],
                    self.sx, self.sy, self.puppet.speed)
            self.move(ret[0], ret[1])


    def update(self):
        self.update_movement()
        if not self.move_target:
            self.set_move_to(random.randint(0, window_width), random.randint(0, window_height))

