from constantes import *
import pygame as pg
from game_object import *
from utils import *


class Button(Game_object):
    """button are Object which display text and an settable value, note that height and width in
    the constructor are not used here, they are set automatically with the parameter size of the method display_text"""
    def __init__(self, game, pos, height, width, text, value, value_min, value_max, step):
        super().__init__(game, pos, height, width)
        self.text = text
        self.value = value
        text_rect = display_text(self.game.screen, self.text, size=12, location=(self.pos[0], self.pos[1]))
        self.height = text_rect.height
        self.width = text_rect.width
        self.value_min = value_min
        self.value_max = value_max
        self.step = step

    def display(self, color=blue):
        super(Button, self).display(color=color)
        text = f'{self.text}{round(self.value, 2)}'
        display_text(self.game.screen, text, size=12, location=(self.pos[0]+self.width//2, self.pos[1]+self.height//2))

    def process_event_edition_mode(self, event):
        """when pressing + or - on a selected button we can adjust its value"""
        super(Button, self).process_event_edition_mode(event)
        if self.selected_right and event.type == const.KEYDOWN:
            if event.unicode == '+':
                self.value = min(self.value_max, self.value+self.step)
            if event.unicode == '-':
                self.value = max(self.value_min, self.value-self.step)







