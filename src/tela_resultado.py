import pygame
from config import alt_tela, larg_tela, caminho_asset
from botao import Botao
from textos import desenhar_texto

class TelaResultado:
    def __init__(self, fontes):
        self.titulo = fontes.titulo
        self.texto_medio = fontes.texto_medio
        self.texto_normal = fontes.texto_normal
        self.texto_pequeno = fontes.texto_pequeno

        # BOTOES DERROTA

        self.larg_botao = 310
        self.alt_botao = 100
                                    # largura          altura
        self.botao_reiniciar = Botao((larg_tela-310)//2, (alt_tela+100)//2, 
                           self.larg_botao, self.alt_botao, "Reiniciar", (255, 255, 255),
                           self.texto_medio, (224, 221, 8), (214, 211, 0))

        self.botao_sair = Botao((larg_tela-self.larg_botao)//2, (alt_tela+self.alt_botao+250)//2, 
                                   self.larg_botao, self.alt_botao, "Sair", (255, 255, 255),
                                   self.texto_medio, (230, 3, 3), (194, 2, 2))

        img = pygame.image.load(caminho_asset("cenarios/Campo aberto.png")).convert_alpha()
        self.fundo = pygame.transform.scale(img, (larg_tela, alt_tela))

        self.efeito_escuro = pygame.Surface((larg_tela, alt_tela))
        self.efeito_escuro.fill((0,0,0))
        self.efeito_escuro.set_alpha(230)

        img_container = pygame.image.load(caminho_asset("cenarios/container_menu.png")).convert_alpha()
        self.larg_container = 550
        self.alt_container = 650
        self.container = pygame.transform.scale(img_container, (self.larg_container, self.alt_container))
        self.container_rect = pygame.Rect((larg_tela-self.larg_container)//2, (alt_tela-self.alt_container)//2, self.larg_container, self.alt_container)

        self.efeito_escuro_container = pygame.Surface((larg_tela, alt_tela))
        self.efeito_escuro_container.fill((0,0,0))
        self.efeito_escuro_container.set_alpha(60)

        self.cenario = None
        
        self.fase = None

        self.resultado = None

        # TITULO E TEXTOS - DERROTA

        self.titulo_derrota = self.titulo.render("DERROTA!", True, (255, 251, 0))
        self.titulo_derrota_rect = self.titulo_derrota.get_rect(
            center=(
                self.container_rect.centerx,
                self.container_rect.centery - 200)
                )

        self.texto_derrota = ""
        self.texto_derrota_x = self.container_rect.centerx - (self.larg_container - 130)//2
        self.texto_derrota_y = self.container_rect.centery - 120

        self.cenario = None

        self.fase = None

        self.resultado = None

        self.estado = "menu"

    def rodar(self, janela, eventos, cenario, fase, resultado):

        self.cenario = cenario

        self.fase = fase

        self.resultado = resultado 

        self.texto_derrota = f"Você foi derrotado na fase {self.fase} do cenario {self.cenario}."

        self.draw(janela)

        acao = self.update(eventos)

        return acao


    def update(self, eventos):

        if self.botao_reiniciar.clicado(eventos) == True:
            return "reiniciar"

        elif self.botao_sair.clicado(eventos) == True:
            return "sair"
            

    def draw(self, janela):

        janela.blit(self.fundo, (0,0))
        janela.blit(self.efeito_escuro, (0,0))
        janela.blit(self.container, self.container_rect)
        janela.blit(self.efeito_escuro_container, (0,0))

        if self.resultado == "derrota":
            janela.blit(self.titulo_derrota, self.titulo_derrota_rect)
            desenhar_texto(janela, [self.texto_derrota], self.texto_derrota_x,
                           self.texto_derrota_y, self.larg_container - 130, self.texto_medio, (255, 251, 0))
            self.botao_reiniciar.draw(janela)
            self.botao_sair.draw(janela)

        elif self.resultado == "vitoria":

            pass
