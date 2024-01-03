from plateau import *
import pygame
from time import sleep
robot_largeur = int(largeur // 16 * 0.9)
robot_hauteur = int(hauteur // 16 * 0.9)
class Robot:
    def __init__(self, position,nom):
        """
        Initialisateur de la classe Robot.

        Args:
            position (tuple): Position initiale du robot (i, j).
            nombre_de_coups (int): Nombre de coups du robot.
        """
        self.position = pygame.Rect(position[1] * taille_case, position[0] * taille_case, robot_largeur, robot_hauteur)
        self.nom = nom


    def deplacer(self, direction, plateau,target):
        """
        Déplace le robot dans la direction spécifiée.

        Args:
            direction (str): Direction du déplacement ('gauche', 'droite', 'haut', 'bas').
            plateau (Plateau): Instance de la classe Plateau.
        """
        #convertir en positions d'affichage
        i, j = self.position.y // taille_case, self.position.x // taille_case
  
        while True:
            if direction == 'gauche' and j > 0 and not plateau.cases[i][j].left and plateau.cases[i][j-1].type !=1:
                plateau.cases[i][j].type = 0 if plateau.cases[i][j].type != 0 else plateau.cases[i][j].type
                self.position.x -= taille_case
            elif direction == 'droite' and j < 15 and not plateau.cases[i][j].right and plateau.cases[i][j+1].type !=1:
                plateau.cases[i][j].type = 0 if plateau.cases[i][j].type != 0 else plateau.cases[i][j].type
                self.position.x += taille_case
            elif direction == 'haut' and i > 0 and not plateau.cases[i][j].top and plateau.cases[i-1][j].type !=1 :
                plateau.cases[i][j].type = 0 if plateau.cases[i][j].type != 0 else plateau.cases[i][j].type
                self.position.y -= taille_case
            elif direction == 'bas' and i < 15 and not plateau.cases[i][j].bottom and plateau.cases[i+1][j].type !=1 :
                plateau.cases[i][j].type = 0 if plateau.cases[i][j].type != 0 else plateau.cases[i][j].type
                self.position.y += taille_case
            elif plateau.cases[i][j].type == 2 and self.nom == target.couleur:
                i,j = self.coordonnee_plateau()
                # print(f"Position du robot dans le tableau : ({i}, {j})")
                print("Victoire !")
                sleep(5)
                # for i in range(15):
                #     print("")
               
                return
            else:
                break  # Arrêter si un mur est rencontré

            #reconvertir la position pixel en position back puis update le plateau
            i, j = self.position.y // taille_case, self.position.x // taille_case
        if plateau.cases[i][j].type != 2:
            plateau.cases[i][j].type = 1 
        
        # print(f"Position du robot dans le tableau : ({i}, {j})")
        # print(f"type de la case : {plateau.cases[i][j].type}")
        # print(f"nom du robot : {self.nom}")
        # print(f"maintarget : {target.couleur} {plateau.cases[target.posX][target.posY].type} {target.posX} {target.posY} ")

    #convertir en positions d'affichage
    def coordonnee_plateau(self):
        i, j = self.position.y // taille_case, self.position.x // taille_case
        return i,j

    def est_clique(self, mouse_x, mouse_y):
        return self.position.collidepoint(mouse_x, mouse_y)

