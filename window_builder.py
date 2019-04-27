import pygame
from pygame.locals import *

class WindowBuilder():
    __white = pygame.Color(255,255,255)
    __black = pygame.Color(0,0,0)
    margin = 0
    rect_width = 10
    rect_height = 10

    def __init__(self, size):
        self.width = size
        self.height = size

    # Creation de la fenetre
    def makeWindow(self):
        fenetre = pygame.display.set_mode((self.width, self.height)) #, RESIZABLE)
        fenetre.fill(self.__white)
        pygame.display.update()
        self.fenetre = fenetre

    def createGrid(self):
        for i in range(0, self.width, self.rect_width):
            for j in range(0, self.height, self.rect_height):
                rect = pygame.Rect((i, j), (self.rect_width,self.rect_height))
                pygame.draw.rect(self.fenetre, self.__black, rect, self.margin)
        pygame.display.update()


