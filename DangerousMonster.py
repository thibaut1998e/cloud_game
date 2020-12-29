from constantes import *
from Monster import *
import numpy as np
from Button import *


class DangerousMonster(Monster):
    """a class of monster which follows the character wherever it is"""
    def __init__(self, game, pos=(0,0), height=40, width=40, im_path=monster_image, transparent_color=white, speed=1):
        super().__init__(game, pos, height, width, im_path, transparent_color)
        self.speed = speed

    def interact(self):
        message = super(DangerousMonster, self).interact()
        if self.game.has_started:
            x_char, y_char = self.game.get_character().get_center()
            char_pos = np.array([x_char, y_char])
            pos = np.array(self.pos)
            direction = char_pos - pos

            self.pos = pos + 0.1*self.speed * direction/np.linalg.norm(direction)
        return message

    def attributes_to_save(self):
        att_to_save = super(DangerousMonster, self).attributes_to_save()
        att_to_save.append('speed')
        return att_to_save

    def create_buttons(self):
        """one button to save the speed"""
        pos = [self.pos[0] + self.width + 10, self.pos[1] + self.height + 10]
        b = Button(self.game, pos, 0, 0,
               f'speed : ', self.speed, value_min=0.5, value_max=6, step=0.1)
        return [b]

    def save_buttons_values(self):
        self.speed = self.buttons_edition_mode[0].value


