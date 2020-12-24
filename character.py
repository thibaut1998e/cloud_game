import pygame
from constantes import *
from time import time

t0_jump = 0

class Character:
    def __init__(self, screen, pos=None, im_path=path_character_image, char_height=40, char_width=40):
        self.screen = screen
        self.screen_width = self.screen.get_width()
        self.screen_height = self.screen.get_height()
        image = pygame.image.load(im_path).convert_alpha()
        image = pygame.transform.scale(image, (char_width, char_height))
        self.image = image
        self.pos = pos
        if pos is None:
            self.pos = [0, 2*char_height]
        self.move_right = False
        self.move_left = False
        self.sprint = False
        self.jump_button = False #True iff jump bitton is currently pressed
        self.v0 = 0
        self.width = char_width
        self.height = char_height
        self.start = False
        #self.check_plateform()

    def render(self):
        x = int(self.pos[0])
        y = int(self.pos[1])
        self.screen.blit(self.image, (x,y))

    def move(self):
        if self.start:
            delta = hor_speed if not self.sprint else hor_speed_sprint
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
            self.start = True
            self.y0 = self.pos[1]



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

    def get_limits(self):
        x_min = self.pos[0]
        y_min = self.pos[1]
        x_max = self.pos[0] + self.width
        y_max = self.pos[1] + self.height
        return x_min, x_max, y_min, y_max

    #def point_inside_limits(self):


