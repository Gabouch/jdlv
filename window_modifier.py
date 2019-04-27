import pygame
from pygame.locals import *
from math import floor

class WindowModifier():
    __white = pygame.Color(255, 255, 255)
    __black = pygame.Color(0, 0, 0)

    def __init__(self, fenetre, rect_width, rect_height, rect_margin):
        self.fenetre = fenetre
        self.rect_width = rect_width
        self.rect_height = rect_height
        self.display_width = fenetre.get_width()
        self.display_height = fenetre.get_height()
        self.margin = rect_margin
        self.__colors = [[False for x in range(self.display_width // self.rect_width)]
                         for y in range(self.display_height// self.rect_height)]

    def modifyColors(self, x, y):
        iX = floor(x / self.rect_width)
        jY = floor(y / self.rect_height)
        print(f"x : {x}, y : {y}")
        self.__colors[jY][iX] = not self.__colors[jY][iX]

    def redrawGrid(self):
        for i in range(0, self.display_width, self.rect_width):
            for j in range(0, self.display_height, self.rect_height):
                x = i // self.rect_width
                y = j // self.rect_height
                # print(str(x) +' ' +  str(y))
                color = self.__colors[y][x]
                rect = pygame.Rect((i, j), (self.rect_width, self.rect_height))
                pygame.draw.rect(
                    self.fenetre, self.__black if color else self.__white, rect, self.margin)
        pygame.display.update()
    
    def displayGrid(self):
        for i in range(len(self.__colors)):
            print(self.__colors[i])