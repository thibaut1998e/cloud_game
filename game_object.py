import pygame as pg
from pygame import locals as const
from utils import *
import copy as cp


class Game_object:
    def __init__(self, game, pos=(0,0), height=40, width=40, im_path=None, transparent_color=black):
        self.pos = [pos[0], pos[1]]
        self.initial_pos = [pos[0], pos[1]]
        #self.initial_pos = self.pos
        self.game = game
        self.height = height
        self.width = width
        if im_path is not None:
            image = load_image(im_path, colorkey=transparent_color)
            image = pg.transform.scale(image, (width, height))
            self.image = image
        else:
            self.image = None
        self.screen_width = game.width
        self.screen_height = game.height
        self.selected = False
        self.selected_right = False
        self.ID = None

    def reset(self):
        self.pos = cp.copy(self.initial_pos)

    def attributes_to_save(self):
        return ['initial_pos', 'height', 'width']

    def __eq__(self, other):
        return self.ID == other.ID

    def display(self, color=black):
        x = int(self.pos[0]) if self.game.has_started else int(self.initial_pos[0])
        y = int(self.pos[1]) if self.game.has_started else int(self.initial_pos[1])
        if self.image is not None:
            self.image = pg.transform.scale(self.image, (int(self.width), int(self.height)))
            self.game.screen.blit(self.image, (x, y))
        else:
            pg.draw.rect(self.game.screen, color, (x, y, self.width, self.height))
        if self.selected_right:
            draw_squared_ring(self.game.screen, [x, y], self.height, self.width)

    def interact(self):
        pass

    def get_limits(self, initial_pos=False):
        x_min = self.pos[0] if not initial_pos else self.initial_pos[0]
        y_min = self.pos[1] if not initial_pos else self.initial_pos[1]
        x_max = self.pos[0] + self.width if not initial_pos else self.initial_pos[0] + self.width
        y_max = self.pos[1] + self.height if not initial_pos else self.initial_pos[1] + self.height
        return x_min, x_max, y_min, y_max

    def point_inside_limits(self, point, initial_pos=False):
        x_min, x_max, y_min, y_max = self.get_limits(initial_pos)
        return x_min < point[0] < x_max and y_min < point[1] < y_max

    def get_center(self):
        x_center = self.pos[0] + self.width // 2
        y_center = self.pos[1] + self.height // 2
        return x_center, y_center

    def process_event(self, event):
        pass

    def process_event_edition_mode(self, event):
        if event.type == pg.MOUSEMOTION:
            if self.selected:
                self.pos = list(event.pos)
                self.initial_pos = [event.pos[0], event.pos[1]]

        if event.type == pg.KEYDOWN:
            if self.selected_right:
                if event.key == const.K_LEFT:
                    if self.width > 10:
                        self.width -= 5
                if event.key == const.K_RIGHT:
                    self.width += 5
                if event.key == const.K_UP:
                    if self.height > 10:
                        self.height -= 5
                if event.key == const.K_DOWN:
                    self.height += 5
                if event.key == const.K_d:
                    self.game.suppress_object(self)

        if event.type == pg.MOUSEBUTTONDOWN and self.point_inside_limits(event.pos, initial_pos=True):
            if event.button == const.BUTTON_LEFT:
                self.selected = True
            if event.button == const.BUTTON_RIGHT:
                self.selected_right = not self.selected_right
        if event.type == pg.MOUSEBUTTONUP:
            self.selected = False



