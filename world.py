import pygame as pg

class World():
    def _init_(self, map_image):
        self.image = map_image

    def draw(self, surface):
        surface.blit(slef.image, (0,0))
        

    