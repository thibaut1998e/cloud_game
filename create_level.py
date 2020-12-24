
from pygame import locals as const
from character import *
from arrival import *
import pygame as pg





class LevelDesigner:
    def __init__(self, window_height, window_width, char_height=40, char_width=40):
        self.screen = pg.display.set_mode((window_width, window_height))
        self.walls = []
        self.character = Character(self.screen, char_height=char_height, char_width=char_width)
        self.arrival = Arrival((window_width-100, window_height//2), self.screen)
        self.objects_to_display = [self.character, *self.walls, self.arrival]
        self.continuer = True
        self.character_selected = False
        self.arrival_selected = False

    def process_event(self, event):
        if event.type == const.QUIT:
            self.continuer = False
        if event.type == pg.MOUSEMOTION:
            if self.character_selected:
                self.character.pos = event.pos
            if self.arrival_selected:
                self.arrival.location = event.pos
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.pos == self.character.pos:
                self.character_selected = True
            if event.pos == self.arrival.location:
                self.arrival_selected = True

        if event.type == pg.MOUSEBUTTONUP:
            self.character_selected = False
            self.arrival_selected = False




    def update_screen(self):
        pygame.draw.rect(self.screen, (255, 255, 255), (0, 0) + self.screen.get_size())  # on dessine le fond
        self.arrival.render()
        for o in self.objects_to_display:
            o.render()


    def start(self):
        print('avant', self.character.pos)
        print(self.arrival.location)
        while self.continuer:
            for event in pg.event.get():
                self.process_event(event)
            self.update_screen()
            pygame.display.flip()
        print('après', self.character.pos)
        print(self.arrival.location)









def save_values(txt_path):
    pass


def create_level(txt_path, window_height=500, window_width=1000):
    #ask_objects_location_to_user(window_height, window_width)
    save_values(txt_path)





#create_level('')

level_designr = LevelDesigner(500, 1000)
level_designr.start()