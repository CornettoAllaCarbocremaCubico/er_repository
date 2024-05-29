import pygame
import random
import math

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
        self.updatetesta()
        self.updatecoda()

        #for pezzo in self.corpo:
        #    pezzo = pygame.Rect(pezzo.x*h_quadretto, pezzo.y*h_quadretto, h_quadretto, h_quadretto)
        #   pygame.draw.rect(screen, (0,0,255), pezzo)
        for index, block in enumerate(self.corpo):
            x_pos = int(block.x * h_quadretto)
            y_pos = int(block.y * h_quadretto)
            block_rect = pygame. Rect(x_pos,y_pos,h_quadretto,h_quadretto)

        if index == 0:
            screen.blit(self.testa,block_rect)
        elif index == len(self.body) - 1:
            screen.blit(self.tail,block_rect)
        else:
            blockprima = self.body[index + 1] - block
            blockdopo = self.body[index - 1] - block
        if blockprima.x == blockdopo.x:
            screen.blit(corpovert,block_rect)
        elif blockprima.y == blockdopo.y:
            screen.blit(corpooriz,block_rect)
        else:
            if blockprima.x == -1 and blockdopo.y == -1 or blockprima.y == -1 and blockdopo.x == -1:
                screen.blit(self.body_tl,block_rect)
            elif blockprima.x == -1 and blockdopo.y == 1 or blockprima.y == 1 and blockdopo.x == -1:
                screen.blit(self.body_bl,block_rect)
            elif blockprima.x == 1 and blockdopo.y == -1 or blockprima.y == -1 and blockdopo.x == 1:
                screen.blit(self.body_tr,block_rect)
            elif blockprima.x == 1 and blockdopo.y == 1 or blockprima.y == 1 and blockdopo.x == 1:
                screen.blit(self.body_tr,block_rect)


    def updatetesta(self):
        head_relation = self.corpo[1] - self.corpo[0]
        if head_relation == math.Vector2(1,0): self.corpo[0] = testadestra
        elif head_relation == math.Vector2(-1,0): self.corpo[0]= testasinistra
        elif head_relation == math.Vector2(0,1): self.corpo[0]= testasu
        elif head_relation == math.Vector2(0,-1): self.corpo[0]= testagiu
    
    def updatecoda(self):   
        tail_relation = self.corpo[-2] - self.corpo[-1]
        if tail_relation == math.Vector2(1,0): self.corpo[-1] = codasinistra
        elif tail_relation == math.Vector2(-1,0): self.corpo[-1]= codadestra
        elif tail_relation == math.Vector2(0,1): self.corpo[-1]= codasu
        elif tail_relation == math.Vecotr2(0,-1): self.corpo[-1]= codagiu

        
    
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

