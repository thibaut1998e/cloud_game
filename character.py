import pygame
from constantes import *
from time import time

t0_jump = 0

class Character:
    def __init__(self, screen, platforms, im_path='nuage.png', char_height=100, char_width=100):
        self.screen = screen
        self.screen_width = self.screen.get_width()
        self.screen_height = self.screen.get_height()
        image = pygame.image.load(im_path).convert_alpha()
        image = pygame.transform.scale(image, (char_width, char_height))
        self.image = image
        self.platforms = platforms
        self.platform_touched = None
        self.pos = [0, self.screen_height-1-char_height]
        print(self.pos)
        self.move_right = False
        self.move_left = False
        self.sprint = False
        self.jump = False
        self.jump2 = False
        self.jump_button = False #True iff jump bitton is currently pressed
        self.descent = False
        self.y0 = self.pos[1]
        self.v0 = 0
        self.width = char_width
        self.height = char_height
        #self.check_plateform()

    def render(self):
        x = int(self.pos[0])
        y = int(self.pos[1])
        #print(x)
        #print(y)
        self.screen.blit(self.image, (x,y))

    def check_plateforms(self):
        for i,p in enumerate(self.platforms):
            b = self.check_platfrm(p)
            if self.pos[1] >= p.mobile_position[1] - self.height and b and self.descent:
                self.platform_touched = i
                return True
        return False

    def check_platfrm(self, p):
        min_p = p.mobile_position[0]
        max_p = p.mobile_position[0]+p.length
        return min_p-self.width < self.pos[0] < max_p


    def move(self):
        delta = hor_speed if not self.sprint else hor_speed_sprint
        if self.move_right and self.pos[0] < self.screen_width - self.width:
            self.pos[0] = self.pos[0] + delta
        if self.move_left and self.pos[0] > 0:
            self.pos[0] = self.pos[0] - delta
        #b = self.check_plateform()

        #print('delta_y', delta_y)
        #print(self.jump)
        if self.jump or self.jump2:
            delta_y = G * (time() - t0_jump)
            if self.jump:
                delta_y -= self.jump_initial_speed()
            if delta_y > 0:
                self.descent = True
            self.pos[1] += delta_y
            b = self.check_plateforms()

            if b:
                print('cc')
                self.jump = False
                self.jump2 = False
            if self.pos[1] >= self.screen_height:
                self.jump = False
                self.pos[1] = self.screen_height-self.height
                self.jump2 = False
        if self.platform_touched is not None:
            if not self.check_platfrm(self.platforms[self.platform_touched]):
                self.platform_touched = None
                self.start_jump2()

    def start_jump(self):
        #print('salut')
        if not self.jump and not self.jump_button and not self.jump2:
            print('salut')
            global t0_jump
            t0_jump = time()
            self.descent = False
            self.jump = True
            self.jump_button = True
            self.y0 = self.pos[1]

    def start_jump2(self):
        global t0_jump
        t0_jump = time()
        self.descent = True
        self.jump2 = True


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



