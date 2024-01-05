from plateau import *
from robot import *
from target import *
class Noeud:
    def __init__(self, position, cout_actuel, cout_heuristique, parent):
        self.position = position
        self.cout_actuel = cout_actuel
        self.cout_heuristique = cout_heuristique
        self.parent = parent

def astar(plateau, start, target):
    start.position = start.position[0] // (800 // 16), start.position[1] // (800 // 16)
    open_set = [Noeud(start.position, 0, heuristique(start.position, plateau), None)]
    closed_set = set()

    while open_set:
        current_node = min(open_set, key=lambda node: node.cout_actuel + node.cout_heuristique)
        open_set.remove(current_node)

        print("Current Node:", current_node.position)
        
        if current_node.position == (target.posX , target.posY):
            # Construire et renvoyer le chemin
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]
        plateau.cases[current_node.position[0]][current_node.position[1]].type = 0
        closed_set.add(current_node.position)

        for neighbor in get_neighbors(plateau, current_node.position):
            if neighbor in closed_set:
                continue

            cout_actuel = current_node.cout_actuel + 1
            cout_heuristique = heuristique(neighbor, plateau)
            if cout_heuristique != 'inf':
                
                new_node = Noeud(neighbor, cout_actuel, cout_heuristique, current_node)

                if new_node not in open_set:
                    open_set.append(new_node)

        print("Open Set:", [node.position for node in open_set])
        print("Closed Set:", closed_set)

    return None  # Aucun chemin trouvé

def heuristique(position, plateau):
    
    return plateau.cases[position[0]][position[1]].poid

def get_neighbors(plateau, position):
    neighbors = []
    i, j = position

    # Déplacement vers la gauche
    j_left = j
    while j_left > 0 and not plateau.cases[i][j_left].left and plateau.cases[i][j_left-1].type != 1:
        j_left -= 1
    if (i,j_left) != (i,j):
        neighbors.append((i, j_left))

    # Déplacement vers la droite
    j_right = j
    while j_right < 15 and not plateau.cases[i][j_right].right and plateau.cases[i][j_right+1].type != 1:
        j_right += 1
    if (i,j_right) != (i,j):
        neighbors.append((i, j_right))

    # Déplacement vers le haut
    i_up = i
    while i_up > 0 and not plateau.cases[i_up][j].top and plateau.cases[i_up-1][j].type != 1:
        i_up -= 1

    if (i_up,j) != (i,j):
        neighbors.append((i_up, j))

    # Déplacement vers le bas
    i_down = i

    while i_down < 15 and not plateau.cases[i_down][j].bottom and plateau.cases[i_down+1][j].type != 1:
        i_down += 1
    if (i_down,j) != (i,j):
        neighbors.append((i_down, j))

    return neighbors
    # Logique pour obtenir les voisins d'une position sur le plateau
    # Adaptée à la logique de votre plateau

   

