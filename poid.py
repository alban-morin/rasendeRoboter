from plateau import * 
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
    queue = deque([(position_cible, 0,typedecoin(plateau.cases[position_cible]))])  # (position, poids,type de coin)
    print("on a definie la queue")
    print(position_cible)
    # Définir le poids de la cible comme 0
    plateau.cases[position_cible].poid = 0

    # Définir les types de cibles
 
    print("on a definie les directions")
    while queue:
        
            current_position, current_poids,direction = queue.popleft()
            print(direction)
            
            
            # Calculer la position suivante
            next_position = current_position

            i, j = next_position
            print("la position actuel est:")
            print(current_position)
            print("")
            print("")
            # Vérifier si la position suivante est valide
            if 0 <= i < 16 and 0 <= j < 16:
                case = plateau.cases[i][j]
                temp = i,j

                # Vérifier si la case a un mur dans la direction actuelle et que la case suivante n'est pas un obstacle
                if (direction == "TD") :
                    
                    
                
                    i,j = check_haut_bas_jmoins1(plateau, i, j,queue,current_poids)

                    i,j = temp
                    
                    
                    i,j = check_gauche_droite_iplus1(plateau, i, j,queue,current_poids)


                    
                       
                elif (direction == "TG") :
                    
                    
                    i,j = check_haut_bas_jplus1(plateau, i, j,queue,current_poids)

                    i,j = temp
                    
                    i,j = check_gauche_droite_iplus1(plateau, i, j,queue,current_poids)
  
                        
                        
                    
                elif (direction == "BG") :
                    
                    
                    i,j = check_gauche_droite_imoins1(plateau, i, j,queue,current_poids)

                    i,j = temp
                    
                    i,j = check_haut_bas_jplus1(plateau, i, j,queue,current_poids)

                        
                        

                        
                elif (direction == "BD") :
                    
                    
                    i,j = check_gauche_droite_imoins1(plateau, i, j,queue,current_poids)

                    i,j = temp
                    
                    i,j = check_haut_bas_jmoins1(plateau, i, j,queue,current_poids)

                else:
                    if(direction == "T"):
                        i,j = check_gauche_droite_iplus1(plateau, i, j,queue,current_poids)

                    elif(direction == "B"):
                        i,j = check_gauche_droite_imoins1(plateau, i, j,queue,current_poids)   

                    elif(direction == "G"):
                        i,j = check_haut_bas_jplus1(plateau, i, j,queue,current_poids)

                    elif(direction == "D"):
                        i,j = check_haut_bas_jmoins1(plateau, i, j,queue,current_poids)


                    

                        
                # print("on a verifier les murs on ajoute a la queue ou pas nous ne sommes plus dans les fonction de checking")
                # print(queue)
                # if plateau.cases[next_position].poid > current_poids+1:

                #     queue.append((next_position, current_poids + 1,typedecoin(plateau.cases[next_position])))
                #     plateau.cases[next_position].poid = current_poids + 1
                #     print(f"le poid de la case {plateau.cases[next_position].posx,plateau.cases[next_position].posy} est :")
                #     print(plateau.cases[next_position].poid)
                #     print("")
                #     print("")
                #     if current_poids > 30:
                #         break
                # elif plateau.cases[temp2].poid == current_poids + 1:
                #     queue.append((temp2, current_poids + 1,typedecoin(plateau.cases[temp2])))
                #     plateau.cases[temp2].poid = current_poids + 1
                #     print(f"le poid de la case {plateau.cases[temp2].posx,plateau.cases[temp2].posy} est :")
                #     print(plateau.cases[temp2].poid)
                #     print("")
                #     print("")
                #     if current_poids > 30:
                #         break

                # else:
                #     print("on a pas ajoute a la queue dans ")
                #     print("")
                #     print("")

                # print("le plateau est :")  
                # plateau.afficher()
        
    return plateau    # Afficher le tableau des poids après chaque itération
 # Ajouter un délai de 0.5 seconde entre chaque itération

def typedecoin(case):
    if case.top and case.right:
        return "TD"
    elif case.top and case.left:
        return "TG"
    elif case.bottom and case.right:
        return "BD"
    elif case.bottom and case.left:
        return "BG"
    elif case.top:
        return "T"
    elif case.bottom:
        return "B"
    elif case.left:
        return "G"
    elif case.right:
        return "D"

def check_gauche_droite_iplus1(plateau, i, j,queue,current_poids):
    next_position = i, j
    while ( i < 15 and not  plateau.cases[i][j].bottom and plateau.cases[i+1][j].type != 1 ) :
        i = i + 1
        next_position = i, j
        if plateau.cases[i][j].left or plateau.cases[i][j].right:
            print("on a ajoute a la queue dans check_gauche_droite_iplus1")
            ajoutqueue(queue,current_poids,(next_position),plateau)
            print(queue)
    print("on a fini la fonction check_gauche_droite_iplus1 on se retrouve a la position :")
    print(i,j)
    print("on ajoute a la queue la position :")
    ajoutqueue(queue,current_poids,(next_position),plateau)
    return i,j

def check_gauche_droite_imoins1(plateau, i, j,queue,current_poids):
    next_position = i, j
    while ( i>0 and not  plateau.cases[i][j].bottom and plateau.cases[i-1][j].type != 1 ) :
        i = i - 1
        next_position = i, j
        if plateau.cases[i][j].left or plateau.cases[i][j].right:
            print("on a ajoute a la queue dans check_gauche_droite_imoins1")
            ajoutqueue(queue,current_poids,next_position,plateau)
            print(queue)
    print("on a fini la fonction check_gauche_droite_imoins1 on se retrouve a la position :")
    print(i,j)
    print("on ajoute a la queue la position :")
    ajoutqueue(queue,current_poids,(next_position),plateau)
    return i,j
    

def check_haut_bas_jplus1(plateau, i, j,queue,current_poids):
    next_position = i, j
    while ( j < 15 and  not plateau.cases[i][j].right and plateau.cases[i][j+1].type != 1) :
        j = j + 1
        next_position = i, j
        if plateau.cases[i][j].top or plateau.cases[i][j].bottom:
            print("on a ajoute a la queue dans check_haut_bas_jplus1")
            ajoutqueue(queue,current_poids,next_position,plateau)
            print(queue)
    print("on a fini la fonction check_haut_bas_jplus1 on se retrouve a la position :")
    print(i,j)
    print("on ajoute a la queue la position :")
    ajoutqueue(queue,current_poids,(next_position),plateau)
    return i,j
    

def check_haut_bas_jmoins1(plateau, i, j,queue,current_poids):
    next_position = i, j
    while ( j > 0 and not  plateau.cases[i][j].left and plateau.cases[i][j-1].type != 1 ) :
        j = j - 1
        next_position = i, j
        if plateau.cases[i][j].top or plateau.cases[next_position].bottom:
            print("on a ajoute a la queue dans check_haut_bas_jmoins1")
            ajoutqueue(queue,current_poids,next_position,plateau)
            print(queue)
    print("on a fini la fonction check_haut_bas_jmoins1 on se retrouve a la position :")
    print(i,j)
    print("on ajoute a la queue la position :")
    ajoutqueue(queue,current_poids,(next_position),plateau)
    return i,j


def ajoutqueue(queue,current_poids,next_position,plateau):
    queue.append((next_position, current_poids + 1,typedecoin(plateau.cases[next_position])))
    print(f"nous sommes dans la fonction ajoutqueue en position{next_position} et le type de coin est :")
    print(typedecoin(plateau.cases[next_position]))
    plateau.cases[next_position].poid = current_poids + 1
    