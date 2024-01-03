#from gameclass import (Game)
from plateau import *
import random
import itertools


# Définition des constantes de couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
ROUGE = (255, 0, 0)
VERT = (0, 255, 0)
BLEU = (0, 0, 255)
JAUNE = (255, 255, 0)

# Liste des couleurs
couleurs_cibles = [ROUGE, VERT, BLEU, JAUNE]
types_cible=[0,1,2,3]

#Types possibles de cible :
#0 : triangle
#1 : rond
#2 : etoile
#3 : carre
class Target:
    def __init__(self, couleur, type, posX, posY):
        self.couleur = couleur
        self.type = type
        self.posX = posX
        self.posY = posY

def create_targetList(plateau):
    targets = [] #initialisation liste vide ou on va mettre la totalité des targets
    for x in range(16):
        for y in range(16):
            for i in range(16):
                #pour mettre des valeurs par "defaut"
                couleur, target_type=ROUGE, 0
                case = plateau.cases[x][y] #on charge la case actuelle du plateau pour verifier si on va y mettre une cible
                if(x==7 or x==8): #gros carré du milieu donc ca compte pas comme cible
                    break
                if case.coin():#vérifier si la case est un coin et donc devrait avoir une cible
                    plateau.cases[x][y].type = 0  # modifier le type de case dans le plateau
                    pos_x = x
                    pos_y = y
                    target = Target(couleur, target_type, pos_x, pos_y)
                    targets.append(target)
                    #print(pos_x, pos_y, couleur, target_type)
                    break

    #avoir toutes les combinaisons possibles de couleur et type
    color_type_combinations = list(itertools.product(couleurs_cibles, types_cible))
    #on melange pour avoir de l'aléatoire
    random.shuffle(color_type_combinations)
    #print(color_type_combinations)

    #on met les couleurs et types dans les targets
    for i in range(16):
        couleur, target_type = color_type_combinations[i]
        targets[i].couleur = couleur
        targets[i].type = target_type
        # print(targets[i].posX,targets[i].posY, couleur, plateau.cases[targets[i].posX][targets[i].posY].type)

    return targets
