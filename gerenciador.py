import pygame
import copy
from config import larg_tela, alt_tela
from combate import combate
from dados_fase import cenarios
from inimigos import Inimigo

class Gerenciador:
    def __init__(self):
        self.lista_inimigos = cenarios

        self.cenario_atual = "floresta"

        self.fase_atual = 1

        self.turno = "jogador"

        self.larg_painel = larg_tela
        
        self.alt_painel = alt_tela // 3

        self.larg_cenario = larg_tela

        self.alt_cenario = alt_tela - self.alt_painel

        self.img_cenario = pygame.image.load(f"assets/cenarios/{self.cenario_atual}.png").convert_alpha()

        self.cenario = pygame.transform.scale(self.img_cenario, (self.larg_cenario, self.alt_cenario))

        self.img_painel = pygame.image.load(f"assets/cenarios/painel.png").convert_alpha()

        self.painel = pygame.transform.scale(self.img_painel, (self.larg_painel, self.alt_painel))


        

    def rodar(self, janela, jogador):

        if self.cenario_atual == "floresta" and self.fase_atual == 1:

            inimigos_fase = self.criar_inimigos()

            combate(janela, self, inimigos_fase, jogador)

    def criar_inimigos(self):

        inimigos = []

        indice_fase = self.fase_atual - 1

        dados = self.lista_inimigos[self.cenario_atual][indice_fase]

        for inimigo in dados:

            inimigos.append(Inimigo(
                inimigo["nome"],
                inimigo["vida"],
                inimigo["dano"],
                inimigo["esquiva"],
                inimigo["chance_critico"], 
                inimigo["critico"], 
                inimigo["caminho"],
                inimigo["largura"],
                inimigo["altura"], 
                inimigo["qtd_frames"] 
            ))

        return inimigos