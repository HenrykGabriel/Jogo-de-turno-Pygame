import pygame
from config import caminho_asset

pygame.init()

pygame.mixer.init()

class Sons:
    def __init__(self):

        self.musica_fundo = caminho_asset("sounds/musica_fundo.mp3")

        self.volume_musica = 0.22
        self.volume_musica_combate = 0.1
        self.volume_efeito = 0.8

        self.clique = pygame.mixer.Sound(caminho_asset("sounds/clique.mp3")) 

        self.clique.set_volume(self.volume_efeito)

    def iniciar_musica(self):

        pygame.mixer.music.load(self.musica_fundo)
        pygame.mixer.music.set_volume(self.volume_musica)
        pygame.mixer.music.play(-1)

    def abaixar_volume_musica(self):

        pygame.mixer.music.set_volume(self.volume_musica_combate)

    def aumentar_volume_musica(self):

        pygame.mixer.music.set_volume(self.volume_musica)

    def som_clique(self):

        self.clique.play()