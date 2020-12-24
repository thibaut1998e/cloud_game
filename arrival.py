import pygame as pg
from constantes import *


class Arrival:
    def __init__(self, location, screen, image_path=path_arrival_image, width=40, height=40):
        image = pg.image.load(image_path).convert_alpha()
        image = pg.transform.scale(image, (width, height))
        self.image = image
        self.width = width
        self.height = height
        self.location = location
        self.screen = screen

    def render(self):
        x = int(self.location[0])
        y = int(self.location[1])
        self.screen.blit(self.image, (x, y))

    def test_end_game(self, character):
        x_min, x_max, y_min, y_max = character.get_limits()
        x_center = self.location[0] + self.width//2
        y_center = self.location[1] + self.height//2
        return x_min < x_center < x_max and y_min < y_center < y_max