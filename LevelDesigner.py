from pygame import locals as const
from character import *
from arrival import *
import pygame as pg
from utils import *
from game import *
from constantes import *
from Coin import *
import pickle
from DangerousMonster import *
from functools import partial
from ThunerCloud import *


class LevelDesigner(Game):
    """class to design levels"""
    def __init__(self, window_height, window_width, image_path=None, wall_color=black):
        super().__init__(window_height, window_width, image_path, wall_color)
        # objets which pop on the screen when pressing the corresponding keys (ex : K_b = B key)
        self.controles = {const.K_c: Coin,
                          const.K_m: DangerousMonster,
                          const.K_w: partial(Wall, height=200, width=10),
                          const.K_x: partial(Wall, height=10, width=200),
                          const.K_t: ThunderCloud}

    def process_event(self, event):
        super(LevelDesigner, self).process_event(event) # it is still possible to use the controls of playing mode
        for i,o in enumerate(self.objects):
            o.process_event_edition_mode(event) # individual event process of each object

        # add new objects when pressing on certain keys
        if event.type == pg.KEYDOWN:
            if event.key in self.controles.keys():
                new_object = self.controles[event.key](self, pos=[self.width//2, self.height//2])
                self.add_object(new_object)

    def save(self, save_location):
        """write the game in a text file"""
        f = open(save_location, 'w')
        # we start by writing some of the game attributes (height and width)
        write_object_in_file(self, f)
        # we then write the attributes of all the objects. (only attributes specified
        # in their method attribute_to_save)
        for o in self.objects:
            # If the class name is not in the keys of dict_class_name, the object is not saved, otherwise the method
            # create_game_with_file in main.py wont be able to reconstruct the object
            if o.__class__.__name__ in dict_class_name.keys():
                write_object_in_file(o, f)
        print(f'game saved at location {save_location}')


def write_object_in_file(o, f):
    print(f'{o.__class__.__name__}', file=f)
    for at in o.attributes_to_save():
        try:
            at_val = getattr(o, at)
            print(f'{at}\t{at_val}', file=f)
        except:
            print(f'{at} is not an attribute of the class {type(o).__name__}')
    print('', file=f)


dict_class_name = {'Character': Character,
                   'Wall': Wall,
                   'Arrival': Arrival,
                   'LevelDesigner': LevelDesigner,
                   'Coin': Coin,
                   'DangerousMonster': DangerousMonster,
                   'ThunderCloud': ThunderCloud}


if __name__ == '__main__':
    from main import main
    level_designr = LevelDesigner(500, 1000)
    char = Character(level_designr)
    arrival = Arrival(level_designr)
    level_designr.add_object(char, arrival)
    main(level_designr, 'levels/level_2.txt')
    #level_designr.save('level_1.txt')



