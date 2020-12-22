import os, sys
import pygame
from pygame.locals import *
import numpy as np
import random as rd


pygame.init()
window_width = 640
window_height = 480
#image_width = 100
#image_height = 100

ecran = pygame.display.set_mode((window_width, window_height))

continuer = True
image = pygame.image.load("Chevalerie_7_dauphins_la_nuit.jpg").convert()
pygame.display.set_icon(image)

pos = (0, 0)

while continuer:
    pygame.draw.rect(ecran, (0, 0, 0), (0, 0, window_width, window_height))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                continuer = False

        if event.type == pygame.MOUSEMOTION:
            pos = event.pos
    ecran.blit(image, pos)
    pygame.display.flip()


pygame.quit()