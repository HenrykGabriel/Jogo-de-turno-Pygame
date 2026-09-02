import pygame

class Cavaleiro:

    def __init__(self):

        self.classe = "Cavaleiro"

        self.caminho_imagem = "assets/cavaleiro/Cavaleiro.png"

        self.vida_maxima = 60

        self.vida = self.vida_maxima

        self.dano = 7

        self.chance_critico = 3

        self.critico = 1.5

        self.esquiva = 3

        self.escudo = 5

        self.larg_frame = 220
        self.alt_frame = 220
        self.qtd_frames = 10