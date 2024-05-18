import pygame, random


class Frutto:
    def __init__(self):
        self.x = random.randint(0,n_quadretti-1)
        self.y = random.randint(0,n_quadretti-1)
        self.posizione = pygame.math.Vector2(self.x, self.y)
    
    def disegna_frutta(self):
        #pygame.rect(x,y,l,h)
        frutta = pygame.Rect(self.x*h_quadretto, self.y*h_quadretto, h_quadretto, h_quadretto)
        pygame.draw.rect(screen, (255,0,255), frutta)

pygame.init()
h_quadretto = 40
n_quadretti = 20
screen = pygame.display.set_mode((h_quadretto*n_quadretti, h_quadretto*n_quadretti))
clock = pygame.time.Clock()

frutto = Frutto()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill("Light Green")
    frutto.disegna_frutta()
    pygame.display.update()
    clock.tick(60)