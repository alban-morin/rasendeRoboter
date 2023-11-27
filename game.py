import pygame as pg
from player import *
from gameboard import *

pg.init()
screen=pg.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])#window size

player = Player()
objective = Objective()
board= Board()


running=True
while running:
    for event in pg.event.get(): #user clicks on quit button
        if event.type == pg.QUIT:
            running=False
        elif event.type == KEYDOWN:#user hit a key?
            if event.key == K_ESCAPE:
                running=False

    pressed_keys = pg.key.get_pressed()#get all keys currently pressed
    player.update(pressed_keys)#update player position


    screen.fill((245,245,220)) #fill background with beige
    screen.blit(board.surf, board.rect)
    screen.blit(player.surf, player.rect)
    screen.blit(objective.surf, objective.rect)



    pg.display.flip()#update screen content

