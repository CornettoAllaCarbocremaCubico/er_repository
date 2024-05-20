import pygame
import random
import os, sys

class Frutto:
    def __init__(self, corpo_serpente):
        self.nuova_posizione(corpo_serpente) #Vector2 è una classe con x e y a cui
                                                                #attribuisco dei valori float
    def nuova_posizione(self, corpo_serpente):
        while True:
            self.x = random.randint(0,n_quadretti-1)
            self.y = random.randint(0,n_quadretti-1)
            self.posizione = pygame.math.Vector2(self.x, self.y)
            if self.posizione not in corpo_serpente:
                break

    def disegna_frutta(self):
        #pygame.rect(x,y,l,h)
        frutta = pygame.Rect(self.x*h_quadretto, self.y*h_quadretto, h_quadretto, h_quadretto)
        pygame.draw.rect(screen, (255,0,255), frutta)

class Spinacina:
    def __init__(self, fps, corpo_serpente):
        self.fps = fps
        self.tempo = 0
        self.prossima = random.randint(5, 10)
        self.posizionata = False
        self.tempo_scomparsa = 0
        self.nuova_posizione_spinacina(corpo_serpente)

    def nuova_posizione_spinacina(self, corpo_serpente):
        while True:
            self.x = random.randint(0, n_quadretti - 1)
            self.y = random.randint(0, n_quadretti - 1)
            self.posizione = pygame.math.Vector2(self.x, self.y)
            if self.posizione not in corpo_serpente:
                break
        self.posizionata = False
        self.tempo_scomparsa = 0
    
    def spawn_spinacina(self, corpo_serpente):
        self.tempo += 1
        if self.posizionata == True:
            self.tempo_scomparsa += 1
            if self.tempo_scomparsa / self.fps >= 5:
                self.rimuovi()
        if self.tempo / self.fps >= self.prossima and not self.posizionata:
            self.nuova_posizione_spinacina(corpo_serpente)
            self.prossima = random.randint(5, 10)
            self.tempo = 0
            self.posizionata = True
            
    def disegna_spinacina(self):
        if self.posizionata == True:
            spinacina = pygame.Rect(self.x * h_quadretto, self.y * h_quadretto, h_quadretto, h_quadretto)
            pygame.draw.rect(screen, (139, 69, 19), spinacina)

    def rimuovi(self):
        self.posizionata = False

class Serpente:
    def __init__(self) -> None:
        self.corpo = [pygame.math.Vector2(9,15), pygame.math.Vector2(8,15),
                        pygame.math.Vector2(7,15)]
        
        self.direzione = pygame.math.Vector2(1, 0)
        self.nuova_direzione = self.direzione
        self.vivo = True
    
    def disegna_serpente(self):
        for pezzo in self.corpo:
            pezzo = pygame.Rect(pezzo.x*h_quadretto, pezzo.y*h_quadretto, h_quadretto, h_quadretto)
            pygame.draw.rect(screen, (0,0,255), pezzo)
    
    def muoviserpente(self):
        if self.direzione != -self.nuova_direzione:
            self.direzione = self.nuova_direzione
        nuova_testa = self.corpo[0] + self.direzione
        self.corpo.insert(0, nuova_testa)
        self.corpo.pop()  
    
    def collisione(self, frutto, spinacina):
        if self.corpo[0] == frutto.posizione:
            frutto.nuova_posizione(self.corpo)
            self.corpo.append(self.corpo[-1])
        if self.corpo[0] == spinacina.posizione:
            self.corpo.append(self.corpo[-1])
            self.corpo.append(self.corpo[-1])
            self.corpo.append(self.corpo[-1])
            spinacina.rimuovi()
    
    def morte(self):
        if not 0 <= self.corpo[0].x < n_quadretti-1 or not 0 <= self.corpo[0].y < n_quadretti:
            self.vivo = False
        for pezzo in self.corpo[1:]:
            if self.corpo[0] == pezzo:
                self.vivo = False
    
    
pygame.init()
h_quadretto = 40
n_quadretti = 20
screen = pygame.display.set_mode((h_quadretto*n_quadretti, h_quadretto*n_quadretti))
clock = pygame.time.Clock()
fps = 5

serpente = Serpente()
frutto = Frutto(serpente.corpo)
spinacina = Spinacina(fps, serpente.corpo)


SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)


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
    screen.fill("Light Green")
    frutto.disegna_frutta()
    serpente.disegna_serpente()
    spinacina.disegna_spinacina()
    # 5. aggiorno schermo
    pygame.display.update()
    clock.tick(fps)


