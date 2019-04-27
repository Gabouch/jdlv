import pygame
from pygame.locals import *


class WindowBuilder():
    __white = pygame.Color(255,255,255)

    def __init__(self):
        pass
    # Creation de la fenetre
    def makeWindow(self, width, height):
        fenetre = pygame.display.set_mode((width, height), RESIZABLE)
        fenetre.fill(self.__white)
        pygame.display.update()

    def createGrid:
        pass
