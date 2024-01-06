from plateau import *
from robot import *
import copy
from time import sleep
from collections import deque

deplacements_liste = ['haut', 'bas', 'droite', 'gauche']

class ai:
    def __init__(self, robots, plateau, nombrecoups, cible):
        self.robots = robots
        self.plateau = plateau
        self.nombrecoups = nombrecoups
        self.cible = cible

    def bfs(self):
        visited = set()
        queue = deque([(self, [])])  # Maintenant, la file contient des tuples avec l'état et le chemin parcouru

        while queue:
            etat_actuel, chemin_parcouru = queue.popleft()

            i = -1
            for robot in etat_actuel.robots:
                i = i + 1
                for deplacement in deplacements_liste:
                    nouvel_etat = copy.deepcopy(etat_actuel)
                    nouvel_etat.robots[i].deplacer(deplacement, nouvel_etat.plateau, self.cible)

                    positions_robots = list_coordonnee(nouvel_etat)

                    if any(nouvel_etat.plateau.cases[x][y].type == 2 for x, y in positions_robots):
                        print("Victoire ! de l'ia")
                        return chemin_parcouru + [deplacement]  # Retourne le chemin parcouru jusqu'à la victoire

                    if nouvel_etat.robots[i].coordonnee_plateau() not in visited:
                        visited.add(robot.coordonnee_plateau())
                        queue.append((nouvel_etat, chemin_parcouru + [deplacement]))
                        
                        # Affiche l'état actuel de la file
                        print("FILE D'ETAT:")
                        count = 0
                        for e, chemin in queue:
                            count = count + 1
                            print("")
                            print("")
                            for r in e.robots:
                                print(f" Etat: {count} Robot: {r.nom} --> {r.coordonnee_plateau()}")
                                print()
                            print("Chemin parcouru:", chemin)
                            print("---")


def list_coordonnee(etat_actuel):
    positions_robots_pixel = [robot.position for robot in etat_actuel.robots]
    positions_robots = [(pos[1] // taille_case, pos[0] // taille_case) for pos in positions_robots_pixel]
    return positions_robots