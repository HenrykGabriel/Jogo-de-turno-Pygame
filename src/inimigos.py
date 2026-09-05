import pygame
import random

class Inimigo:
    def __init__(self, nome, vida, dano, esquiva, chance_critico, critico, caminho_sprite, larg_frame, alt_frame, qtd_frames):

        self.nome = nome
        self.sprite_sheet = pygame.image.load(caminho_sprite).convert_alpha()
        self.larg_frame = larg_frame
        self.alt_frame = alt_frame
        self.qtd_frames = qtd_frames
        
        # Atributos
        self.vida_maxima = vida
        self.vida = self.vida_maxima
        self.dano = dano
        self.esquiva = esquiva
        self.chance_critico = chance_critico
        self.critico = critico

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

        for i in range(qtd_frames):

            tamanho_corte = pygame.Rect(i * frame_width, 0, frame_width, frame_height)

            frame_normal = self.sprite_sheet.subsurface(tamanho_corte)

            frame_redimensionado = pygame.transform.scale(frame_normal, (self.larg_frame, self.alt_frame))

            self.frames_ataque.append(frame_redimensionado)

    def iniciar_ataque(self):

        self.atacando = True

        self.frame_atual = 0

        self.tempo_frame = pygame.time.get_ticks()


    def atacar(self, jogador):

        self.iniciar_ataque()

        dano_critico = False

        self.dano_normal = self.dano
        
        num = random.randint(1, 100)

        if num <= self.chance_critico:

            dano_final = self.dano * self.critico

            dano_critico = True

        else:

            dano_final = self.dano

        return jogador.receber_dano(dano_final, dano_critico)

    def receber_dano(self, dano_jogador, dano_critico):

        num = random.randint(1, 100)
        
        if num <= self.esquiva:

            return "ESQUIVOU"

        else:

            self.vida -= dano_jogador
            
            if dano_critico == True:

                return f"DANO CRITÍCO: {dano_jogador}"
            
            else:

                return dano_jogador

    def draw(self, janela):

        if self.atacando:

            tempo_atual = pygame.time.get_ticks()

            if tempo_atual - self.tempo_frame >= self.velocidade_animacao:

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