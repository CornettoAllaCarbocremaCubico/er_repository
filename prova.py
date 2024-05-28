import pygame

class Bottone:
    def __init__(self, pos, larghezza, altezza, testo) -> None:
        self.cliccato = False
        self.red = (200, 0, 0)
        self.blue = (0, 0, 200)
        self.rett_colore = self.blue
        self.rett = pygame.Rect(pos, (larghezza, altezza))

        self.testo = font.render(testo, True, (255, 255, 255))  # Cambiato il colore del testo a bianco per maggiore visibilità
        self.testo_rett = self.testo.get_rect(center=self.rett.center)

    def disegna_bottone(self):
        pygame.draw.rect(screen, self.rett_colore, self.rett)
        screen.blit(self.testo, self.testo_rett)
    
    def controlla_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.rett.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                self.cliccato = True
            else:
                if self.cliccato:
                    print("cliccato")
                    if self.rett_colore == self.blue:
                        self.rett_colore = self.red
                    else:
                        self.rett_colore = self.blue

                    self.cliccato = False

# Impostazioni della finestra
WINDOW_SIZE = (1000, 800)

# Inizializzazione di Pygame
pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)
clock = pygame.time.Clock()
fps = 60
font = pygame.font.Font(None, 30)

# Creazione del bottone
bottone = Bottone((200, 650), 250, 100, "Cliccami")

# Loop principale del programma
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Riempie lo schermo con il colore nero
    screen.fill((0, 0, 0))

    # Disegna e controlla il bottone
    bottone.disegna_bottone()
    bottone.controlla_click()

    # Aggiorna lo schermo
    pygame.display.update()
    clock.tick(fps)

