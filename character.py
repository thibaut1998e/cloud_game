
from constantes import *
from time import time
from game_object import *
from pygame import locals as const
import copy as cp
import pygame as pg
from Button import *


t0_jump = 0


class Character(Game_object):
    """character which can be control by the player, it can move left and right and jump in the air (ie it can start
    a new jump before landing. The longer the player press the jump key, the higher it jumps. More precisely, the initial speed
    of the jump is a linear function of the time the jump key is pressed. (with a threshold v0_max, the initial speed cant
    be grater than v0max)"""
    def __init__(self, game, height=40, width=40, pos=None, im_path=path_character_image,
                 speed=hor_speed, speed_sprint=hor_speed_sprint, v0_min=v0_min, v0_max=v0_max, time_to_reach_max_speed=time_to_reach_max_speed):
        if pos is None:
            pos = [0, 2 * height]
        super().__init__(game, pos, height, width, im_path)
        self.move_right = False # move_right is true iff the right arrow is pressed, it is set to true when pressing the
        # key and reset to False whn it is dropped
        self.move_left = False
        self.sprint = False # True iff the sprint key is being pressed
        self.jump_button = False # True iff jump button is currently pressed
        self.v0 = 0 # initial speed of a jump
        self.speed = speed # speed when the sprint button is not pressed
        self.speed_sprint = speed_sprint # speed when sprint button is being pressed
        self.v0_min = v0_min # minimum of v0 (when pressing the jump button 0s)
        self.v0_max = v0_max # maximum value of v0
        self.time_to_reach_max_speed = time_to_reach_max_speed
        self.controles = {
            UP:const.K_SPACE,
            #UP: const.K_UP,
            DOWN: const.K_DOWN,
            RIGHT: const.K_RIGHT,
            LEFT: const.K_LEFT,
            SPRINT: const.K_s
        }
        #self.check_plateform()

    def reset(self):
        super(Character, self).reset()
        self.jump_button = False
        self.sprint = False
        self.move_left = False
        self.move_right = False

    def attributes_to_save(self):
        att_to_save = super(Character, self).attributes_to_save()
        att_to_save.append('speed')
        att_to_save.append('speed_sprint')
        return att_to_save

    def move(self):
        if self.game.has_started:
            # if the game has not started, the character can't move right and left
            delta = self.speed if not self.sprint else self.speed_sprint
            if self.move_right and self.pos[0] < self.screen_width - self.width:
                self.pos[0] = self.pos[0] + delta
            if self.move_left and self.pos[0] > 0:
                self.pos[0] = self.pos[0] - delta
            # delta_y is the vertical variation of the position
            delta_y = G * (time() - t0_jump) # contribution of the gravity
            delta_y -= self.jump_initial_speed() # contribution of the initial speed given to the character
            self.pos[1] += delta_y

    def start_jump(self):
        if not self.jump_button:
            global t0_jump #
            t0_jump = time()
            self.jump_button = True
            self.game.has_started = True

    def drop_jump_button(self):
        self.v0 = self.jump_initial_speed() # when the jump button is dropped the value of the initial speed is stored
        # in v0
        self.jump_button = False

    def jump_initial_speed(self):
        # vertical initial speed of jump with respect to time the key is pressed
        if self.jump_button:
            v = self.v0_min + (self.v0_max - self.v0_min) / self.time_to_reach_max_speed * (time()-t0_jump)
            return min(v, self.v0_max)
        else:
            # when the jump button is nt being pressed we simply return the value which has been stored
            # when it was dropped
            return self.v0

    def process_event(self, event):
        if event.type == const.KEYDOWN:
            if event.key == self.controles[RIGHT]:
                self.move_right = True
            if event.key == self.controles[LEFT]:
                self.move_left = True
            if event.key == self.controles[UP]:
                self.start_jump()
            if event.key == self.controles[SPRINT]:
                self.sprint = True

        if event.type == const.KEYUP:
            if event.key == self.controles[RIGHT]:
                self.move_right = False
            if event.key == self.controles[LEFT]:
                self.move_left = False
            if event.key == self.controles[SPRINT]:
                self.sprint = False
            if event.key == self.controles[UP]:
                self.drop_jump_button()

    def test_outside_screen(self):
        return self.pos[0] < -self.width or self.pos[0] > self.game.width \
               or self.pos[1] < -self.height-20 or self.pos[1] > self.game.height

    def interact(self):
        game_over = self.test_outside_screen()
        self.move()
        if game_over:
            # if the character goes outside the screen, we set game.continuer to False so that the game ends
            # other ending condtions, such as wall collision are handle in other Classes
            self.game.continuer = False
            return messages[1]
        return ''

    def create_buttons(self):
        """in edition mode, we create 2 buttons when b is pressed on a selected character, one to adjust the  horizontal
        speed and the other to adjust the horizontal speed when sprinting"""
        pos1 = [self.pos[0] + self.width + 10, self.pos[1] + self.height//2]
        pos2 = [self.pos[0]+self.width//2, self.pos[1]+self.height+10]
        b1 = Button(self.game, pos1, 0, 0,
                    'speed : ', self.speed, value_min=0.05, value_max=0.2, step=0.01)
        b2 = Button(self.game, pos2, 0, 0,
                    'speed sprint: ', self.speed_sprint, value_min=0.1, value_max=0.5, step=0.01)
        return [b1, b2]

    def save_buttons_values(self):
        self.speed = self.buttons_edition_mode[0].value
        self.speed_sprint = self.buttons_edition_mode[1].value










