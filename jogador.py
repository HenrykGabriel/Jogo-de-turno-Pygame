import pygame
import random

class Jogador:
    def __init__(self):

        self.classe = ""

        self.imagem = None

        self.rect = None

        self.vivo = True

        self.vida = 0

        self.dano = 0

        self.dano_normal = 0

        self.chance_critico = 0

        self.critico = 0

        self.esquiva = 0

        self.habilidades = []

    def escolher_classe(self, classe):

        self.classe = classe.classe

        self.imagem = classe.imagem

        self.rect = self.imagem.get_rect()

        self.vida = classe.vida

        self.dano = classe.dano

        self.chance_critico = classe.chance_critico

        self.critico = classe.critico

        self.esquiva = classe.esquiva

    def atacar(self, inimigo):

        self.dano_normal = self.dano

        num = random.randint(1, 100)

        if num <= self.chance_critico:

            dano_final = self.dano * self.critico

        else:

            dano_final = self.dano

        inimigo.receber_dano(dano_final)

    def receber_dano(self, dano_inimigo):

        num = random.randint(1, 100)

        if num <= self.esquiva:

            pass

        else:

            self.vida -= dano_inimigo

    def draw(self, janela):

        janela.blit(self.imagem, self.rect)