import pygame
from pygame import locals as const
from character import *
from constantes import *
from Plateforme import *
from arrival import *


class Game:
    def __init__(self, screen, walls, arrival_location):
        self.screen = screen
        self.continuer = True
        self.controles = {
            UP: const.K_SPACE,
            DOWN: const.K_DOWN,
            RIGHT : const.K_RIGHT,
            LEFT : const.K_LEFT,
            SPRINT:const.K_s
        }
        self.character = Character(self.screen)
        self.walls = walls
        self.arrival = Arrival(arrival_location, screen)
        self.object_to_display = [*self.walls,  self.arrival]

    def prepare(self):
        pygame.key.set_repeat(200, 50)
        self.continuer = True
        self.character = Character(self.screen)

    def update_screen(self):
        pygame.draw.rect(self.screen, (255, 255, 255), (0, 0) + self.screen.get_size())  # on dessine le fond
        self.character.render()
        for o in self.object_to_display:
            o.render()


    def process_event(self, event: pygame.event):
        if event.type == const.KEYDOWN:
            if event.key == self.controles[RIGHT]:
                self.character.move_right = True
            if event.key == self.controles[LEFT]:
                self.character.move_left = True
            if event.key == self.controles[UP]:
                self.character.start_jump()
            if event.key == self.controles[SPRINT]:
                self.character.sprint = True

        if event.type == const.KEYUP:
            if event.key == self.controles[RIGHT]:
                self.character.move_right = False
            if event.key == self.controles[LEFT]:
                self.character.move_left = False
            if event.key == self.controles[SPRINT]:
                self.character.sprint = False
            if event.key == self.controles[UP]:
                self.character.drop_jump_button()

        if event.type == const.QUIT:
            self.continuer = False

    def test_outside_screen(self):
        return self.character.pos[0] < -self.character.width or self.character.pos[0] > self.screen.get_width() \
               or self.character.pos[1] < -self.character.height or self.character.pos[1] > self.screen.get_height()

    def test_game_over(self):
        for w in self.walls:
            if w.collide_with_me(self.character):
                self.continuer = False
                return messages[0]
        if self.test_outside_screen():
            self.continuer = False
            return messages[1]
        if self.arrival.test_end_game(self.character):
            self.continuer = False
            return messages[2]
        return ''

    def start(self):
        self.prepare()
        message = ''
        while self.continuer:
            for event in pygame.event.get():
                self.process_event(event)

            self.character.move()
            self.update_screen()
            pygame.display.flip()
            message = self.test_game_over()
        return message
