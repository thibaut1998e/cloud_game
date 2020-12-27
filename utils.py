import pygame as pg
from constantes import *
import pickle
import os
from pygame import locals as const


def display_text(screen, message, size=32, location=(100,100)):
    font = pg.font.Font('freesansbold.ttf', size)
    text = font.render(message, True, green, blue)
    textRect = text.get_rect()
    textRect.center = location
    screen.blit(text, textRect)
    return textRect


def draw_squared_ring(screeen, pos, height, width):
    pg.draw.rect(screeen, red, (pos[0], pos[1], width, 3))
    pg.draw.rect(screeen, red, (pos[0], pos[1], 3, height))
    pg.draw.rect(screeen, red, (pos[0]+width, pos[1], 3, height))
    pg.draw.rect(screeen, red, (pos[0], pos[1]+height, width+3, 3))


def load_image(im_path, colorkey=None):
    try:
        image = pg.image.load(im_path)
    except:
        print("Impossible de charger l'image :", im_path)
        raise ValueError
    image = image.convert()
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, const.RLEACCEL)
    return image




"""
class Test():
    def __init__(self, a=3):
        self.a = a
        self.b = 7
        self.oiseau = 12

o = Test()
print('name', str(type(o)))
print(getattr(o, 'oiseau'))
setattr(o, 'b', 4)
print(o.b)
with open('test_save_object', 'wb') as f:
    pickle.dump(o, f)
with open('test_save_object', 'rb') as f:
    o2 = pickle.load(f)
print(o2.oiseau)
a = o.__class__(a=2)
print(a.a)
print(o.__class__.__name__)

print(type(Test.__name__.__str__()))

c = Test
b = c(1)
"""


