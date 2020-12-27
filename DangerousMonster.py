from constantes import *
from Monster import *


class DangerousMonster(Monster):
    def __init__(self, game, pos=(0,0), height=40, width=40, im_path=None, transparent_color=white):
        super().__init__(game, pos, height, width, im_path, transparent_color)

    def interact(self):
        pass