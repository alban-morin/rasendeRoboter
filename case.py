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
    

    # def set_wall(self, direction, value=True):
    #     """
    #     Définit la présence ou l'absence d'un mur dans la direction spécifiée.

    #     Args:
    #         direction (str): Direction du mur ('top', 'bottom', 'left', 'right').
    #         value (bool): True pour ajouter un mur, False pour supprimer le mur.
    #     """
    #     setattr(self, direction, value)

    #     # Met à jour la case adjacente dans la direction opposée
    #     if direction == 'top' and self.posy > 0:
    #         self.adjacent_case('top').bottom = value
    #     elif direction == 'bottom' and self.posy < 15:
    #         self.adjacent_case('bottom').top = value
    #     elif direction == 'left' and self.posx > 0:
    #         self.adjacent_case('left').right = value
    #     elif direction == 'right' and self.posx < 15:
    #         self.adjacent_case('right').left = value

    # def adjacent_case(self, direction):
    #     """
    #     Renvoie la case adjacente dans la direction spécifiée.

    #     Args:
    #         direction (str): Direction ('top', 'bottom', 'left', 'right').

    #     Returns:
    #         Case: La case adjacente.
    #     """
    #     if direction == 'top':
    #         return self.grid[self.posy - 1][self.posx]
    #     elif direction == 'bottom':
    #         return self.grid[self.posy + 1][self.posx]
    #     elif direction == 'left':
    #         return self.grid[self.posy][self.posx - 1]
    #     elif direction == 'right':
    #         return self.grid[self.posy][self.posx + 1]