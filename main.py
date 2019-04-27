import pygame
from pygame.locals import *
from window_builder import WindowBuilder

def main():
    # Initialisation de pygame
    pygame.init()

    # Creation d'un window builder
    builder = WindowBuilder(640, 400)
    builder.makeWindow()
    builder.createGrid()

    # Controle de la boucle
    continuer = True

    while continuer:
        for event in pygame.event.get():
            if event.type == QUIT:
                continuer = False
            if event.type == KEYDOWN and (event.key == K_ESCAPE or K_BACKSPACE):
                continuer = False
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                pass

main()