import pygame
import random
from config import caminho_asset

class Jogador:
    def __init__(self, classe):

        self.classe = classe.classe
        self.sprite_sheet = pygame.image.load(classe.caminho_imagem).convert_alpha()
        self.larg_frame = classe.larg_frame
        self.alt_frame = classe.alt_frame
        self.qtd_frames = classe.qtd_frames

        # Sons

        self.som_ataque = pygame.mixer.Sound(classe.som_ataque)
        
        # Atributos
        self.vida_maxima = classe.vida_maxima
        self.vida = classe.vida
        self.dano = classe.dano
        self.esquiva = classe.esquiva
        self.chance_critico = classe.chance_critico
        self.critico = classe.critico
        self.escudo_maximo = classe.escudo_maximo
        self.escudo = 0

        # Lógica de Frames de Animação
        frame_width = self.sprite_sheet.get_width() // self.qtd_frames
        frame_height = self.sprite_sheet.get_height()

        # Guarda o frame parado do índice 0
        img_parado = self.sprite_sheet.subsurface(pygame.Rect(0, 0, frame_width, frame_height))
        self.imagem_parado = pygame.transform.scale(img_parado, (self.larg_frame, self.alt_frame))
        
        # A imagem atual que será desenhada na tela
        self.imagem = self.imagem_parado
        self.rect = self.imagem.get_rect()

        # IMAGEM DO ESCUDO
        self.img_escudo = pygame.image.load(caminho_asset("escudo/Escudo.png"))
        self.imagem_escudo = pygame.transform.scale(self.img_escudo, (80, 160))
        self.imagem_escudo_rect = self.imagem_escudo.get_rect()

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

    def iniciar_ataque(self):
    
        self.atacando = True

        self.frame_atual = 0

        self.tempo_frame = pygame.time.get_ticks()

    def atacar(self, inimigo):

        self.iniciar_ataque()

        dano_critico = False

        self.dano_normal = self.dano

        num = random.randint(1, 100)

        if num <= self.chance_critico:

            dano_final = self.dano * self.critico
            dano_critico = True

        else:

            dano_final = self.dano

        self.som_ataque.play()

        return inimigo.receber_dano(dano_final, dano_critico)

    def receber_dano(self, dano_inimigo, dano_critico):

        resultado = None

        num = random.randint(1, 100)

        if num <= self.esquiva:

            resultado = "ESQUIVOU"

        else:

            if self.escudo > 0:

                if dano_inimigo <= self.escudo:

                    self.escudo -= dano_inimigo

                    resultado = "BLOQUEADO"

                else:

                    dano_inimigo -= self.escudo

                    self.escudo = 0

                    self.vida -= dano_inimigo

                    if dano_critico == True:

                        resultado = f"CRITÍCO: {dano_inimigo}"
                    
                    else:

                        resultado = dano_inimigo

            else:

                self.vida -= dano_inimigo
                
                if dano_critico == True:

                    resultado = f"CRITÍCO: {dano_inimigo}"
                
                else:

                    resultado = dano_inimigo

        return resultado


    def ativar_escudo(self):

        self.escudo = self.escudo_maximo

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

        if self.escudo > 0:

            self.imagem_escudo_rect.midleft = (
                    self.rect.right - 10,
                    self.rect.centery
                )

            janela.blit(self.imagem_escudo, self.imagem_escudo_rect)