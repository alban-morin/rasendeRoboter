class Case:
    def __init__(self, posx, posy, type, top=False, bottom=False, left=False, right=False,poid=0):
        """ 
        Args:
            posx (int): Position en x de la case.
            posy (int): Position en y de la case.
            type (int): Type de la case (0 pour vide, 1 pour obstacle, 2 pour robot, 3 pour objectif).
            top (bool): True si la case a un mur en haut, False sinon.
            bottom (bool): True si la case a un mur en bas, False sinon.
            left (bool): True si la case a un mur à gauche, False sinon.
            right (bool): True si la case a un mur à droite, False sinon.
        """
        
        self.posx = posx
        self.posy = posy
        self.type = type
        self.top = top
        self.bottom = bottom
        self.left = left
        self.right = right
        self.poid = poid
    def coin(self):
        """
        Renvoie True si la case est un coin, False sinon.
        """
        if self.top and self.right or self.top and self.left or self.bottom and self.right or self.bottom and self.left:
            return True
        else:
            return False
