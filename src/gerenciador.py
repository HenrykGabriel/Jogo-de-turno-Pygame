import pygame
from inimigos import Inimigo
from combate import Combate
from dados_fase import dados

class Gerenciador:
    def __init__(self, jogador):

        self.cenario_atual = "Campo aberto"
        
        self.fase_atual = 1

        self.jogando = False

        self.jogador = jogador

        self.inimigos = []

        self.combate = None

        self.dados = dados
        

    def rodar(self, janela, eventos):

        if self.jogando == False:

            self.inimigos = self.criar_inimigos()

            self.combate = Combate(
                self.jogador,
                self.inimigos
            )

            self.jogando = True

        resultado = self.combate.comecar(janela, eventos, self.cenario_atual)

        if resultado == "vitoria":
            self.fase_atual += 1
            self.jogando = False

        elif resultado == "derrota":
            self.jogando = False

    def criar_inimigos(self):

        inimigos = []

        indice_fase = self.fase_atual - 1

        dados = self.dados[self.cenario_atual][indice_fase]

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