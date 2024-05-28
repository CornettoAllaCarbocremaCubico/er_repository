import pygame

class Bottone:
    def __init__(self, pos, larghezza, altezza, testo):
        self.cliccato = False
        self.rett = pygame.Rect(pos, (larghezza, altezza))
        self.testo = pygame.font.Font(None, 35).render(testo, True, (255, 255, 255))
        self.testo_rett = self.testo.get_rect(center=self.rett.center)
    
    def disegna_bottone(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), self.rett)
        screen.blit(self.testo, self.testo_rett)

    def controllaclick(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.rett.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0] and not self.cliccato:
                self.cliccato = True
                return True
            if not pygame.mouse.get_pressed()[0]:
                self.cliccato = False
        return False


