from time import time
import pygame as pg
import numpy as np


class Platform:
    def __init__(self, screen, position, length, width, period_x=7, period_y=7, ampli_x=0, ampli_y=0, color=(0, 0, 0)):
        self.position = position
        self.mobile_position = position
        self.period_X = period_x
        self.period_Y = period_y
        self.ampli_X = ampli_x
        self.ampli_Y = ampli_y
        self.length = length
        self.width = width
        self.screen = screen
        self.color = color

    def render(self):
        posx = self.position[0] + self.ampli_X*np.sin(2*np.pi*time()/self.period_X)
        posy = self.position[1] + self.ampli_Y*np.sin(2*np.pi*time()/self.period_Y)
        self.mobile_position = (posx, posy)
        pg.draw.rect(self.screen, self.color, (posx, posy, self.length, self.width))
