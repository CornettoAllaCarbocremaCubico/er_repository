import pygame
from pygame import mixer
import math

pygame.init()

n_quadretti = 15
h_quadretto = 40
screen = pygame.display.set_mode((h_quadretto * n_quadretti, h_quadretto * n_quadretti))
clock = pygame.time.Clock()
fps = 7

mixer.init()
suono_munch = mixer.Sound('632231__audacitier__biting-apple-2.mp3')
suono_spinacina = mixer.Sound('441415__matrixxx__lucky-7-cheerful.wav')


# Caricamento delle immagini
codadestra = pygame.image.load('codadestra.png')
codadestra = pygame.transform.scale(codadestra, (h_quadretto, h_quadretto))

codagiu = pygame.image.load('codagiu.png')
codagiu = pygame.transform.scale(codagiu, (h_quadretto, h_quadretto))

codasinistra = pygame.image.load('codasinistra.png')
codasinistra = pygame.transform.scale(codasinistra, (h_quadretto, h_quadretto))

codasu = pygame.image.load('codasu.png')
codasu = pygame.transform.scale(codasu, (h_quadretto, h_quadretto))

corpooriz = pygame.image.load('corpooriz.png')
corpooriz = pygame.transform.scale(corpooriz, (h_quadretto, h_quadretto))

corpovert = pygame.image.load('corpovert.png')
corpovert = pygame.transform.scale(corpovert, (h_quadretto, h_quadretto))

curvagd = pygame.image.load('curvagd2.png')
curvagd = pygame.transform.scale(curvagd, (h_quadretto, h_quadretto))

curvags = pygame.image.load('curvags2.png')
curvags = pygame.transform.scale(curvags, (h_quadretto, h_quadretto))

curvasd = pygame.image.load('curvasd2.png')
curvasd = pygame.transform.scale(curvasd, (h_quadretto, h_quadretto))

curvass = pygame.image.load('curvass2.png')
curvass = pygame.transform.scale(curvass, (h_quadretto, h_quadretto))

testadestra = pygame.image.load('testadestra2.png')
testadestra = pygame.transform.scale(testadestra, (h_quadretto, h_quadretto))

testagiu = pygame.image.load('testagiu2.png')
testagiu = pygame.transform.scale(testagiu, (h_quadretto, h_quadretto))

testasinistra = pygame.image.load('testasinistra2.png')
testasinistra = pygame.transform.scale(testasinistra, (h_quadretto, h_quadretto))

testasu = pygame.image.load('testasu2.png')
testasu = pygame.transform.scale(testasu, (h_quadretto, h_quadretto))

class Serpente:
    def __init__(self) -> None:
        self.corpo = [pygame.math.Vector2(2, 8), pygame.math.Vector2(1, 8), pygame.math.Vector2(0, 8)]
        self.direzione = pygame.math.Vector2(1, 0)
        self.nuova_direzione = self.direzione
        self.vivo = True
        self.aggiorna_immagini()

    def aggiorna_immagini(self):
        head_direction = self.corpo[0] - self.corpo[1]
        if head_direction == pygame.math.Vector2(1, 0): self.head = testadestra
        elif head_direction == pygame.math.Vector2(-1, 0): self.head = testasinistra
        elif head_direction == pygame.math.Vector2(0, 1): self.head = testagiu
        elif head_direction == pygame.math.Vector2(0, -1): self.head = testasu

        tail_direction = self.corpo[-2] - self.corpo[-1]
        if tail_direction == pygame.math.Vector2(1, 0): self.tail = codasinistra
        elif tail_direction == pygame.math.Vector2(-1, 0): self.tail = codadestra
        elif tail_direction == pygame.math.Vector2(0, 1): self.tail = codasu
        elif tail_direction == pygame.math.Vector2(0, -1): self.tail = codagiu

    def disegna_serpente(self):
        for i, block in enumerate(self.corpo):
            xpos = int(block.x * h_quadretto)
            ypos = int(block.y * h_quadretto)
            block_rect = pygame.Rect(xpos, ypos, h_quadretto, h_quadretto)

            if i == 0:
                screen.blit(self.head, block_rect)
            elif i == len(self.corpo) - 1:
                screen.blit(self.tail, block_rect)
            else:
                blockprima = self.corpo[i + 1] - block
                blockdopo = self.corpo[i - 1] - block

                if blockprima.x == blockdopo.x:
                    screen.blit(corpovert, block_rect)
                elif blockprima.y == blockdopo.y:
                    screen.blit(corpooriz, block_rect)
                else:
                    if (blockprima.x == -1 and blockdopo.y == -1) or (blockprima.y == -1 and blockdopo.x == -1):
                        screen.blit(curvags, block_rect)
                    elif (blockprima.x == -1 and blockdopo.y == 1) or (blockprima.y == 1 and blockdopo.x == -1):
                        screen.blit(curvass, block_rect)
                    elif (blockprima.x == 1 and blockdopo.y == -1) or (blockprima.y == -1 and blockdopo.x == 1):
                        screen.blit(curvagd, block_rect)
                    elif (blockprima.x == 1 and blockdopo.y == 1) or (blockprima.y == 1 and blockdopo.x == 1):
                        screen.blit(curvasd, block_rect)

    def muoviserpente(self):
        if self.direzione != -self.nuova_direzione:
            self.direzione = self.nuova_direzione
        nuova_testa = self.corpo[0] + self.direzione
        self.corpo.insert(0, nuova_testa)
        self.corpo.pop()
        self.aggiorna_immagini()

    def collisione(self, frutto, spinacina):
        if self.corpo[0] == frutto.posizione:
            frutto.nuova_posizionemela(self.corpo)
            self.corpo.append(self.corpo[-1])
            suono_munch.play()
        if self.corpo[0] == spinacina.posizione:
            self.corpo.append(self.corpo[-1])
            self.corpo.append(self.corpo[-1])
            self.corpo.append(self.corpo[-1])
            suono_spinacina.play()
            spinacina.rimuovi()

    def morte(self):
        if not 0 <= self.corpo[0].x < n_quadretti or not 0 <= self.corpo[0].y < n_quadretti:
            self.vivo = False
        for pezzo in self.corpo[1:]:
            if self.corpo[0] == pezzo:
                self.vivo = False
        
        
