from Monster import *
from time import time
from Lightning import *




class ThunderCloud(Monster):
    def __init__(self, game, pos=(0,0), height=80, width=200, im_path=nasty_cloud_image, transparent_color=white, period=2,
                 lighting_speed=0.5):
        super().__init__(game, pos, height, width, im_path, transparent_color)
        self.period = period
        self.lightning_speed = lighting_speed
        self.current_time = time()

    def attributes_to_save(self):
        att_to_save = super(ThunderCloud, self).attributes_to_save()
        att_to_save.append('period')
        att_to_save.append('lightning_speed')
        return att_to_save

    def interact(self):
        message = super(ThunderCloud, self).interact()
        t = time()
        if t - self.current_time > self.period:
            self.current_time = t
            pos = [self.pos[0] + self.width//2, self.pos[1]+self.height]
            lightning = Lightning(self.game, pos=pos, speed=self.lightning_speed)
            self.game.add_object(lightning)
        return message

    def create_buttons(self):
        pos1 = [self.pos[0] - 30, self.pos[1] + self.width//2]
        pos2 = [self.pos[0] + self.width, self.pos[1]+self.width//2]
        b1 = Button(self.game, pos1, 0, 0,
                    'lightning speed : ', self.lightning_speed, value_min=0.1, value_max=2, step=0.1)
        b2 = Button(self.game, pos2, 0, 0,
                    'period : ', self.period, value_min=0.5, value_max=5, step=0.1)
        return [b1, b2]

    def save_buttons_values(self):
        self.lightning_speed = self.buttons_edition_mode[0].value
        self.period = self.buttons_edition_mode[1].value

