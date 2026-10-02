import pygame
from config import caminho_asset

class Mago:

    def __init__(self):

        self.classe = "Mago"

        self.caminho_imagem = caminho_asset("mago/Mago.png")

        self.vida_maxima = 60

        self.vida = self.vida_maxima

        self.dano = 7

        self.chance_critico = 3

        self.critico = 1.5

        self.esquiva = 3

        self.escudo_maximo = 5

        self.larg_frame = 220

        self.alt_frame = 220
        
        self.qtd_frames = 7

        self.velocidade_animacao = 80

        self.som_ataque = caminho_asset("sounds/som_classes/som_ataque_cavaleiro.mp3")

        sprite_sheet = pygame.image.load(self.caminho_imagem).convert_alpha()

        frame_width = sprite_sheet.get_width() // self.qtd_frames
        frame_height = sprite_sheet.get_height()

        img = sprite_sheet.subsurface(pygame.Rect(0, 0, frame_width, frame_height))
        self.imagem = pygame.transform.scale(img, (self.larg_frame, self.alt_frame))
        
        self.imagem_rect = self.imagem.get_rect()