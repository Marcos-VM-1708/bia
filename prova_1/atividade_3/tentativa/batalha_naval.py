import cenario as cn
import pygame

tela = pygame.display.set_mode((800, 600), 0)

class cenario():
    def __init__(self, tela):
        self.matriz = cn.cenario
        self.x = 0
        self.y = 0
        self.x_matriz = self.matriz[self.x][self.y]




eventos = pygame.event.get()
for e in eventos:
    if e.type == pygame.QUIT:
        exit()