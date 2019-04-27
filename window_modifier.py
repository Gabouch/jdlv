import pygame
from pygame.locals import *


class WindowModifier():
    __white = pygame.Color(255, 255, 255)
    __black = pygame.Color(0, 0, 0)

    def __init__(self, fenetre, rect_widht, rect_height, rect_margin):
        self.fenetre = fenetre
        self.rect_width = rect_widht
        self.rect_height = rect_height
        self.display_width = fenetre.get_width()
        self.display_height = fenetre.get_height()
        self.margin = rect_margin
        self.__colors = [[0 for x in range(self.display_width // self.rect_width)]
                         for y in range(self.fenetre.get_height() // self.rect_height)]

    def modifyColors(self):
        pass

    def redrawGrid(self):
        for i in range(0, self.display_width, self.rect_width):
            for j in range(0, self.display_height, self.rect_height):
                color = self.__colors[self.rect_width // self.display_width
                                      ][self.rect_height // self.display_height]
                rect = pygame.Rect((i, j), (self.rect_width, self.rect_height))
                pygame.draw.rect(
                    self.fenetre, self.__white if color == 0 else self.__black, rect, self.margin)
        pygame.display.update()
