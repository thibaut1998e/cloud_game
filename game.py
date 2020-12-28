import pygame
from pygame import locals as const
from character import *
from constantes import *
from wall import *
from arrival import *
from Coin import *


class Game:
    def __init__(self, window_height, window_width, image_path=None, wall_color=black):
        screen = pg.display.set_mode((window_width, window_height))
        self.screen = screen
        self.height = self.screen.get_height()
        self.width = self.screen.get_width()
        self.continuer = True # the game is stopped when False
        self.objects = []  # list of objects
        self.id_cpt = 0   # count the number objects added to the list (used to assign an ID to each object)
        self.image = None
        self.wall_color = wall_color
        self.has_started = False   # true iff the game has started (the character starts moving). Before
        # the game has started, the character can't move right and left and objects are displayed at their initial
        # position instead of their actual position. (to avoid moving objects in the edition mode while not playing)
        if image_path is not None:
            # load and rescale the background image
            image = load_image(image_path)
            self.image = pg.transform.scale(image, (self.width, self.height))

    def attributes_to_save(self):
        """attributes saved in the txt file when closing the window in edition mode"""
        return ['height', 'width']

    def get_character(self):
        """the character is the first object in the list (it is ensure by the add_onject method)"""
        return self.objects[0]

    def prepare(self):
        """reset the boolean continuer and has started and reset all the objects"""
        pygame.key.set_repeat(200, 50)
        self.has_started = False
        self.continuer = True
        for o in self.objects:
            o.reset()

    def add_object(self, *objects):
        """must be called to add new object to the game"""
        if len(self.objects) == 0 and not isinstance(objects[0], Character):
            print('the first object of the game object list must be a Character')
            raise ValueError
        for o in objects:
            o.ID = self.id_cpt
            self.id_cpt += 1
            self.objects.append(o)

    def suppress_object(self, object):
        """remove object from the game. (used in edition mode), can't remove character and arrival"""
        idx_object = -1
        for i in range(len(self.objects)):
            if object == self.objects[i]:
                idx_object = i
                break
        if idx_object == -1:
            print(f'try to supress object {object} from the game but it is not in the list of objects')
        elif idx_object == 0 or idx_object == 1:
            print('cant supress character or arrival from the game')
        else:
            del self.objects[idx_object]

    def interact_and_display(self):
        """display the background and all the objects, then make all the objects interact with the game by calling
        their methods intercat()"""
        if self.image is None:
            #if no Image was provided, display a white backgrounf
            pygame.draw.rect(self.screen, white, (0, 0) + self.screen.get_size())  # on dessine le fond
        else:
            self.screen.blit(self.image, (0, 0))
        message_to_return = ''
        for o in self.objects:
            message = o.interact()
            if message != '':
                message_to_return = message
            o.display(color=self.wall_color)

        return message_to_return

    def process_event(self, event: pygame.event):
        """process the events (interaction between the keyboard and the objects)"""
        for o in self.objects:
            o.process_event(event)
        if event.type == const.QUIT:
            self.continuer = False

    def get_ojects_of_class(self, cls):
        """returns the list of objects instance of cls"""
        objs = []
        for o in self.objects:
            if isinstance(o, cls):
                objs.append(o)
        return objs

    def all_coins_caught(self):
        """returns true iff all the coins in the game have been caught
        (used in the class Arrival to test the end of the game)"""
        for c in self.get_ojects_of_class(Coin):
            if not c.caught:
                return False
        return True

    def start(self):
        """main loop of the game"""
        message = ''
        self.prepare()
        while self.continuer:
            for event in pygame.event.get():
                self.process_event(event)

            message = self.interact_and_display()
            pygame.display.flip()
        return message




