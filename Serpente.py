import pygame
import random

pygame.init()

n_quadretti = 15
h_quadretto = 40
screen = pygame.display.set_mode((h_quadretto*n_quadretti, h_quadretto*n_quadretti))

codadestra=pygame.image.load('codadestra.png')
codadestra = pygame.transform.scale(codadestra, (h_quadretto, h_quadretto))  

codagiu=pygame.image.load('codagiu.png')
codagiu = pygame.transform.scale(codagiu, (h_quadretto, h_quadretto))  

codasinistra=pygame.image.load('codasinistra.png')
codasinistra = pygame.transform.scale(codasinistra, (h_quadretto, h_quadretto))  

codasu=pygame.image.load('codasu.png')
codasu = pygame.transform.scale(codasu, (h_quadretto, h_quadretto))  

corpooriz=pygame.image.load('corpooriz.png')
corpooriz = pygame.transform.scale(corpooriz, (h_quadretto, h_quadretto))  

corpovert=pygame.image.load('corpovert.png')
corpovert = pygame.transform.scale(corpovert, (h_quadretto, h_quadretto))  

curvagd=pygame.image.load('curvagd.png')
curvagd = pygame.transform.scale(curvagd, (h_quadretto, h_quadretto))  

curvags=pygame.image.load('curvags.png')
curvags = pygame.transform.scale(curvags, (h_quadretto, h_quadretto))

curvasd=pygame.image.load('curvasd.png')
curvasd = pygame.transform.scale(curvasd, (h_quadretto, h_quadretto))  

curvass=pygame.image.load('curvass.png')
curvass = pygame.transform.scale(curvass, (h_quadretto, h_quadretto))  

testadestra=pygame.image.load('testadestra.png')
testadestra= pygame.transform.scale(testadestra, (h_quadretto, h_quadretto))  

testagiu=pygame.image.load('testagiu.png')
testagiu= pygame.transform.scale(testagiu, (h_quadretto, h_quadretto))  

testasinistra=pygame.image.load('testasinistra.png')
testasinistra = pygame.transform.scale(testasinistra, (h_quadretto, h_quadretto)) 
 
testasu=pygame.image.load('testasu.png')
testasu = pygame.transform.scale(testasu, (h_quadretto, h_quadretto))  


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
        if not 0 <= self.corpo[0].x <= n_quadretti-1 or not 0 <= self.corpo[0].y <= n_quadretti:
            self.vivo = False
        for pezzo in self.corpo[1:]:
            if self.corpo[0] == pezzo:
                self.vivo = False

