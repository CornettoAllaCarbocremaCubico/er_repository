import pygame
import random

n_quadretti = 15
h_quadretto = 40
screen = pygame.display.set_mode((h_quadretto*n_quadretti, h_quadretto*n_quadretti))

mela = pygame.image.load("mela2.png")
mela = pygame.transform.scale(mela, (h_quadretto, h_quadretto))  

class Frutto:
    def __init__(self, corpo_serpente):
        self.nuova_posizione(corpo_serpente) #Vector2 è una classe con x e y a cui
                                                                #attribuisco dei valori float
    def nuova_posizione(self, corpo_serpente):
        while True:
            self.x = random.randint(0,n_quadretti-1)
            self.y = random.randint(0,n_quadretti-1)
            self.posizione = pygame.math.Vector2(self.x, self.y)
            if self.posizione not in corpo_serpente:
                break

    def disegna_frutta(self):
        #pygame.rect(x,y,l,h)
        frutta = pygame.Rect(self.x*h_quadretto, self.y*h_quadretto, h_quadretto, h_quadretto)
        screen.blit(mela, (self.x*h_quadretto, self.y*h_quadretto, h_quadretto, h_quadretto))