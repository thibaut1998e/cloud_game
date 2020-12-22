import os, sys
import pygame
from pygame.locals import *
import numpy as np
import random as rd


pygame.init()
window_width = 640
window_height = 480
rectangle_width = 300
rectangle_height = 200

ecran = pygame.display.set_mode((window_width, window_height))

continuer = True
image = pygame.image.load("Chevalerie_7_dauphins_la_nuit.jpg").convert()
pygame.display.set_icon(image)

class Rectange():
    def __init__(self, width, height, x, y, color=(180, 20, 150)):
        self.width = width
        self.height = height
        self.color = color
        self.x = x
        self.y = y

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    def move(self, direction, step_size=10):
        if direction == 'U':
            self.y -= step_size
        if direction == 'D':
            self.y += step_size
        if direction == 'R':
            self.x += step_size
        if direction == 'L':
            self.x -= step_size

rectangle = Rectange(rectangle_width, rectangle_height, 0, 0)
i = 0
while continuer:
    rectangle.draw(ecran)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                continuer = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                rectangle.move('D')
            if event.key == pygame.K_UP:
                rectangle.move('U')
            if event.key == pygame.K_LEFT:
                rectangle.move('L')
            if event.key == pygame.K_RIGHT:
                rectangle.move('R')
            pygame.draw.rect(ecran, (0, 0, 0), (0, 0, window_width, window_height))
            rectangle.draw(ecran)

    pygame.display.flip()

pygame.quit()








