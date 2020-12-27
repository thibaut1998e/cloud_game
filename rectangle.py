import pygame as pg
from game_object import *
from constantes import *


class Rectangle(Game_object):
    def __init__(self, screen, pos, height, width, color=blue):
        super().__init__(screen, pos, height, width)
        self.color = color

    def render(self):
        pg.draw.rect(self.screen, self.color, (self.pos[0], self.pos[1], self.width, self.height))









