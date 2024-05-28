import pygame
import random
import os, sys
from Frutto import Frutto
from spinacina import Spinacina
from Serpente import Serpente
from Punteggio import Punteggio
from Bottone import Bottone

pygame.init()
h_quadretto = 40
n_quadretti = 15
screen = pygame.display.set_mode((h_quadretto * n_quadretti, h_quadretto * n_quadretti))
clock = pygame.time.Clock()
fps = 8
font = pygame.font.Font(None, 35)

def disegna_testo(text, font, color, surface, x, y):
    text = font.render(text, True, color)
    textrect = text.get_rect()
    textrect.topleft = (x, y)
    surface.blit(text, textrect)

def main_menu():
    start_button = Bottone((150, 150), 200, 50, "Inizia Gioco")
    quit_button = Bottone((150, 350), 200, 50, "Esci")
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if start_button.controllaclick():
            game()
        if quit_button.controllaclick():
            pygame.quit()
            sys.exit()

        screen.fill((173, 216, 230))

    # 1. muovo il serpente
    serpente.muoviserpente()
    # 2. verifico collisioni (che fa succedere cose) 
    serpente.collisione(frutto, spinacina)
    serpente.morte()
     # 3. spawn spinacina
    spinacina.spawn_spinacina(serpente.corpo)
    # 4. disegno tutti gli elementi
    screen.blit(sfondo, (0,0))
    frutto.disegna_frutta()
    serpente.disegna_serpente()
    spinacina.disegna_spinacina()
    serpente.punteggio()
    # 5. aggiorno schermo
    pygame.display.update()
    clock.tick(fps)
  


    disegna_testo('Menu Principale', font, (0, 0, 0), screen, 150, 50)
    start_button.disegna_bottone(screen)
    quit_button.disegna_bottone(screen)

    pygame.display.flip()

def game():
    serpente = Serpente()
    frutto = Frutto(serpente.corpo)
    spinacina = Spinacina(fps, serpente.corpo)
    punteggio = Punteggio()
    sfondo = pygame.image.load("sfondo snake2.jpg")
    sfondo = pygame.transform.scale(sfondo, (h_quadretto * n_quadretti, h_quadretto * n_quadretti))

    SCREEN_UPDATE = pygame.USEREVENT
    pygame.time.set_timer(SCREEN_UPDATE, 150)

    while serpente.vivo:
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

        serpente.muoviserpente()
        serpente.collisione(frutto, spinacina)
        serpente.morte()
        spinacina.spawn_spinacina(serpente.corpo)

        screen.blit(sfondo, (0, 0))
        punteggio.disegna_punteggio(serpente.corpo, font)
        frutto.disegna_frutta()
        serpente.disegna_serpente()
        spinacina.disegna_spinacina()
        punteggio.disegna_punteggio(serpente.corpo, font)

        pygame.display.update()
        clock.tick(fps)

    main_menu()

def options():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

        screen.fill((0, 0, 0))
        disegna_testo('Opzioni', font, (255, 255, 255), screen, 100, 100)
        pygame.display.flip()

    main_menu()

if __name__ == '__main__':
    main_menu()
