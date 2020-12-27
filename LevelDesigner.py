
from pygame import locals as const
from character import *
from arrival import *
import pygame as pg
from utils import *
from game import *
from constantes import *
from Coin import *
import pickle


class LevelDesigner(Game):
    def __init__(self, window_height, window_width, image_path=None, wall_color=black):
        super().__init__(window_height, window_width, image_path, wall_color)
        self.controles = {VER_WALL: const.K_w,
                          HOR_WALL:const.K_x,
                          DELETE:const.K_d,
                          ADD_BUTTON_WALL:const.K_b,
                          COIN:const.K_c}

    def process_event(self, event):
        super(LevelDesigner, self).process_event(event)
        for i,o in enumerate(self.objects):
            o.process_event_edition_mode(event)

        if event.type == pg.KEYDOWN:
            if event.key == self.controles[VER_WALL]:
                new_wall = Wall(self, [self.width//2, self.height//2], 200, 10)
                self.add_object(new_wall)
            if event.key == self.controles[HOR_WALL]:
                new_wall = Wall(self, [self.width // 2, self.height // 2], 10, 200)
                self.add_object(new_wall)
            if event.key == self.controles[COIN]:
                new_coin = Coin(self, [self.width//2, self.height//2])
                self.add_object(new_coin)

    def save(self, save_location):
        f = open(save_location, 'w')
        write_object_in_file(self, f)
        for o in self.objects:
            if o.__class__.__name__ in dict_class_name.keys():
                write_object_in_file(o, f)
        print(f'game saved at location {save_location}')


def write_object_in_file(o, f):
    #print(type(o).__str__)
    print(f'{o.__class__.__name__}', file=f)
    for at in o.attributes_to_save():
        try:
            at_val = getattr(o, at)
            print(f'{at}\t{at_val}', file=f)
        except:
            print(f'{at} is not an attribute of the class {type(o).__name__}')
    print('', file=f)


dict_class_name = {'Character':Character,
                   'Wall':Wall,
                   'Arrival':Arrival,
                   'LevelDesigner': LevelDesigner,
                   'Coin':Coin}


if __name__ == '__main__':
    from main import main
    level_designr = LevelDesigner(500, 1000)
    char = Character(level_designr)
    arrival = Arrival(level_designr)
    level_designr.add_object(char, arrival)
    main(level_designr, 'levels/level_2.txt')
    #level_designr.save('level_1.txt')



