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
fps = 7
font = pygame.font.Font("Snakebite-Regular.ttf", 180)
fontpunteggio = pygame.font.Font(None, 40)
mixer.init()
suono_morte = pygame.mixer.Sound('735797__leochavolla__goofy-instrument-jumpscare.wav')
suono_vittoria = pygame.mixer.Sound("397353__plasterbrain__tada-fanfare-g.flac")


def disegna_testo(text, font, color, surface, x, y):
    text = font.render(text, True, color)
    textrect = text.get_rect()
    textrect.topleft = (x, y)
    surface.blit(text, textrect)

def mostra_schermata_di_morte():
    morte_font = pygame.font.Font("DeathMohawk_PERSONAL_USE_ONLY.otf", 155)
    morte_surf = morte_font.render('GAME OVER', True, (0, 0, 0))
    morte_rect = morte_surf.get_rect(center = (n_quadretti * h_quadretto // 2, n_quadretti * h_quadretto // 2))
    screen.blit(morte_surf, morte_rect)
    pygame.display.flip()
    suono_morte.play()
    pygame.time.wait(3500) 
    main_menu()

def schermata_vittoria():
    vittoria_font = pygame.font.Font("Snakebite-Regular.ttf", 175)
    vittoria_surf = vittoria_font.render('YOU WIN!', True, (0, 0, 0))
    vittoria_rect = vittoria_surf.get_rect(center = (n_quadretti * h_quadretto // 2, n_quadretti * h_quadretto // 2))
    screen.blit(vittoria_surf, vittoria_rect)
    suono_vittoria.play()
    pygame.display.flip()
    pygame.time.wait(3500)
    main_menu()

def main_menu():
    start_button = Bottone((70, 330), 200, 50, "Start")
    quit_button = Bottone((330, 330), 200, 50, "Exit")

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if start_button.controllaclick():
            pygame.time.wait(1500)
            game()

        if quit_button.controllaclick():
            pygame.quit()
            sys.exit()

        screen.fill((173, 216, 230))  

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
    vittoria = False

    while serpente.vivo and not vittoria:
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

        if len(serpente.corpo) > 40:  # Condizione di vittoria
            vittoria = True

        screen.blit(sfondo, (0, 0))
        frutto.disegna_frutta()
        serpente.disegna_serpente()
        spinacina.disegna_spinacina()
        punteggio.disegna_punteggio(serpente.corpo, fontpunteggio)
       
        pygame.display.update()
        clock.tick(fps)

    if vittoria:
        schermata_vittoria()
    else:
        mostra_schermata_di_morte()

if __name__ == '__main__':
    main_menu()
