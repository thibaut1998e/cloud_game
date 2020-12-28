from game_object import *
from constantes import *


class Coin(Game_object):
    def __init__(self, game, pos=(0,0), height=25, width=25, im_path=coin_image, transparent_color=white):
        super().__init__(game, pos, height, width, im_path, transparent_color)
        self.caught = False
    
    def display(self, color=black):
        if not self.caught:
            super(Coin, self).display()

    def interact(self):
        x_center, y_center = self.game.get_character().get_center()
        if self.point_inside_limits([x_center, y_center]):
            self.caught = True
        return ''
    
    def reset(self):
        super(Coin, self).reset()
        self.caught = False

