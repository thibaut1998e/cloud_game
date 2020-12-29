import pygame
from pygame import locals as const
from game import Game
from wall import Wall
from utils import *
from LevelDesigner import *
from character import *
from arrival import *


def main(game, save_location):
    pg.init()
    pygame.display.set_caption('cloud game')
    # text, textRect = get_text('press space to continue')
    message = 'press space to continue'
    continuer = True
    nb_tries = 0
    while continuer:
        for event in pygame.event.get():
            if event.type == const.QUIT or (event.type == const.KEYDOWN and event.key == const.K_ESCAPE):
                # de manière à pouvoir quitter le menu avec echap ou la croix
                continuer = False
            if event.type == const.KEYDOWN and event.key == const.K_SPACE:
                message = game.start()
                nb_tries += 1

        if message in winning_messages:
            message = f'{message}, number of tries : {nb_tries}'
        display_text(game.screen, message, location=(game.width // 2, game.height//2))
        pygame.display.flip()
    if save_location is not None:
        if isinstance(game, LevelDesigner):
            game.save(save_location)
    pygame.quit()


def create_game_with_file(level_path, edition_mode=False, im_path=None, wall_color=black):
    f = open(level_path, 'r')
    lines = f.readlines()
    height = int(lines[1].split('\t')[1])
    width = int(lines[2].split('\t')[1])
    if edition_mode:
        game = LevelDesigner(height, width, im_path, wall_color)
    else:
        game = Game(height, width, im_path, wall_color)

    def get_line(line):
        return line.split('\n')[0]

    first = 1
    while get_line(lines[first]) not in dict_class_name.keys():
        first += 1
    o = dict_class_name[get_line(lines[first])](game)
    for i in range(first+1, len(lines)):
        line = get_line(lines[i])
        if line in dict_class_name.keys():
            o = dict_class_name[line](game)
        elif line == '':
            game.add_object(o)
        else:
            at_name, at_val = line.split('\t')
            at_val = convert(at_val)
            setattr(o, at_name, at_val)
    main(game, level_path)
    return game


def convert(at_val):
    try:
        at_val = float(at_val)
    except:
        if type(at_val) == str:
            if at_val[0] == '[' or at_val[0] == '(':
                at_val = at_val[1:-1]
                vals = at_val.split(',')
                at_val = []
                for v in vals:
                    at_val.append(float(v))
    return at_val


def create_level_from_scratch(window_height, window_width, save_location, im_path=None, wall_color=black):
    level_designr = LevelDesigner(window_height, window_width, im_path, wall_color)
    char = Character(level_designr)
    arrival = Arrival(level_designr)
    level_designr.add_object(char, arrival)
    main(level_designr, save_location)
    return level_designr


if __name__ == '__main__':
    save_location = 'levels/level_1.txt'
    game = create_game_with_file(save_location, edition_mode=True)


