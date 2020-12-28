from time import time
import pygame as pg
import numpy as np
from game_object import Game_object
from rectangle import *
from Button import *
from Monster import *


class Wall(Monster):
    def __init__(self, game, pos=(0,0), height=200, width=10, period_x=2, period_y=2, ampli_x=0, ampli_y=0):
        super().__init__(game, pos, height, width)
        #self.mobile_position = pos
        self.period_X = period_x
        self.period_Y = period_y
        self.ampli_X = ampli_x
        self.ampli_Y = ampli_y
        #self.color = color
        self.display_button_edition_mode = False
        #self.buttons_edition_mode = []

    def attributes_to_save(self):
        att_to_save = super(Wall, self).attributes_to_save()
        att_to_save.append('period_X')
        att_to_save.append('period_Y')
        att_to_save.append('ampli_X')
        att_to_save.append('ampli_Y')
        return att_to_save

    def interact(self):
        self.pos[0] = self.initial_pos[0] + self.ampli_X*np.sin(2*np.pi*time()/self.period_X)
        self.pos[1] = self.initial_pos[1] + self.ampli_Y*np.sin(2*np.pi*time()/self.period_Y)
        message = super(Wall, self).interact()
        return message

    def collide_with_me(self, character):
        """return true iff characcter colide with the wall self"""
        x_min, x_max, y_min, y_max = self.get_limits()
        x_min_char, x_max_char, y_min_char, y_max_char = character.get_limits()
        return (x_min < x_min_char < x_max and y_min < y_min_char < y_max) or \
               (x_min < x_min_char < x_max and y_min < y_max_char < y_max) or \
               (x_min < x_max_char < x_max and y_min < y_min_char < y_max) or \
               (x_min < x_max_char < x_max and y_min < y_max_char < y_max) or \
                (x_min_char < x_min < x_max < x_max_char) and (y_min<y_min_char<y_max) or \
               (y_min_char < y_min < y_max < y_max_char) and (x_min<x_min_char<x_max)

    def create_buttons(self):
        pos1 = [self.initial_pos[0] - 90, self.initial_pos[1]]
        pos2 = [self.initial_pos[0] - 90, self.initial_pos[1] + 70]
        pos3 = [self.initial_pos[0] + 20, self.initial_pos[1]]
        pos4 = [self.initial_pos[0] + 20, self.initial_pos[1] + 70]

        hor_period_button = Button(self.game, pos1, 0, 0,
                                   f'hor period : ', self.period_X, value_min=0.5, value_max=30, step=0.5)
        hor_ampl_button = Button(self.game, pos2, 0, 0, f'hor ampli : ', self.ampli_X,
                                 value_min=-300, value_max=300, step=5)
        ver_period_button = Button(self.game, pos3, 0, 0, f'ver period : ', self.period_Y,
                                   value_min=0.5, value_max=30, step=0.5)
        ver_ampl_button = Button(self.game, pos4, 0, 0, f'ver ampli : ', self.ampli_Y,
                                 value_min=-300, value_max=300, step=5)
        buttons = [hor_period_button, hor_ampl_button, ver_period_button, ver_ampl_button]
        return buttons

    def save_buttons_values(self):
        self.period_X = self.buttons_edition_mode[0].value
        self.ampli_X = self.buttons_edition_mode[1].value
        self.period_Y = self.buttons_edition_mode[2].value
        self.ampli_Y = self.buttons_edition_mode[3].value

def f(x, a, b):
    #returns x if x in [a, b], a if x < a and b if x > b
    if x < a:
        return a
    if x > b:
        return b
    return x
















