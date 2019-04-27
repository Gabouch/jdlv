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
        pass

main()