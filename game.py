import pygame as pg
pg.init()

screen=pg.display.set_mode([900,720])#window size

running=True
while running:
    for event in pg.event.get(): #user clicks on quit button
        if event.type == pg.QUIT:
            running=False
    screen.fill((245,245,220))#fill background with beige
    pg.display.flip()

