from itertools import product
from window_modifier import WindowModifier
import copy

class GameOfLife():

    def __init__(self, modifier):
        self.colors = modifier.colors
        self.nbRows = len(self.colors)
        self.nbCol = len(self.colors[0])
        self.size = self.nbCol

    def nextGen(self):
        nextColors = copy.deepcopy(self.colors)
        for i, j in product(range(self.nbCol), range(self.nbRows)):
            if self.colors[j][i]:
                # Si la cellule est vivante
                c = 0
                for n in self.getNeighbours((i,j)):
                    if self.colors[n[1]][n[0]]:
                        c += 1
                if not (c == 2 or c == 3) : 
                    nextColors[j][i] = False
            else:
                # Si la cellule est morte
                d = 0
                for n in self.getNeighbours((i,j)):
                    if self.colors[n[1]][n[0]]:
                        d += 1
                if d == 3: 
                    nextColors[j][i] = True
        self.colors = copy.deepcopy(nextColors)

    def getNeighbours(self, pos):
        for c in product(*(range(n-1, n+2) for n in pos)):
            if c != pos and all(0 <= n < self.size for n in c):
                yield c
