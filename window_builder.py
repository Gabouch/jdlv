import pygame
from pygame.locals import *


class WindowBuilder():
    __white = pygame.Color(255,255,255)
    __black = pygame.Color(0,0,0)
    __margin = 1
    __rect_width = 20
    __rect_height = 20

    def __init__(self, width, height):
        self.width = width
        self.height = height
    # Creation de la fenetre
    def makeWindow(self):
        fenetre = pygame.display.set_mode((self.width, self.height), RESIZABLE)
        fenetre.fill(self.__white)
        pygame.display.update()
        self.fenetre = fenetre

    def createGrid(self):
        for i in range(0, self.width, self.__rect_width):
            for j in range(0, self.height, self.__rect_height):
                rect = pygame.Rect((i, j), (self.__rect_width,self.__rect_height))
                pygame.draw.rect (self.fenetre, self.__black, rect, self.__margin)
        pygame.display.update()
