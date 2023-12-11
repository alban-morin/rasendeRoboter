# Importer les modules nécessaires
import pygame
from plateau import * 
from robot import *
import random
import numpy as np
from ai import *
import os
from target import *

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
        self.robot_vert = Robot(position=(0, 15), nom="Vert")
        self.robot_rouge = Robot(position=(15, 0), nom="Rouge")

        # Liste des robots
        self.liste_robots = [self.robot_bleu, self.robot_jaune]

        # Charger les images et redimensionner
        folder = os.path.dirname(os.path.realpath(__file__))
        self.robot_bleu_image = pygame.image.load(os.path.join(folder, 'img', 'robotbleu.JPG'))
        self.robot_jaune_image = pygame.image.load(os.path.join(folder, 'img', 'robotjaune.JPG'))
        self.robot_vert_image= pygame.image.load(os.path.join(folder, 'img', 'robotvert.JPG'))
        self.robot_rouge_image= pygame.image.load(os.path.join(folder, 'img', 'robotrouge.JPG'))

        self.robot_largeur = int(self.largeur // 16 * 0.9)
        self.robot_hauteur = int(self.hauteur // 16 * 0.9)
        self.robot_bleu_image = pygame.transform.scale(self.robot_bleu_image, (self.robot_largeur, self.robot_hauteur))
        self.robot_jaune_image = pygame.transform.scale(self.robot_jaune_image, (self.robot_largeur, self.robot_hauteur))
        self.robot_vert_image = pygame.transform.scale(self.robot_vert_image, (self.robot_largeur, self.robot_hauteur))
        self.robot_rouge_image = pygame.transform.scale(self.robot_rouge_image, (self.robot_largeur, self.robot_hauteur))

        # Charger les images des cibles
        self.cible_jaune_image = [None]*4
        self.cible_bleu_image = [None]*4
        self.cible_vert_image = [None]*4
        self.cible_rouge_image = [None]*4
        for i in range(4):
            self.cible_jaune_image[i]= pygame.image.load(os.path.join(folder, 'targets_img', 'jaune'+str(i)+'.png'))
            self.cible_jaune_image[i]=pygame.transform.scale(self.cible_jaune_image[i], (self.robot_largeur, self.robot_hauteur))
            self.cible_bleu_image[i]= pygame.image.load(os.path.join(folder, 'targets_img', 'bleu'+str(i)+'.png'))
            self.cible_bleu_image[i]=pygame.transform.scale(self.cible_bleu_image[i], (self.robot_largeur, self.robot_hauteur))
            self.cible_vert_image[i]= pygame.image.load(os.path.join(folder, 'targets_img', 'vert'+str(i)+'.png'))
            self.cible_vert_image[i]=pygame.transform.scale(self.cible_vert_image[i], (self.robot_largeur, self.robot_hauteur))
            self.cible_rouge_image[i]= pygame.image.load(os.path.join(folder, 'targets_img', 'rouge'+str(i)+'.png'))
            self.cible_rouge_image[i]=pygame.transform.scale(self.cible_rouge_image[i], (self.robot_largeur, self.robot_hauteur))

        # Définir la taille de chaque case
        self.taille_case = self.largeur // 16

        #initialiser les cibles (fonction dans target.py, en dehors de la classe target)
        self.targets_list= create_targetList(self.plateau)

        # Choix de la cible principale A FAIRE CORRECTEMENT
        self.target_main = random.choice(self.targets_list)

        # Compteur de coups
        self.count = 0

        #self.ai = ai(self.liste_robots,self.plateau,self.count)
    def dessiner_plateau(self):
        #remplir de le fond de blanc
        self.fenetre.fill(BLANC)
        pygame.draw.rect(self.fenetre, NOIR, (0, 0, self.largeur, self.hauteur), 4)

        #dessiner les lignes de séparation entre les cases
        for i in range(1, 16):
            pygame.draw.line(self.fenetre, NOIR, (i * self.taille_case, 0), (i * self.taille_case, self.hauteur))
            pygame.draw.line(self.fenetre, NOIR, (0, i * self.taille_case), (self.largeur, i * self.taille_case))

        #Dessiner les targets
        for i in range(16):
            for j in range(16):
                case = self.plateau.cases[i][j] # on etudie chaque case du plateau
                x, y = j * self.taille_case, i * self.taille_case
                for element in self.targets_list: #on parcourt la liste des targets et on compare les coordonnées avec celles de la case
                    if (i == element.posX and j == element.posY):
                        if element.couleur == ROUGE:
                            self.fenetre.blit(self.cible_rouge_image[element.type], (x, y))
                        elif element.couleur == VERT:
                            self.fenetre.blit(self.cible_vert_image[element.type], (x, y))
                        elif element.couleur == JAUNE:
                            self.fenetre.blit(self.cible_jaune_image[element.type], (x, y))
                        elif element.couleur == BLEU:
                            self.fenetre.blit(self.cible_bleu_image[element.type], (x, y))
                        continue

        for i in range(16):
            for j in range(16):
                case = self.plateau.cases[i][j]
                #convertir position back en positions display
                x, y = j * self.taille_case, i * self.taille_case

                # if (i, j) in [(7, 7), (7, 8), (8, 7), (8, 8)]:
                #     pygame.draw.rect(self.fenetre, self.cible, (x, y, self.taille_case, self.taille_case))

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
        self.fenetre.blit(self.robot_vert_image, self.robot_vert.position.topleft)
        self.fenetre.blit(self.robot_rouge_image, self.robot_rouge.position.topleft)
        pygame.display.flip()

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
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    mouse_x, mouse_y = event.pos
                    # Vérifier quel robot a été cliqué
                    for robot in self.liste_robots:
                        if robot.est_clique(mouse_x, mouse_y):
                            robot_selectionne = robot

            # Gérer les déplacements du robot
            keys = pygame.key.get_pressed()

            if robot_selectionne:
                self.pressed_key_robot(robot_selectionne, keys)

            self.dessiner_plateau()
            # clock.tick(10)
            # if(self.ai.bfs()):
            #     pygame.quit()
            #     return
        pygame.quit()
        # Quitter Pygame
        

# Créer une instance de la classe Game et exécuter le jeu
if __name__ == "__main__":
    jeu = Game()
    #for index in range(16):
        #print(jeu.targets_list[index].posX,jeu.targets_list[index].posY,jeu.targets_list[index].couleur,jeu.targets_list[index].type)
    #jeu.def_cible()  # Initialise les cibles

    jeu.run()