import pygame


def display_text(screen, message, size=32, location=(100,100)):
    green = (0, 255, 0)
    blue = (0, 0, 128)
    font = pygame.font.Font('freesansbold.ttf', size)
    text = font.render(message, True, green, blue)
    textRect = text.get_rect()
    textRect.center = location
    screen.blit(text, textRect)