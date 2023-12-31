# Importer les modules nécessaires
import pygame
from plateau import * 
from robot import *
import random
import numpy as np
from ai import *
import os
from target import *
from ia import *
from poid import *
from astar import *
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
        # Définir la taille de chaque case
        self.taille_case = self.largeur // 16
        # Initialiser les robots
        self.robot_bleu = Robot(position=(0, 0), nom= BLEU)
        self.robot_jaune = Robot(position=(15, 15), nom= JAUNE)
        self.robot_vert = Robot(position=(0, 15), nom= VERT)
        self.robot_rouge = Robot(position=(15, 0), nom= ROUGE)
        self.ai = None
        # Liste des robots
        self.liste_robots = [self.robot_bleu, self.robot_jaune,self.robot_vert,self.robot_rouge]
        for robot in self.liste_robots:
            i, j = robot.position.y // self.taille_case, robot.position.x // self.taille_case
            self.plateau.cases[i][j].type = 1

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



        #initialiser les cibles (fonction dans target.py, en dehors de la classe target)
        self.targets_list= create_targetList(self.plateau)

        # Choix de la cible principale 
        self.target_main = random.choice(self.targets_list)
        print("Cible principale :")
        print(self.target_main.posX,self.target_main.posY,self.target_main.couleur)
        self.plateau.cases[self.target_main.posX][self.target_main.posY].type = 2
        print(self.plateau.cases[self.target_main.posX][self.target_main.posY].type)
    
        # Compteur de coups
        self.count = 0

    def start(self):
        target_color = self.target_main.couleur

        for robot in self.liste_robots:
            if robot.nom == target_color:
                    return robot
            

        #self.ai = ai(self.liste_robots,self.plateau,self.count)
    def dessiner_plateau(self):
        #remplir de le fond de blanc
        self.fenetre.fill(BLANC)
        pygame.draw.rect(self.fenetre, NOIR, (0, 0, self.largeur, self.hauteur), 4)
        

        for i in range(1, 16):
            for j in range(1, 16):

                pygame.draw.line(self.fenetre, NOIR, (i * self.taille_case, 0), (i * self.taille_case, self.hauteur))
                pygame.draw.line(self.fenetre, NOIR, (0, j * self.taille_case), (self.largeur, j * self.taille_case))

        for (i, j) in [(7, 7), (7, 8), (8, 7), (8, 8)]:
            x, y = j * self.taille_case, i * self.taille_case
            pygame.draw.rect(self.fenetre, BLANC, (x, y, self.taille_case, self.taille_case), 4)



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
        
        #echantillon de scale pour les targets
            etalonage = pygame.transform.scale(
        self.cible_rouge_image[self.target_main.type], (int(1.5 * self.robot_largeur), int(1.5 * self.robot_hauteur)))
        target_main_x = self.largeur // 2 - etalonage.get_width() // 2
        target_main_y = self.hauteur // 2 - etalonage.get_height() // 2

        # Dessiner la cible principale
        if self.target_main.couleur == ROUGE:
            # Redimensionner seulement l'image de la cible principale au milieu
            target_main_image = pygame.transform.scale(
                self.cible_rouge_image[self.target_main.type], (int(1.5 * self.robot_largeur), int(1.5 * self.robot_hauteur)))
            self.fenetre.blit(target_main_image, (target_main_x, target_main_y))
        elif self.target_main.couleur == VERT:
            # Redimensionner seulement l'image de la cible principale au milieu
            target_main_image = pygame.transform.scale(
                self.cible_vert_image[self.target_main.type], (int(1.5 * self.robot_largeur), int(1.5 * self.robot_hauteur)))
            self.fenetre.blit(target_main_image, (target_main_x, target_main_y))
        elif self.target_main.couleur == JAUNE:
            # Redimensionner seulement l'image de la cible principale au milieu
            target_main_image = pygame.transform.scale(
                self.cible_jaune_image[self.target_main.type], (int(1.5 * self.robot_largeur), int(1.5 * self.robot_hauteur)))
            self.fenetre.blit(target_main_image, (target_main_x, target_main_y))
        elif self.target_main.couleur == BLEU:
            # Redimensionner seulement l'image de la cible principale au milieu
            target_main_image = pygame.transform.scale(
                self.cible_bleu_image[self.target_main.type], (int(1.5 * self.robot_largeur), int(1.5 * self.robot_hauteur)))
            self.fenetre.blit(target_main_image, (target_main_x, target_main_y))
        

        font = pygame.font.SysFont(None, 30)

        for i in range(16):
            for j in range(16):
                case = self.plateau.cases[i][j]
                x, y = j * self.taille_case, i * self.taille_case

                poids_texte = font.render(str(case.poid), True, NOIR)
                poids_rect = poids_texte.get_rect(center=(x + self.taille_case // 2, y + self.taille_case // 2))
                self.fenetre.blit(poids_texte, poids_rect)

        for i in range(16):
            for j in range(16):
                case = self.plateau.cases[i][j]
                x, y = j * self.taille_case, i * self.taille_case
  

                if case.top:
                    # pygame.draw.line(self.fenetre, BLANC, (x, y), (x + self.taille_case, y), 0)
                    pygame.draw.line(self.fenetre, NOIR, (x, y), (x + self.taille_case, y), 4)
                    
                if case.bottom:
                    pygame.draw.line(self.fenetre, NOIR, (x, y + self.taille_case), (x + self.taille_case, y + self.taille_case), 4)
                if case.left:
                    pygame.draw.line(self.fenetre, NOIR, (x, y), (x, y + self.taille_case), 4)
                if case.right:
                    pygame.draw.line(self.fenetre, NOIR, (x + self.taille_case, y), (x + self.taille_case, y + self.taille_case), 4)

        self.fenetre.blit(self.robot_bleu_image, self.robot_bleu.position)
        self.fenetre.blit(self.robot_jaune_image, self.robot_jaune.position)
        self.fenetre.blit(self.robot_vert_image, self.robot_vert.position)
        self.fenetre.blit(self.robot_rouge_image, self.robot_rouge.position)
        pygame.display.flip()

    


    def pressed_key_robot(self, robot, keys):
        #self.count += 1
        #print("nombre de coups : ", self.count)
        if keys[pygame.K_LEFT]:
            robot.deplacer('gauche', self.plateau, self.target_main)
        elif keys[pygame.K_RIGHT]:
            robot.deplacer('droite', self.plateau, self.target_main)
        elif keys[pygame.K_UP]:
            robot.deplacer('haut', self.plateau, self.target_main)
        elif keys[pygame.K_DOWN]:
            robot.deplacer('bas', self.plateau, self.target_main)

    def run(self):
        # Boucle principale
        clock = pygame.time.Clock()
        robot_selectionne = None
        running_user = False # variable pour savoir si on joue par nous meme ou si on lance l'ia
        running_ai = False # variable pour savoir si on lance l'ia
        print("Voulez vous jouer par vous-meme?")
        print("1. Oui")
        print("2. Non")
        choix = int(input())
        #choix=1
        
        if choix == 1:
            running_user = True

        else:
            print("L'ia se lance...")

            running_ai = True
            self.ai = ai(self.liste_robots,self.plateau,self.count,self.target_main)
            
        while running_user:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running_user = False
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

            self.dessiner_plateau() #dessine le plateau avec les robots

        while running_ai:
            #afficher le plateau
            self.plateau =  poidplateau(self.plateau, self.target_main)
            self.dessiner_plateau()
            chemin = self.ai.bfs()
            if(chemin):
                print("on a un chemin pour le bfs")
                print(chemin)
                break
            else: 
 


        # Appeler A* ici en utilisant self.plateau et les positions des robots/targets
                print("pas de chemin pour le bfs")
                print("on lance A*")
                print(self.start().nom)
                print(self.target_main.couleur)
                path = astar(self.plateau, self.start(), self.target_main)
                if path:
                    print("on a un chemin")
                    print(path)
                    
                    print("l'ia à trouvé en ", len(path), "coups")
                    break
                else:
                    print("pas de chemin")
                    break
        
    


        pygame.quit()
        # Quitter Pygame
        

# Créer une instance de la classe Game et exécuter le jeu
if __name__ == "__main__":
    jeu = Game()
    #for index in range(16):
        #print(jeu.targets_list[index].posX,jeu.targets_list[index].posY,jeu.targets_list[index].couleur,jeu.targets_list[index].type)
    #jeu.def_cible()  # Initialise les cibles

    jeu.run()

    