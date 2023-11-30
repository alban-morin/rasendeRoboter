import pygame
from plateau import *
import numpy as np

# Définir les couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)  # Couleur rouge pour les murs

# Initialiser Pygame
pygame.init()

# Définir les dimensions de la fenêtre
largeur, hauteur = 800, 800

# Créer la fenêtre
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Plateau de jeu")

# Charger l'image de l'objet et redimensionner
objet_image = pygame.image.load("D:\\REMI\\COURS\\UTBM\\INFO\\IA41\\PROJET\\rasendeRoboter\\img\\robotbleu.JPG")
object_largeur = int(largeur // 16 * 0.9)
object_hauteur = int(hauteur // 16 * 0.9)
objet_image = pygame.transform.scale(objet_image, (object_largeur, object_hauteur))

# Définir la position initiale de l'objet
objet_rect = objet_image.get_rect(topleft=(0, 0))

# Définir la taille de chaque case
taille_case = largeur // 16

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

            if case.top:
                pygame.draw.line(fenetre, NOIR, (x, y), (x + taille_case, y), 4)
            if case.bottom:
                pygame.draw.line(fenetre, NOIR, (x, y + taille_case), (x + taille_case, y + taille_case), 4)
            if case.left:
                pygame.draw.line(fenetre, NOIR, (x, y), (x, y + taille_case), 4)
            if case.right:
                pygame.draw.line(fenetre, NOIR, (x + taille_case, y), (x + taille_case, y + taille_case), 4)

    fenetre.blit(objet_image, robot.position.topleft)
    pygame.display.flip()

class Robot:
    def __init__(self, position, nombre_de_coups):
        """
        Initialisateur de la classe Robot.

        Args:
            position (tuple): Position initiale du robot (i, j).
            nombre_de_coups (int): Nombre de coups du robot.
        """
        self.position = pygame.Rect(position[1] * taille_case, position[0] * taille_case, object_largeur, object_hauteur)
        self.nombre_de_coups = nombre_de_coups

    def deplacer(self, direction, plateau):
        """
        Déplace le robot dans la direction spécifiée.

        Args:
            direction (str): Direction du déplacement ('gauche', 'droite', 'haut', 'bas').
            plateau (Plateau): Instance de la classe Plateau.
        """
        i, j = self.position.y // taille_case, self.position.x // taille_case

        if direction == 'gauche' and j > 0 and not plateau.cases[i][j].left:
            self.position.x -= taille_case
        elif direction == 'droite' and j < 15 and not plateau.cases[i][j].right:
            self.position.x += taille_case
        elif direction == 'haut' and i > 0 and not plateau.cases[i][j].top:
            self.position.y -= taille_case
        elif direction == 'bas' and i < 15 and not plateau.cases[i][j].bottom:
            self.position.y += taille_case
        print(f"Position du robot dans le tableau : ({i}, {j})")
# Créer un plateau
plateau = Plateau()

# Créer un robot
robot = Robot(position=(0, 0), nombre_de_coups=0)

# Boucle principale
clock = pygame.time.Clock()
running = True
count = 0
while running:
    count += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Gérer les déplacements du robot
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        robot.deplacer('gauche', plateau)
    elif keys[pygame.K_RIGHT]:
        robot.deplacer('droite', plateau)
    elif keys[pygame.K_UP]:
        robot.deplacer('haut', plateau)
    elif keys[pygame.K_DOWN]:
        robot.deplacer('bas', plateau)

    dessiner_plateau(plateau, robot)
    clock.tick(10) 
# Quitter Pygame
pygame.quit()