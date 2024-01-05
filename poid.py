from gameclass import *

from collections import deque
from time import sleep

def poidplateau(plateaugame, target):
    # Récupérer la position de la cible
    plateau = plateaugame
    position_cible = target.posX, target.posY

    # Initialiser la matrice des poids avec des valeurs élevées
   
        # Initialiser la matrice des poids avec des valeurs élevées
    for i in range(16):
        for j in range(16):
            plateau.cases[i][j].poid = float('inf')

    # Initialiser la file pour le parcours en largeur
    queue = deque([(position_cible, 0)])  # (position, poids)
    print("on a definie la queue")
    print(position_cible)
    # Définir le poids de la cible comme 0
    plateau.cases[position_cible].poid = 0

    # Définir les directions possibles
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # droite, gauche, bas, haut
    print("on a definie les directions")
    
    while queue:
        
        print("on est dans la boucle")
        current_position, current_poids = queue.popleft()
        flags = [False, False]
        k = -1
        # Parcourir les 4 directions possibles
        for direction in directions:
            
            print("on est dans la boucle for")
            # Calculer la position suivante
            next_position = current_position

            i, j = next_position
            print(next_position)
            # Vérifier si la position suivante est valide
            if 0 <= i < 16 and 0 <= j < 16:
                case = plateau.cases[i][j]
                
                # Vérifier si la case a un mur dans la direction actuelle et que la case suivante n'est pas un obstacle
                if (direction == (0, -1)) :
                 
                    while ( j > 0 and not  plateau.cases[i][j].left and plateau.cases[i][j-1].type != 1 ) :
                      
                        j = j - 1
                        next_position = i, j
                        print(next_position)
                elif (direction == (0, 1)) :
                    
                    while ( j < 15 and  not plateau.cases[i][j].right and plateau.cases[i][j+1].type != 1) :

                        j = j + 1
                        next_position = i, j 
                        print(next_position)
                        
                        

                elif (direction == (-1, 0)) :
                    
                    while (i > 0 and  not plateau.cases[i][j].top and plateau.cases[i-1][j].type != 1) :
                        
                        i = i - 1
                        next_position = i, j
                        print(next_position)
                elif (direction == (1, 0)) :
                    
                    while ( i < 15 and not  plateau.cases[i][j].bottom and plateau.cases[i+1][j].type != 1 ) :
                        
                        i = i + 1
                        next_position = i, j
                        print(next_position)
                print("on a verifier les murs")
                
                if plateau.cases[next_position].poid > current_poids + 1 and next_position != current_position:
                    print("on a verifier les obstacles on ajoute a la queue")
            
                    k = k + 1
                        

                    queue.append((next_position, current_poids + 1))
                    plateau.cases[next_position].poid = current_poids + 1
                    print("le poid de la case est :")
                    print(plateau.cases[next_position].poid)
                print (verifposition(plateau,current_position,next_position,direction))
        #         if verifposition(plateau,current_position,next_position,direction):

        #             print("on a verifier la position")
        #             flags[k] == True

        # if flags[0] == False and flags[1] == False and current_poids<=1 and next_position != current_position:
        #     print("il faut deplacer un robot pour gagner probleme avec :------------------------------------------------------------------------------------------------------------------------------------------------")
        #     print(current_position)
        #     sleep(3)
 



    
                        
                        
    return plateau    # Afficher le tableau des poids après chaque itération
 # Ajouter un délai de 0.5 seconde entre chaque itération
def verifposition(plateau,position1,position2,direction):
    print("on est dans la fonction verifposition")
    print(direction)
    i, j = position2

    # Déplacement vers la gauche si direction vers la droite
    if direction == (0, 1) :
        j_left = j
        while j_left > 0 and not plateau.cases[i][j_left].left and plateau.cases[i][j_left-1].type != 1:
            j_left -= 1
        if (i,j_left) == position1:
            return True
        else:    
            return False
        
    # Déplacement vers la droite
    if direction == (0, -1) :
        j_right = j
        while j_right < 15 and not plateau.cases[i][j_right].right and plateau.cases[i][j_right+1].type != 1:
            j_right += 1
        if (i,j_right) == position1:
            return True
        else:    
            return False
    # Déplacement vers le haut
    if direction == (1, 0) :
        i_up = i
        while i_up > 0 and not plateau.cases[i_up][j].top and plateau.cases[i_up-1][j].type != 1:
            i_up -= 1
        if (i_up,j) == position1:
            return True
        else:    
            return False

    # Déplacement vers le bas
    if direction == (-1, 0) :
        i_down = i
        while i_down < 15 and not plateau.cases[i_down][j].bottom and plateau.cases[i_down+1][j].type != 1:
            i_down += 1
        if (i_down,j) == position1:
            return True
        else:    
            return False
        
    else:
        return False
    

    

