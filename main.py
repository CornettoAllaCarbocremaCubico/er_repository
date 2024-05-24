import pygame
import random
import os, sys
from Frutto import Frutto
from spinacina import Spinacina
from Serpente import Serpente
#from erba import erba
    
pygame.init()
h_quadretto = 64
n_quadretti = 64
screen = pygame.display.set_mode((964, 964))
clock = pygame.time.Clock()
fps = 8

serpente = Serpente()
frutto = Frutto(serpente.corpo)
spinacina = Spinacina(fps, serpente.corpo)
#grass=erba()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

sfondo=pygame.image.load("sfondo snake2.jpg")
sfondo=pygame.transform.scale(sfondo,(964,964))
screen.blit(sfondo,(0,0))
while serpente.vivo == True:
    # 0. tasti
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and serpente.direzione != pygame.math.Vector2(0, 1):
                serpente.nuova_direzione = pygame.math.Vector2(0, -1)
            if event.key == pygame.K_DOWN and serpente.direzione != pygame.math.Vector2(0, -1):
                serpente.nuova_direzione = pygame.math.Vector2(0, 1)
            if event.key == pygame.K_LEFT and serpente.direzione != pygame.math.Vector2(1, 0):
                serpente.nuova_direzione = pygame.math.Vector2(-1, 0)
            if event.key == pygame.K_RIGHT and serpente.direzione != pygame.math.Vector2(-1, 0):
                serpente.nuova_direzione = pygame.math.Vector2(1, 0)

    # 1. muovo il serpente
    serpente.muoviserpente()
    # 2. verifico collisioni (che fa succedere cose) 
    serpente.collisione(frutto, spinacina)
    serpente.morte()
    # 3. spawn spinacina
    spinacina.spawn_spinacina(serpente.corpo)
    # 4. disegno tutti gli elementi
    screen.fill((144, 238, 144))
    screen.blit(sfondo,(0,0))
    frutto.disegna_frutta()
    serpente.disegna_serpente()
    spinacina.disegna_spinacina()
    
    #grass.disegna_erba()
    # 5. aggiorno schermo
    pygame.display.update()
    clock.tick(fps)


