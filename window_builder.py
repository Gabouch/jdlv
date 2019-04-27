import pygame
from pygame.locals import *

class WindowBuilder():
    def __init__(self):
        pass
    # Creation de la fenetre
    def makeWindow(self):
        fenetre = pygame.display.set_mode((640, 400), RESIZABLE)