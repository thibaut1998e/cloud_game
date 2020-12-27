
from constantes import *
from time import time
from game_object import *
from pygame import locals as const
import copy as cp
import pygame as pg


t0_jump = 0



class Character(Game_object):
    def __init__(self, game, height=40, width=40, pos=None, im_path=path_character_image,
                 speed=hor_speed, speed_sprint=hor_speed_sprint):
        if pos is None:
            pos = [0, 2 * height]
        super().__init__(game, pos, height, width, im_path)
        #self.initial_pos = [pos[0], pos[1]]
        self.move_right = False
        self.move_left = False
        self.sprint = False
        self.jump_button = False #True iff jump bitton is currently pressed
        self.v0 = 0
        #self.start = False
        self.speed = speed
        self.speed_sprint = speed_sprint
        self.controles = {
            UP: const.K_SPACE,
            DOWN: const.K_DOWN,
            RIGHT: const.K_RIGHT,
            LEFT: const.K_LEFT,
            SPRINT: const.K_s
        }
        #self.check_plateform()

    def reset(self):
        super(Character, self).reset()
        #self.start = False
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
            delta = self.speed if not self.sprint else self.speed_sprint
            if self.move_right and self.pos[0] < self.screen_width - self.width:
                self.pos[0] = self.pos[0] + delta
            if self.move_left and self.pos[0] > 0:
                self.pos[0] = self.pos[0] - delta

            delta_y = G * (time() - t0_jump)
            delta_y -= self.jump_initial_speed()
            self.pos[1] += delta_y

    def start_jump(self):
        if not self.jump_button:
            global t0_jump
            t0_jump = time()
            self.jump_button = True
            self.game.has_started = True

    def drop_jump_button(self):
        self.v0 = self.jump_initial_speed()
        self.jump_button = False

    def jump_initial_speed(self):
        # vertical initial speed of jump with respect to time the key is pressed
        if self.jump_button:
            v = v0_min + (v0_max - v0_min) / time_to_reach_max_speed * (time()-t0_jump)
            return min(v, v0_max)
        else:
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
            self.game.continuer = False
            return messages[1]
        return ''

    """
    def process_event_edition_mode(self, event):
        if event.type == pg.MOUSEBUTTONUP and self.selected:
            self.initial_pos = [event.pos[0], event.pos[1]]
        super(Character, self).process_event_edition_mode(event)
    """









