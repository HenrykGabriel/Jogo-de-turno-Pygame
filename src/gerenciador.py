import pygame
from inimigos import Inimigo
from combate import Combate
from dados_fase import dados
from jogador import Jogador
from cavaleiro import Cavaleiro
from menu import Menu
from fontes import Fontes
from tela_resultado import TelaResultado
from escolher_classe import EscolherClasse
from escolher_carta import TelaEscolherCarta
from sons import Sons

class Gerenciador:
    def __init__(self):

        self.cenario_atual = "Campo aberto"

        self.sons = Sons()
        
        self.fase_atual = 1

        self.jogando = False

        self.jogador = None

        self.inimigos = []

        self.combate = None

        self.dados = dados

        self.estado = "menu"

        self.resultado_combate = None

        self.acao = None

        self.menu = Menu(Fontes())

        self.tela_resultado = TelaResultado(Fontes())

        self.tela_escolher_classe = EscolherClasse(Fontes())
        self.tela_escolher_carta = TelaEscolherCarta(Fontes())

    def rodar(self, janela, eventos):

        if self.estado == "menu":

            self.menu.draw(janela)
            self.menu.update(eventos)

            if self.menu.update_comecar(eventos) == True:
                self.estado = "escolher_classe"

        elif self.estado == "escolher_classe":

            classe_escolhida = self.tela_escolher_classe.rodar(janela, eventos)

            if classe_escolhida:
                self.jogador = Jogador(classe_escolhida)
                self.estado = "jogando"

        elif self.estado == "jogando":

            if self.jogando == False:

                self.inimigos = self.criar_inimigos()

                self.jogador.vida = self.jogador.vida_maxima
                self.jogador.escudo = 0

                self.combate = Combate(
                    self.jogador,
                    self.inimigos
                )

                self.sons.abaixar_volume_musica()

                self.jogando = True

            self.resultado_combate = self.combate.comecar(janela, eventos, self.cenario_atual, self.fase_atual)

            if self.resultado_combate == "vitoria":

                self.sons.aumentar_volume_musica()

                if self.fase_atual == 3:

                    if self.cenario_atual == "Campo aberto":

                        self.cenario_atual = "Deserto"
                        self.fase_atual = 1
                        self.jogando = False

                    elif self.cenario_atual == "Deserto":
                    
                        self.cenario_atual = "Zona vulcânica"
                        self.fase_atual = 1
                        self.jogando = False

                    elif self.cenario_atual == "Zona vulcânica":
                                        
                        self.fase_atual += 1
                        self.jogando = False

                else:

                    self.fase_atual += 1
                    self.jogando = False

                self.estado = "tela_resultado"

            elif self.resultado_combate == "derrota":

                self.sons.aumentar_volume_musica()
                
                self.jogando = False
                self.estado = "tela_resultado"

        elif self.estado == "tela_resultado":

            self.acao = self.tela_resultado.rodar(janela, eventos, self.cenario_atual, self.fase_atual, self.resultado_combate)

            if self.acao == "sair":
                return "sair"

            elif self.acao == "reiniciar":
                self.estado = "menu"
                self.menu.estado = "menu"
                self.fase_atual = 1
                self.cenario_atual = "Campo aberto"
                self.jogando = False

            elif self.acao == "escolher carta":
                self.estado = "tela_escolher_carta"

        elif self.estado == "tela_escolher_carta":
            
            self.acao = self.tela_escolher_carta.rodar(janela, eventos, self.cenario_atual, self.jogador)

            if self.acao == "escolheu carta":
                self.estado = "jogando"
                self.jogador.atacando = False


    def criar_inimigos(self):

        inimigos = []

        indice_fase = self.fase_atual - 1

        dados = self.dados[self.cenario_atual][indice_fase]

        for inimigo in dados:

            inimigos.append(Inimigo(
                inimigo["nome"],
                inimigo["vida"],
                inimigo["dano_max"],
                inimigo["dano_min"],
                inimigo["esquiva"],
                inimigo["chance_critico"], 
                inimigo["critico"], 
                inimigo["caminho"],
                inimigo["largura"],
                inimigo["altura"], 
                inimigo["qtd_frames"],
                inimigo["velocidade_animacao"],
                inimigo["som_ataque"]
            ))

        return inimigos