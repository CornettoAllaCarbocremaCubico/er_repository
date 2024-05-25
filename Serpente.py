import pygame
import random

pygame.init()

n_quadretti = 15
h_quadretto = 40
screen = pygame.display.set_mode((h_quadretto*n_quadretti, h_quadretto*n_quadretti))

class Serpente:

    def __init__(self) -> None:
        self.corpo = [pygame.math.Vector2(7,9), pygame.math.Vector2(6,9),
                        pygame.math.Vector2(5,9)]
        
        self.direzione = pygame.math.Vector2(1, 0)
        self.nuova_direzione = self.direzione
        self.vivo = True
    
    def disegna_serpente(self):
        for pezzo in self.corpo:
            pezzo = pygame.Rect(pezzo.x*h_quadretto, pezzo.y*h_quadretto, h_quadretto, h_quadretto)
            pygame.draw.rect(screen, (0,0,255), pezzo)
    
    def muoviserpente(self):
        if self.direzione != -self.nuova_direzione:
            self.direzione = self.nuova_direzione
        nuova_testa = self.corpo[0] + self.direzione
        self.corpo.insert(0, nuova_testa)
        self.corpo.pop()  
        

    def collisione(self, frutto, spinacina):
        if self.corpo[0] == frutto.posizione:
            frutto.nuova_posizione(self.corpo)
            self.corpo.append(self.corpo[-1])
        if self.corpo[0] == spinacina.posizione:
            self.corpo.append(self.corpo[-1])
            self.corpo.append(self.corpo[-1])
            self.corpo.append(self.corpo[-1])
            spinacina.rimuovi()
    
    def morte(self):
        if not 0 <= self.corpo[0].x < n_quadretti-1 or not 0 <= self.corpo[0].y < n_quadretti:
            self.vivo = False
        for pezzo in self.corpo[1:]:
            if self.corpo[0] == pezzo:
                self.vivo = False
                print("scontro")


    def punteggio(self):
        punti= str(len(self.corpo)-3)
        font= pygame.font.Font(None,36)
        supepunti=font.render(punti, True,(0,0,0))
        rect_punti=supepunti.get_rect(center=(501,61))
        screen.blit(supepunti,rect_punti)




