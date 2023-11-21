from plateau import *

robot=Robot(1,1)
#robot.posx=1
#robot.posy=1

jeutest=plateau()
jeutest.print_lignes()
jeutest.print_colonnes()

#print(verif_obstacle(jeutest.lignes,0,0))
jeutest.movement(robot,"l")
print(robot.posy)

