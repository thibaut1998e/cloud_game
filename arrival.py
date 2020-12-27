import pygame as pg
from constantes import *
from game_object import *


class Arrival(Game_object):
    def __init__(self, game, pos=None, im_path=path_arrival_image, width=40, height=40):
        if pos is None:
            pos = [game.width - 100, game.height//2]
        super().__init__(game, pos, height, width, im_path)

    def test_end_game(self, character):
        x_center, y_center = character.get_center()
        return self.point_inside_limits((x_center, y_center))

    def interact(self):
        if self.test_end_game(self.game.get_character()):
            self.game.continuer = False
            return messages[2]
        return ''