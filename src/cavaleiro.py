import pygame
from config import caminho_asset

class Cavaleiro:

    def __init__(self):

        self.classe = "Cavaleiro"

        self.caminho_imagem = caminho_asset("cavaleiro/Cavaleiro.png")

        self.vida_maxima = 22

        self.vida = self.vida_maxima

        self.dano = 3

        self.chance_critico = 2

        self.critico = 1.5

        self.esquiva = 4

        self.escudo_maximo = 4

        self.larg_frame = 220

        self.alt_frame = 220
        
        self.qtd_frames = 8

        self.velocidade_animacao = 60

        self.som_ataque = caminho_asset("sounds/som_classes/som_ataque_cavaleiro.mp3")

        sprite_sheet = pygame.image.load(self.caminho_imagem).convert_alpha()

        frame_width = sprite_sheet.get_width() // self.qtd_frames
        frame_height = sprite_sheet.get_height()

        img = sprite_sheet.subsurface(pygame.Rect(0, 0, frame_width, frame_height))
        self.imagem = pygame.transform.scale(img, (self.larg_frame, self.alt_frame))
        
        self.imagem_rect = self.imagem.get_rect()