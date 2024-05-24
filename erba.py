import pygame
import random

n_quadretti = 20
h_quadretto = 40
screen = pygame.display.set_mode((h_quadretto*n_quadretti, h_quadretto*n_quadretti))
class erba:
    def __init__(self,pos,screen,size):
        self.pos=pos
        self.screen=screen
        self.size=size
        self.rect=pygame.rect(self.pos[0],self.pos[1],self.size[0],self.size[1])
        self.image = pygame.Surface(size)
        self.image.fill(color)
        
   
    colore= (167,209,61)
    def disegna_erba(self):
        colore= (167,209,61)
        for r in range(n_quadretti):
            if r %2==0:
                for col in range(n_quadretti):
                    if col %2==0:
                        rect_erba=pygame.Rect(col*h_quadretto,0,h_quadretto,h_quadretto)
                        pygame.draw.rect(screen,colore,rect_erba)
