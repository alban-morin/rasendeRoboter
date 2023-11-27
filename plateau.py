import numpy as np
def verif_obstacle(tab,i,j):
    if(tab[i][j]==1):
        return True
    else:
        return False
    
class Robot:
    def __init__(self, posx, posy):
        self.posx = 1 #going from 0 to 15
        self.posy = 1
        
    def ask_direction(self): 
        print("In which direction do you want to go? (u/d/l/r)")
        direction=input()
        
class plateau:
    lines= np.zeros((16,16))#creating a matrix full of 0s
    columns= np.zeros((16,16))
    
    def __init__(self):
        self.lines[0]=[1]*16 #on remplit les bords de 1 pour les obstacles
        self.lines[15]=[1]*16
        self.columns[:,0]=1
        self.columns[:,15]=1

    def print_lignes(self):
        print("lines")
        print(self.lines)

    def print_colonnes(self):
        print("columns")
        print(self.columns)
    
    def movement(self,robot,direction):
        if(direction=="u"):
            while(verif_obstacle(self.lines,robot.posx+1,robot.posy)==False):
                robot.posx+=1
        elif(direction=="d"):
            while(verif_obstacle(self.lines,robot.posx-1,robot.posy)==False):
                robot.posx-=1
        elif(direction=="l"):
            while(verif_obstacle(self.columns,robot.posx,robot.posy-1)==False):
                robot.posy-=1
        elif(direction=="r"):
            while(verif_obstacle(self.columns,robot.posx,robot.posy+1)==False):
                robot.posy+=1
