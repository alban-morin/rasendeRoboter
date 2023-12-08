import pygame
from plateau import *
import numpy as np
from robot import * 
# Définir les couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)  # Couleur rouge pour les murs
ROUGE = (255, 0, 0)
VERT = (0, 255, 0)
BLEU = (0, 0, 255)
JAUNE = (255, 255, 0)

# Liste des couleurs
couleurs_cibles = [ROUGE, VERT, BLEU, JAUNE]
# Initialiser Pygame
pygame.init()

# Définir les dimensions de la fenêtre
largeur, hauteur = 800, 800

# Créer la fenêtre
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Plateau de jeu")

# Charger les image et redimensionner
robotbleu_image = pygame.image.load("D:\\REMI\\COURS\\UTBM\\INFO\\IA41\\PROJET\\rasendeRoboter\\img\\robotbleu.JPG")
robotjaune_image = pygame.image.load("D:\\REMI\\COURS\\UTBM\\INFO\\IA41\\PROJET\\rasendeRoboter\\img\\robotjaune.JPG")
robot_largeur = int(largeur // 16 * 0.9)
robot_hauteur = int(hauteur // 16 * 0.9)
robotbleu_image = pygame.transform.scale(robotbleu_image, (robot_largeur,robot_hauteur))
robotjaune_image = pygame.transform.scale(robotjaune_image, (robot_largeur,robot_hauteur))

# Définir la position initiale de l'objet
objet_rect = robotbleu_image.get_rect(topleft=(0, 0))

# Définir la taille de chaque case
taille_case = largeur // 16

# choix de la couleur cible
cible =  random.choice(couleurs_cibles)

count = 0 


# Fonction pour dessiner le plateau
def dessiner_plateau(plateau, robot):
    fenetre.fill(BLANC)  # Fond blanc
    pygame.draw.rect(fenetre, NOIR, (0, 0, largeur, hauteur), 4)

    # Dessiner les lignes de séparation entre les cases
    for i in range(1, 16):
        pygame.draw.line(fenetre, NOIR, (i * taille_case, 0), (i * taille_case, hauteur))
        pygame.draw.line(fenetre, NOIR, (0, i * taille_case), (largeur, i * taille_case))
    
    # Dessiner les murs
    for i in range(16):
        for j in range(16):
            case = plateau.cases[i][j]
            x, y = j * taille_case, i * taille_case
            # Dessiner les cibles
            for cible_pos, couleur_cible in liste_cible_position_couleur:
                if (i, j) == cible_pos:
                    pygame.draw.rect(fenetre, couleur_cible, (x, y, taille_case, taille_case))

            if (i, j) in [(7, 7), (7, 8), (8, 7), (8, 8)]:
                pygame.draw.rect(fenetre, cible, (x, y, taille_case, taille_case))
            if case.top:
                pygame.draw.line(fenetre, NOIR, (x, y), (x + taille_case, y), 4)
            if case.bottom:
                pygame.draw.line(fenetre, NOIR, (x, y + taille_case), (x + taille_case, y + taille_case), 4)
            if case.left:
                pygame.draw.line(fenetre, NOIR, (x, y), (x, y + taille_case), 4)
            if case.right:
                pygame.draw.line(fenetre, NOIR, (x + taille_case, y), (x + taille_case, y + taille_case), 4)

    fenetre.blit(robotbleu_image, robot.position.topleft)
    fenetre.blit(robotjaune_image, robotjaune.position.topleft)
    pygame.display.flip()

"""la classe robot est dans un autre fichier à présent cela cause un probleme avec le conteur qu'il faudra regler"""


# class Robot:
#     def __init__(self, position):
#         """
#         Initialisateur de la classe Robot.

#         Args:
#             position (tuple): Position initiale du robot (i, j).
#             nombre_de_coups (int): Nombre de coups du robot.
#         """
#         self.position = pygame.Rect(position[1] * taille_case, position[0] * taille_case, robot_largeur, robot_hauteur)
    


#     def deplacer(self, direction, plateau):
#         """
#         Déplace le robot dans la direction spécifiée.

#         Args:
#             direction (str): Direction du déplacement ('gauche', 'droite', 'haut', 'bas').
#             plateau (Plateau): Instance de la classe Plateau.
#         """
#         i, j = self.position.y // taille_case, self.position.x // taille_case
#         global count
#         while True:
#             if direction == 'gauche' and j > 0 and not plateau.cases[i][j].left and plateau.cases[i][j-1].type !=1:
#                 plateau.cases[i][j].type = 0 if plateau.cases[i][j].type != 0 else plateau.cases[i][j].type
#                 self.position.x -= taille_case
#             elif direction == 'droite' and j < 15 and not plateau.cases[i][j].right and plateau.cases[i][j+1].type !=1:
#                 plateau.cases[i][j].type = 0 if plateau.cases[i][j].type != 0 else plateau.cases[i][j].type
#                 self.position.x += taille_case
#             elif direction == 'haut' and i > 0 and not plateau.cases[i][j].top and plateau.cases[i-1][j].type !=1 :
#                 plateau.cases[i][j].type = 0 if plateau.cases[i][j].type != 0 else plateau.cases[i][j].type
#                 self.position.y -= taille_case
#             elif direction == 'bas' and i < 15 and not plateau.cases[i][j].bottom and plateau.cases[i+1][j].type !=1 :
#                 plateau.cases[i][j].type = 0 if plateau.cases[i][j].type != 0 else plateau.cases[i][j].type
#                 self.position.y += taille_case
#             elif plateau.cases[i][j].type == 2:
#                 print("Victoire !")
 
#                 break
#             else:
#                 break  # Arrêter si un mur est rencontré

#             i, j = self.position.y // taille_case, self.position.x // taille_case
#         plateau.cases[i][j].type = 1
#         count += 1
#         print(f"Position du robot dans le tableau : ({i}, {j})")


#     def est_clique(self, mouse_x, mouse_y):
#         return self.position.collidepoint(mouse_x, mouse_y)







# Créer un plateau
plateau = Plateau()
# Créer une liste de cibles avec leur position et leur couleur
def def_cible(plateau):
    liste_cible_position_couleur = []
    for i in range(16):
        for j in range(16):
            case = plateau.cases[i][j]
            x, y = j * taille_case, i * taille_case
            if case.top and case.right or case.top and case.left or case.bottom and case.right or case.bottom and case.left:
                couleur_case_cible = random.choice(couleurs_cibles)
                liste_cible_position_couleur.append(((i,j),couleur_case_cible))
                if couleur_case_cible == cible:
                    case.type = 2

    return liste_cible_position_couleur

liste_cible_position_couleur = def_cible(plateau)

def pressed_key_robot(robot , keys):
    if keys[pygame.K_LEFT]:
        robot.deplacer('gauche', plateau)
    elif keys[pygame.K_RIGHT]:
        robot.deplacer('droite', plateau)
    elif keys[pygame.K_UP]:
        robot.deplacer('haut', plateau)
    elif keys[pygame.K_DOWN]:
        robot.deplacer('bas', plateau)

# Créer un robot
robotbleu = Robot(position=(0, 0))
robotjaune = Robot(position=(15, 15))

liste_robot = [robotbleu, robotjaune]

# Boucle principale
clock = pygame.time.Clock()
running = True

robot_selectionne = None
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_x, mouse_y = event.pos
            # Vérifier quel robot a été cliqué
            for robot in liste_robot:
                if robot.est_clique(mouse_x, mouse_y):
                    robot_selectionne = robot

    # Gérer les déplacements du robot
    keys = pygame.key.get_pressed()
    
    if robot_selectionne:
        pressed_key_robot(robot_selectionne, keys)
    
       


   
    dessiner_plateau(plateau, robotbleu)
    clock.tick(10) 
# Quitter Pygame
pygame.quit()

