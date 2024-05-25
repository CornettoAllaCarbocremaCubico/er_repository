import pygame
import random

n_quadretti = 15
h_quadretto = 40
screen = pygame.display.set_mode((h_quadretto*n_quadretti,h_quadretto*n_quadretti))

spinacheena = pygame.image.load("spinacinafake1.png")  
spinacheena = pygame.transform.scale(spinacheena, (h_quadretto, h_quadretto)) 
#spinacheena.set_colorkey((255, 255, 255))

class Spinacina:
    def __init__(self, fps, corpo_serpente):
        self.fps = fps
        self.tempo = 0
        self.prossima = random.randint(5, 10)
        self.posizionata = False
        self.tempo_scomparsa = 0
        self.nuova_posizione_spinacina(corpo_serpente)

    def nuova_posizione_spinacina(self, corpo_serpente):
        while True:
            self.x = random.randint(0, n_quadretti - 1)
            self.y = random.randint(0, n_quadretti - 1)
            self.posizione = pygame.math.Vector2(self.x, self.y)
            if self.posizione not in corpo_serpente:
                break
        self.posizionata = False
        self.tempo_scomparsa = 0
    
    def spawn_spinacina(self, corpo_serpente):
        self.tempo += 1
        if self.posizionata == True:
            self.tempo_scomparsa += 1
            if self.tempo_scomparsa / self.fps >= 5:
                self.rimuovi()
        if self.tempo / self.fps >= self.prossima and not self.posizionata:
            self.nuova_posizione_spinacina(corpo_serpente)
            self.prossima = random.randint(5, 10)
            self.tempo = 0
            self.posizionata = True
            
    def disegna_spinacina(self):
        if self.posizionata == True:
            spinacina = pygame.Rect(self.x * h_quadretto, self.y * h_quadretto, h_quadretto, h_quadretto)
            screen.blit(spinacheena, (self.x*h_quadretto, self.y*h_quadretto, h_quadretto, h_quadretto))

    def rimuovi(self):
        self.posizionata = False