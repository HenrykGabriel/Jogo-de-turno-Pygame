import pygame
from config import alt_tela, larg_tela, caminho_asset
from botao import Botao
from textos import desenhar_texto

class Menu:
    def __init__(self, fontes):
        self.titulo = fontes.titulo
        self.texto_maior = fontes.texto_maior
        self.texto_normal = fontes.texto_normal
        self.texto_pequeno = fontes.texto_pequeno

        # MENU

        self.larg_botao = 310
        self.alt_botao = 120
                                    # largura          altura
        self.botao_como_jogar = Botao((larg_tela-310)//2, (alt_tela+100)//2, 
                           self.larg_botao, self.alt_botao, "Como jogar", (255, 255, 255),
                           self.texto_maior, (224, 221, 8), (214, 211, 0))

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

        self.nome_jogo1 = self.titulo.render("The Last", True, (255, 251, 0))
        self.nome1_rect = self.nome_jogo1.get_rect(
            center=(
                self.container_rect.centerx,
                self.container_rect.centery - 190)
                )
        self.nome_jogo2 = self.titulo.render("Vanguard", True, (255, 251, 0))
        self.nome2_rect = self.nome_jogo2.get_rect(
            center=(
                self.container_rect.centerx,
                self.container_rect.centery - 100)
                )

        # COMO JOGAR

        self.titulo_tutorial = self.texto_maior.render("Como jogar", True, (255, 251, 0))
        self.titulo_tutoruial_rect = self.titulo_tutorial.get_rect(
                    center=(
                        self.container_rect.centerx,
                        self.container_rect.centery - 240)
                        )

        self.texto_tutorial = [
            "Primeiro, escolha a classe do seu personagem, cada uma com seus próprios atributos.",
            
            "Durante os combates, use as cartas de Ataque para causar dano e Defesa para aumentar seu escudo e se proteger.",
            
            "Cada cenário possui três fases, com um chefe na última. Ao vencer uma fase, você irá receber cartas de atributo, que melhoram suas características.",
            
            "Escolha suas ações com cuidado, fortaleça seu personagem e derrote todos os inimigos!"
        ]
        self.largura_maxima = 420
        self.texto_x = self.container_rect.centerx - (self.largura_maxima//2)  # Ajuste baseado na largura máxima abaixo
        self.texto_y = self.container_rect.centery - 180

        self.larg_botao_comecar = 270
        self.alt_botao_comecar = 100
        self.botao_comecar = Botao((larg_tela-self.larg_botao_comecar)//2, (alt_tela+310)//2, 
                           self.larg_botao_comecar, self.alt_botao_comecar, "Começar", (255, 255, 255),
                           self.texto_maior, (224, 221, 8), (214, 211, 0))

        self.estado = "menu"

    def update(self, eventos):

        if self.botao_como_jogar.clicado(eventos) == True:
            self.estado = "tutorial"

    def update_comecar(self, eventos):

        return self.botao_comecar.clicado(eventos)
            

    def draw(self, janela):

        janela.blit(self.fundo, (0,0))
        janela.blit(self.efeito_escuro, (0,0))
        janela.blit(self.container, self.container_rect)
        janela.blit(self.efeito_escuro_container, (0,0))

        if self.estado == "menu":
            janela.blit(self.nome_jogo1, (self.nome1_rect))
            janela.blit(self.nome_jogo2, (self.nome2_rect))
            self.botao_como_jogar.draw(janela)

        elif self.estado == "tutorial":
            janela.blit(self.titulo_tutorial, (self.titulo_tutoruial_rect))
            desenhar_texto(janela, self.texto_tutorial, self.texto_x, self.texto_y,
                           self.largura_maxima, self.texto_pequeno, (255, 251, 0))
            self.botao_comecar.draw(janela)
