import pygame

class Guerreiro:

    def __init__(self):

        self.classe = "Cavaleiro"

        self.img = pygame.image.load("assets/cavaleiro/Cavaleiro.png")

        self.imagem = pygame.transform.scale(self.img, (140, 150))

        self.vida = 60

        self.dano = 7

        self.chance_critico = 5

        self.critico = 1.5

        self.esquiva = 3