from time import time
import pygame as pg
import numpy as np


class Wall:
    def __init__(self, screen, position, height, width, period_x=7, period_y=7, ampli_x=0, ampli_y=0, color=(0, 0, 0)):
        self.position = position
        self.mobile_position = position
        self.period_X = period_x
        self.period_Y = period_y
        self.ampli_X = ampli_x
        self.ampli_Y = ampli_y
        self.height = height
        self.width = width
        self.screen = screen
        self.color = color

    def render(self):
        posx = self.position[0] + self.ampli_X*np.sin(2*np.pi*time()/self.period_X)
        posy = self.position[1] + self.ampli_Y*np.sin(2*np.pi*time()/self.period_Y)
        self.mobile_position = (posx, posy)
        pg.draw.rect(self.screen, self.color, (posx, posy, self.width, self.height))

    def get_limits(self):
        x_min = self.mobile_position[0]
        y_min = self.mobile_position[1]
        x_max = self.mobile_position[0] + self.width
        y_max = self.mobile_position[1] + self.height
        return x_min, x_max, y_min, y_max

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

