import pygame
import random

class Jogador:
    def __init__(self, classe):

        self.classe = classe.classe
        self.sprite_sheet = pygame.image.load(classe.caminho_imagem).convert_alpha()
        self.larg_frame = classe.larg_frame
        self.alt_frame = classe.alt_frame
        self.qtd_frames = classe.qtd_frames
        
        # Atributos
        self.vida_maxima = classe.vida_maxima
        self.vida = classe.vida
        self.dano = classe.dano
        self.esquiva = classe.esquiva
        self.chance_critico = classe.chance_critico
        self.critico = classe.critico
        self.escudo = classe.escudo

        # Lógica de Frames de Animação
        frame_width = self.sprite_sheet.get_width() // self.qtd_frames
        frame_height = self.sprite_sheet.get_height()

        # Guarda o frame parado do índice 0
        img_parado = self.sprite_sheet.subsurface(pygame.Rect(0, 0, frame_width, frame_height))
        self.imagem_parado = pygame.transform.scale(img_parado, (self.larg_frame, self.alt_frame))
        
        # A imagem atual que será desenhada na tela
        self.imagem = self.imagem_parado
        self.rect = self.imagem.get_rect()

        # ESTADOS E CONTROLE DE ANIMAÇÃO
        self.frame_atual = 0
        self.atacando = False 
        self.tempo_frame = pygame.time.get_ticks()
        self.velocidade_animacao = 50

        self.frames_ataque = []

        for i in range(self.qtd_frames):

            tamanho_corte = pygame.Rect(i * frame_width, 0, frame_width, frame_height)

            frame_normal = self.sprite_sheet.subsurface(tamanho_corte)

            frame_redimensionado = pygame.transform.scale(frame_normal, (self.larg_frame, self.alt_frame))

            self.frames_ataque.append(frame_redimensionado)

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

        if self.atacando:
        
            tempo_atual = pygame.time.get_ticks()

            if tempo_atual - self.tempo_frame <= self.velocidade_animacao:

                self.tempo_frame = tempo_atual

                self.frame_atual += 1

                if self.frame_atual >= len(self.frames_ataque):

                    self.atacando = False

                    self.frame_atual = 0

                    self.imagem = self.imagem_parado

                else:

                    self.imagem = self.frames_ataque[self.frame_atual]
        
        else:

            self.imagem = self.imagem_parado

        janela.blit(self.imagem, self.rect)