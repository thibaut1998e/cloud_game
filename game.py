import pygame
from pygame import locals as const
from character import *
from constantes import *
from Plateforme import *

class Game:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.continuer = True
        self.controles = {
            UP: const.K_UP,
            DOWN: const.K_DOWN,
            RIGHT : const.K_RIGHT,
            LEFT : const.K_LEFT,
            SPRINT:const.K_s
        }
        platform = Platform(screen, (300, 300), 200, 10)
        platform2 = Platform(screen, (400, 200), 200, 10)
        platform3 = Platform(screen, (200, 400), 200, 10)
        platform1 = Platform(screen, (0, screen.get_height()-1), screen.get_width(), 10)
        self.platforms = [platform, platform2, platform3]
        self.character = Character(self.screen, self.platforms)

    def prepare(self):
        pygame.key.set_repeat(200, 50)
        self.continuer = True
        self.character = Character(self.screen, self.platforms)

    def update_screen(self):
        pygame.draw.rect(self.screen, (255, 255, 255), (0, 0) + self.screen.get_size())  # on dessine le fond
        self.character.render()
        for i in range(len(self.platforms)):
            self.platforms[i].render()



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

    def start(self):
        self.prepare()

        while self.continuer:
            for event in pygame.event.get():
                self.process_event(event)

            self.character.move()
            self.update_screen()
            pygame.display.flip()