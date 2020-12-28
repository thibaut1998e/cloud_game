import pygame as pg
from pygame import locals as const
from utils import *
import copy as cp


class Game_object:
    """general class of objects. All objects of the game must extend this class. It represents rectangle """
    def __init__(self, game, pos=(0,0), height=40, width=40, im_path=None, transparent_color=black):
        self.pos = [pos[0], pos[1]] # current position
        self.initial_pos = [pos[0], pos[1]] # initial position (used to reset position for moving objects)
        # self.initial_pos = self.pos
        self.game = game # contains all the information about the game (which includes the list of all other objects),
        # used by the object to interact with its environment
        self.height = height # height in pixels
        self.width = width
        if im_path is not None:
            # if the image path provided is not none, it loads the image using a transparency color so that we can
            # see the background. If transparent color = - 1, it is set to the color of pixel (0,0)
            image = load_image(im_path, colorkey=transparent_color)
            image = pg.transform.scale(image, (width, height))
            self.image = image
        else:
            self.image = None
        self.screen_width = game.width
        self.screen_height = game.height
        self.selected = False # used to make the object follow the mouse when the left click is maintain on it
        self.selected_right = False # used in edition mode : is set to true when the object is selected with right click
        # other actions are then possible on the object such as changing its size, until right click is pressed again
        self.ID = None # ID is set when the object is added to a game
        self.display_button_edition_mode = False
        self.buttons_edition_mode = []

    def __eq__(self, other):
        return self.ID == other.ID

    def reset(self):
        self.pos = cp.copy(self.initial_pos)

    def attributes_to_save(self):
        """attributes saved in txt file when the window is closed. Override it if you want to save other attributes in
        the children class.
        Called at each iteration of the game loop"""
        return ['initial_pos', 'height', 'width']

    def display(self, color=black):
        x = int(self.pos[0]) if self.game.has_started else int(self.initial_pos[0])
        y = int(self.pos[1]) if self.game.has_started else int(self.initial_pos[1])
        # if no image is provided displays a rectangle with specified color
        if self.image is not None:
            self.image = pg.transform.scale(self.image, (int(self.width), int(self.height)))
            self.game.screen.blit(self.image, (x, y))
        # else display the image
        else:
            pg.draw.rect(self.game.screen, color, (x, y, self.width, self.height))
        # display a red ring around the object when right-selected
        if self.selected_right:
            draw_squared_ring(self.game.screen, [x, y], self.height, self.width)

    def interact(self):
        """interaction of the object with its environment, call at each iteration of the game loop.
        To be overrided
        """
        pass

    def process_event(self, event):
        """event process in playing mode"""
        pass

    def create_buttons(self):
        """list of buttons created when pressing b on selected object"""
        return []

    def save_buttons_values(self):
        """save the recorded values of the buttons"""
        pass

    def button_event(self):
        if not self.display_button_edition_mode:
            # if no buttons are being displayed we create them
            buttons = self.create_buttons()
            self.game.add_object(*buttons)
            self.buttons_edition_mode = buttons
            self.display_button_edition_mode = True
        else:
            # otherwise we delete them and record their values
            self.save_buttons_values()
            for b in self.buttons_edition_mode:
                self.game.suppress_object(b)
            self.display_button_edition_mode = False

    def process_event_edition_mode(self, event):
        # if selected with left click, follows the mouse
        if event.type == pg.MOUSEMOTION:
            if self.selected:
                self.pos = list(event.pos)
                self.initial_pos = [event.pos[0], event.pos[1]]

        if event.type == pg.KEYDOWN:
            # all possible action when selected with right click
            if self.selected_right:
                # change size of object with arrows
                if event.key == const.K_LEFT:
                    if self.width > 10:
                        self.width -= 5
                if event.key == const.K_RIGHT:
                    self.width += 5
                if event.key == const.K_UP:
                    if self.height > 10:
                        self.height -= 5
                if event.key == const.K_DOWN:
                    self.height += 5
                # suppress the object
                if event.key == const.K_d:
                    self.game.suppress_object(self)
                # process button event
                if event.key == const.K_b:
                    self.button_event()
        # detects a right or left click inside the limits, if so set the corresponding booleans
        if event.type == pg.MOUSEBUTTONDOWN and self.point_inside_limits(event.pos, initial_pos=True):
            if event.button == const.BUTTON_LEFT:
                self.selected = True
            if event.button == const.BUTTON_RIGHT:
                self.selected_right = not self.selected_right
        if event.type == pg.MOUSEBUTTONUP:
            self.selected = False

    def get_limits(self, initial_pos=False):
        x_min = self.pos[0] if not initial_pos else self.initial_pos[0]
        y_min = self.pos[1] if not initial_pos else self.initial_pos[1]
        x_max = self.pos[0] + self.width if not initial_pos else self.initial_pos[0] + self.width
        y_max = self.pos[1] + self.height if not initial_pos else self.initial_pos[1] + self.height
        return x_min, x_max, y_min, y_max

    def point_inside_limits(self, point, initial_pos=False):
        x_min, x_max, y_min, y_max = self.get_limits(initial_pos)
        return x_min < point[0] < x_max and y_min < point[1] < y_max

    def get_center(self):
        x_center = self.pos[0] + self.width // 2
        y_center = self.pos[1] + self.height // 2
        return x_center, y_center








