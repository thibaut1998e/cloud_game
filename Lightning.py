from Monster import *
from constantes import *
from Button import *


class Lightning(Monster):
    def __init__(self, game, pos=(0,0), height=100, width=20, im_path=lightning_image, transparent_color=white, speed=1):
        super().__init__(game, pos, height, width, im_path, transparent_color)
        self.speed = speed
        
    def display(self, color=black):
        if self.game.has_started:
            super(Lightning, self).display()

    def interact(self):
        message = super(Lightning, self).interact()
        self.pos[1] = self.pos[1] + self.speed
        if self.pos[1] >= self.game.height:
            self.game.suppress_object(self)
        return message

