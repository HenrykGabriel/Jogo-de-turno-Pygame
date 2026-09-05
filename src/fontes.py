import pygame
from config import caminho_asset

class Fontes:
    def __init__(self):

        self.titulo = pygame.font.Font(caminho_asset("fonts/Cinzel-Bold.ttf"), 80)

        self.texto_maior = pygame.font.Font(caminho_asset("fonts/Cinzel-Bold.ttf"), 40)

        self.texto_normal_bold = pygame.font.Font(caminho_asset("fonts/Cinzel-Bold.ttf"), 22)

        self.texto_normal = pygame.font.Font(caminho_asset("fonts/Cinzel-Medium.ttf"), 20)

        self.texto_pequeno_bold = pygame.font.Font(caminho_asset("fonts/Cinzel-Bold.ttf"), 18)

        self.texto_pequeno = pygame.font.Font(caminho_asset("fonts/Cinzel-Medium.ttf"), 16)