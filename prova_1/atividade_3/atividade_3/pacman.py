import pygame
import cenario as cn
pygame.init()

screen = pygame.display.set_mode((800, 600), 0)

AMARELO = (255, 255, 0)
PRETO = (0, 0, 0)
AZUL = (0, 0, 255)
VELOCIDADE = 1


class Cenario:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.matriz = cn.cenario

    def pintar_linha(self, tela, numero_linha, linha):
        for numero_coluna, coluna in enumerate(linha):
            x = numero_coluna * self.tamanho
            y = numero_linha * self.tamanho
            if coluna == 2:
                cor = PRETO
                pygame.draw.rect(tela, cor, (x, y, self.tamanho, self.tamanho), 0)

            if coluna == 1:
                cor = AZUL
                pygame.draw.rect(tela, cor, (x, y, self.tamanho, self.tamanho), 0)
                pygame.draw.rect(tela, PRETO, (x, y, self.tamanho, self.tamanho),1,0)

            if coluna == 3:
                cor == AMARELO
                pygame.draw.rect(tela, cor, (x, y, self.tamanho, self.tamanho), 0)
                print(self.matriz)
    def pintar(self, tela):
        for numero_linha, linha in enumerate(self.matriz):
            self.pintar_linha(tela, numero_linha, linha)

class Pacman:
    def __init__(self, tamanho,):
        self.x_m = 0
        self.y_m = 0
        self.coluna = self.x_m
        self.linha = self.y_m
        self.centro_x = 400
        self.centro_y = 300
        self.tamanho = tamanho
        self.vel_x = 0
        self.vel_y = 0
        self.raio = self.tamanho // 2

    def processar_eventos(self, eventos):

        for e in eventos:
            if e.type == pygame.MOUSEBUTTONDOWN:
                x_m, y_m = pygame.mouse.get_pos()

                self.x_m = x_m * self.tamanho
                self.y_m = y_m * self.tamanho

    def calcular_regras(self):
        self.coluna = self.x_m * self.tamanho
        self.linha = self.y_m * self.tamanho

        self.centro_x = int(self.coluna * self.tamanho + self.raio)
        self.centro_y = int(self.linha * self.tamanho + self.raio)


    def pintar(self, tela):
        # Desenhar o corpo do Pacman
        pygame.draw.circle(tela, AMARELO, (self.centro_x, self.centro_y), self.raio, 0)

        # Desenho da boca do Pacman
        canto_boca = (self.centro_x, self.centro_y)
        labio_superior = (self.centro_x + self.raio, self.centro_y - self.raio)
        labio_inferior = (self.centro_x + self.raio, self.centro_y)
        pontos = [canto_boca, labio_superior, labio_inferior]
        pygame.draw.polygon(tela, PRETO, pontos, 0)

        # Olho do Pacman
        olho_x = int(self.centro_x + self.raio / 3)
        olho_y = int(self.centro_y - self.raio * 0.70)
        olho_raio = int(self.raio / 10)
        pygame.draw.circle(tela, PRETO, (olho_x, olho_y), olho_raio, 0)



if __name__ == "__main__":
    size = 600 // 30
    eventos = pygame.event.get()
    eventos = pygame.event.get()
    pacman = Pacman(size)
    cenario = Cenario(size)

    while True:
        # Calcular as regras
        pacman.calcular_regras()

        # Pintar a tela
        screen.fill(PRETO)
        cenario.pintar(screen)
        pacman.pintar(screen)
        pygame.display.update()
        pygame.time.delay(100)


        # Captura os eventos
        eventos = pygame.event.get()
        for e in eventos:
            if e.type == pygame.QUIT:
                exit()
        pacman.processar_eventos(eventos)
