import pygame

pygame.init()

pygame.mixer.init()

class Sons:
    def __init__(self):

        self.musica_fundo = "sounds/musica_fundo.mp3"

        self.volume_musica = 0.3
        self.volume_efeito = 0.8

        self.clique = pygame.mixer.Sound("sounds/clique.mp3") 

        self.clique.set_volume(self.volume_efeito)

    def iniciar_musica(self):

        pygame.mixer.music.load(self.musica_fundo)
        pygame.mixer.music.set_volume(self.volume_musica)
        pygame.mixer.music.play(-1)

    def som_clique(self):

        self.clique.play()