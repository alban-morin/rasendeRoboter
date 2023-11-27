import pygame as pg
from player import *

class Board(pg.sprite.Sprite):
    def __init__(self):
        super(Board, self).__init__()
        self.surf = pg.Surface((SCREEN_WIDTH/1.1,SCREEN_HEIGHT/1.1),pg.SRCALPHA)
        self.surf.fill((0,0,0,0))
        #self.border_color = (255, 255, 255)
        pg.draw.rect(self.surf, (0,0,0),(0,0, SCREEN_WIDTH/1.1, SCREEN_HEIGHT/1.1), 5)
        self.rect = self.surf.get_rect()
        self.rect.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
