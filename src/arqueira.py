import pygame
from config import caminho_asset

class Arqueira:

    def __init__(self):

        self.classe = "Arqueira"

        self.caminho_imagem = caminho_asset("arqueira/Arqueira.png")

        self.vida_maxima = 15

        self.vida = self.vida_maxima

        self.dano = 4

        self.chance_critico = 5

        self.critico = 1.5

        self.esquiva = 6

        self.escudo_maximo = 2

        self.larg_frame = 210

        self.alt_frame = 210
        
        self.qtd_frames = 10

        self.velocidade_animacao = 60

        self.som_ataque = caminho_asset("sounds/som_classes/som_ataque_arqueira.mpeg")

        sprite_sheet = pygame.image.load(self.caminho_imagem).convert_alpha()

        frame_width = sprite_sheet.get_width() // self.qtd_frames
        frame_height = sprite_sheet.get_height()

        img = sprite_sheet.subsurface(pygame.Rect(0, 0, frame_width, frame_height))
        self.imagem = pygame.transform.scale(img, (self.larg_frame, self.alt_frame))
        
        self.imagem_rect = self.imagem.get_rect()