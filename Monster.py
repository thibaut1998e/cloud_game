from game_object import *


class Monster(Game_object):
    """general class for objects which ends the game when the charcater collide with them"""
    def __init__(self, game, pos=(0,0), height=40, width=40, im_path=None, transparent_color=black):
        super().__init__(game, pos, height, width, im_path, transparent_color)

    def collide_with_me(self, character):
        """return true iff characcter colide with the wall self"""
        x_min, x_max, y_min, y_max = self.get_limits()
        x_min_char, x_max_char, y_min_char, y_max_char = character.get_limits()
        return (x_min < x_min_char < x_max and y_min < y_min_char < y_max) or \
               (x_min < x_min_char < x_max and y_min < y_max_char < y_max) or \
               (x_min < x_max_char < x_max and y_min < y_min_char < y_max) or \
               (x_min < x_max_char < x_max and y_min < y_max_char < y_max) or \
                (x_min_char < x_min < x_max < x_max_char) and (y_min<y_min_char<y_max) or \
               (y_min_char < y_min < y_max < y_max_char) and (x_min<x_min_char<x_max)

    def interact(self):
        message = ''
        if self.game.has_started and self.collide_with_me(self.game.get_character()):
            self.game.continuer = False
            return losing_messages[0]
        return message
