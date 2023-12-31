import numpy as np
from case import*
import random

largeur, hauteur = 800, 800
taille_case = largeur // 16

class Plateau:
    def __init__(self):
        self.cases = np.zeros((16, 16), dtype=Case)  # Crée une matrice de cases

        # On remplit toutes les cases de la matrice avec des objets Case
        for i in range(16):
            for j in range(16):
                self.cases[i][j] = Case(posx=i, posy=j, type=0)

        for i in range(16):
            self.update_walls(i, 0, 'left')
            self.update_walls(0, i, 'top')
            self.update_walls(i, 15, 'right')
            self.update_walls(15, i, 'bottom')
        
        self.update_walls(7,7,'top')
        self.update_walls(7,7,'left')
        self.update_walls(8,7,'left')
        self.update_walls(8,7,'bottom')
        self.update_walls(8,8,'bottom')
        self.update_walls(8,8,'right')
        self.update_walls(7,8,'right')
        self.update_walls(7,8,'top')
            # Add walls on the sides


        # Murs extérieurs
        self.update_walls(0, 3, 'right')

        self.update_walls(0, 9, 'right')


        self.update_walls(15, 4, 'right')

        self.update_walls(15, 11, 'right')

        self.update_walls(4, 0, 'bottom')

        self.update_walls(10, 0, 'bottom')


        self.update_walls(1, 15, 'bottom')

        self.update_walls(11, 15, 'bottom')


        # Murs angles internes
        self.update_walls(4, 2, 'right')
        self.update_walls(4, 2, 'top')
        self.update_walls(2, 5, 'right')
        self.update_walls(2, 5, 'bottom')
        self.update_walls(3, 9, 'left')
        self.update_walls(3, 9, 'top')
        self.update_walls(1, 13, 'right')
        self.update_walls(1, 13, 'bottom')
        self.update_walls(4, 14, 'right')
        self.update_walls(4, 14, 'top')
        self.update_walls(5, 7, 'left')
        self.update_walls(5, 7, 'bottom')
        self.update_walls(6, 1, 'left')
        self.update_walls(6, 1, 'top')
        self.update_walls(6, 12, 'left')
        self.update_walls(6, 12, 'bottom')
        self.update_walls(9, 4, 'left')
        self.update_walls(9, 4, 'bottom')
        self.update_walls(10, 6, 'left')
        self.update_walls(10, 6, 'top')
        self.update_walls(9, 13, 'left')
        self.update_walls(9, 13, 'bottom')
        self.update_walls(11, 9, 'right')
        self.update_walls(11, 9, 'bottom')
        self.update_walls(12, 7, 'right')
        self.update_walls(12, 7, 'bottom')
        self.update_walls(13, 1, 'right')
        self.update_walls(13, 1, 'top')
        self.update_walls(14, 3, 'right')
        self.update_walls(14, 3, 'bottom')
        self.update_walls(14, 10, 'left')
        self.update_walls(14, 10, 'top')
        self.update_walls(13, 14, 'right')
        self.update_walls(13, 14, 'top')

    def update_walls(self, i, j, direction):
        # Direction peut être 'left', 'right', 'top', ou 'bottom'
        
        if direction == 'left':
            if j > 0:
                self.cases[i][j].left = True
                self.cases[i][j - 1].right = True
        elif direction == 'right':
            if j < 15:
                self.cases[i][j].right = True
                self.cases[i][j + 1].left = True
        elif direction == 'top':
            if i > 0:
                self.cases[i][j].top = True
                self.cases[i - 1][j].bottom = True
        elif direction == 'bottom':
            if i < 15:
                self.cases[i][j].bottom = True
                self.cases[i + 1][j].top = True
        elif j == 15 and direction == 'right':
            self.cases[i][j].right = True
        elif j == 0 and direction == 'left':
            self.cases[i][j].left = True
        elif i == 0 and direction == 'top':
            self.cases[i][j].top = True
        elif i == 15 and direction == 'bottom':
            self.cases[i][j].bottom = True

    def afficher(self):
        for i in range(16):
            for j in range(16):
                print(self.cases[i][j].poid, end=' ')
            print()
        


    
