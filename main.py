import pygame
from pygame.locals import *
from window_builder import WindowBuilder
from window_modifier import WindowModifier
from gameoflife import GameOfLife
import time

def main():
    # Initialisation de pygame
    pygame.init()

    # Creation d'un window builder
    builder = WindowBuilder(1000)
    builder.makeWindow()
    builder.createGrid()

    # Creation d'un modifier
    modifier = WindowModifier(builder.fenetre, builder.rect_width, builder.rect_height, builder.margin)

    # Controleur de la boucle
    continuer = True
    gameOn = False

    while continuer:
        for event in pygame.event.get():
            if event.type == QUIT:
                continuer = False
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                modifier.modifyColors(event.pos[0], event.pos[1])
            if event.type == KEYDOWN and event.key == K_SPACE:
                game = GameOfLife(modifier)
                gameOn = not gameOn
        if gameOn:
            game.nextGen()
            modifier.colors = game.colors
            time.sleep(0.3)
        modifier.redrawGrid()
    
main()