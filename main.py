import pygame, random

class Frutto:
    def __init__(self):
        self.x = random.randint(0,n_quadretti-1)
        self.y = random.randint(0,n_quadretti-1)
        self.posizione = pygame.math.Vector2(self.x, self.y) #Vector2 è una classe con x e y a cui
                                                                #attribuisco dei valori float
    
    def disegna_frutta(self):
        #pygame.rect(x,y,l,h)
        frutta = pygame.Rect(self.x*h_quadretto, self.y*h_quadretto, h_quadretto, h_quadretto)
        pygame.draw.rect(screen, (255,0,255), frutta)

class Serpente:
    def __init__(self) -> None:
        self.corpo = [pygame.math.Vector2(9,15), pygame.math.Vector2(8,15),
                        pygame.math.Vector2(7,15)]
        
        self.direzione = pygame.math.Vector2(1, 0)
    
    def disegna_serpente(self):
        for pezzo in self.corpo:
            pezzo = pygame.Rect(pezzo.x*h_quadretto, pezzo.y*h_quadretto, h_quadretto, h_quadretto)
            pygame.draw.rect(screen, (0,0,255), pezzo)
    
    def muoviserpente(self):
        nuovatesta = self.corpo[0] + self.direzione  
        self.corpo.pop()  
        self.corpo.insert(0, nuovatesta)  

    def cambia_direzione(self, nuova_direzione):
        if nuova_direzione != -self.direction:
            self.direction = nuova_direzione
            
    

pygame.init()
h_quadretto = 40
n_quadretti = 20
screen = pygame.display.set_mode((h_quadretto*n_quadretti, h_quadretto*n_quadretti))
clock = pygame.time.Clock()

frutto = Frutto()
serpente = Serpente()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == SCREEN_UPDATE:
            serpente.muoviserpente()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                serpente.direzione = pygame.math.Vector2(0, -1)
            if event.key == pygame.K_DOWN:
                serpente.direzione = pygame.math.Vector2(0, 1)
            if event.key == pygame.K_LEFT:
                serpente.direzione = pygame.math.Vector2(-1, 0)
            if event.key == pygame.K_RIGHT:
                serpente.direzione = pygame.math.Vector2(1, 0)

    screen.fill("Light Green")
    frutto.disegna_frutta()
    serpente.disegna_serpente()
    pygame.display.update()
    clock.tick(60)