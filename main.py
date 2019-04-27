import pygame
from pygame.locals import *
from window_builder import WindowBuilder

# Initialisation de pygame
pygame.init()

builder = WindowBuilder()
builder.makeWindow(640, 400)

# Controle de la boucle
continuer = True

while continuer:
    pass