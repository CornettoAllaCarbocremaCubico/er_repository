import pygame
from pygame import mixer
import random
import os
import sys
from Frutto import Frutto
from spinacina import Spinacina
from Serpente import Serpente
from Punteggio import Punteggio
from Bottone import Bottone

pygame.init()
pygame.display.set_caption("Snake")
h_quadretto = 40
n_quadretti = 15
screen = pygame.display.set_mode((h_quadretto * n_quadretti, h_quadretto * n_quadretti))
clock = pygame.time.Clock()
fps = 8
font = pygame.font.Font("Snakebite-Regular.ttf", 180)
fontpunteggio = pygame.font.Font(None, 40)

mixer.init()
sound_morte = mixer.Sound('145421__soughtaftersounds__haunted-organ-1.mp3')

def disegna_testo(text, font, color, surface, x, y):
    text = font.render(text, True, color)
    textrect = text.get_rect()
    textrect.topleft = (x, y)
    surface.blit(text, textrect)

def mostra_schermata_di_morte():
    morte_font = pygame.font.Font("DeathMohawk_PERSONAL_USE_ONLY.otf", 155)
    morte_surf = morte_font.render('GAME OVER', True, (155, 0, 0))
    morte_rect = morte_surf.get_rect(center = (n_quadretti * h_quadretto // 2, n_quadretti * h_quadretto // 2))
    screen.blit(morte_surf, morte_rect)
    pygame.display.flip()
    pygame.time.wait(9000) 
    main_menu()

def main_menu():
    start_button = Bottone((70, 330), 200, 50, "Start")
    quit_button = Bottone((330, 330), 200, 50, "Exit")

    trasparenza_testo = 0

    clock = pygame.time.Clock()

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
        if trasparenza_testo < 255:
            trasparenza_testo += 1

        disegna_testo('Snake', font, (0, 0, 0), screen, 125, 100)
        
        start_button.disegna_bottone(screen)
        quit_button.disegna_bottone(screen)

        pygame.display.flip()
        clock.tick(30)

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
        frutto.disegna_frutta()
        serpente.disegna_serpente()
        spinacina.disegna_spinacina()
        punteggio.disegna_punteggio(serpente.corpo, fontpunteggio)

        pygame.display.update()
        clock.tick(fps)

    mostra_schermata_di_morte()
    sound_morte.play()


if __name__ == '__main__':
    main_menu()
