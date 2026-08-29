import pygame
from config import larg_tela, alt_tela
from fontes import Fontes

class Combate:
    def __init__(self, jogador, inimigos):
        self.jogador = jogador

        self.inimigos = inimigos

        self.fontes = Fontes()
        self.texto_normal = self.fontes.texto_normal
        self.texto_pequeno = self.fontes.texto_pequeno
        self.texto_normal_bold = self.fontes.texto_normal_bold

        self.turno = "jogador"

        self.inimigo_selecionado = None

        self.turno = "jogador"

        self.larg_painel = larg_tela
        
        self.alt_painel = alt_tela // 3

        self.larg_cenario = larg_tela

        self.alt_cenario = alt_tela - self.alt_painel

        # CENARIO 1 - CAMPO ABERTO
        self.img_campo_aberto = pygame.image.load(f"assets/cenarios/Campo aberto.png").convert_alpha()

        self.campo_aberto = pygame.transform.scale(self.img_campo_aberto, (self.larg_cenario, self.alt_cenario))

        self.img_painel = pygame.image.load("assets/cenarios/painel.png").convert_alpha()

        self.painel = pygame.transform.scale(self.img_painel, (self.larg_painel, self.alt_painel))

        self.painel_rect = self.painel.get_rect(bottom=alt_tela)
        # -------------------------------------
        self.cenario_rect = self.campo_aberto.get_rect()
        
        self.jogador.rect = self.jogador.imagem.get_rect()

        self.jogador.rect.center = (
            self.cenario_rect.centerx - 240,
            self.cenario_rect.centery + 10
        )

        self.posicionar_inimigos()

        # ATRIBUTOS
        self.jogador_classe = self.texto_normal_bold.render(f"Classe: {self.jogador.classe}", True, (255, 251, 0))
        self.jogador_classe_rect = self.jogador_classe.get_rect(
                    midleft=(
                            self.painel_rect.left + 130,
                            self.painel_rect.top + 40
                        ))
        
        self.jogador_vida = self.texto_normal.render(f"Vida: {self.jogador.vida}", True, (255, 251, 0))
        self.jogador_vida_rect = self.jogador_vida.get_rect(
                    midleft=(
                            self.painel_rect.left + 60,
                            self.painel_rect.top + 80
                        ))

        self.jogador_dano = self.texto_normal.render(f"Dano: {self.jogador.dano}", True, (255, 251, 0))
        self.jogador_dano_rect = self.jogador_dano.get_rect(
                    midleft=(
                            self.painel_rect.left + 220,
                            self.painel_rect.top + 80
                        ))

        self.jogador_esquiva = self.texto_normal.render(f"Esquiva: {self.jogador.esquiva}", True, (255, 251, 0))
        self.jogador_esquiva_rect = self.jogador_esquiva.get_rect(
                    midleft=(
                            self.painel_rect.left + 60,
                            self.painel_rect.top + 130
                        ))

        self.jogador_chance_critico = self.texto_normal.render(f"Chance de crítico: {self.jogador.chance_critico}%", True, (255, 251, 0))
        self.jogador_chance_critico_rect = self.jogador_chance_critico.get_rect(
                    midleft=(
                            self.painel_rect.left + 220,
                            self.painel_rect.top + 130
                        ))

        self.jogador_critico = self.texto_normal.render(f"Crítico: {self.jogador.critico}X", True, (255, 251, 0))
        self.jogador_critico_rect = self.jogador_critico.get_rect(
                    midleft=(
                            self.painel_rect.left + 60,
                            self.painel_rect.top + 180
                        ))

        self.jogador_escudo = self.texto_normal.render(f"Escudo: {self.jogador.escudo}", True, (255, 251, 0))
        self.jogador_escudo_rect = self.jogador_escudo.get_rect(
                    midleft=(
                            self.painel_rect.left + 220,
                            self.painel_rect.top + 180
                        ))
        # CARTAS ---------------------------------------
        self.larg_cartas = 160
        self.alt_cartas = self.alt_painel - 40
        self.img_carta_ataque = pygame.image.load("assets/cartas/carta_ataque.png").convert_alpha()
        self.carta_ataque = pygame.transform.scale(self.img_carta_ataque, (self.larg_cartas, self.alt_cartas))
        self.carta_ataque_rect = self.carta_ataque.get_rect(
                    midleft=(
                            self.painel_rect.centerx + 80,
                            self.painel_rect.centery
                        ))

        self.img_carta_defesa = pygame.image.load("assets/cartas/carta_defesa.png").convert_alpha()
        self.carta_defesa = pygame.transform.scale(self.img_carta_defesa, (self.larg_cartas, self.alt_cartas))
        self.carta_defesa_rect = self.carta_defesa.get_rect(
                    midleft=(
                            self.painel_rect.centerx + 80 + self.larg_cartas + 40,
                            self.painel_rect.centery
                        ))


    def comecar(self, janela, inimigos, jogador, eventos, cenario_atual):

        self.draw(janela, cenario_atual)

    def draw(self, janela, cenario_atual):

        if cenario_atual == "Campo aberto":
            janela.blit(self.campo_aberto, (0, 0))

        janela.blit(self.painel, (0, self.alt_cenario))

        self.jogador.draw(janela)

        for inimigo in self.inimigos:

            inimigo.draw(janela)

        self.draw_atributos(janela)

        self.draw_cartas(janela)

    def posicionar_inimigos(self):

        x = self.cenario_rect.centerx + 130
        y = self.cenario_rect.centery + 10

        for inimigo in self.inimigos:

            inimigo.rect.center = (x, y)

            x += inimigo.rect.width + 40

    def draw_atributos(self, janela):

        janela.blit(self.jogador_classe, self.jogador_classe_rect)

        janela.blit(self.jogador_vida, self.jogador_vida_rect)

        janela.blit(self.jogador_dano, self.jogador_dano_rect)

        janela.blit(self.jogador_esquiva, self.jogador_esquiva_rect)

        janela.blit(self.jogador_chance_critico, self.jogador_chance_critico_rect)

        janela.blit(self.jogador_critico, self.jogador_critico_rect)

        janela.blit(self.jogador_escudo, self.jogador_escudo_rect)

    def draw_cartas(self, janela):

        janela.blit(self.carta_ataque, self.carta_ataque_rect)

        janela.blit(self.carta_defesa, self.carta_defesa_rect)