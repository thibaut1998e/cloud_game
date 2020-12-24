import pygame
from pygame import locals as const
from game import Game
from Plateforme import Wall
from utils import *


def main(window_height=500, window_width=1000):
    print("Appuyez sur espace pour lancer la partie !")

    pygame.init()

    ecran = pygame.display.set_mode((window_width, window_height))
    #fond = pygame.image.load("Chevalerie_7_dauphins_la_nuit.jpg").convert_alpha()
    #fond = pygame.transform.scale(fond, (window_width, window_height))

    continuer = True
    wall = Wall(ecran, (ecran.get_width() // 2, 100), width=ecran.get_height() - 311, height=100, ampli_y=100, period_y=3)
    walls = [wall]
    jeu = Game(ecran, walls, (900, 200))
    pygame.display.set_caption('cloud game')

    #text, textRect = get_text('press space to continue')
    message = 'press space to continue'
    while continuer:
        for event in pygame.event.get():
            if event.type == const.QUIT or (event.type == const.KEYDOWN and event.key == const.K_ESCAPE):
                # de manière à pouvoir quitter le menu avec echap ou la croix
                continuer = 0
            if event.type == const.KEYDOWN and event.key==const.K_SPACE:
                #print('cc')
                message = jeu.start()


        #ecran.blit(fond, (0, 0))
        #ecran.blit(text, textRect)
        display_text(ecran, message, location=(window_width//2, window_height//2))
        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    main()