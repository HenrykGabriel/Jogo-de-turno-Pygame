import pygame
from sons import Sons

sons = Sons()

class Botao:
    def __init__(self, x, y, largura, altura, texto, cor_texto, fonte, cor, cor_hover):

        self.rect = pygame.Rect(x, y, largura, altura)

        self.texto = texto

        self.cor_texto = cor_texto

        self.fonte = fonte

        self.cor = cor

        self.cor_hover = cor_hover


    def draw(self, janela):

        if self.em_cima():

            pygame.draw.rect(
                janela,
                (self.cor_hover),
                self.rect,
                0,
                20
            )

        else:

            pygame.draw.rect(
                janela,
                (self.cor),
                self.rect,
                0,
                20
            )

        texto = self.fonte.render(
            self.texto,
            True,
            self.cor_texto
        )

        texto_rect = texto.get_rect(
            center=self.rect.center
        )

        janela.blit(texto, texto_rect)

    def em_cima(self):

        mouse = pygame.mouse.get_pos()

        return self.rect.collidepoint(mouse)

    def clicado(self, eventos):
            
        for evento in eventos:

            if evento.type == pygame.MOUSEBUTTONDOWN:

                if self.rect.collidepoint(evento.pos) and evento.button == 1:
                    sons.som_clique()
                    return True