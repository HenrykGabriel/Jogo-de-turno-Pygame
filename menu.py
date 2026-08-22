import pygame
from config import alt_tela, larg_tela
from botao import Botao

class Menu:
    def __init__(self, fontes):
        self.titulo = fontes.titulo
        self.texto_maior = fontes.texto_maior

        self.larg_botao = 310
        self.alt_botao = 120
                                    # largura          altura
        self.botao = Botao((larg_tela-310)//2, (alt_tela+100)//2, 
                           self.larg_botao, self.alt_botao, "Como jogar", (255, 255, 255),
                           self.texto_maior, (224, 221, 8), (214, 211, 0))

        img = pygame.image.load("assets/cenarios/cenario1.png").convert_alpha()
        self.fundo = pygame.transform.scale(img, (larg_tela, alt_tela))

        self.efeito_escuro = pygame.Surface((larg_tela, alt_tela))
        self.efeito_escuro.fill((0,0,0))
        self.efeito_escuro.set_alpha(220)

        img_container = pygame.image.load("assets/cenarios/container_menu.png").convert_alpha()
        self.larg_container = 550
        self.alt_container = 650
        self.container = pygame.transform.scale(img_container, (self.larg_container, self.alt_container))
        self.container_rect = pygame.Rect((larg_tela-self.larg_container)//2, (alt_tela-self.alt_container)//2, self.larg_container, self.alt_container)

        self.efeito_escuro_container = pygame.Surface((larg_tela, alt_tela))
        self.efeito_escuro_container.fill((0,0,0))
        self.efeito_escuro_container.set_alpha(80)

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

    def update(self):
        pass

    def draw(self, janela):

        janela.blit(self.fundo, (0,0))
        janela.blit(self.efeito_escuro, (0,0))
        janela.blit(self.container, self.container_rect)
        janela.blit(self.efeito_escuro_container, (0,0))
        janela.blit(self.nome_jogo1, (self.nome1_rect))
        janela.blit(self.nome_jogo2, (self.nome2_rect))
        self.botao.draw(janela)

    
