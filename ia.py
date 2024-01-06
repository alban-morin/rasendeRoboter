import math as math
import heapq
from collections import deque

#FICHIER D'IMPLEMENTATION DE  A ETOILE ET HEURISTIQUE
#NE FONCTIONNE PAS, PROBLEME DE TYPE

class ia:
    def __init__(self, robot, plateau, compteurCoups, cible):
        self.robot = robot
        self.plateau = plateau
        self.compteurCoups = compteurCoups
        self.cible = cible

    def astarInitialisation(self,plateau):
        #Noeud de départ
        Ndepart=Noeud(self.robot.coordonnee_plateau()[0],self.robot.coordonnee_plateau()[1],0,None)
        #Noeud d'arrivée
        Nfin=Noeud(self.cible.posX,self.cible.posY,0,None)
        #liste des noeuds
        listeNoeudsAVisiter = []
        return Aetoile(Ndepart,Nfin,listeNoeudsAVisiter,plateau)

    # distance euclidienne entre le robot et la cible, retourne un float
    def distanceEuclidienne(self):
        robot_posX=self.robot.coordonnee_plateau()[0]
        robot_posY=self.robot.coordonnee_plateau()[1]
        return math.sqrt((robot_posX - self.cible.posX)**2 + (robot_posY - self.cible.posY)**2)


class Noeud:
    def __init__(self, posX, posY, cout, parent):
        self.posX = posX
        self.posY = posY
        self.cout = cout
        self.parent = parent


class Aetoile:
    def __init__(self, depart, arrivee, listeNoeudsAVisiter, plateau ):
        self.depart = depart # noeud
        self.arrivee = arrivee # noeud
        self.listeNoeudsAVisiter = listeNoeudsAVisiter # liste de noeuds
        self.plateau = plateau

    def distanceEuclide(self, noeud, cible):
        return math.sqrt((noeud.posX - cible.posX)**2 + (noeud.posY - cible.posY)**2)

    def evaluationNoeud(self,noeud):
        f= self.distanceEuclide(noeud,self.arrivee)+noeud.cout
        return f


    # A executer pour le A* fasse son boulot
    def astarExecution(self):
        print(self.depart.posX,self.depart.posY)
        # on ajoute le noeud de départ à la liste des noeuds à visiter (tas)
        open_set = []
        open_set.append(Noeud(self.depart.posX, self.depart.posY, 0, None))
        print(open_set[0].posX,open_set[0].posY)
        closed_set = set()
        while open_set:
            # on récupère le noeud avec le plus petit f
            #current_node = min(open_set, key=lambda node: self.evaluationNoeud(node))
            current_node = open_set.pop(0)
            print(current_node)
            print(current_node.posX,current_node.posY)
            positionX = current_node.posX
            positionY = current_node.posY
            print(positionX,positionY)
            #IL ME DIT QUE CEST UN TUPLE ET PAS UN NOEUD, MAIS QUAND JE L'UTILISE COMME UN TUPLE IL ME DIT QUE CEST UN NOEUD
            #JE COMPRENDS PAS
            # on supprime le noeud de la liste des noeuds à visiter
            #open_set.remove(current_node)
            # on ajoute le noeud à la liste des noeuds visités
            closed_set.add((current_node.posX,current_node.posY))
            # on récupère les voisins du noeud courant
            neighbors = self.get_neighbors(self.plateau,current_node)
            # on vérifie si on a atteint la cible
            if (current_node.posX,current_node.posY) == (self.arrivee.posX,self.arrivee.posY):
                # on reconstruit le chemin
                path = []
                while current_node:
                    path.append((current_node.posX,current_node.posY))
                    current_node = current_node.parent
                return path[::-1]
            # on parcourt les voisins
            for neighbor in neighbors:
                # on vérifie si le voisin a déjà été visité
                if neighbor in closed_set:
                    continue
                # on calcule le cout du voisin
                cout = current_node.cout + 1
                # on vérifie si le voisin a déjà été visité
                if neighbor not in open_set:
                    # si le voisin n'a pas été visité, on l'ajoute à la liste des noeuds à visiter
                    open_set.append(neighbor)

        return None


    #fonction pour récupérer les voisins d'un noeud
    def get_neighbors(self, plateau,noeud):
        neighbors = []
        i=noeud.posX
        j=noeud.posY

        # Déplacement vers la gauche
        j_left = j
        while j_left > 0 and not plateau.cases[i][j_left].left and plateau.cases[i][j_left - 1].type != 1:
            j_left -= 1
        if (i, j_left) != (i, j):
            neighbors.append((i, j_left))

        # Déplacement vers la droite
        j_right = j
        while j_right < 15 and not plateau.cases[i][j_right].right and plateau.cases[i][j_right + 1].type != 1:
            j_right += 1
        if (i, j_right) != (i, j):
            neighbors.append((i, j_right))

        # Déplacement vers le haut
        i_up = i
        while i_up > 0 and not plateau.cases[i_up][j].top and plateau.cases[i_up - 1][j].type != 1:
            i_up -= 1

        if (i_up, j) != (i, j):
            neighbors.append((i_up, j))

        # Déplacement vers le bas
        i_down = i

        while i_down < 15 and not plateau.cases[i_down][j].bottom and plateau.cases[i_down + 1][j].type != 1:
            i_down += 1
        if (i_down, j) != (i, j):
            neighbors.append((i_down, j))

        return neighbors
