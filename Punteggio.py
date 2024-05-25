import pygame
h_quadretto = 40
n_quadretti = 15
screen = pygame.display.set_mode((h_quadretto*n_quadretti, h_quadretto*n_quadretti))


class Punteggio:
    def __init__(self):
        self.punteggio_x = int(h_quadretto*n_quadretti - 40)
        self.punteggio_y = int(h_quadretto*n_quadretti - 60)
        
    def disegna_punteggio(self, corpo, font):
        testo_punteggio = str(len(corpo)-3)
        sup_punteggio = font.render(testo_punteggio, True, (56,74,12))
        rect_punteggio = sup_punteggio.get_rect(center = (self.punteggio_x, self.punteggio_y))
        screen.blit(sup_punteggio, rect_punteggio)

