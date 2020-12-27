import pygame
from pygame import locals as const
from character import *
from constantes import *
from wall import *
from arrival import *




class Game:
    def __init__(self, window_height, window_width, image_path=None, wall_color=black):
        screen = pg.display.set_mode((window_width, window_height))
        self.screen = screen
        self.height = self.screen.get_height()
        self.width = self.screen.get_width()
        self.continuer = True
        self.objects = []
        self.id_cpt = 0
        self.image = None
        self.wall_color = wall_color
        self.has_started = False
        if image_path is not None:
            image = load_image(image_path)
            self.image = pg.transform.scale(image, (self.width, self.height))

    def attributes_to_save(self):
        return ['height', 'width']

    def get_character(self):
        return self.objects[0]

    def prepare(self):
        pygame.key.set_repeat(200, 50)
        self.has_started = False
        self.continuer = True
        for o in self.objects:
            o.reset()

    def add_object(self, *objects):
        if len(self.objects) == 0 and not isinstance(objects[0], Character):
            print('the first object of the game object list must be a Character')
            raise ValueError
        for o in objects:
            o.ID = self.id_cpt
            self.id_cpt += 1
            self.objects.append(o)

    def suppress_object(self, object):
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
        if self.image is None:
            pygame.draw.rect(self.screen, white, (0, 0) + self.screen.get_size())  # on dessine le fond
        else:
            self.screen.blit(self.image, (0, 0))
        #self.character.render()
        for o in self.objects:
            message = o.interact()
            o.display(color=self.wall_color)
            if not self.continuer:
                return message
        return ''

    def process_event(self, event: pygame.event):
        for o in self.objects:
            o.process_event(event)
        if event.type == const.QUIT:
            self.continuer = False

    def start(self):
        message = ''
        self.prepare()
        while self.continuer:
            for event in pygame.event.get():
                self.process_event(event)

            message = self.interact_and_display()
            pygame.display.flip()
        for o in self.objects:
            if isinstance(o, Button):
                self.suppress_object(o)

        return message




