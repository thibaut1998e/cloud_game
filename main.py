import pygame
from pygame import locals as const
from game import Game


def main(window_height=500, window_width=1000):
    print("Appuyez sur n'importe quelle touche pour lancer la partie !")

    pygame.init()

    ecran = pygame.display.set_mode((window_width, window_height))
    fond = pygame.image.load("Chevalerie_7_dauphins_la_nuit.jpg").convert_alpha()
    fond = pygame.transform.scale(fond, (window_width, window_height))
    continuer = True
    jeu = Game(ecran)  # Game() est une class qui va se charger ... du jeu :)

    while continuer:
        for event in pygame.event.get():
            if event.type == const.QUIT or (event.type == const.KEYDOWN and event.key == const.K_ESCAPE):
                # de manière à pouvoir quitter le menu avec echap ou la croix
                continuer = 0
            if event.type == const.KEYDOWN:
                # start() sera une méthode de la class Game(), et s'occupera de lancer le jeu
                #print('cc')
                jeu.start()

        ecran.blit(fond, (0, 0))
        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    main()