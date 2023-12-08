# Importez les modules nécessaires
import pygame
from plateau import * 
from robot import *
import random
import numpy as np
from ai import *
import os
# Définissez les constantes de couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
ROUGE = (255, 0, 0)
VERT = (0, 255, 0)
BLEU = (0, 0, 255)
JAUNE = (255, 255, 0)

# Liste des couleurs
couleurs_cibles = [ROUGE, VERT, BLEU, JAUNE]

class Game:
    def __init__(self):
        # Initialisation de Pygame
        pygame.init()

        
        # Définir les dimensions de la fenêtre
        self.largeur, self.hauteur = 800, 800

        # Créer la fenêtre
        self.fenetre = pygame.display.set_mode((self.largeur, self.hauteur))
        pygame.display.set_caption("Plateau de jeu")

        # Initialiser le plateau
        self.plateau = Plateau()

        # Initialiser les robots
        self.robot_bleu = Robot(position=(0, 0), nom="Bleu")
        self.robot_jaune = Robot(position=(15, 15), nom="Jaune")

        # Liste des robots
        self.liste_robots = [self.robot_bleu, self.robot_jaune]

        # Charger les images et redimensionner
        script_dir = os.path.dirname(os.path.realpath(__file__))
        self.robot_bleu_image = pygame.image.load(os.path.join(script_dir, 'img', 'robotbleu.JPG'))
        self.robot_jaune_image = pygame.image.load(os.path.join(script_dir, 'img', 'robotjaune.JPG'))
        self.robot_largeur = int(self.largeur // 16 * 0.9)
        self.robot_hauteur = int(self.hauteur // 16 * 0.9)
        self.robot_bleu_image = pygame.transform.scale(self.robot_bleu_image, (self.robot_largeur, self.robot_hauteur))
        self.robot_jaune_image = pygame.transform.scale(self.robot_jaune_image, (self.robot_largeur, self.robot_hauteur))

        # Définir la taille de chaque case
        self.taille_case = self.largeur // 16

        # Choix de la couleur cible
        self.cible = random.choice(couleurs_cibles)

        # Compteur de coups
        self.count = 0

        self.ai = ai(self.liste_robots,self.plateau,self.count)
    def dessiner_plateau(self):
        self.fenetre.fill(BLANC)
        pygame.draw.rect(self.fenetre, NOIR, (0, 0, self.largeur, self.hauteur), 4)

        for i in range(1, 16):
            pygame.draw.line(self.fenetre, NOIR, (i * self.taille_case, 0), (i * self.taille_case, self.hauteur))
            pygame.draw.line(self.fenetre, NOIR, (0, i * self.taille_case), (self.largeur, i * self.taille_case))

        for i in range(16):
            for j in range(16):
                case = self.plateau.cases[i][j]
                x, y = j * self.taille_case, i * self.taille_case

                # Dessiner les cibles
                for cible_pos, couleur_cible in self.liste_cible_position_couleur:
                    if (i, j) == cible_pos:
                        pygame.draw.rect(self.fenetre, couleur_cible, (x, y, self.taille_case, self.taille_case))

                if (i, j) in [(7, 7), (7, 8), (8, 7), (8, 8)]:
                    pygame.draw.rect(self.fenetre, self.cible, (x, y, self.taille_case, self.taille_case))

                if case.top:
                    pygame.draw.line(self.fenetre, NOIR, (x, y), (x + self.taille_case, y), 4)
                if case.bottom:
                    pygame.draw.line(self.fenetre, NOIR, (x, y + self.taille_case), (x + self.taille_case, y + self.taille_case), 4)
                if case.left:
                    pygame.draw.line(self.fenetre, NOIR, (x, y), (x, y + self.taille_case), 4)
                if case.right:
                    pygame.draw.line(self.fenetre, NOIR, (x + self.taille_case, y), (x + self.taille_case, y + self.taille_case), 4)

        self.fenetre.blit(self.robot_bleu_image, self.robot_bleu.position.topleft)
        self.fenetre.blit(self.robot_jaune_image, self.robot_jaune.position.topleft)
        pygame.display.flip()

    def def_cible(self):
        self.liste_cible_position_couleur = []
        for i in range(16):
            for j in range(16):
                case = self.plateau.cases[i][j]
                x, y = j * self.taille_case, i * self.taille_case
                if case.top and case.right or case.top and case.left or case.bottom and case.right or case.bottom and case.left:
                    couleur_case_cible = random.choice(couleurs_cibles)
                    self.liste_cible_position_couleur.append(((i, j), couleur_case_cible))
                    if couleur_case_cible == self.cible:
                        case.type = 2

    def pressed_key_robot(self, robot, keys):
        if keys[pygame.K_LEFT]:
            robot.deplacer('gauche', self.plateau)
        elif keys[pygame.K_RIGHT]:
            robot.deplacer('droite', self.plateau)
        elif keys[pygame.K_UP]:
            robot.deplacer('haut', self.plateau)
        elif keys[pygame.K_DOWN]:
            robot.deplacer('bas', self.plateau)

    def run(self):
        # Boucle principale
        clock = pygame.time.Clock()
        running = True
        robot_selectionne = None

        while running:
            # for event in pygame.event.get():
            #     if event.type == pygame.QUIT:
            #         running = False
            #     elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            #         mouse_x, mouse_y = event.pos
            #         # Vérifier quel robot a été cliqué
            #         for robot in self.liste_robots:
            #             if robot.est_clique(mouse_x, mouse_y):
            #                 robot_selectionne = robot

            # # Gérer les déplacements du robot
            # keys = pygame.key.get_pressed()

            # if robot_selectionne:
            #     self.pressed_key_robot(robot_selectionne, keys)

            # self.dessiner_plateau()
            clock.tick(10)
            if(self.ai.bfs()):
                pygame.quit()
                return
        pygame.quit()
        # Quitter Pygame
        

# Créez une instance de la classe Game et exécutez le jeu
if __name__ == "__main__":
    jeu = Game()
    jeu.def_cible()  # Initialise les cibles
    
    jeu.run()